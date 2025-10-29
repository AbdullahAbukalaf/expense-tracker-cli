from models import Expense
from utils import format_currency, format_expense_row
import os
from commands import (
    add_expense,
    delete_expense,
    get_all_expenses,
    get_summary,
    filter_expenses_by_category,
)

# Later this will use `textual` or similar to:
# - render the table of expenses
# - highlight selected row
# - show total this month
# - listen for key events


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_added(expense: Expense) -> None:
    print(
        f"Added #{expense.id}: "
        f"{expense.title} "
        f"({format_currency(expense.amount)}, {expense.category}, {expense.date.isoformat()})"
    )


def print_list(expenses: list[Expense]) -> None:
    if not expenses:
        print("No expenses recorded yet.")
        return

    print(f"{'ID':<4} {'TITLE':<15} {'DESCRIPTION':<40} {'AMOUNT':<10} {'CATEGORY':<15} DATE")
    print("-" * 100)

    for e in expenses:
        print(format_expense_row(e))


def print_deleted(was_deleted: bool, expense_id: int) -> None:
    if was_deleted:
        print(f"Deleted expense #{expense_id}.")
    else:
        print(f"No expense found with id {expense_id}.")


def print_summary(summary_data: dict) -> None:
    print(
        f"Total spent (all time): {format_currency(summary_data['total_all_time'])}")
    print(
        f"Total spent ({summary_data['month']}): {format_currency(summary_data['total_this_month'])}")
    print("Top categories this month:")

    top_cats = summary_data["top_categories_this_month"]
    if top_cats:
        for cat, amt in top_cats:
            print(f"  - {cat}: {format_currency(amt)}")
    else:
        print("  (no spending yet this month)")


def run_app():
    """
    Interactive TUI loop (Phase 3 idea).
    Not used by main.py in Phase 2.
    """
    while True:
        # 1. Show header / summary
        # clear_screen()
        summary = get_summary()
        print("\n=====================================================================")
        print(f"Total this month ({summary['month']}): {format_currency(summary['total_this_month'])}")
        print("=====================================================================")

        # 2. Show current expenses (list view)
        expenses = get_all_expenses()
        if not expenses:
            print("No expenses recorded yet.")
        else:
            print(f"\n{'ID':<4} {'TITLE':<15} {'DESCRIPTION':<40} {'AMOUNT':<10} {'CATEGORY':<15} DATE")
            print("-" * 100)
            for e in expenses:
                print(format_expense_row(e))

        # 3. Menu
        print("\n[a] Add   [d] Delete   [f] Filter by category   [q] Quit")
        choice = input("> ").strip().lower()

        if choice == "q":
            print("Goodbye 👋")
            break

        elif choice == "a":
            title = input("Title: ").strip()
            description = input("Description: ").strip()
            amount_str = input("Amount (number): ").strip()
            category = input("Category: ").strip()

            try:
                amount = float(amount_str)
            except ValueError:
                print("Invalid amount. Please enter a number.")
                continue

            expense = add_expense(title, description, amount, category)
            print(f"Added #{expense.id}.")

        elif choice == "d":
            id_str = input("Enter ID to delete: ").strip()
            try:
                expense_id = int(id_str)
            except ValueError:
                print("Invalid ID. Must be an integer.")
                continue

            was_deleted = delete_expense(expense_id)
            if was_deleted:
                print(f"Deleted #{expense_id}.")
            else:
                print(f"No expense with ID {expense_id} found.")

        elif choice == "f":
            cat = input("Category name: ").strip()
            filtered = filter_expenses_by_category(cat)

            if not filtered:
                print(f"No expenses found for '{cat}'.")
            else:
                print(f"\nFiltered by '{cat}':")
                print(f"{'ID':<4} {'TITLE':<15} {'DESCRIPTION':<40} {'AMOUNT':<10} {'CATEGORY':<15} DATE")
                print("-" * 100)
                for e in filtered:
                    print(format_expense_row(e))

        else:
            print("Unknown choice. Please use a/d/f/q.")
