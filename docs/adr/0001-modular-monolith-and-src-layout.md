# ADR 0001: Use a modular monolith with a Python src layout

- Status: Accepted
- Date: 2026-09-28

## Context

The API, SDK, batch jobs, background ingestion, and GUI must share the same graphs, domain models, and deterministic safety behavior. Premature services would add network and schema-version complexity before capability boundaries are validated.

## Decision

Use one repository and one installable Python core under `src/safety_gateway`. Keep deployable entry points thin under `apps`. Organize the core by domain capability, with dedicated graph packages for orchestration.

## Consequences

Tests can exercise core behavior without starting a server, and entry points cannot legitimately fork safety logic. A future service split remains possible, but only across measured operational boundaries and with explicit contract versioning.
