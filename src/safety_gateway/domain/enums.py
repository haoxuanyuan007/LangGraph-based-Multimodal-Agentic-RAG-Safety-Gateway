"""Closed vocabularies fixed by the project charter."""

from enum import StrEnum


class RiskCategory(StrEnum):
    """Risk categories emitted by an analysis decision."""

    CREDENTIAL_LEAK = "credential_leak"
    PROMPT_INJECTION = "prompt_injection"
    DANGEROUS_TOOL_CALL = "dangerous_tool_call"
    MALICIOUS_LINK = "malicious_link"
    MULTIMODAL_MISMATCH = "multimodal_mismatch"
    KNOWN_VULNERABILITY_EXPOSURE = "known_vulnerability_exposure"
    BENIGN = "benign"


class DecisionAction(StrEnum):
    """Actions available to deterministic policy evaluation."""

    ALLOW = "allow"
    BLOCK = "block"
    REDACT = "redact"
    REVIEW = "review"
