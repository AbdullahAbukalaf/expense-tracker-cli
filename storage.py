"""
storage.py
Handles persistence: reading and writing expenses to data.json.
"""

from pathlib import Path
from typing import List
from models import Expense

DATA_FILE = Path("data.json")

def load_expenses() -> List[Expense]:
    """
    Load all expenses from the data file.
    If file doesn't exist or is invalid, return an empty list.
    """
    # TODO:
    # - if not DATA_FILE.exists(): return []
    # - open file, json.load()
    # - handle json errors
    pass

def save_expenses(expenses: List[Expense]) -> None:
    """
    Save the full expense list to the data file.
    """
    # TODO:
    # - open file
    # - json.dump(expenses, indent=2)
    pass
