# LeetPrep Local

A self-contained, offline coding-interview prep tool: a Monaco-based editor with a real
Python/C++ compiler and judge running underneath, plus progress tracking and spaced
repetition — all stored in a single SQLite file on your machine. No account, no cloud,
no browser cache.

Built around the topics that show up in Anduril's actual technical screens: graph/BFS
traversal, Dijkstra's shortest path, arrays, DP, trees, and general algorithmic
efficiency — with a C++ track since that's their preferred language.

Currently 63 problems, covering all but 5 of a 40-question Anduril-tagged list plus a
second batch pulled from a general LeetCode practice list. 4 from the Anduril list
overlapped with problems already in the set (Two Sum, Valid Parentheses, Number of
Islands, Merge Intervals), and 5 don't fit the judge's current type system, so they
were skipped rather than faked:
- **Insert into a Sorted Circular Linked List**, **Merge k Sorted Lists** — need a
  linked-list type (the judge currently supports int/bool/string/array/tree, no list)
- **Maximum Number of Visible Points** — needs floating-point/trig support (angles),
  which the judge doesn't have
- **Accounts Merge** — its output has positional meaning (`[name, email, email...]`)
  that the judge's order-independent comparison mode isn't safe to apply to
- **Race Car** — the correct DP has enough subtlety that I didn't want to ship it
  without being able to verify the recurrence carefully

The second batch (20 problems: Take Gifts From the Richest Pile, Can Place Flowers,
Zero Array Transformation I, Squares of a Sorted Array, Expression Add Operators,
Longest Substring Without Repeating Characters, Container With Most Water, Max
Consecutive Ones III, Kth Smallest Element in a Sorted Matrix, Rank Transform of a
Matrix, Longest Increasing Subsequence, Jump Game, Add Two Integers, Longest
Consecutive Sequence, Same Tree, Asteroid Collision, Final Array State After K
Multiplication Operations I, Generate Parentheses, Evaluate Division, Ransom Note)
had a few of its own overlaps, same policy as above -- skipped as duplicates rather
than added again under a new title:
- **Binary Tree Vertical Order Traversal** was already in the set exactly as-is.
- **Two Sum**, **Valid Parentheses**, **Coin Change** are functionally identical to
  existing problems (Pair Sum Indices, Valid Bracket Sequence, Minimum Coins for
  Amount respectively) -- same signature, same algorithm.
- **Find Median from Data Stream** is covered by the existing doubled-median variant
  (`median_data_stream_doubled`) for the same no-floating-point reason noted above.
- **Evaluate Division** *is* included, but adapted: LeetCode's version returns
  `vector<double>`, which this judge can't do. Values and results are integers
  instead, and a query returns `-1` if the true ratio isn't a whole number.

Ask if you want any of these added — the linked-list type in particular is a
reasonable follow-up if you want it.

## Requirements

- Python 3.9+
- A C++ compiler (`g++`) to use the C++ track.
  - **Windows:** `run.bat` handles this automatically — if it doesn't find `g++`,
    it downloads a portable compiler (about 150MB, one-time, needs internet) into a
    `tools\` folder next to the app. Nothing gets installed system-wide and your PATH
    isn't touched.
  - **macOS:** run `xcode-select --install` once.
  - **Linux:** `sudo apt install build-essential` (or your distro's equivalent).
  - The Python track needs none of this and works immediately either way.
- Internet connection **only** to load the Monaco editor from a CDN the first time your
  browser opens the page, and (Windows only, one-time) to download the portable C++
  compiler if needed — everything else (code execution, problems, your progress) is
  100% local.

## Run it

**macOS / Linux:**
```
./run.sh
```

**Windows:**
```
run.bat
```

First run creates a virtual environment and installs FastAPI/uvicorn (a few seconds).
After that it just starts instantly. Your browser opens automatically to
`http://127.0.0.1:8420`. Close the terminal window (or Ctrl+C) to stop it — nothing
stays running in the background.

### Access from other devices on your network

The server listens on all interfaces, so once it's running, other devices on the same
network can reach it at `http://<this-machine's-LAN-IP>:8420` (the terminal prints this
address on startup). Two things to know before you do this:

- **Progress is shared, not per-user.** There's no login -- everyone hitting the same
  server reads and writes the same `progress.db`. Fine for "my own laptop and phone,"
  probably not what you want for "my roommate practices on their own account."
- **There's no sandbox.** The judge runs submitted code directly as a subprocess with no
  isolation (see the warning at the bottom of this file). Opening it to your network
  means anyone who can reach that port can run arbitrary code on this machine through
  the Run/Submit buttons -- only do this on a network of people you trust.

You'll also need a firewall rule allowing inbound traffic on port 8420:
- **Windows:** `netsh advfirewall firewall add rule name="LeetPrep" dir=in action=allow protocol=TCP localport=8420`
- **macOS:** the first connection attempt triggers an "allow incoming connections?"
  prompt for Python -- accept it.
- **Linux:** `sudo ufw allow 8420/tcp` (if you're running `ufw`).

## How it works

- **Run** compiles/executes your code against the visible sample test cases only —
  use it to iterate.
- **Submit** runs against the full test suite (including hidden edge cases), and if it
  all passes, marks the problem solved and schedules it for spaced-repetition review
  (1 → 3 → 7 → 16 → 35 → 75 day intervals — fail a review and it resets to day 1).
- Your code, per problem and per language, is saved automatically every time you Run
  or Submit, so you can close the app and pick up where you left off.
- Everything lives in `progress.db` (SQLite) next to `app.py`. Delete that file any
  time to wipe your progress and start over. Back it up by just copying the file.

## Adding your own problems

Open `problems/_generate.py`, copy one of the existing problem dicts, fill in your own
`description_md`, `function_name`, `params` (supported types: `int`, `bool`, `string`,
`vector<int>`, `vector<vector<int>>`, `tree`), `return_type`, starter code for both
languages, and test cases. Then re-run:

```
cd problems && python3 _generate.py
```

Restart the app and your new problem shows up in the sidebar.

## Architecture (for your own reference)

```
app.py              FastAPI app: routes for problems / run / submit / stats, serves static/
engine/runner.py     The judge: builds a driver program around your code per language,
                      runs it as a subprocess with a hard timeout, parses PASS/FAIL
engine/db.py          SQLite progress + spaced-repetition scheduling
problems/*.json      Problem definitions (statement, params, test cases, starter code)
static/               Monaco-based frontend (vanilla JS, no build step)
```

The judge has no network sandbox or container isolation — it runs code directly as a
subprocess with a timeout. That's a deliberate simplification for a personal local tool
running your own code on your own machine; don't expose this server to the network or
run untrusted code through it.
