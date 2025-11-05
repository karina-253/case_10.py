from collections import defaultdict, Counter
import local as lcl


def create_budget_template(analysis: dict, total_income: float = None) -> dict:
    """
    Creates a budget template based on historical analysis and total income.

    Args:
        analysis (dict): The output of historical spending analysis.
        total_income (float, optional): Total income for computations. Defaults to None.

    Returns:
        dict: Budget limits and recommended amounts per category.
    """
    avg_spending = analysis.get("average_spending", {})
    total_expenses = sum(avg_spending.values())
    savings = round((total_income * 0.15 if total_income else total_expenses * 0.1), 2)
    budget = {cat: {"limit": round(val * 1.05, 2), "recommended": val}
              for cat, val in avg_spending.items()}
    budget[f'{lcl.SAVINGS}'] = {"limit": savings, "recommended": savings}
    return budget


def compare_budget_vs_actual(budget: dict, transactions: list) -> dict:
    """
    Compares actual spending against the budget limits for each category.

    Args:
        budget (dict): Budget template with limits.
        transactions (list): List of transactions with categories and amounts.

    Returns:
        dict: Report with actual spending, limits, differences, and status indicators.
    """
    actual = defaultdict(float)
    for t in transactions:
        if t["amount"] < 0:
            actual[t["category"]] += abs(t["amount"])
    report = {}
    for cat, data in budget.items():
        limit = data["limit"]
        spent = actual.get(cat, 0)
        diff = limit - spent
        report[cat] = {
            "limit": limit,
            "actual": spent,
            "difference": diff,
            "status": "\u2705" f'{lcl.WITHIN_BUDGET}' if diff >= 0 else "⚠️" f'{lcl.BUDGET_EXCEEDED}'
        }
    return report
