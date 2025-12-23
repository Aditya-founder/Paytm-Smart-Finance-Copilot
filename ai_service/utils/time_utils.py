from typing import List, Dict, Any
from collections import Counter


def extract_hours(transactions: List[Dict[str, Any]]) -> List[int]:
    """
    Extracts hour-of-day from transaction records.
    Assumes 'hour' field exists (0–23).
    """
    hours = []

    for txn in transactions:
        hour = txn.get("hour")
        if isinstance(hour, int) and 0 <= hour <= 23:
            hours.append(hour)

    return hours


def most_active_hour(hours: List[int]) -> Dict[str, Any]:
    """
    Determines the most active hour and confidence score.
    """
    if not hours:
        return {
            "hour": 18,
            "confidence": 0.3,
            "reason": "No valid hour data available"
        }

    counter = Counter(hours)
    hour, freq = counter.most_common(1)[0]

    confidence = min(freq / len(hours), 0.95)

    return {
        "hour": hour,
        "confidence": round(confidence, 2),
        "reason": "Based on historical transaction activity"
    }


def format_hour(hour: int) -> str:
    """
    Converts hour integer to readable string.
    Example: 19 -> '19:00'
    """
    return f"{hour:02d}:00"


def determine_best_time_from_transactions(
    transactions: List[Dict[str, Any]]
) -> Dict[str, Any]:
    """
    High-level utility to determine best attention time.
    """
    hours = extract_hours(transactions)
    active_hour_info = most_active_hour(hours)

    return {
        "best_time": format_hour(active_hour_info["hour"]),
        "confidence": active_hour_info["confidence"],
        "reason": active_hour_info["reason"]
    }
