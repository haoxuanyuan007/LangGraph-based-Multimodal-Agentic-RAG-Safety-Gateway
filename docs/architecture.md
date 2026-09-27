# Architecture

## Style

The initial system is a modular monolith in one repository. API, worker, CLI, SDK, batch, and GUI are entry points around a shared Python core. Deployment units may be separated later without duplicating the domain model or graphs.

## Dependency direction

```text
apps -> graphs -> domain capabilities -> ports
                                  adapters -> external systems
```

The domain layer must not depend on FastAPI, LangGraph, a specific model vendor, or a specific database. Graphs own orchestration state and routing; normal Python modules own deterministic rules and domain behavior.

## Planned graph boundaries

- Offline ingestion graph: source registration, parsing, quality routing, chunking, embedding/indexing, vulnerability synchronization, quarantine, and review.
- Online analysis graph: multimodal evidence extraction, component recognition, planned retrieval, applicability and permission checks, evidence review, bounded retry, decision, interrupt/resume, and trace.

See `adr/0001-modular-monolith-and-src-layout.md` for the first architecture decision.
