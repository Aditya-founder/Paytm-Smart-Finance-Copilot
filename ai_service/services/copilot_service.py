from typing import Dict, Any

from ai_service.core.behavior_baseline import build_behavior_baseline
from ai_service.core.deviation_detection import detect_sales_deviation
from ai_service.core.risk_profiling import calculate_risk_profile
from ai_service.core.segmentation import determine_user_segment
from ai_service.decision.action_recommender import recommend_action

#  LLM client (Ollama)
from ai_service.utils.llm_client import generate_copilot_explanation


def generate_copilot_response(
    context: Dict[str, Any],
    question: str
) -> Dict[str, Any]:
    """
    Generates personalized copilot response based on user behavior
    and converts it into a natural language explanation using LLM.
    """

    #  Build behavioral baseline
    baseline = build_behavior_baseline(context)

    # Latest transaction (assume last entry)
    transactions = context.get("merchant", {}).get("transactions", [])
    latest_transaction = transactions[-1] if transactions else {}

    #  Detect deviation
    deviation = detect_sales_deviation(baseline, latest_transaction)

    #  Risk profiling
    risk_profile = calculate_risk_profile(context)

    #  Segmentation
    segment = determine_user_segment(baseline, deviation, risk_profile)

    #  Action recommendation
    action = recommend_action(baseline, deviation, risk_profile, segment)

    #  Structured AI output (FACTS ONLY)
    insight = (
        "Your sales behavior shows unusual changes"
        if deviation.get("is_deviation")
        else "Your business performance is stable"
    )

    reason = deviation.get("explanation", "No major behavioral changes detected")

    ai_output = {
        "type": "copilot",
        "question": question,
        "segment": segment.get("segment"),
        "insight": insight,
        "reason": reason,
        "recommended_action": action.get("action"),
        "priority": action.get("priority"),
        "expected_impact": action.get("expected_impact")
    }

    # LLM-based explanation (LANGUAGE ONLY)
    explanation = generate_copilot_explanation(ai_output)

    #  Attach explanation to response
    ai_output["explanation"] = explanation

    return ai_output
