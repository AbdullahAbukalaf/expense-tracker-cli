"""
models.py
Defines the data model for an expense.
"""

from dataclasses import dataclass
from datetime import date
@dataclass
class Expense:
    id: int
    title: str
    description: str    
    amount: float
    category: str
    date: str 


def expense_to_dict(expense : Expense) -> dict:
    return {
        "id" : expense.id,
        "title" : expense.title,
        "description" : expense.description,
        "amount" : expense.amount,
        "category" : expense.category,
        "date" : expense.date.isoformat(),
    }


def expense_from_dict(data: dict) -> Expense:
    return Expense( 
        id=data["id"],
        title=data["title"],
        description=data["description"],
        amount=float(data["amount"]),
        category=data["category"],
        date=date.fromisoformat(data["date"])
    )