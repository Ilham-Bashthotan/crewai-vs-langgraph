# Multi-Agent Automated Pseudocode Scoring & Feedback System: CrewAI vs LangGraph

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/)
[![CrewAI](https://img.shields.io/badge/Orchestration-CrewAI-orange.svg)](https://www.crewai.com/)
[![LangGraph](https://img.shields.io/badge/Orchestration-LangGraph-purple.svg)](https://www.langchain.com/langgraph)
[![Ollama](https://img.shields.io/badge/Local%20LLM-Ollama%20(Llama%203.1)-black.svg)](https://ollama.ai/)

An experimental research and engineering benchmark comparing **CrewAI** and **LangGraph** in orchestrating multi-agent LLM workflows. The pipeline automates the evaluation of student pseudocode assignments, combining syntax auditing, rubric-based score deduction, and pedagogy-grounded misconception detection.

---

## 🎯 Research Objective & Background

Grading introductory programming and pseudocode assignments manually is repetitive and labor-intensive for university instructors. Standard automated unit-testing cannot evaluate pseudocode or uncompiled algorithms, and monolithic LLM prompts frequently hallucinate grading rubrics or deliver unstructured commentary.

This project designs a **modular multi-agent pipeline** that breaks grading down into discrete cognitive stages:
1. **Syntax & Style Compliance**: Validating variable dictionaries, keywords, and structural conventions against standard textbook specifications.
2. **Algorithmic Logic & Misconception Analysis**: Verifying loop invariants, conditional branching, and identifying specific cognitive pitfalls (e.g., *While Demon*, *IfWhile*, *Intentional Bug*).
3. **Supervisor Aggregation & Scoring**: Synthesizing audit findings into deterministic, Pydantic-validated JSON containing final numerical scores, deduction line items, and actionable student remediation.

Both **CrewAI** and **LangGraph** were implemented to compare their orchestration paradigms, state propagation, and output determinism.

---

## 🤖 Multi-Agent Architecture

```
                    +---------------------------+
                    | Student Pseudocode Input  |
                    | + Problem Specification   |
                    +-------------+-------------+
                                  |
                                  v
      +-------------------------------------------------------+
      |               Parallel / Sub-Agent Audit              |
      |                                                       |
      |  +---------------------------+   +-----------------+  |
      |  |   Style & Syntax Auditor  |   | Logic Analyst   |  |
      |  |   - Dictionary check      |   | - Flow correctness |
      |  |   - Convention validation |   | - Misconception |  |
      |  |   - Syntax deductions     |   |   taxonomy match|  |
      |  +-------------+-------------+   +--------+--------+  |
      |                \                         /            |
      +-----------------\-----------------------/-------------+
                         v                     v
                    +-----------------------------+
                    |     Scoring Supervisor      |
                    |  - Validates deductions     |
                    |  - Applies strict rubric    |
                    |  - Outputs Pydantic JSON    |
                    +-----------------------------+
                                  |
                                  v
                    +-----------------------------+
                    | Final Report & Actionable   |
                    | Student Remediation         |
                    +-----------------------------+
```

### Agent Roles & Responsibilities

| Agent Role | Goal & Specialization | Knowledge Base / Grounding |
|---|---|---|
| **Style & Syntax Auditor** | Validates structural layout, variable dictionary declarations, type assignments, and reserved keywords. Returns structured JSON deductions without prose. | Pseudocode convention specification (`doc/Pseudocode Dasar.md`) |
| **Logic & Misconception Analyst** | Analyzes algorithmic behavior and pinpoints cognitive misconceptions (e.g., *While Demon*, *IfWhile*, *Drop Through Error*, *Nesting Ignorance*). | Formal misconception taxonomy (`doc/List of misconceptions.md`) |
| **Scoring Supervisor** | Aggregates sub-agent evaluations, ensures no hallucinations or duplicate penalties exist, calculates numerical score (`Score = Max - Total Penalties`), and generates constructive guidance. | Institutional rubric (`SCORING_RUBRIC` schema) |

---

## 🔬 Framework Comparison: CrewAI vs. LangGraph

| Dimension | CrewAI Implementation | LangGraph Implementation |
|---|---|---|
| **Orchestration Model** | Role-based agents, hierarchical crews, and sequential tasks with native agent delegation. | Explicit directed acyclic/cyclic graphs (`StateGraph`) with typed states (`TypedDict`). |
| **State Management** | Implicit inter-agent context sharing via task outputs and crew memory. | Explicit, centralized state schema with fine-grained delta reducers (`operator.add`). |
| **Control Flow & Guardrails** | High-level iteration limits (`max_iter`) and role prompt constraints. | Granular conditional branching, routing nodes, and cycle limits. |
| **Structured Output** | JSON output enforcement via pydantic schemas and formatting system prompts. | Native integration with `ChatOllama` / `ChatOpenAI` structured tool-calling nodes. |
| **Best Suited For** | Rapid prototyping, autonomous agent personas, role-driven delegation workflows. | Complex deterministic branching, fine-grained state manipulation, mission-critical pipelines. |

---

## 📁 Repository Structure

```
├── doc/
│   ├── List of misconceptions.md         # Ground truth taxonomy of student programming misconceptions
│   ├── Pseudocode Dasar.md               # Standard pseudocode formatting guidelines & Golang mapping
│   ├── Pseudocode dan Golang Dasar.md
│   └── *.html                            # Visual workflow documentation and process diagrams
├── src/
│   ├── crewai/
│   │   ├── scoring/                      # Iterative implementations of CrewAI scoring pipelines (v1–v5)
│   │   ├── config/                       # YAML definitions for agent roles and tasks
│   │   ├── Parallel Crews.ipynb          # Concurrent execution tests
│   │   └── CrewAI Hierarchical Process.ipynb
│   └── langgraph/
│       ├── config/                       # LangGraph agent configurations
│       ├── Langgraph Hierarchical Process.ipynb
│       └── Langgraph Batasan Iterasi.ipynb
├── output/
│   └── parallel_processing_results.json  # Sample pipeline evaluation outputs
├── main.py                               # CLI entrypoint
├── pyproject.toml                        # Project dependencies managed via uv
└── uv.lock
```

---

## 🚀 Getting Started

### 1. Prerequisites
- Python `>= 3.11`
- [`uv`](https://github.com/astral-sh/uv) (recommended) or `pip`
- [Ollama](https://ollama.ai/) running locally with `llama3.1:8b` (or API keys for cloud LLM providers)

```bash
# Pull the evaluation model
ollama pull llama3.1:8b
```

### 2. Installation
Clone the repository and install dependencies:

```bash
git clone https://github.com/Ilham-Bashthotan/crewai-vs-langgraph.git
cd crewai-vs-langgraph

# Install via uv
uv sync

# Or install via pip
pip install -r pyproject.toml
```

### 3. Environment Configuration
Copy the environment template:

```bash
cp .env.example .env
```

Configure your local model settings or provider credentials in `.env`:
```env
OLLAMA_BASE_URL="http://localhost:11434"
DEFAULT_MODEL="ollama/llama3.1:8b"
```

### 4. Running the Pipelines
Explore the end-to-end multi-agent scoring workflows inside the interactive Jupyter notebooks:
- **CrewAI Pipeline**: Open `src/crewai/scoring/CrewAI Scoring(5).ipynb`
- **LangGraph Pipeline**: Open `src/langgraph/Langgraph Hierarchical Process.ipynb`

---

## 📊 Sample Output Schema

Both frameworks produce structured JSON conforming to the `AssessmentResult` schema:

```json
{
  "score": 12,
  "max_score": 20,
  "correct": false,
  "summary": "Algorithm correctly declares variables but inverts the primary conditional statement.",
  "style_violations": [],
  "misconceptions_detected": [
    {
      "code": "WD",
      "name": "While Demon / Inverted Logic",
      "penalty": 8,
      "line": 6,
      "details": "Conditional statement checks 'n < 75' for pass condition instead of 'n >= 75'."
    }
  ],
  "recommendations": [
    "Recheck the problem narrative: passing condition requires a score >= 75.",
    "Ensure comparison operators align with the desired Boolean outcome."
  ]
}
```

---

## 👤 Author
**Ilham Bashthotan**  
Informatics Undergraduate, Telkom University  
- 💼 [LinkedIn](https://www.linkedin.com/in/ilham-bashthotan)
- 💻 [GitHub](https://github.com/Ilham-Bashthotan)
- 🎮 [itch.io](https://ilham-bashthotan.itch.io)
