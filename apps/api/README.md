# API application

This directory will contain the thin HTTP entry point and routes for `/analyze`, `/authorize-tool`, `/scan-artifact`, and human-review resume operations.

Request handling belongs here; graph construction, domain models, and policy logic belong in `src/safety_gateway/`.
