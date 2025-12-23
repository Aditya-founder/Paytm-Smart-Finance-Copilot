from typing import Dict, Any


def detect_sales_deviation(
    baseline: Dict[str, Any],
    latest_transaction: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Detects deviation in sales compared to personal baseline.
    """

    if not baseline.get("baseline_available", True):
        return {
            "is_deviation": False,
            "reason": "Baseline not available"
        }

    avg_sales = baseline["avg_daily_sales"]
    std_dev = baseline["sales_std_dev"]

    latest_sales = latest_transaction.get("total_sales", 0)

    # Percentage change from personal average
    percentage_change = ((latest_sales - avg_sales) / avg_sales) * 100

    # No deviation if within normal range
    if baseline["normal_sales_min"] <= latest_sales <= baseline["normal_sales_max"]:
        return {
            "is_deviation": False,
            "deviation_type": None,
            "severity": "none",
            "percentage_change": round(percentage_change, 2),
            "explanation": "Sales are within your normal range"
        }

    # Determine severity
    deviation_magnitude = abs(latest_sales - avg_sales)

    if deviation_magnitude > 2 * std_dev:
        severity = "high"
    else:
        severity = "medium"

    deviation_type = "sales_drop" if latest_sales < avg_sales else "sales_spike"

    return {
        "is_deviation": True,
        "deviation_type": deviation_type,
        "severity": severity,
        "percentage_change": round(percentage_change, 2),
        "explanation": (
            "Sales are significantly below your normal range"
            if deviation_type == "sales_drop"
            else "Sales are significantly above your normal range"
        )
    }
