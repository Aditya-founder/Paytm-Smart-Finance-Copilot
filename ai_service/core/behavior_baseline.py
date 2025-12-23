import math
from typing import Dict, Any, List


def _safe_mean(values: List[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def _safe_std(values: List[float], mean: float) -> float:
    if not values:
        return 0.0
    variance = sum((x - mean) ** 2 for x in values) / len(values)
    return math.sqrt(variance)


def build_behavior_baseline(context: Dict[str, Any]) -> Dict[str, Any]:
    """
    Builds a personal behavior baseline from historical transactions.
    This represents what is NORMAL for this user/merchant.
    """

    transactions = context.get("merchant", {}).get("transactions", [])

    if len(transactions) < 2:
        return {
            "baseline_available": False,
            "reason": "Not enough transaction history"
        }

    daily_sales = [t.get("total_sales", 0) for t in transactions]
    refunds = [t.get("refunds", 0) for t in transactions]
    upi_counts = [t.get("upi_transactions", 0) for t in transactions]

    avg_sales = _safe_mean(daily_sales)
    std_sales = _safe_std(daily_sales, avg_sales)

    baseline = {
        "baseline_available": True,
        "days_observed": len(transactions),

        # Sales behavior
        "avg_daily_sales": round(avg_sales, 2),
        "sales_std_dev": round(std_sales, 2),
        "normal_sales_min": round(avg_sales - std_sales, 2),
        "normal_sales_max": round(avg_sales + std_sales, 2),

        # Refund behavior
        "avg_refunds_per_day": round(_safe_mean(refunds), 2),

        # UPI usage behavior
        "avg_upi_transactions": round(_safe_mean(upi_counts), 2)
    }

    return baseline
