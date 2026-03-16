# Contributing to EvoScientist

We appreciate your interest and the time you spend helping improve EvoScientist. Please read the following instruction on how to help us.

## How you can contribute

- Report ideas, bugs, and feature requests: open an issue describing intent, motivation, and high-level impact. Make sure to correctly label the Issue. Use the provided template.
- Propose design changes: use issues or discussion threads to outline the problem, alternatives, and trade-offs before implementing.
- Contribute code or docs: submit PRs that tackle an open issue. They must have a clear rationale and tests where applicable. 

## What we are looking for in PRs

We aim to keep the EvoScientist with only core functionality that will be used by majority of users. Therefore PRs should only include:
- Bug fixes / Improvements to existing features
- New features that were proposed in an Issue and agreed with Contributor
- Updating documentation
- Improving test suite with meaningful tests

If you want to add nice to have or niche feature look at contributing to the [EvoSkills repository](https://github.com/EvoScientist/EvoSkills)

---

## Project overview

EvoScientist is a multi-agent AI system for automated scientific experimentation and discovery. It orchestrates specialized sub-agents that plan experiments, search literature, write code, debug, analyze data, and draft reports.

| Fact | Value |
|------|-------|
| Language | Python 3.11+ |
| License | Apache 2.0 |
| Framework | [DeepAgents](https://github.com/langchain-ai/deepagents) + [LangChain](https://python.langchain.com/) + [LangGraph](https://langchain-ai.github.io/langgraph/) |
| Default model | `claude-sonnet-4-6` (Anthropic) |
| Tests | ~890 across 36 files, no API keys needed |
| Config file | `~/.config/evoscientist/config.yaml` |

### Sub-Agents (defined in `EvoScientist/subagent.yaml`)

| Agent | Purpose |
|-------|---------|
| `planner-agent` | Creates and updates experimental plans (no web search, no implementation) |
| `research-agent` | Web research for methods, baselines, and datasets (Tavily search) |
| `code-agent` | Implements experiment code and runnable scripts |
| `debug-agent` | Reproduces failures, identifies root causes, applies minimal fixes |
| `data-analysis-agent` | Computes metrics, creates plots, summarizes insights |
| `writing-agent` | Drafts paper-ready Markdown experiment reports |

### Data Flow

```txt
User Input (CLI / TUI / 10 Channel Integrations)
    |
CLI (cli/) / TUI (cli/tui_*) / Channel Server (channels/)
    |
Main Agent (EvoScientist.py) -- create_deep_agent()
    +-- System Prompt (prompts.py)
    +-- Chat Model (llm/ -- multi-provider)
    +-- Middleware: Memory (middleware/memory.py)
    +-- Backend: CompositeBackend (backends.py)
    |     / --> CustomSandboxBackend (workspace read/write + execute)
    |     /skills/ --> MergedReadOnlyBackend (user > built-in)
    |     /memory/ --> FilesystemBackend (persistent cross-session)
    +-- MCP Tools (mcp/ -- optional, cached by config signature)
    |
task tool --> Delegates to Sub-Agents
    |
Stream Events --> Emitter --> Tracker --> State --> Rich Display / TUI
```

---

## Need help?
You can reach us on Discord or WeChat linked in README
