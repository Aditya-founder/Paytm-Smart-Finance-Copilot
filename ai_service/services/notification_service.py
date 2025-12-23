from typing import Dict, Any

from ai_service.core.behavior_baseline import build_behavior_baseline
from ai_service.core.deviation_detection import detect_sales_deviation
from ai_service.core.segmentation import determine_user_segment
from ai_service.core.attention_timing import determine_best_attention_time



def generate_notification(context: Dict[str, Any]) -> Dict[str, Any]:
    """
    Generates a proactive personalized notification.
    """

    baseline = build_behavior_baseline(context)

    transactions = context.get("merchant", {}).get("transactions", [])
    latest_transaction = transactions[-1] if transactions else {}

    deviation = detect_sales_deviation(baseline, latest_transaction)

    # If no deviation → no notification
    if not deviation.get("is_deviation"):
        return {
            "should_notify": False,
            "reason": "No abnormal behavior detected"
        }

    segment = determine_user_segment(
        baseline=baseline,
        deviation=deviation,
        risk_profile={"risk_level": "medium"}  # minimal dependency
    )

    timing = determine_best_attention_time(context)

    return {
        "type": "notification",
        "should_notify": True,
        "segment": segment.get("segment"),
        "priority": deviation.get("severity"),
        "best_time": timing.get("best_time"),
        "message": deviation.get("explanation")
    }
