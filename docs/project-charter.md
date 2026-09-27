# Project charter

## Goal

Build an embeddable multimodal safety gateway for LLM, RAG, and tool-using Agent applications, together with a standalone analysis, review, knowledge-management, and audit console.

## Supported inputs

The target scope includes text, one or more images, native/scanned/mixed multi-page PDFs, dependency manifests and lockfiles, CycloneDX/SPDX SBOM, and optional VEX.

## Fixed decisions

Risk categories are `credential_leak`, `prompt_injection`, `dangerous_tool_call`, `malicious_link`, `multimodal_mismatch`, `known_vulnerability_exposure`, and `benign`. Actions are `allow`, `block`, `redact`, and `review`.

## Non-goals

Audio/video analysis, binary scanning, exploit execution, and real execution of destructive or high-risk tools are outside scope. The product must not claim transparent interception of closed systems without an integration point.

## Current status

Engineering skeleton only. No production analysis, ingestion, model, retrieval, vulnerability, or storage capability is implemented yet.
