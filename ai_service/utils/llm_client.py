import requests
from typing import Dict, Any

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "phi3"


def _call_ollama(prompt: str) -> str:
    """
    Low-level Ollama HTTP call.
    """
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload, timeout=30)
    response.raise_for_status()

    return response.json()["response"].strip()


# =========================================================
# COPILOT EXPLANATION
# =========================================================

def generate_copilot_explanation(ai_output: Dict[str, Any]) -> str:
    """
    Convert structured copilot AI output into user-friendly explanation.
    """

    prompt = f"""
You are a financial assistant.

Explain the following AI analysis to a user in simple, clear English.
Rules:
- Do NOT add new facts
- Do NOT change numbers
- Do NOT give advice beyond what is stated
- Keep it professional and easy to understand

Analysis facts:
- Segment: {ai_output.get("segment")}
- Insight: {ai_output.get("insight")}
- Reason: {ai_output.get("reason")}
- Recommended action: {ai_output.get("recommended_action")}
- Priority: {ai_output.get("priority")}
- Expected impact: {ai_output.get("expected_impact")}

Generate a short explanation (3–4 sentences).
"""

    return _call_ollama(prompt)


# =========================================================
# REMINDER MESSAGE
# =========================================================

def generate_reminder_message(ai_output: Dict[str, Any]) -> str:
    """
    Convert reminder decision into a polite reminder message.
    """

    prompt = f"""
You are a financial assistant.

Create a polite and clear payment reminder using the facts below.
Rules:
- Do NOT invent amounts or dates
- Do NOT change urgency or timing
- Keep the message short and friendly

Facts:
- Should notify: {ai_output.get("should_notify")}
- Urgency: {ai_output.get("urgency")}
- Best time to notify: {ai_output.get("best_time")}
- Payment type: {ai_output.get("payment_type")}
- Amount: {ai_output.get("amount")}
- Due date: {ai_output.get("due_date")}

Generate a 1–2 sentence reminder message.
"""

    return _call_ollama(prompt)


# =========================================================
# NOTIFICATION MESSAGE
# =========================================================

def generate_notification_message(ai_output: Dict[str, Any]) -> str:
    """
    Convert notification trigger into short in-app notification text.
    """

    prompt = f"""
You are a financial assistant.

Create a short proactive notification message based only on the information below.
Rules:
- Do NOT add new insights
- Keep it concise and user-friendly

Information:
- Segment: {ai_output.get("segment")}
- Priority: {ai_output.get("priority")}
- Message context: {ai_output.get("message")}
- Best time: {ai_output.get("best_time")}

Generate a clear 1–2 sentence notification.
"""

    return _call_ollama(prompt)
