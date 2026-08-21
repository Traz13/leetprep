"""
Local progress storage. Everything lives in a single SQLite file
(progress.db) next to the app -- no server, no cloud, no browser cache.
"""
import sqlite3
import datetime
import os

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "progress.db")

# Fixed spaced-repetition ladder (days). Solve it -> jump to next stage.
# Fail a review -> drop back to stage 0.
REVIEW_LADDER = [1, 3, 7, 16, 35, 75]


def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_conn()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS progress (
            problem_id TEXT PRIMARY KEY,
            status TEXT DEFAULT 'not_started',       -- not_started | attempted | solved
            stage INTEGER DEFAULT 0,                  -- index into REVIEW_LADDER
            attempts INTEGER DEFAULT 0,
            last_language TEXT,
            last_code_python TEXT,
            last_code_cpp TEXT,
            solved_at TEXT,
            last_attempt_at TEXT,
            next_review_at TEXT
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS submissions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            problem_id TEXT,
            language TEXT,
            passed INTEGER,
            total INTEGER,
            runtime_ms REAL,
            created_at TEXT
        )
    """)
    conn.commit()
    conn.close()


def get_progress_map():
    conn = get_conn()
    rows = conn.execute("SELECT * FROM progress").fetchall()
    conn.close()
    return {r["problem_id"]: dict(r) for r in rows}


def get_progress(problem_id):
    conn = get_conn()
    row = conn.execute("SELECT * FROM progress WHERE problem_id=?", (problem_id,)).fetchone()
    conn.close()
    return dict(row) if row else None


def save_code(problem_id, language, code):
    conn = get_conn()
    conn.execute("""
        INSERT INTO progress (problem_id, last_language, last_code_python, last_code_cpp, last_attempt_at)
        VALUES (?, ?, ?, ?, ?)
        ON CONFLICT(problem_id) DO UPDATE SET
            last_language=excluded.last_language,
            last_code_python=CASE WHEN ?='python' THEN excluded.last_code_python ELSE progress.last_code_python END,
            last_code_cpp=CASE WHEN ?='cpp' THEN excluded.last_code_cpp ELSE progress.last_code_cpp END,
            last_attempt_at=excluded.last_attempt_at
    """, (
        problem_id, language,
        code if language == "python" else None,
        code if language == "cpp" else None,
        datetime.datetime.utcnow().isoformat(),
        language, language,
    ))
    conn.commit()
    conn.close()


def record_submission(problem_id, language, passed, total, runtime_ms, all_passed):
    conn = get_conn()
    now = datetime.datetime.utcnow().isoformat()
    conn.execute(
        "INSERT INTO submissions (problem_id, language, passed, total, runtime_ms, created_at) VALUES (?,?,?,?,?,?)",
        (problem_id, language, passed, total, runtime_ms, now),
    )

    row = conn.execute("SELECT * FROM progress WHERE problem_id=?", (problem_id,)).fetchone()
    attempts = (row["attempts"] if row else 0) + 1
    stage = row["stage"] if row else 0
    status = row["status"] if row else "not_started"
    solved_at = row["solved_at"] if row else None

    if all_passed:
        status = "solved"
        stage = min(stage + 1, len(REVIEW_LADDER) - 1)
        if not solved_at:
            solved_at = now
        next_review = (datetime.datetime.utcnow() + datetime.timedelta(days=REVIEW_LADDER[stage])).isoformat()
    else:
        if status != "solved":
            status = "attempted"
        else:
            # was solved before, failed a review -> reset ladder
            stage = 0
        next_review = (datetime.datetime.utcnow() + datetime.timedelta(days=REVIEW_LADDER[0])).isoformat()

    conn.execute("""
        INSERT INTO progress (problem_id, status, stage, attempts, last_language, solved_at, last_attempt_at, next_review_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(problem_id) DO UPDATE SET
            status=excluded.status,
            stage=excluded.stage,
            attempts=excluded.attempts,
            last_language=excluded.last_language,
            solved_at=excluded.solved_at,
            last_attempt_at=excluded.last_attempt_at,
            next_review_at=excluded.next_review_at
    """, (problem_id, status, stage, attempts, language, solved_at, now, next_review))
    conn.commit()
    conn.close()
    return status, next_review


def due_for_review():
    conn = get_conn()
    now = datetime.datetime.utcnow().isoformat()
    rows = conn.execute(
        "SELECT problem_id, next_review_at FROM progress WHERE status='solved' AND next_review_at<=?",
        (now,),
    ).fetchall()
    conn.close()
    return [r["problem_id"] for r in rows]


def reset_db():
    """Wipe all progress/submission rows but keep the schema -- used by the
    Clear All Progress action. Callers are responsible for backing up the
    file first if they want it recoverable."""
    conn = get_conn()
    conn.execute("DELETE FROM progress")
    conn.execute("DELETE FROM submissions")
    conn.commit()
    conn.close()
