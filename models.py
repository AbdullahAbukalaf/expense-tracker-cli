"""
models.py
Defines the data model for an expense.
"""

from typing import TypedDict

class Expense(TypedDict):
    id: int
    title: str
    amount: float
    category: str
    date: str  # ISO timestamp, e.g. "2025-10-28T14:32:10"

def create_expense(expense_id: int, title: str, amount: float, category: str) -> Expense:
    """
    Build a new Expense object.
    NOTE: actual timestamp will be added when we implement this.
    """
    # TODO:
    # - from datetime import datetime
    # - datetime.now().isoformat(timespec="seconds")
    pass
