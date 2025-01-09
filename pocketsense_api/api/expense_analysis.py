import numpy as np
import pandas as pd


def analyze_spending(user_expenses):
    """
    Basic spending analysis function to categorize user expenses and calculate averages.

    :param user_expenses: Dictionary of expenses per user, with categories (e.g., {'student1': {'food': 300, 'travel': 150}})
    :return: Dictionary with spending analysis results.
    """

    analysis_result = {}

    for user, expenses in user_expenses.items():
        total_spent = sum(expenses.values())
        average_spent = np.mean(list(expenses.values()))

        category_spending = {category: round(amount, 2) for category, amount in expenses.items()}

        analysis_result[user] = {
            "total_spent": total_spent,
            "average_spent": average_spent,
            "category_spending": category_spending
        }

    return analysis_result


def detect_spending_patterns(user_expenses, threshold=500):
    """
    Detect if a user is overspending in a particular category based on predefined thresholds.

    :param user_expenses: Dictionary of user expenses per category.
    :param threshold: Threshold value for each category.
    :return: Dictionary indicating if the user is overspending.
    """

    overspending_alert = {}

    for user, expenses in user_expenses.items():
        overspending_alert[user] = {}

        for category, amount in expenses.items():
            if amount > threshold:
                overspending_alert[user][category] = "Overspending"
            else:
                overspending_alert[user][category] = "Within Budget"

    return overspending_alert
