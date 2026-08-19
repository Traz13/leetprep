let editor = null;
let monacoReady = false;
let currentProblem = null;
let currentLang = "python";
let allProblems = [];

const MONACO_LANG = { python: "python", cpp: "cpp" };
const DIFFICULTY_ORDER = { Easy: 0, Medium: 1, Hard: 2 };

require.config({ paths: { vs: "https://cdn.jsdelivr.net/npm/monaco-editor@0.47.0/min/vs" } });
require(["vs/editor/editor.main"], () => {
  monacoReady = true;
  editor = monaco.editor.create(document.getElementById("editor-container"), {
    value: "# select a problem to begin",
    language: "python",
    theme: "vs-dark",
    fontSize: 13,
    fontFamily: "SF Mono, Cascadia Code, Consolas, monospace",
    minimap: { enabled: false },
    automaticLayout: true,
    scrollBeyondLastLine: false,
    padding: { top: 14 },
  });
  init();
});

async function api(path, opts) {
  const res = await fetch(path, opts);
  let data;
  try {
    data = await res.json();
  } catch (e) {
    throw new Error(`Server returned a non-JSON response (HTTP ${res.status}). Check the terminal running app.py for a traceback.`);
  }
  if (!res.ok) {
    const msg = data.detail || data.error || `HTTP ${res.status}`;
    throw new Error(msg);
  }
  return data;
}

async function init() {
  await refreshStats();
  await loadProblemList();
  wireToolbar();
}

async function refreshStats() {
  const stats = await api("/api/stats");
  const panel = document.getElementById("stats-panel");
  const solvedPct = stats.total ? (stats.solved / stats.total * 100) : 0;
  const attemptedPct = stats.total ? (stats.attempted / stats.total * 100) : 0;
  panel.innerHTML = `
    <div class="stats-row"><span>Solved</span><b>${stats.solved} / ${stats.total}</b></div>
    <div class="bar-track">
      <div class="bar-solved" style="width:${solvedPct}%"></div>
      <div class="bar-attempted" style="width:${attemptedPct}%"></div>
    </div>
    ${stats.due_for_review > 0 ? `<div class="due-badge">⟳ ${stats.due_for_review} due for review</div>` : ""}
  `;
}

async function loadProblemList() {
  allProblems = await api("/api/problems");
  allProblems.sort((a, b) => {
    const diff = DIFFICULTY_ORDER[a.difficulty] - DIFFICULTY_ORDER[b.difficulty];
    return diff !== 0 ? diff : a.title.localeCompare(b.title);
  });
  renderProblemList();
}

function renderProblemList() {
  const list = document.getElementById("problem-list");
  list.innerHTML = "";
  let lastDifficulty = null;
  for (const p of allProblems) {
    if (p.difficulty !== lastDifficulty) {
      lastDifficulty = p.difficulty;
      const count = allProblems.filter((x) => x.difficulty === p.difficulty).length;
      const header = document.createElement("div");
      header.className = "difficulty-header";
      header.innerHTML = `<span class="diff-${p.difficulty}">${p.difficulty}</span><span class="difficulty-count">${count}</span>`;
      list.appendChild(header);
    }
    const item = document.createElement("div");
    item.className = "problem-item" + (currentProblem && currentProblem.id === p.id ? " active" : "");
    item.innerHTML = `
      <div class="problem-row1">
        <span class="status-dot ${p.status}"></span>
        <span class="problem-title">${p.title}</span>
      </div>
      <div class="problem-meta">
        <span class="diff-${p.difficulty}">${p.difficulty}</span>
        <span>${p.topic}</span>
        ${p.due_for_review ? '<span class="review-flag">⟳ review</span>' : ""}
      </div>
    `;
    item.onclick = () => selectProblem(p.id);
    list.appendChild(item);
  }
}

function wireToolbar() {
  document.querySelectorAll(".lang-btn").forEach((btn) => {
    btn.onclick = () => {
      document.querySelectorAll(".lang-btn").forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");
      currentLang = btn.dataset.lang;
      monaco.editor.setModelLanguage(editor.getModel(), MONACO_LANG[currentLang]);
      loadCodeForLang();
    };
  });
  document.getElementById("btn-run").onclick = () => runOrSubmit(false);
  document.getElementById("btn-submit").onclick = () => runOrSubmit(true);
}

function loadCodeForLang() {
  if (!currentProblem) return;
  const prog = currentProblem.progress;
  const savedKey = currentLang === "python" ? "last_code_python" : "last_code_cpp";
  const saved = prog[savedKey];
  editor.setValue(saved || currentProblem.starter_code[currentLang]);
}

async function selectProblem(id) {
  const p = await api(`/api/problems/${id}`);
  currentProblem = p;
  document.getElementById("btn-run").disabled = false;
  document.getElementById("btn-submit").disabled = false;

  // pick up whichever language they last worked in for this problem
  currentLang = p.progress.last_language || "python";
  document.querySelectorAll(".lang-btn").forEach((b) => {
    b.classList.toggle("active", b.dataset.lang === currentLang);
  });
  monaco.editor.setModelLanguage(editor.getModel(), MONACO_LANG[currentLang]);
  loadCodeForLang();

  renderDescription(p);
  resetConsole();
  renderProblemList();
}

function renderDescription(p) {
  const el = document.getElementById("desc-content");
  const tagsHtml = p.tags.map((t) => `<span class="tag">${t}</span>`).join("");
  const exHtml = p.examples.map((ex, i) => `
    <div class="example-block">
      <div class="ex-label">Example ${i + 1}</div>
      <div class="ex-input">${escapeHtml(ex.input_display || "")}</div>
      <div class="ex-output">→ ${escapeHtml(JSON.stringify(ex.expected))}</div>
      ${ex.explanation ? `<div class="ex-explanation">${escapeHtml(ex.explanation)}</div>` : ""}
    </div>
  `).join("");
  el.className = "";
  el.innerHTML = `
    <h1>${p.title}</h1>
    <div class="desc-meta">
      <span class="diff-${p.difficulty}">${p.difficulty}</span>
      <span class="tag">${p.topic}</span>
      ${tagsHtml}
    </div>
    <div id="desc-body">${mdToHtml(p.description_md)}</div>
    ${exHtml}
    ${p.hidden_count > 0 ? `<div class="hidden-note">+ ${p.hidden_count} additional hidden test case(s) checked on Submit</div>` : ""}
  `;
}

function mdToHtml(md) {
  // minimal markdown: **bold**, `code`, paragraphs
  const esc = escapeHtml(md);
  const withInline = esc
    .replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>")
    .replace(/`(.+?)`/g, "<code>$1</code>");
  return withInline.split(/\n\s*\n/).map((p) => `<p>${p.replace(/\n/g, "<br/>")}</p>`).join("");
}

function escapeHtml(s) {
  return String(s).replace(/[&<>"']/g, (c) => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;",
  }[c]));
}

function resetConsole() {
  document.getElementById("console-body").innerHTML =
    '<div class="console-placeholder">Run your code to see test results here.</div>';
  document.getElementById("run-status").textContent = "";
}

async function runOrSubmit(isSubmit) {
  if (!currentProblem || !editor) return;
  const code = editor.getValue();
  const btnRun = document.getElementById("btn-run");
  const btnSubmit = document.getElementById("btn-submit");
  const statusEl = document.getElementById("run-status");

  btnRun.disabled = true;
  btnSubmit.disabled = true;
  statusEl.textContent = currentLang === "cpp" ? "compiling & running…" : "running…";
  document.getElementById("console-body").innerHTML = '<div class="console-placeholder">Working…</div>';

  try {
    const res = await api(isSubmit ? "/api/submit" : "/api/run", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ problem_id: currentProblem.id, language: currentLang, code }),
    });
    renderResult(res, isSubmit);
    if (isSubmit) {
      await refreshStats();
      await loadProblemList();
    }
  } catch (e) {
    document.getElementById("console-body").innerHTML = `<div class="error-block">Request failed: ${e}</div>`;
  } finally {
    btnRun.disabled = false;
    btnSubmit.disabled = false;
    statusEl.textContent = "";
  }
}

function renderResult(res, isSubmit) {
  const body = document.getElementById("console-body");

  if (!res.compiled) {
    body.innerHTML = `<div class="summary-line fail">Compile error</div><div class="error-block">${escapeHtml(res.compile_error)}</div>`;
    return;
  }
  if (res.timed_out) {
    body.innerHTML = `<div class="summary-line fail">Timed out</div><div class="error-block">Your code took too long to run (possible infinite loop) and was killed.</div>`;
    return;
  }
  if (res.runtime_error) {
    body.innerHTML = `<div class="summary-line fail">Runtime error</div><div class="error-block">${escapeHtml(res.runtime_error)}</div>`;
    return;
  }

  const passClass = res.all_passed ? "pass" : "fail";
  const label = isSubmit
    ? (res.all_passed ? "Accepted" : "Wrong Answer")
    : (res.all_passed ? "All sample tests passed" : "Some sample tests failed");

  let casesHtml = "";
  for (const c of res.cases) {
    const icon = c.passed ? '<span class="case-icon pass">✓</span>' : '<span class="case-icon fail">✗</span>';
    casesHtml += `
      <div class="case-row">
        ${icon}
        <div class="case-detail">
          <div class="input-line">Case ${c.index + 1}${c.hidden ? " (hidden)" : ""}: ${escapeHtml(c.input_display || "")}</div>
          <div class="expected-actual">expected <b>${escapeHtml(JSON.stringify(c.expected))}</b> — got <b>${escapeHtml(JSON.stringify(c.actual))}</b></div>
        </div>
      </div>
    `;
  }

  let reviewHtml = "";
  if (isSubmit && res.progress_status) {
    if (res.all_passed) {
      const nextDate = new Date(res.next_review_at + "Z").toLocaleDateString();
      reviewHtml = `<div class="review-toast">Scheduled for spaced-repetition review on ${nextDate}</div>`;
    } else {
      reviewHtml = `<div class="review-toast">Marked as attempted — try again, then Submit once it passes.</div>`;
    }
  }

  body.innerHTML = `
    <div class="summary-line ${passClass}">${label} — ${res.passed}/${res.total} passed (${res.runtime_ms}ms)</div>
    ${casesHtml}
    ${reviewHtml}
  `;
}
