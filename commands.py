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

from ast import Dict
from typing import List
from models import Expense
from storage import load_expenses, save_expenses, get_next_id
from datetime import date


def create_expense(expense_id: int, title: str, description: str, amount: float, category: str) -> Expense:
    return Expense(
        id=expense_id,
        title=title,
        description=description,
        amount=float(amount),
        category=category,
        date=date.today()
    )


def add_expense(title: str, description: str, amount: float, category: str) -> Expense:
    expenses = load_expenses()
    next_id = get_next_id(expenses)
    new_expense = create_expense(next_id, title, description, amount, category)
    expenses.append(new_expense)
    save_expenses(expenses)
    return new_expense


def delete_expense(expense_id: int) -> bool:
    expenses = load_expenses()
    new_expenses = [e for e in expenses if e.id != expense_id]
    deleted = len(expenses) != len(new_expenses)
    if deleted:
        save_expenses(new_expenses)
    return deleted


def get_all_expenses() -> List[Expense]:
    return load_expenses()


def filter_expenses_by_category(category: str) -> List[Expense]:
    expenses = load_expenses()
    filtered_expenses = [
        e for e in expenses if e.category.lower() == category.lower()]
    return filtered_expenses


def get_month_total(year: int, month: int) -> float:
    expenses = load_expenses()
    total = sum(e.amount for e in expenses if hasattr(e.date, "date")
                and e.date.year == year and e.date.month == month)
    return total


def get_summary() -> dict:
    expenses = load_expenses()

    # Total all time
    total_all_time = sum(e.amount for e in expenses)

    # Total this month
    today = date.today()
    this_month_expenses = [
        e for e in expenses
        if e.date.year == today.year and e.date.month == today.month
    ]
    total_this_month = sum(e.amount for e in this_month_expenses)

    # Spend per category (this month only)
    by_category: Dict[str, float] = {}
    for e in this_month_expenses:
        by_category[e.category] = by_category.get(e.category, 0.0) + e.amount

    # Sort top 3 categories this month
    top_categories = sorted(
        by_category.items(),
        key=lambda x: x[1],
        reverse=True
    )[:3]

    return {
        "total_all_time": total_all_time,
        "total_this_month": total_this_month,
        "month": today.strftime("%Y-%m"),
        "top_categories_this_month": top_categories,
    }
