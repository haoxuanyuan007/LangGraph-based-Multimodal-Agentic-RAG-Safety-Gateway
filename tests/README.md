# Tests

- `unit/`: isolated deterministic behavior.
- `integration/`: storage, parser, model, and index adapter boundaries.
- `contract/`: API and schema compatibility.
- `graph/`: routing, fan-out/fan-in, bounded loops, checkpoints, and interrupts.
- `security/`: hostile files, redaction, permissions, and citation validation.
- `e2e/`: user-visible flows across entry points.

Tests may begin at the repository root while a capability is small, then move into the matching directory as the suite grows.
