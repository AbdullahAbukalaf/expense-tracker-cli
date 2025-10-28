"""
utils.py
Small helper utilities:
- formatting amounts
- formatting rows for display
- extracting year/month from ISO date
"""

from models import Expense

def format_currency(amount: float) -> str:
    """
    Return amount like '28.65 JOD'.
    """
    # TODO
    pass

def format_expense_row(expense: Expense) -> str:
    """
    Return a single line string for the table row.
    Example:
    '#1  Coffee        2.75   food     2025-10-28'
    (UI layer can use this to render rows)
    """
    # TODO
    pass
