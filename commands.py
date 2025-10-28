"""
commands.py
Contains high-level actions the UI can trigger.

Example actions:
- add_expense(...)
- delete_expense(...)
- get_all_expenses()
- get_total_for_current_month(...)
- filter_by_category(...)
"""

from typing import List, Optional
from models import Expense
# from storage import load_expenses, save_expenses
# from utils import current_month_total  # (future helper maybe)

def add_expense(title: str, amount: float, category: str) -> Expense:
    """
    Create and store a new expense.
    Returns the created expense.
    """
    # TODO:
    # - load all expenses
    # - compute next id
    # - build expense using models.create_expense(...)
    # - append and save
    pass

def delete_expense(expense_id: int) -> bool:
    """
    Delete an expense by id.
    Returns True if deleted, False if not found.
    """
    # TODO:
    # - load all expenses
    # - remove matching id
    # - save
    pass

def get_all_expenses() -> List[Expense]:
    """
    Return the full list of expenses.
    """
    # TODO:
    # - load_expenses()
    pass

def filter_expenses_by_category(category: str) -> List[Expense]:
    """
    Return only expenses matching the given category.
    """
    # TODO:
    # - load_expenses()
    # - filter
    pass

def get_month_total(year: int, month: int) -> float:
    """
    Return the total amount spent in a given month (year, month).
    Ex: get_month_total(2025, 10) -> 28.65
    """
    # TODO:
    # - load_expenses()
    # - sum amounts where expense.date is in that month
    pass
