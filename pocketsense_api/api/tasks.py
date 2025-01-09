from datetime import datetime
from .models import Expense
from django.core.mail import send_mail
from .openai_service import get_openai_response  # Import the OpenAI service


def check_spending_patterns():
    """
    Check if users have spent too much in a category or are nearing their budget limits.
    For now, we will notify if they exceed a certain amount.
    Additionally, use AI to analyze and suggest budget recommendations.
    """
    threshold = 1000  # Example threshold for overspending
    expenses = Expense.objects.filter(date__month=datetime.now().month)

    for expense in expenses:
        if expense.amount > threshold:
            # Send an alert email for overspending
            send_mail(
                "Spending Alert",
                f"You've spent over {threshold} in the {expense.category.name} category!",
                'ppurigoswami2002@gmail.com',
                ['bangtanboy3023@gmail.com'],
            )

            # AI-powered analysis for spending patterns
            prompt = f"Analyze the following spending pattern: A user has spent {expense.amount} in the category '{expense.category.name}' this month. Provide a suggestion on how to stay within budget and whether this is a healthy spending habit."

            # Get OpenAI response for suggestions
            ai_suggestion = get_openai_response(prompt)

            # Send AI-powered analysis to user or save for reporting
            send_mail(
                "AI-powered Spending Analysis",
                f"AI suggests: {ai_suggestion}",
                'ppurigoswami2002@gmail.com',
                ['bangtanboy3023@gmail.com'],
            )
