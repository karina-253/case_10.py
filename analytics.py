def calculate_basic_stats(transactions: list) -> dict:
    """
    Calculates basic financial statistics from a list of transactions.

    Args:
        transactions (list): List of transaction dictionaries.

    Returns:
        dict: A dictionary containing total income, total expense, balance,
              transaction count, income transaction count, expense transaction count.
    """
    total_income = sum(t["amount"] for t in transactions if t["amount"] > 0)
    total_expense = sum(t["amount"] for t in transactions if t["amount"] < 0)
    balance = total_income + total_expense
    transaction_count = len(transactions)
    count_income = sum(1 for t in transactions if t["amount"] > 0)
    count_expense = sum(1 for t in transactions if t["amount"] < 0)
    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": balance,
        "transaction_count": transaction_count,
        "income_transactions": count_income,
        "expense_transactions": count_expense
    }


def calculate_by_category(transactions: list) -> dict:
    """
    Calculates total amounts and percentages per category from transactions.

    Args:
        transactions (list): List of transaction dictionaries, each with a 'category'.

    Returns:
        dict: Sorted dictionary with categories as keys and dicts with sum, count, and percent.
    """
    totals = defaultdict(lambda: {"sum": 0, "count": 0})
    total_expense = sum(t["amount"] for t in transactions if t["amount"] < 0)
    for t in transactions:
        cat = t.get("category", f'{lcl.NO_CATEGORY}')
        totals[cat]["sum"] += t["amount"]
        totals[cat]["count"] += 1
    for cat, val in totals.items():
        val["percent"] = (-val["sum"] / -total_expense * 100) if total_expense else 0
    sorted_categories = sorted(totals.items(), key=lambda item: abs(item[1]["sum"]), reverse=True)
    return dict(sorted_categories)


def analyze_by_time(transactions: list) -> dict:
    """
    Analyzes transactions grouped by month, summarizing income, expenses, and top categories.

    Args:
        transactions (list): List of transaction dictionaries.

    Returns:
        dict: Dictionary with month keys, each containing income, expenses, and top categories.
    """
    monthly = defaultdict(lambda: {"income": 0, "expenses": 0, "categories": []})
    for t in transactions:
        try:
            d = datetime.datetime.strptime(t["date"], "%Y-%m-%d")
        except Exception:
            continue
        key = d.strftime("%Y-%m")
        if t["amount"] >= 0:
            monthly[key]["income"] += t["amount"]
        else:
            monthly[key]["expenses"] += t["amount"]
            monthly[key]["categories"].append(t.get("category", f'{lcl.NO_CATEGORY}'))
    for m, data in monthly.items():
        data["top_categories"] = Counter(data["categories"]).most_common(3)
    return dict(monthly)


def analyze_seasonal_trends(transactions: list) -> dict:
    """
    Analyzes transactions grouped by fiscal quarter, summarizing income, expenses, and top categories.

    Args:
        transactions (list): List of transaction dictionaries.

    Returns:
        dict: Dictionary with quarter keys, each containing income, expenses, and top categories.
    """
    quarterly = defaultdict(lambda: {"income": 0, "expenses": 0, "categories": []})
    for t in transactions:
        try:
            d = datetime.datetime.strptime(t["date"], "%Y-%m-%d")
        except Exception:
            continue
        year = d.year
        quarter = (d.month - 1) // 3 + 1
        key = f"{year}-Q{quarter}"
        amount = t["amount"]
        if amount >= 0:
            quarterly[key]["income"] += amount
        else:
            quarterly[key]["expenses"] += amount
            category = t.get("category", f'{lcl.NO_CATEGORY}')
            quarterly[key]["categories"].append(category)
    for q, data in quarterly.items():
        data["top_categories"] = Counter(data["categories"]).most_common(3)
    return dict(quarterly)

def analyze_historical_spending(transactions: list) -> dict:
    """
    Calculates average monthly spending per category and identifies top categories.

    Args:
        transactions (list): List of transaction dictionaries.

    Returns:
        dict: Contains 'average_spending' per category and 'top_categories' list.
    """
    monthly_spending = defaultdict(lambda: defaultdict(float))
    for t in transactions:
        if t["amount"] < 0:
            try:
                d = datetime.datetime.strptime(t["date"], "%Y-%m-%d")
            except Exception:
                continue
            month = d.strftime("%Y-%m")
            cat = t.get("category", f'{lcl.NO_CATEGORY}')
            monthly_spending[cat][month] += abs(t["amount"])
    avg_spending = {
        cat: round(statistics.mean(vals.values()), 2)
        for cat, vals in monthly_spending.items() if vals
    }
    top_cats = sorted(avg_spending.items(), key=lambda x: x[1], reverse=True)[:3]
    return {
        "average_spending": avg_spending,
        "top_categories": top_cats
    }
