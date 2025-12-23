from typing import Dict, Any

from ai_service.core.risk_profiling import calculate_risk_profile
from ai_service.core.attention_timing import determine_best_attention_time

#  LLM client (Ollama)
from ai_service.utils.llm_client import generate_reminder_message


def generate_payment_reminder(context: Dict[str, Any]) -> Dict[str, Any]:
    """
    Generates a personalized payment reminder and converts it into
    a natural language message using LLM.
    """

    #  Risk profiling
    risk_profile = calculate_risk_profile(context)
    timing = determine_best_attention_time(context)

    risk_level = risk_profile.get("risk_level", "low")

    #  No reminder for low-risk users
    if risk_level == "low":
        return {
            "type": "reminder",
            "should_notify": False,
            "reason": "User has good payment discipline"
        }

    #  Determine urgency
    urgency = "high" if risk_level == "high" else "medium"

    #  Structured reminder decision (FACTS ONLY)
    ai_output = {
        "type": "reminder",
        "should_notify": True,
        "urgency": urgency,
        "best_time": timing.get("best_time"),
        "confidence": timing.get("confidence"),

        # Optional fields if present in context
        "payment_type": context.get("payment", {}).get("payment_type"),
        "amount": context.get("payment", {}).get("amount"),
        "due_date": context.get("payment", {}).get("due_date")
    }

    #  LLM-based reminder message (LANGUAGE ONLY)
    message = generate_reminder_message(ai_output)

    #  Attach generated message
    ai_output["message"] = message

    return ai_output
