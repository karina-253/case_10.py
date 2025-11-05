from collections import defaultdict, Counter
import matplotlib.pyplot as plt
import local as lcl


def visualize_financial_data(transactions: list):
    """
    Visualizes expenses by category using a bar chart.

    Args:
        transactions (list): List of transaction dictionaries.
    """
    if not transactions:
        print(f'{lcl.NO_VISUALIZATION_DATA}')
        return

    expenses = defaultdict(float)
    for t in transactions:
        if t["amount"] < 0:
            expenses[t["category"]] += abs(t["amount"])
    if expenses:
        plt.figure(figsize=(8, 5))
        plt.bar(expenses.keys(), expenses.values())
        plt.title(f'{lcl.EXPENSES_BY_CATEGORY}')
        plt.xlabel(f'{lcl.CATEGORY}')
        plt.ylabel(f'{lcl.AMOUNT_RUB}')
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.show()
