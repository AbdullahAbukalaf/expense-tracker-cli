"""
utils.py
Small helper utilities:
- formatting amounts
- formatting rows for display
- extracting year/month from ISO date
"""

from models import Expense

def format_currency(amount: float) -> str:
    return f"{amount:.2f} JOD"

def format_expense_row(expense: Expense) -> str:
    return (
        f"#{expense.id:<3} "
        f"{expense.title:<15} "
        f"{expense.description:<40} "
        f"{format_currency(expense.amount):<10} "
        f"{expense.category:<15} "
        f"{expense.date.isoformat()}"
    )

