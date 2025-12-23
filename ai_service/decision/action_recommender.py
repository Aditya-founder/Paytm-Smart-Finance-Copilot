from typing import Dict, Any


def recommend_action(
    baseline: Dict[str, Any],
    deviation: Dict[str, Any],
    risk_profile: Dict[str, Any],
    segment: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Recommends the best next action based on
    behavior, deviation, risk, and user segment.
    """

    risk_level = risk_profile.get("risk_level", "low")
    is_deviation = deviation.get("is_deviation", False)
    deviation_type = deviation.get("deviation_type")
    segment_type = segment.get("segment")

    # ---- High risk + abnormal behavior ----
    if risk_level == "high" and is_deviation:
        return {
            "action": "urgent_attention",
            "priority": "high",
            "reason": "High risk profile with abnormal recent behavior",
            "expected_impact": "Prevent missed payments or further losses"
        }

    # ---- Sales drop for merchants ----
    if is_deviation and deviation_type == "sales_drop":
        return {
            "action": "boost_sales",
            "priority": "high",
            "reason": "Sales dropped below your normal performance",
            "expected_impact": "Increase customer engagement and revenue"
        }

    # ---- High growth opportunity ----
    if is_deviation and deviation_type == "sales_spike":
        return {
            "action": "scale_operations",
            "priority": "medium",
            "reason": "Sales performing significantly above normal",
            "expected_impact": "Sustain growth and avoid service bottlenecks"
        }

    # ---- Stable and disciplined users ----
    if segment_type == "stable_merchant" and risk_level == "low":
        return {
            "action": "maintain_strategy",
            "priority": "low",
            "reason": "Stable performance and good payment discipline",
            "expected_impact": "Continue consistent growth"
        }

    # ---- Default fallback ----
    return {
        "action": "monitor",
        "priority": "low",
        "reason": "No strong signals detected",
        "expected_impact": "Observe for future behavior changes"
    }
    
    
    