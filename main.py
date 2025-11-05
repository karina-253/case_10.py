import local as lcl
from data import import_financial_data
from analytics import (calculate_basic_stats, calculate_by_category, analyze_by_time,
                       analyze_historical_spending)
from budget import create_budget_template, compare_budget_vs_actual
from vizualization import visualize_financial_data
from categories import (all_categories, priority_categories,
                        categorize_transaction_with_multiple, categorize_all_transactions)


def smart_piggy_bank(csv_file=None, json_file=None):
    """
    Main function to perform comprehensive financial analysis and visualization.

    Args:
        csv_file (str): Path to CSV data file.
        json_file (str): Path to JSON data file.
    """
    print("=" * 70)
    print("\U0001F4B0" f'{lcl.SMART_PIGGY_BANK}' "\U0001F4A1")
    print("=" * 70)

    if csv_file is None:
        csv_file = input(f'{lcl.CSV_INPUT}')
    if json_file is None:
        json_file = input(f'{lcl.JSON_INPUT}')

    transactions = []
    if csv_file:
        transactions += import_financial_data(csv_file)
    if json_file:
        transactions += import_financial_data(json_file)

    if not transactions:
        print("\u274C" f'{lcl.NO_ANALYSIS_DATA}')
        return

    transactions = categorize_all_transactions(transactions)

    stats = calculate_basic_stats(transactions)
    categories_stats = calculate_by_category(transactions)
    timeline = analyze_by_time(transactions)
    analysis = analyze_historical_spending(transactions)
    budget = create_budget_template(analysis, stats["total_income"])
    comparison = compare_budget_vs_actual(budget, transactions)


    print("\n===" f'{lcl.FINANCIAL_REPORT}' "===")
    print(f'\U0001F4B0 {lcl.INCOME} {stats['total_income']:.2f}')
    print(f'\U0001F4B8 {lcl.EXPENSES} {abs(stats['total_expense']):.2f}')
    print(f'\u2696 {lcl.BALANCE}{stats['balance']:.2f}')

    print("\n\U0001F4CA" f'{lcl.EXPENSES_BY_CATEGORY_TITLE}')
    for cat, data in categories_stats.items():
        print(f"  {cat}: {abs(data['sum']):.2f} {lcl.RUB} ({data['percent']:.1f}%)")

    print("\n\U0001F4C5" f'{lcl.MONTHLY_ANALYSIS}')
    for month, data in timeline.items():
        top = ", ".join([f"{c} ({n})" for c, n in data["top_categories"]])
        print(f"  {month}: {lcl.INCOME_LABEL} {data['income']:.2f} | {lcl.EXPENSE_LABEL}"
              f" {abs(data['expenses']):.2f} → {lcl.TOP} {top}")

    print("\n\U0001F3AF" f'{lcl.RECOMMENDATIONS}')
    for cat, val in analysis["top_categories"]:
        print(f"  {cat}: {val:.2f} {lcl.AVERAGE_RUB}")

    print("\n\U0001F4CB" f'{lcl.BUDGET_COMPARISON}')
    for cat, info in comparison.items():
        print(f"  {cat}: {lcl.SPENT} {info['actual']:.2f} / {lcl.LIMIT} "
              f"{info['limit']:.2f} → {info['status']}")

    print("\n\u2705" f'{lcl.ANALYSIS_SUCCESS}' "\n")

    visualize_financial_data(transactions)


if __name__ == "__main__":
    smart_piggy_bank()
    
