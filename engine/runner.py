"""
Local judge. Takes user code + a problem's test cases, builds a small
driver program per language, executes it as a subprocess with a hard
timeout, and parses PASS/FAIL results back out.

No Docker / network sandbox -- this is meant to run on your own machine
for your own practice, not to accept code from strangers.
"""
import subprocess
import tempfile
import os
import json
import time
import uuid

TIMEOUT_SECONDS = 6
CPP_COMPILE_TIMEOUT = 15


class RunResult:
    def __init__(self):
        self.compiled = True
        self.compile_error = ""
        self.runtime_error = ""
        self.timed_out = False
        self.runtime_ms = 0.0
        self.cases = []          # list of dicts: {index, passed, actual, expected, input_display}
        self.passed = 0
        self.total = 0

    @property
    def all_passed(self):
        return self.compiled and not self.runtime_error and not self.timed_out and self.total > 0 and self.passed == self.total

    def to_dict(self):
        return {
            "compiled": self.compiled,
            "compile_error": self.compile_error,
            "runtime_error": self.runtime_error,
            "timed_out": self.timed_out,
            "runtime_ms": round(self.runtime_ms, 2),
            "cases": self.cases,
            "passed": self.passed,
            "total": self.total,
            "all_passed": self.all_passed,
        }


# ---------------------------------------------------------------------------
# PYTHON
# ---------------------------------------------------------------------------

PY_PRELUDE = '''
import json, sys

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(vals):
    """Level-order build. None marks a missing child."""
    if not vals or vals[0] is None:
        return None
    it = iter(vals)
    root = TreeNode(next(it))
    queue = [root]
    while queue:
        node = queue.pop(0)
        try:
            lv = next(it)
        except StopIteration:
            break
        if lv is not None:
            node.left = TreeNode(lv)
            queue.append(node.left)
        try:
            rv = next(it)
        except StopIteration:
            break
        if rv is not None:
            node.right = TreeNode(rv)
            queue.append(node.right)
    return root
'''


def _py_prep_arg(param_type, value):
    if param_type == "tree":
        return f"build_tree({value!r})"
    return json.dumps(value)


def run_python(user_code, problem):
    fn = problem["function_name"]
    params = problem["params"]
    cases = problem["test_cases"]

    lines = [PY_PRELUDE, "\n# ---- USER CODE ----\n", user_code, "\n# ---- DRIVER ----\n"]
    lines.append("__results = []")
    for i, tc in enumerate(cases):
        args = [ _py_prep_arg(p["type"], v) for p, v in zip(params, tc["inputs"]) ]
        call = f"{fn}({', '.join(args)})"
        lines.append(f"""
try:
    __r = {call}
    if isinstance(__r, tuple):
        __r = list(__r)
    __results.append({{"ok": True, "value": __r}})
except Exception as __e:
    __results.append({{"ok": False, "error": f"{{type(__e).__name__}}: {{__e}}"}})
""")
    lines.append('print("###RESULTS###")')
    lines.append("print(json.dumps(__results))")

    script = "\n".join(lines)

    result = RunResult()
    result.total = len(cases)

    with tempfile.TemporaryDirectory() as td:
        path = os.path.join(td, "sol.py")
        with open(path, "w") as f:
            f.write(script)

        start = time.time()
        try:
            proc = subprocess.run(
                ["python3", path],
                capture_output=True, text=True, timeout=TIMEOUT_SECONDS, cwd=td,
            )
        except subprocess.TimeoutExpired:
            result.timed_out = True
            result.runtime_ms = TIMEOUT_SECONDS * 1000
            return result
        result.runtime_ms = (time.time() - start) * 1000

        if "###RESULTS###" not in proc.stdout:
            result.runtime_error = (proc.stderr or proc.stdout or "Unknown error").strip()[-4000:]
            return result

        try:
            payload = json.loads(proc.stdout.split("###RESULTS###")[1].strip())
        except Exception as e:
            result.runtime_error = f"Could not parse output: {e}\n{proc.stdout[-2000:]}"
            return result

        _score(result, cases, payload, unordered=problem.get("unordered", False))

    return result


def _normalize_unordered(value):
    """Recursively sort nested lists so order-independent results (e.g. Group
    Anagrams, Word Break II) compare equal regardless of the order a
    particular implementation produces them in. Only used when the problem
    sets "unordered": true -- unsafe for structures where position carries
    meaning (e.g. [name, email, email...]), so those problems don't use it."""
    if isinstance(value, list):
        normalized = [_normalize_unordered(v) for v in value]
        normalized.sort(key=lambda x: json.dumps(x))
        return normalized
    return value


def _score(result, cases, payload, unordered=False):
    for i, (tc, r) in enumerate(zip(cases, payload)):
        expected = tc["expected"]
        if r["ok"]:
            actual = r["value"]
            if unordered:
                passed = _normalize_unordered(actual) == _normalize_unordered(expected)
            else:
                passed = _values_equal(actual, expected)
            result.cases.append({
                "index": i, "passed": passed, "hidden": tc.get("hidden", False),
                "input_display": tc.get("input_display", str(tc["inputs"])),
                "expected": expected if not tc.get("hidden") else ("(hidden)" if not passed else expected),
                "actual": actual,
            })
        else:
            result.cases.append({
                "index": i, "passed": False, "hidden": tc.get("hidden", False),
                "input_display": tc.get("input_display", str(tc["inputs"])),
                "expected": expected if not tc.get("hidden") else "(hidden)",
                "actual": r["error"],
            })
        if result.cases[-1]["passed"]:
            result.passed += 1


def _values_equal(a, b):
    if isinstance(a, list) and isinstance(b, list):
        return a == b
    return a == b


# ---------------------------------------------------------------------------
# C++
# ---------------------------------------------------------------------------

CPP_PRELUDE = r'''
#include <bits/stdc++.h>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

TreeNode* buildTree(vector<int> vals, vector<bool> present) {
    if (vals.empty() || !present[0]) return nullptr;
    TreeNode* root = new TreeNode(vals[0]);
    vector<TreeNode*> q = {root};
    size_t i = 1;
    while (i < vals.size() && !q.empty()) {
        TreeNode* node = q.front(); q.erase(q.begin());
        if (i < vals.size()) {
            if (present[i]) { node->left = new TreeNode(vals[i]); q.push_back(node->left); }
            i++;
        }
        if (i < vals.size()) {
            if (present[i]) { node->right = new TreeNode(vals[i]); q.push_back(node->right); }
            i++;
        }
    }
    return root;
}

string __toJson(int v) { return to_string(v); }
string __toJson(bool v) { return v ? "true" : "false"; }
string __toJson(const string &v) {
    string out = "\"";
    for (char c : v) { if (c=='"'||c=='\\') out += '\\'; out += c; }
    return out + "\"";
}
string __toJson(const vector<int> &v) {
    string out = "[";
    for (size_t i=0;i<v.size();++i){ if(i) out+=","; out+=to_string(v[i]); }
    return out + "]";
}
string __toJson(const vector<vector<int>> &v) {
    string out = "[";
    for (size_t i=0;i<v.size();++i){ if(i) out+=","; out+=__toJson(v[i]); }
    return out + "]";
}
string __toJson(const vector<string> &v) {
    string out = "[";
    for (size_t i=0;i<v.size();++i){ if(i) out+=","; out+=__toJson(v[i]); }
    return out + "]";
}
string __toJson(const vector<vector<string>> &v) {
    string out = "[";
    for (size_t i=0;i<v.size();++i){ if(i) out+=","; out+=__toJson(v[i]); }
    return out + "]";
}
'''


def _cpp_literal(param_type, value):
    if param_type == "int":
        return str(value)
    if param_type == "bool":
        return "true" if value else "false"
    if param_type == "string":
        escaped = value.replace("\\", "\\\\").replace('"', '\\"')
        return f'"{escaped}"'
    if param_type == "vector<int>":
        return "{" + ",".join(str(x) for x in value) + "}"
    if param_type == "vector<vector<int>>":
        return "{" + ",".join("{" + ",".join(str(y) for y in row) + "}" for row in value) + "}"
    if param_type == "vector<string>":
        return "{" + ",".join(_cpp_literal("string", x) for x in value) + "}"
    if param_type == "vector<vector<string>>":
        return "{" + ",".join("{" + ",".join(_cpp_literal("string", x) for x in row) + "}" for row in value) + "}"
    if param_type == "tree":
        vals = [x if x is not None else 0 for x in value]
        present = ["true" if x is not None else "false" for x in value]
        return f"buildTree({{{','.join(str(v) for v in vals)}}}, {{{','.join(present)}}})"
    raise ValueError(f"unsupported cpp param type: {param_type}")


def _cpp_arg_decl(param_type):
    return {
        "int": "int",
        "bool": "bool",
        "string": "string",
        "vector<int>": "vector<int>",
        "vector<vector<int>>": "vector<vector<int>>",
        "vector<string>": "vector<string>",
        "vector<vector<string>>": "vector<vector<string>>",
        "tree": "TreeNode*",
    }[param_type]


def _gpp_path():
    """Resolve which g++ to invoke. Checks, in order: an explicit override env
    var, a portable compiler previously auto-installed by run.bat into
    tools/, then falls back to whatever 'g++' resolves to on PATH."""
    override = os.environ.get("LEETPREP_GPP")
    if override:
        return override
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    marker = os.path.join(root, "tools", "gpp_path.txt")
    if os.path.isfile(marker):
        with open(marker) as f:
            candidate = f.read().strip()
        if candidate and os.path.isfile(candidate):
            return candidate
    return "g++"


_WINDOWS_CRASH_CODES = {
    0xC0000005: "The program crashed with an access violation (segmentation fault) -- "
                "likely a null pointer dereference (e.g. calling a method on a nullptr TreeNode, "
                "or indexing past the end of a vector) or a dangling pointer.",
    0xC00000FD: "The program crashed with a stack overflow -- check for infinite/unbounded recursion "
                "(e.g. a base case that's never reached).",
    0xC0000094: "The program crashed on an integer division by zero.",
    0xC0000409: "The program aborted due to a stack buffer overflow (e.g. writing past the end of "
                "a fixed-size array).",
}

_POSIX_SIGNAL_NAMES = {
    4: "SIGILL (illegal instruction)",
    6: "SIGABRT (abort -- often an unhandled C++ exception, a failed assert(), or heap corruption)",
    8: "SIGFPE (floating point exception -- likely integer division by zero)",
    11: "SIGSEGV (segmentation fault -- likely a null pointer dereference or out-of-bounds access)",
}


def _describe_crash(returncode):
    """The program crashed (e.g. segfault) before writing anything to stdout/stderr,
    so there's no message to surface. Translate the raw exit/signal code into
    something a user can actually act on instead of a bare 'Unknown error'."""
    if returncode < 0:
        sig = -returncode
        name = _POSIX_SIGNAL_NAMES.get(sig, f"signal {sig}")
        return f"Program crashed: killed by {name}."
    unsigned = returncode & 0xFFFFFFFF
    known = _WINDOWS_CRASH_CODES.get(unsigned)
    if known:
        return f"Program crashed (exit code {hex(unsigned)}): {known}"
    if returncode != 0:
        return f"Program exited with code {returncode} and produced no output."
    return "Unknown error"


def run_cpp(user_code, problem):
    fn = problem["function_name"]
    params = problem["params"]
    ret_type = problem["return_type"]
    cases = problem["test_cases"]

    driver = [CPP_PRELUDE, "\n// ---- USER CODE ----\n", user_code, "\n// ---- DRIVER ----\n", "int main(){\n"]
    driver.append(f'  vector<pair<bool,string>> results;\n')
    for i, tc in enumerate(cases):
        arg_names = []
        for j, (p, v) in enumerate(zip(params, tc["inputs"])):
            varname = f"a{i}_{j}"
            decl = _cpp_arg_decl(p["type"])
            lit = _cpp_literal(p["type"], v)
            driver.append(f"  {decl} {varname} = {lit};\n")
            arg_names.append(varname)
        driver.append(f"  try {{\n")
        driver.append(f"    {ret_type} r{i} = {fn}({', '.join(arg_names)});\n")
        driver.append(f'    results.push_back({{true, __toJson(r{i})}});\n')
        driver.append(f"  }} catch (const exception &e) {{\n")
        driver.append(f'    results.push_back({{false, string("EXC: ") + e.what()}});\n')
        driver.append(f"  }} catch (...) {{\n")
        driver.append(f'    results.push_back({{false, "EXC: unknown"}});\n')
        driver.append(f"  }}\n")
    driver.append('  cout << "###RESULTS###\\n";\n')
    driver.append('  cout << "[";\n')
    driver.append('  for (size_t i=0;i<results.size();++i){\n')
    driver.append('    if(i) cout << ",";\n')
    driver.append('    if(results[i].first) cout << "{\\"ok\\":true,\\"value\\":" << results[i].second << "}";\n')
    driver.append('    else cout << "{\\"ok\\":false,\\"error\\":" << __toJson(results[i].second) << "}";\n')
    driver.append('  }\n')
    driver.append('  cout << "]" << endl;\n')
    driver.append("  return 0;\n}\n")

    source = "".join(driver)

    result = RunResult()
    result.total = len(cases)

    with tempfile.TemporaryDirectory() as td:
        src_path = os.path.join(td, "sol.cpp")
        bin_path = os.path.join(td, "sol.out")
        with open(src_path, "w") as f:
            f.write(source)

        try:
            compile_proc = subprocess.run(
                [_gpp_path(), "-O2", "-std=c++17", "-static-libgcc", "-static-libstdc++", "-static",
                 "-o", bin_path, src_path],
                capture_output=True, text=True, timeout=CPP_COMPILE_TIMEOUT,
            )
        except subprocess.TimeoutExpired:
            result.compiled = False
            result.compile_error = f"Compilation took longer than {CPP_COMPILE_TIMEOUT}s and was killed."
            return result
        except FileNotFoundError:
            result.compiled = False
            result.compile_error = (
                "Could not find a 'g++' compiler, so C++ code can't be compiled here.\n\n"
                "  - Windows: close this and re-run run.bat -- it will automatically download "
                "and set up a portable compiler (about 150MB, one-time, needs internet). If it "
                "already tried and this still shows up, check tools\\gpp_path.txt exists and "
                "points at a real g++.exe, or delete the tools\\ folder and re-run run.bat to retry.\n"
                "  - macOS: run 'xcode-select --install' in Terminal, then restart this app.\n"
                "  - Linux: run 'sudo apt install build-essential' (or your distro's equivalent), "
                "then restart this app.\n\n"
                "The Python track works right now regardless -- switch the language toggle to "
                "Python while you sort out a C++ compiler."
            )
            return result
        if compile_proc.returncode != 0:
            result.compiled = False
            result.compile_error = compile_proc.stderr[-4000:]
            return result

        start = time.time()
        try:
            run_proc = subprocess.run(
                [bin_path], capture_output=True, text=True, timeout=TIMEOUT_SECONDS, cwd=td,
            )
        except subprocess.TimeoutExpired:
            result.timed_out = True
            result.runtime_ms = TIMEOUT_SECONDS * 1000
            return result
        result.runtime_ms = (time.time() - start) * 1000

        if "###RESULTS###" not in run_proc.stdout:
            msg = (run_proc.stderr or run_proc.stdout or "").strip()
            if not msg:
                msg = _describe_crash(run_proc.returncode)
            result.runtime_error = msg[-4000:]
            return result

        try:
            payload = json.loads(run_proc.stdout.split("###RESULTS###")[1].strip())
        except Exception as e:
            result.runtime_error = f"Could not parse output: {e}\n{run_proc.stdout[-2000:]}"
            return result

        _score(result, cases, payload, unordered=problem.get("unordered", False))

    return result


def run(language, user_code, problem):
    if language == "python":
        return run_python(user_code, problem)
    elif language == "cpp":
        return run_cpp(user_code, problem)
    raise ValueError(f"unsupported language: {language}")
