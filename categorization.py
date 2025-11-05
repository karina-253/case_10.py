import local as lcl
from categories import all_categories, priority_categories


def categorize_transaction_with_multiple(description: str, categories: dict,
                                         categories_priority: list) -> str:
    """
    Categorizes a transaction based on its description by matching keywords with categories,
    considering a priority sequence.

    Args:
        description (str): The transaction description.
        categories (dict): A dictionary mapping category names to lists of keywords.
        categories (list): A list specifying the priority order of categories.

    Returns:
        str: The name of the matched category or 'Other' if no match found.
    """
    description_low = description.lower()
    matched_categories = []

    for category in categories_priority:
        keywords = categories.get(category, [])
        if any(keyword in description_low for keyword in keywords):
            matched_categories.append(category)


    if matched_categories:
        return matched_categories[0]
    return f'{lcl.OTHER}'


def categorize_all_transactions(transactions: list) -> list:
    """
    Categorizes all transactions in the list based on their descriptions.

    Args:
        transactions (list): List of transaction dictionaries.

    Returns:
        list: The same list, with each transaction augmented with a 'category' key.
    """
    for transaction in transactions:
        desc = transaction.get("description", "")
        category = categorize_transaction_with_multiple(desc, all_categories(), priority_categories())
        transaction["category"] = category
    return transactions
