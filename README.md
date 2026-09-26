# Multi-Agent Pseudocode Scoring & Feedback: CrewAI vs LangGraph

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/)
[![CrewAI](https://img.shields.io/badge/Orchestration-CrewAI-orange.svg)](https://www.crewai.com/)
[![LangGraph](https://img.shields.io/badge/Orchestration-LangGraph-purple.svg)](https://www.langchain.com/langgraph)
[![Ollama](https://img.shields.io/badge/Local%20LLM-Ollama-black.svg)](https://ollama.com/)

Research project on **automated assessment of student pseudocode** using multi-agent LLM workflows. A team of AI agents checks a submission's syntax and style, detects programming misconceptions, and produces a score with written feedback. The repository also explores **CrewAI** and **LangGraph** as orchestration frameworks for this kind of pipeline.

> **Status:** work in progress. The scoring pipeline is implemented in CrewAI. The LangGraph notebooks are currently orchestration experiments (supervisor pattern and iteration limits) and do not yet implement the scoring pipeline.

---

## Background

Grading introductory pseudocode by hand is repetitive, and unit tests cannot run pseudocode. A single large LLM prompt tends to mix up rubric rules and return unstructured comments. This project splits grading into separate steps handled by specialized agents, each grounded in its own reference document, and forces the final result into a validated schema.

---

## Scoring Pipeline (CrewAI)

The pipeline runs three agents **sequentially** (`Process.sequential`) on a local model (`ollama/llama3.1:8b`, temperature 0):

```
                    +---------------------------+
                    | Student Pseudocode Input  |
                    | + Problem Specification   |
                    +-------------+-------------+
                                  |
                                  v
      +-------------------------------------------------------+
      |        Sub-Agent Audit (run sequentially, 1 → 2)      |
      |                                                       |
      |  +---------------------------+  +------------------+  |
      |  | 1. Style & Syntax Auditor |  | 2. Logic Analyst |  |
      |  |  - Dictionary check       |  |  - Flow          |  |
      |  |  - Convention validation  |  |    correctness   |  |
      |  |  - Syntax deductions      |  |  - Misconception |  |
      |  |                           |  |    taxonomy match|  |
      |  +-------------+-------------+  +--------+---------+  |
      |                \                        /             |
      +-----------------\----------------------/--------------+
                         v                    v
                    +-----------------------------+
                    |   3. Scoring Supervisor     |
                    |  - Combines both reports    |
                    |  - Removes duplicate        |
                    |    penalties                |
                    |  - Outputs Pydantic JSON    |
                    +--------------+--------------+
                                   |
                                   v
                    +-----------------------------+
                    |  AssessmentResult: score,   |
                    |  correctness, summary,      |
                    |  misconceptions found       |
                    +-----------------------------+
```

| Agent | Responsibility | Grounding |
|---|---|---|
| **Style & Syntax Auditor** | Structure, variable declarations, assignment operator (`<-`), reserved keywords | `doc/Pseudocode dan Golang Dasar.md` |
| **Logic & Misconception Analyst** | Control-flow correctness and misconceptions such as *While Demon (WD)*, *IfWhile*, *Drop Through (DT)*, *Ignore Nesting (IN1/IN2)* | `doc/List of misconceptions.md` |
| **Scoring Supervisor** | Aggregates the two reports and produces the final structured result | Task outputs of the two agents above |

The final task uses `output_pydantic=AssessmentResult`:

```python
class AssessmentResult(BaseModel):
    score: int              # final score, 0–100
    correct: bool           # whether the logic is correct
    summary: str            # narrative summary of the assessment
    misconceptions: List[str]  # misconceptions found (from the reference list)
    pseudocode: str         # the student's original pseudocode
```

### Example output

Actual output from `src/crewai/scoring/CrewAI Scoring(5).ipynb`:

```json
{
  "score": 82,
  "correct": false,
  "summary": "The student's pseudocode contains style violations and logic misconceptions. The while loop uses a premature break pattern, and there are assignment syntax errors and operator usage errors.",
  "misconceptions": ["While demon (WD)"],
  "pseudocode": "if x > 5 then\n  y = 10\nelse\n  z = 20\nend if\nwhile x < 10 do\n  x = x + 1\n  if x == 7 then break end if\n  print(x)\nend while"
}
```

---

## CrewAI vs LangGraph: What Is Explored

| | CrewAI (`src/crewai/`) | LangGraph (`src/langgraph/`) |
|---|---|---|
| **Orchestration model** | Role-based agents and tasks in a `Crew` (sequential and hierarchical processes) | Explicit `StateGraph` with a typed state (`TypedDict`) |
| **State passing** | Implicit, through task `context` | Explicit shared state with reducers (`operator.add`) |
| **Loop control** | `max_iter` per agent/task | Iteration limits enforced in the graph |
| **Structured output** | `output_pydantic` on the final task | Not yet implemented for scoring |
| **Notebooks** | Scoring pipeline (v1–v5), hierarchical process, parallel crews, tools, iteration limits | Supervisor/hierarchical process, iteration limits, content-planner example |
| **Model used** | `ollama/llama3.1:8b` | `qwen3:0.6b` (via `ChatOllama`) |

---

## Repository Structure

```
├── doc/
│   ├── List of misconceptions.md        # Misconception & error taxonomy used by the logic agent
│   ├── Pseudocode Dasar.md              # Pseudocode conventions
│   ├── Pseudocode dan Golang Dasar.md   # Pseudocode ↔ Go reference used by the style agent
│   └── *.html / *.pdf                   # Exported notebooks and course material
├── src/
│   ├── crewai/
│   │   ├── scoring/                     # Scoring pipeline iterations (latest: CrewAI Scoring(5).ipynb)
│   │   ├── config/                      # YAML agent/task definitions (content-planner example)
│   │   └── *.ipynb                      # Hierarchical process, parallel crews, tools, iteration limits
│   └── langgraph/
│       ├── Langgraph Hierarchical Process.ipynb
│       ├── Langgraph Batasan Iterasi.ipynb
│       └── Langgraph Sosmed Content Planner.ipynb
├── pyproject.toml                       # Dependencies (managed with uv)
└── uv.lock
```

---

## Getting Started

**Requirements:** Python 3.11+, [uv](https://github.com/astral-sh/uv), and [Ollama](https://ollama.com/) running locally.

```bash
git clone https://github.com/Ilham-Bashthotan/crewai-vs-langgraph.git
cd crewai-vs-langgraph
uv sync

ollama pull llama3.1:8b      # CrewAI scoring pipeline
ollama pull qwen3:0.6b       # LangGraph experiments
```

Then open the notebooks with Jupyter:

- Scoring pipeline: `src/crewai/scoring/CrewAI Scoring(5).ipynb`
- LangGraph experiments: `src/langgraph/Langgraph Hierarchical Process.ipynb`

> **Note:** the scoring notebook reads the reference documents from an absolute path. Change it to `doc/Pseudocode dan Golang Dasar.md` and `doc/List of misconceptions.md` before running.

---

## Roadmap

- [ ] Implement the same three-agent scoring pipeline in LangGraph
- [ ] Evaluate both pipelines on the same set of student submissions and compare scores with instructor grading
- [ ] Move the pipeline from notebooks into a runnable script (`main.py`)

---

## Author

**Ilham Bashthotan** · Informatics, Telkom University
[LinkedIn](https://www.linkedin.com/in/ilham-bashthotan) · [GitHub](https://github.com/Ilham-Bashthotan) · [itch.io](https://ilham-bashthotan.itch.io)
