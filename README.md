# AgentRE-Reliability-Engineering-for-AI-Coding-Agents
AgentRE — Reliability Loop for Coding Agents. Test, break, diagnose, improve, and verify AI-generated software through automated evaluation, failure analysis, regression testing, and measurable baseline-vs-advanced benchmarking. Supports local LLMs with Ollama and is designed for reproducible, reliability-first AI engineering.

# AgentRE — Reliability Loop for Coding Agents

> **Test. Break. Diagnose. Improve. Verify.**

AgentRE is a reliability-first framework for AI coding agents.

Instead of assuming that AI-generated code is correct, AgentRE creates an engineering feedback loop that **implements, tests, deliberately breaks, diagnoses, improves, and verifies** software.

The goal is simple:

> **Don't trust generated code because it looks correct. Prove that it works.**

---

## 🚀 What AgentRE Does

A traditional AI coding workflow looks like:

```text
Prompt
  ↓
LLM generates code
  ↓
Code looks correct
  ↓
Done
```

AgentRE changes this to:

```text
                    Engineering Task
                           │
                           ▼
                  Requirement Analysis
                           │
                           ▼
                       Baseline
                           │
                           ▼
                       Evaluation
                           │
                           ▼
                    Failure Discovery
                           │
                           ▼
                    Root-Cause Analysis
                           │
                           ▼
                   Improvement Proposal
                           │
                           ▼
                     Human Review
                           │
                           ▼
                    Advanced Solution
                           │
                           ▼
                   Regression Testing
                           │
                           ▼
                       Benchmark
                           │
                           ▼
                  Baseline vs Advanced
```

Every improvement should be backed by evidence.

---

# 🎯 Core Objectives

AgentRE is designed to help coding agents:

* Understand engineering requirements
* Build a baseline implementation
* Generate and execute tests
* Discover edge cases and failure modes
* Reproduce failures
* Analyze logs and stack traces
* Identify root causes
* Propose targeted improvements
* Protect changes with regression tests
* Benchmark baseline vs advanced implementations
* Record agent actions and engineering decisions
* Operate with controlled permissions

---

# 🧠 Core Philosophy

AgentRE follows one principle:

> **AI should generate hypotheses. Engineering systems should provide the evidence.**

The LLM can reason about:

* requirements
* source code
* failures
* possible fixes
* trade-offs

But deterministic tools should verify:

* whether tests pass
* whether the failure is reproducible
* whether regressions exist
* whether runtime improved
* whether the final result satisfies acceptance criteria

This separation makes the system more reliable.

---

# 🏗️ Architecture

```text
                         ┌──────────────────┐
                         │  Engineering     │
                         │      Task        │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │ Analyst Agent    │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │ Builder Agent    │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │ Test Runner      │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │ Failure Hunter   │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │ Debugger Agent   │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │ Improvement      │
                         │ Proposal         │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │ Human Review     │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │ Advanced Fix     │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │ Regression       │
                         │ Testing          │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │ Benchmark Engine │
                         └────────┬─────────┘
                                  │
                                  ▼
                     ┌────────────────────────┐
                     │ Baseline vs Advanced   │
                     └────────────────────────┘
```

---

# 🤖 Agent System

AgentRE uses specialized agents instead of giving one agent unrestricted responsibility.

## 1. Analyst Agent

Analyzes:

* requirements
* constraints
* assumptions
* dependencies
* acceptance criteria
* potential risks

Output:

```text
Requirement Analysis
        +
Implementation Plan
        +
Risk Assessment
```

---

## 2. Builder Agent

Creates the baseline implementation.

The baseline should be:

* simple
* understandable
* testable
* reproducible

The purpose of the baseline is to provide a measurable starting point.

---

## 3. Failure Hunter Agent

Attempts to find weaknesses in the implementation.

It focuses on:

```text
Normal inputs
     +
Boundary cases
     +
Malformed inputs
     +
Unexpected types
     +
Large inputs
     +
Dependency failures
     +
Timeouts
     +
Regression cases
```

The goal is not simply to generate many tests.

The goal is to find **high-value failures**.

---

## 4. Debugger Agent

When a failure occurs, the debugger investigates:

```text
Failure
   ↓
Reproduction
   ↓
Logs
   ↓
Stack trace
   ↓
Source code
   ↓
Root cause
   ↓
Proposed fix
```

Example output:

```yaml
failure_id: F-017

category: input-validation

symptom: HTTP 500 for null request

root_cause:
  missing request validation

affected_component:
  src/api.py

proposed_fix:
  validate request schema before processing

regression_tests:
  - test_null_request
```

---

## 5. Reviewer Agent

Reviews proposed changes for:

* correctness
* unnecessary complexity
* security concerns
* regressions
* scope violations
* maintainability

---

## 6. Benchmarker Agent

Measures the engineering outcome.

Example:

```text
Baseline
────────
Success: 68%

Advanced
────────
Success: 94%

Improvement
───────────
+26 percentage points
```

**Actual numbers will be generated from executed experiments.**

---

# 🔌 LLM Architecture

AgentRE is designed to be **LLM-provider independent**.

The initial implementation uses **Ollama** for local model execution.

```text
                    AgentRE
                       │
                       ▼
                 LLM Interface
                       │
             ┌─────────┼─────────┐
             ▼         ▼         ▼
          Ollama     OpenAI    Gemini
           Local      Cloud      Cloud
```

The agent layer communicates with a common interface instead of directly depending on a specific provider.

### Current provider

```text
Provider: Ollama
Execution: Local
API Key: Not required
```

Additional providers can be added through the `llm/` layer.

---

# 🦙 Ollama

Ollama allows AgentRE to run a local LLM.

Basic architecture:

```text
┌──────────────────────┐
│       AgentRE        │
│                      │
│ Analyst              │
│ Builder              │
│ Debugger             │
│ Reviewer             │
└──────────┬───────────┘
           │
           │ HTTP
           ▼
┌──────────────────────┐
│       Ollama         │
│    Local LLM Server   │
└──────────────────────┘
```

Set the model in:

```text
config/models.yaml
```

Example:

```yaml
provider: ollama
model: CHANGE_ME
base_url: http://localhost:11434
```

Or through environment variables:

```bash
LLM_PROVIDER=ollama
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=CHANGE_ME
```

---

# 🧪 Evaluation System

Evaluation is the heart of AgentRE.

The system evaluates both:

```text
Baseline
   ↓
Evaluation

Advanced
   ↓
Evaluation
```

Then compares them.

### Primary metrics

* Task Success Rate
* Edge-Case Success Rate
* Failure Recovery Rate
* Regression Rate
* Mean Runtime
* P95 Runtime
* Test Coverage
* Resource Usage where applicable

---

# 📊 Baseline vs Advanced

The competition workflow is based on controlled comparison.

Example:

| Metric           | Baseline | Advanced | Change |
| ---------------- | -------: | -------: | -----: |
| Task Success     |      TBD |      TBD |    TBD |
| Edge Cases       |      TBD |      TBD |    TBD |
| Failure Recovery |      TBD |      TBD |    TBD |
| Regression Rate  |      TBD |      TBD |    TBD |
| Mean Runtime     |      TBD |      TBD |    TBD |
| P95 Runtime      |      TBD |      TBD |    TBD |

No benchmark result is considered valid until it has actually been executed.

---

# 💥 Failure Reproduction

Every important failure should become reproducible.

Example:

```text
failures/
└── F-001/
    ├── input.json
    ├── expected.json
    ├── actual.json
    ├── logs.txt
    ├── traceback.txt
    └── reproduce.py
```

This allows us to move from:

```text
"We saw a failure."
```

to:

```text
"We can reproduce the failure."
```

and eventually:

```text
"The fix eliminates the failure without introducing regressions."
```

---

# 🔄 Improvement Loop

AgentRE follows an evidence-based improvement process.

```text
Evaluation
    ↓
Failure
    ↓
Root Cause
    ↓
Improvement Proposal
    ↓
Human Review
    ↓
Implementation
    ↓
Regression Tests
    ↓
Benchmark
```

An improvement is accepted only when it provides measurable value.

---

# 👤 Human-in-the-Loop

AgentRE does not give the AI unrestricted authority.

For consequential changes:

```text
Agent
  ↓
Proposal
  ↓
Risk Assessment
  ↓
Human Review
  ↓
Approve / Reject
  ↓
Implementation
```

This is especially important for:

* permission changes
* security-sensitive modifications
* external integrations
* destructive operations
* deployment actions
* major architectural changes

---

# 🧪 Testing

The project uses **pytest** as the primary testing framework.

Test categories:

```text
tests/
├── unit/
├── integration/
├── evaluation/
└── security/
```

Challenge-specific evaluation cases:

```text
evaluation/test_cases/
├── normal/
├── edge_cases/
├── adversarial/
└── regression/
```

Where useful, **Hypothesis** can be used for property-based testing.

---

# 🛠️ Tools Available to Agents

Agents interact with the development environment through controlled tools.

```text
tools/
├── filesystem.py
├── shell.py
├── git.py
├── test_runner.py
└── code_search.py
```

The goal is to avoid giving the LLM unrestricted control over the host environment.

---

# 🔐 Security Model

AgentRE follows a least-privilege approach.

Example:

```text
Operation                    Permission
─────────────────────────────────────────
Read source                  ✓
Search source                ✓
Run tests                    ✓
Generate files               ✓
Modify source                Controlled
Git commit                   Controlled
Deploy                       Restricted
Access secrets               ✗
Change security boundaries   ✗
```

Secrets should never be committed to GitHub.

Use:

```text
.env
```

and keep it in `.gitignore`.

A safe template is provided as:

```text
.env.example
```

---

# 📁 Project Structure

```text
agentre/
│
├── README.md
├── LICENSE
├── .gitignore
├── .env.example
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
│
├── config/
│   ├── config.yaml
│   ├── agents.yaml
│   └── models.yaml
│
├── src/
│   └── agentre/
│       ├── core/
│       ├── agents/
│       ├── llm/
│       ├── tools/
│       └── evaluation/
│
├── challenge/
│   ├── problem/
│   ├── baseline/
│   └── advanced/
│
├── evaluation/
│   ├── test_cases/
│   ├── run_baseline.py
│   ├── run_advanced.py
│   ├── compare.py
│   └── run_all.py
│
├── failures/
├── trajectories/
├── improvements/
├── prompts/
├── tests/
├── reports/
└── docs/
```

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone <your-github-repository>
cd agentre
```

## 2. Create a virtual environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🦙 Configure Ollama

Install and start Ollama on your system.

Verify that it is available:

```bash
ollama list
```

Configure the selected model:

```bash
set OLLAMA_MODEL=<model-name>
```

Linux/macOS:

```bash
export OLLAMA_MODEL=<model-name>
```

Or place the configuration in `.env`.

---

# ▶️ Run AgentRE

Once the core implementation is configured:

```bash
python -m src.agentre.core.orchestrator
```

Run the evaluation:

```bash
python evaluation/run_all.py
```

The evaluation should produce:

```text
Baseline Results
Advanced Results
Improvement
Regression Results
Benchmark Results
```

---

# 🐳 Docker

Build:

```bash
docker build -t agentre .
```

Run:

```bash
docker run --rm agentre
```

For local Ollama development, AgentRE can communicate with the Ollama server through its configured HTTP endpoint.

---

# 📈 Example Evaluation Output

The final system is intended to produce output similar to:

```text
========================================
             AgentRE Evaluation
========================================

BASELINE
--------
Total Tests : 50
Passed      : 34
Failed      : 16
Success     : 68%

FAILURE ANALYSIS
----------------
Input Validation : 7
Dependencies     : 4
Boundary Cases   : 3
Regression       : 2

ADVANCED
--------
Total Tests : 50
Passed      : 47
Failed      : 3
Success     : 94%

IMPROVEMENT
-----------
+26 percentage points

REGRESSION
----------
Passed: 100%

========================================
```

These values are **illustrative only** and must be replaced with real experiment results.

---

# 📝 Agent Trajectories

Agent actions are recorded to make the engineering process auditable.

Example:

```text
trajectories/
└── task-001/
    ├── task.md
    ├── plan.md
    ├── actions.jsonl
    ├── tests.json
    ├── failure-analysis.md
    ├── improvement-proposal.md
    └── final-result.json
```

A trajectory should make it possible to understand:

```text
Task
 ↓
Analysis
 ↓
Implementation
 ↓
Testing
 ↓
Failure
 ↓
Debugging
 ↓
Improvement
 ↓
Verification
```

---

# 📋 Improvement Changelog

Every important improvement is documented.

Example:

```markdown
## Improvement 001 — Input Validation

### Problem
Null input caused an unexpected server error.

### Evidence
Failure F-001 reproduced consistently.

### Root Cause
Missing request validation.

### Change
Added structured input validation.

### Verification
Added regression test:
`test_null_input`

### Result
Before: TBD
After: TBD
```

This prevents unsupported claims and creates a clear engineering history.

---

# 🧮 Improvement Measurement

AgentRE measures improvement rather than assuming it.

Basic formulation:

```text
Improvement =
Advanced Score - Baseline Score
```

Example:

```text
Baseline = 0.68
Advanced = 0.94

Improvement = +0.26
```

For percentage-point reporting:

```text
68% → 94%

+26 percentage points
```

---

# 🔬 Engineering Experiments

Each experiment should contain:

```text
Hypothesis
     ↓
Baseline Measurement
     ↓
Change
     ↓
Controlled Evaluation
     ↓
Advanced Measurement
     ↓
Comparison
     ↓
Decision
```

If an improvement does not produce meaningful gains, it should be documented rather than hidden.

---

# 🚧 Current Status

### Foundation

* [x] Project structure
* [x] Agent architecture
* [x] LLM abstraction
* [x] Ollama provider scaffold
* [x] Evaluation structure
* [x] Failure structure
* [x] Trajectory structure
* [x] Docker scaffold
* [x] Documentation structure

### In Development

* [ ] Complete Ollama agent implementation
* [ ] Agent orchestration
* [ ] Tool execution layer
* [ ] Failure reproduction engine
* [ ] Automated test generation
* [ ] Root-cause analysis
* [ ] Improvement application
* [ ] Regression pipeline
* [ ] Benchmark engine
* [ ] Final challenge implementation

### Final Validation

* [ ] Run baseline
* [ ] Run advanced solution
* [ ] Measure improvement
* [ ] Validate regression suite
* [ ] Capture agent trajectories
* [ ] Generate final report
* [ ] Verify fresh-clone reproduction

---

# 🏆 Competition Strategy

AgentRE is designed around a simple engineering story:

```text
                 BASELINE
                    │
                    ▼
               Find Failures
                    │
                    ▼
              Explain Failures
                    │
                    ▼
               Fix Failures
                    │
                    ▼
             Prevent Regression
                    │
                    ▼
              Measure Again
                    │
                    ▼
              PROVEN IMPROVEMENT
```

The objective is **not** to use the largest number of agents or technologies.

The objective is to demonstrate:

> **A measurable improvement from a baseline to a stronger engineering solution.**

---

# ⚠️ Limitations

AgentRE currently depends on the capability of the selected LLM for tasks such as:

* code understanding
* root-cause reasoning
* test generation
* improvement proposals

A local Ollama model may perform differently from a cloud model.

Therefore, model choice should be treated as an experimental variable rather than an assumption.

The evaluation system is designed to make those differences measurable.

---

# 🔮 Future Improvements

Potential future work includes:

* Additional LLM providers
* Better automated test generation
* Property-based failure discovery
* More advanced code localization
* Automatic patch ranking
* Multi-model evaluation
* Persistent failure knowledge
* Cross-task learning
* Performance optimization
* Expanded security sandboxing
* CI/CD integration
* Rich experiment dashboards

---

# 🤝 Contributing

Contributions are welcome.

Suggested workflow:

```bash
git checkout -b feature/<feature-name>
```

Implement the change, add tests, run the evaluation suite, and document the engineering decision.

---

# 📄 License

MIT License.

---

# 👨‍💻 Project Philosophy

AgentRE is built around one idea:

> **Generated code is a hypothesis. Tests are evidence.**

A reliable coding agent should not stop when the code compiles.

It should:

```text
Understand
    ↓
Implement
    ↓
Test
    ↓
Break
    ↓
Diagnose
    ↓
Improve
    ↓
Verify
    ↓
Measure
```

### AgentRE

**Test. Break. Diagnose. Improve. Verify.**
