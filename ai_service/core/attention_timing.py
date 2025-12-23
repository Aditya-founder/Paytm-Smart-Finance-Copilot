from typing import Dict, Any
from collections import Counter

from ai_service.utils.time_utils import determine_best_time_from_transactions



def determine_best_attention_time(context: Dict[str, Any]) -> Dict[str, Any]:
    """
    Determines the optimal time to send notifications/reminders
    based on user's transaction activity.
    """

    transactions = context.get("merchant", {}).get("transactions", [])

    if not transactions:
        return {
            "best_time": "18:00",
            "confidence": 0.3,
            "reason": "No transaction history available"
        }

    # Extract hours (if available)
    hours = []
    for txn in transactions:
        hour = txn.get("hour")
        if hour is not None:
            hours.append(hour)

    if not hours:
        return {
            "best_time": "18:00",
            "confidence": 0.4,
            "reason": "Transaction timing not available"
        }

    hour_counts = Counter(hours)
    most_common_hour, freq = hour_counts.most_common(1)[0]

    confidence = min(freq / len(hours), 0.95)

    return {
        "best_time": f"{most_common_hour}:00",
        "confidence": round(confidence, 2),
        "reason": "User is most active during this hour"
    }
