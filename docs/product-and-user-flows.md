# Product and user flows

## Agent integration

- Call `/analyze` before content enters a model.
- Call `/authorize-tool` immediately before a high-risk tool executes.
- Call `/scan-artifact` before an external artifact enters business RAG or a build pipeline.

## Human console

The GUI will support request analysis, evidence-backed results, a human-review queue with LangGraph interrupt/resume, knowledge and vulnerability-intelligence management, retrieval experiments, and run history.

All entry points must invoke the same graph and domain contracts rather than reimplementing decisions.
