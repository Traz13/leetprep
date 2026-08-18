import json
import os
import webbrowser
import threading

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from engine import db, runner

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROB_DIR = os.path.join(BASE_DIR, "problems")

app = FastAPI(title="LeetPrep Local")

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


app.mount("/", StaticFiles(directory=os.path.join(BASE_DIR, "static"), html=True), name="static")


def _open_browser():
    import time
    time.sleep(1.2)
    webbrowser.open("http://127.0.0.1:8420")


if __name__ == "__main__":
    import uvicorn
    threading.Thread(target=_open_browser, daemon=True).start()
    print("\nLeetPrep running at http://127.0.0.1:8420  (Ctrl+C to stop)\n")
    uvicorn.run(app, host="127.0.0.1", port=8420, log_level="warning")
