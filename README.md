# LangGraph-based Multimodal Agentic RAG Safety Gateway

A multimodal Agentic RAG input-safety system orchestrated with LangGraph.

The project is currently at the engineering-skeleton stage. The finished product will inspect text, images, multi-page PDFs, dependency manifests, and SBOMs before they enter LLM, RAG, or tool-using Agent workflows. A shared set of graphs and domain models will serve the API, SDK, batch processing, and GUI.

## Current boundaries

- The Python package uses a `src` layout, with environments and lock files managed by `uv`.
- `apps/` contains thin entry points; core behavior belongs in `src/safety_gateway/`.
- LangGraph graphs own orchestration, while deterministic safety rules and domain capabilities remain ordinary Python modules.
- LangGraph, models, parsers, databases, and external data sources are not connected yet.

## Local checks

The baseline Python version is recorded in `.python-version`. The current skeleton tests require no third-party packages:

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -v
```

After dependencies are introduced, use `uv sync` to create the environment and commit the generated `uv.lock`.

## Repository map

- `apps/`: thin entry points for the API, workers, CLI, and GUI.
- `src/safety_gateway/`: domain models, workflows, and safety behavior.
- `tests/`: unit, integration, graph, contract, security, and end-to-end tests.
- `evals/`: isolated evaluation code and result specifications; never part of business indexes.
- `data/`: manifests, license records, and safe-to-commit synthetic definitions only.
- `docs/`: product, architecture, data-governance, experiment, and learning records.
