from typing import Dict, Any


def determine_user_segment(
    baseline: Dict[str, Any],
    deviation: Dict[str, Any],
    risk_profile: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Assigns a behavioral segment to the user/merchant.
    """

    if not baseline.get("baseline_available", True):
        return {
            "segment": "new_user",
            "explanation": "Not enough historical data"
        }

    risk_level = risk_profile.get("risk_level", "low")
    is_deviation = deviation.get("is_deviation", False)
    deviation_type = deviation.get("deviation_type")

    # Segment logic
    if risk_level == "high" and is_deviation:
        return {
            "segment": "at_risk_merchant",
            "explanation": "High risk profile with abnormal recent behavior"
        }

    if risk_level == "high":
        return {
            "segment": "financially_undisciplined",
            "explanation": "Consistently high payment risk"
        }

    if is_deviation and deviation_type == "sales_spike":
        return {
            "segment": "high_growth_merchant",
            "explanation": "Recent performance significantly above normal"
        }

    if not is_deviation and risk_level == "low":
        return {
            "segment": "stable_merchant",
            "explanation": "Stable performance and good payment discipline"
        }

    return {
        "segment": "moderate_activity_user",
        "explanation": "No extreme behavior detected"
    }
