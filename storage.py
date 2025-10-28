"""
storage.py
Handles persistence: reading and writing expenses to data.json.
"""

from pathlib import Path
from typing import List
from models import Expense
import json
from models import Expense, expense_from_dict, expense_to_dict

DATA_FILE = Path("data.json")

def load_expenses() -> List[Expense]:
    if not DATA_FILE.exists():
        return []
    
    with DATA_FILE.open('r', encoding="utf-8") as f:
        try:
            data = json.load(f)
            return [expense_from_dict(e) for e in data]
        except (json.JSONDecodeError, FileNotFoundError):
            return []
        

def save_expenses(expenses: List[Expense]) -> None:
    data = [expense_to_dict(e) for e in expenses]
    with DATA_FILE.open('w', encoding="utf-8") as f:
        return json.dump(data, f, indent=2, ensure_ascii=False)
    


def get_next_id(expenses: list[Expense]) -> int:
    if not expenses:
        return 1
    else:
        return max(e.id for e in expenses) + 1
