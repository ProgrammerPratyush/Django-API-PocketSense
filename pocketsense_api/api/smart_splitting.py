import numpy as np


def split_expenses(expenses, members):
    """
    AI algorithm to split expenses evenly or optimally among group members.
    This is a basic implementation that splits expenses equally among members.

    :param expenses: List of individual expenses to be split (e.g., [100, 50, 30])
    :param members: List of members in the group (e.g., ["student1", "student2", "student3"])
    :return: Dictionary with each member's share of the expenses
    """

    total_expense = sum(expenses)  # Total amount of all expenses combined
    num_members = len(members)  # Number of members in the group

    # Evenly split the total expenses among all members
    split_amount = total_expense / num_members

    result = {member: round(split_amount, 2) for member in members}

    return result


def smart_split_based_on_history(expenses, members, spending_history):
    """
    AI-based algorithm to split expenses based on historical spending data and income levels.
    This function adjusts splits by analyzing historical spending data for each member.

    :param expenses: List of expenses to be split.
    :param members: List of members in the group.
    :param spending_history: Dictionary of each member's spending history (e.g., {"student1": 1000, "student2": 500})
    :return: Dictionary with a personalized split for each member.
    """

    total_expense = sum(expenses)
    total_spending_history = sum(spending_history.values())

    # Calculate each member's share of the total spending history
    member_shares = {member: spending_history.get(member, 0) / total_spending_history for member in members}

    # Assign each member an expense amount based on their share of historical spending
    expense_split = {member: round(member_shares[member] * total_expense, 2) for member in members}

    return expense_split
