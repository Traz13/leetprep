import datetime
import json
import os
import shutil
import sqlite3
import tempfile
import webbrowser
import threading

from fastapi import FastAPI, File, HTTPException, Request, UploadFile
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from starlette.background import BackgroundTask
from starlette.middleware.base import BaseHTTPMiddleware

from engine import db, runner

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROB_DIR = os.path.join(BASE_DIR, "problems")

app = FastAPI(title="LeetPrep Local")


class NoCacheStaticMiddleware(BaseHTTPMiddleware):
    """This is a local dev tool that gets its own frontend edited in place --
    stale cached app.js/style.css after a reload is a worse failure mode than
    the (negligible, localhost-only) cost of always refetching them."""

    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        if not request.url.path.startswith("/api"):
            response.headers["Cache-Control"] = "no-store"
        return response


app.add_middleware(NoCacheStaticMiddleware)

db.init_db()


@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception):
    # Make sure the frontend always gets JSON back, even if something here
    # throws unexpectedly -- a plain-text error page breaks res.json() in
    # app.js with a confusing "not valid JSON" error instead of a clear one.
    return JSONResponse(
        status_code=500,
        content={"error": f"{type(exc).__name__}: {exc}"},
    )


def load_problems():
    problems = {}
    for fname in sorted(os.listdir(PROB_DIR)):
        if fname.endswith(".json"):
            with open(os.path.join(PROB_DIR, fname)) as f:
                p = json.load(f)
                problems[p["id"]] = p
    return problems


PROBLEMS = load_problems()


def get_problem_or_404(problem_id: str):
    p = PROBLEMS.get(problem_id)
    if p is None:
        raise HTTPException(status_code=404, detail=f"No such problem: {problem_id}")
    return p


class RunRequest(BaseModel):
    problem_id: str
    language: str
    code: str


def _visible_result(res_dict, submit: bool):
    """On 'run' (not submit), hide the hidden test cases entirely so you can't
    peek at them by reading the response, same as LeetCode's Run vs Submit."""
    if submit:
        return res_dict
    res_dict = dict(res_dict)
    res_dict["cases"] = [c for c in res_dict["cases"] if not c.get("hidden")]
    return res_dict


@app.get("/api/problems")
def api_list_problems():
    progress = db.get_progress_map()
    out = []
    for pid, p in PROBLEMS.items():
        prog = progress.get(pid, {})
        out.append({
            "id": pid,
            "title": p["title"],
            "difficulty": p["difficulty"],
            "topic": p["topic"],
            "tags": p["tags"],
            "status": prog.get("status", "not_started"),
            "next_review_at": prog.get("next_review_at"),
        })
    due = set(db.due_for_review())
    for o in out:
        o["due_for_review"] = o["id"] in due
    return out


@app.get("/api/problems/{problem_id}")
def api_get_problem(problem_id: str):
    p = get_problem_or_404(problem_id)
    prog = db.get_progress(problem_id) or {}
    visible_cases = [c for c in p["test_cases"] if not c.get("hidden")]
    return {
        "id": p["id"],
        "title": p["title"],
        "difficulty": p["difficulty"],
        "topic": p["topic"],
        "tags": p["tags"],
        "description_md": p["description_md"],
        "diagram_svg": p.get("diagram_svg"),
        "starter_code": p["starter_code"],
        "examples": visible_cases,
        "hidden_count": len(p["test_cases"]) - len(visible_cases),
        "progress": {
            "status": prog.get("status", "not_started"),
            "attempts": prog.get("attempts", 0),
            "last_language": prog.get("last_language"),
            "last_code_python": prog.get("last_code_python"),
            "last_code_cpp": prog.get("last_code_cpp"),
            "next_review_at": prog.get("next_review_at"),
        },
    }


@app.post("/api/run")
def api_run(req: RunRequest):
    problem = get_problem_or_404(req.problem_id)
    res = runner.run(req.language, req.code, problem)
    db.save_code(req.problem_id, req.language, req.code)
    return _visible_result(res.to_dict(), submit=False)


@app.post("/api/submit")
def api_submit(req: RunRequest):
    problem = get_problem_or_404(req.problem_id)
    res = runner.run(req.language, req.code, problem)
    db.save_code(req.problem_id, req.language, req.code)
    status, next_review = db.record_submission(
        req.problem_id, req.language, res.passed, res.total, res.runtime_ms, res.all_passed
    )
    out = _visible_result(res.to_dict(), submit=True)
    out["progress_status"] = status
    out["next_review_at"] = next_review
    return out


@app.get("/api/stats")
def api_stats():
    progress = db.get_progress_map()
    total = len(PROBLEMS)
    solved = sum(1 for p in progress.values() if p["status"] == "solved")
    attempted = sum(1 for p in progress.values() if p["status"] == "attempted")
    due = db.due_for_review()
    return {
        "total": total,
        "solved": solved,
        "attempted": attempted,
        "not_started": total - solved - attempted,
        "due_for_review": len(due),
        "due_ids": due,
    }


SQLITE_MAGIC = b"SQLite format 3\x00"


@app.get("/api/backup/info")
def api_backup_info():
    exists = os.path.isfile(db.DB_PATH)
    return {
        "path": db.DB_PATH,
        "exists": exists,
        "size_bytes": os.path.getsize(db.DB_PATH) if exists else 0,
    }


@app.get("/api/backup/export")
def api_backup_export():
    if not os.path.isfile(db.DB_PATH):
        raise HTTPException(status_code=404, detail="No progress database found yet -- solve or attempt a problem first.")

    # VACUUM INTO writes a clean, consistent snapshot to a brand-new file --
    # safer than copying the live file's bytes directly, which could in
    # principle race a concurrent write.
    fd, tmp_path = tempfile.mkstemp(suffix=".db")
    os.close(fd)
    os.remove(tmp_path)
    conn = sqlite3.connect(db.DB_PATH)
    conn.execute("VACUUM INTO ?", (tmp_path,))
    conn.close()

    stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    return FileResponse(
        tmp_path,
        filename=f"leetprep-progress-{stamp}.db",
        media_type="application/octet-stream",
        background=BackgroundTask(lambda: os.path.isfile(tmp_path) and os.remove(tmp_path)),
    )


@app.post("/api/backup/import")
async def api_backup_import(file: UploadFile = File(...)):
    data = await file.read()
    if not data.startswith(SQLITE_MAGIC):
        raise HTTPException(status_code=400, detail="That doesn't look like a SQLite database file.")

    tmp_dir = os.path.dirname(db.DB_PATH)
    fd, tmp_path = tempfile.mkstemp(dir=tmp_dir, suffix=".upload.db")
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(data)

        conn = sqlite3.connect(tmp_path)
        try:
            conn.execute("SELECT problem_id, status FROM progress LIMIT 1")
            conn.execute("SELECT problem_id, language FROM submissions LIMIT 1")
        except sqlite3.Error:
            raise HTTPException(
                status_code=400,
                detail="This file doesn't have the tables LeetPrep expects -- it might not be a LeetPrep backup.",
            )
        finally:
            # Must close before the outer `finally` tries to remove tmp_path --
            # on Windows a lingering open connection keeps the file locked.
            conn.close()

        if os.path.isfile(db.DB_PATH):
            shutil.copy2(db.DB_PATH, db.DB_PATH + ".bak")

        os.replace(tmp_path, db.DB_PATH)
    finally:
        if os.path.isfile(tmp_path):
            os.remove(tmp_path)

    return {"ok": True}


@app.post("/api/backup/clear")
def api_backup_clear():
    if os.path.isfile(db.DB_PATH):
        stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        shutil.copy2(db.DB_PATH, f"{db.DB_PATH}.before-clear-{stamp}.bak")
    db.reset_db()
    return {"ok": True}


app.mount("/", StaticFiles(directory=os.path.join(BASE_DIR, "static"), html=True), name="static")


def _open_browser():
    import time
    time.sleep(1.2)
    webbrowser.open("http://127.0.0.1:8420")


def _lan_ip():
    """Best-effort local network IP for printing a URL other devices can use.
    Doesn't actually send anything -- UDP connect() just picks the outbound
    interface so we can read its address back off the socket."""
    import socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return None


if __name__ == "__main__":
    import uvicorn
    threading.Thread(target=_open_browser, daemon=True).start()
    lan_ip = _lan_ip()
    print("\nLeetPrep running at http://127.0.0.1:8420  (Ctrl+C to stop)")
    if lan_ip:
        print(f"Other devices on your network: http://{lan_ip}:8420")
        print("(needs a firewall rule allowing inbound TCP 8420 -- see README)\n")
    else:
        print()
    uvicorn.run(app, host="0.0.0.0", port=8420, log_level="warning")
