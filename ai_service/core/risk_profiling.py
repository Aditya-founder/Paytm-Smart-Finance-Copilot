from typing import Dict, Any


def _clamp(value: float, min_v: float = 0.0, max_v: float = 1.0) -> float:
    return max(min_v, min(max_v, value))


def calculate_risk_profile(context: Dict[str, Any]) -> Dict[str, Any]:
    """
    Calculates payment risk profile based on user payment behavior.
    Returns a normalized risk score and explainable factors.
    """

    behavior = (
        context.get("user", {})
        .get("paymentBehavior", {})
    )

    late_payments = behavior.get("late_payments", 0)
    avg_delay = behavior.get("average_payment_delay_days", 0)
    missed_payments = behavior.get("missed_payments", 0)
    on_time_rate = behavior.get("on_time_payment_rate", 1.0)

    # ---- Risk scoring (weighted) ----
    risk_score = 0.0
    factors = []

    # Late payments contribution
    if late_payments > 0:
        risk_score += min(late_payments * 0.12, 0.36)
        factors.append("frequent late payments")

    # Average delay contribution
    if avg_delay > 1:
        risk_score += min(avg_delay * 0.08, 0.24)
        factors.append("payment delays")

    # Missed payments (strong signal)
    if missed_payments > 0:
        risk_score += min(missed_payments * 0.25, 0.5)
        factors.append("missed payments")

    # On-time payment rate (stability reducer)
    stability_penalty = (1 - on_time_rate) * 0.4
    risk_score += stability_penalty

    # Clamp risk score between 0 and 1
    risk_score = _clamp(risk_score)

    # ---- Risk level classification ----
    if risk_score >= 0.65:
        risk_level = "high"
    elif risk_score >= 0.35:
        risk_level = "medium"
    else:
        risk_level = "low"

    confidence = round(min(0.6 + risk_score * 0.5, 0.95), 2)

    return {
        "risk_score": round(risk_score, 2),
        "risk_level": risk_level,
        "primary_factors": factors if factors else ["stable payment behavior"],
        "confidence": confidence
    }
