"""Contract tests for the charter's closed vocabularies."""

import unittest

from safety_gateway.domain import DecisionAction, RiskCategory


class RiskCategoryTests(unittest.TestCase):
    def test_contains_exactly_the_charter_categories(self) -> None:
        self.assertEqual(
            {category.value for category in RiskCategory},
            {
                "credential_leak",
                "prompt_injection",
                "dangerous_tool_call",
                "malicious_link",
                "multimodal_mismatch",
                "known_vulnerability_exposure",
                "benign",
            },
        )

    def test_rejects_unknown_category(self) -> None:
        with self.assertRaises(ValueError):
            RiskCategory("unknown")


class DecisionActionTests(unittest.TestCase):
    def test_contains_exactly_the_charter_actions(self) -> None:
        self.assertEqual(
            {action.value for action in DecisionAction},
            {"allow", "block", "redact", "review"},
        )

    def test_rejects_unknown_action(self) -> None:
        with self.assertRaises(ValueError):
            DecisionAction("warn")


if __name__ == "__main__":
    unittest.main()
