from models import Expense
from utils import format_currency, format_expense_row
import os
from storage import save_expenses
from version import __version__ as VERSION
from commands import (
    add_expense,
    delete_expense,
    get_all_expenses,
    get_summary,
    filter_expenses_by_category,
    get_expense_by_id,
    update_expense,
)

# Later this will use `textual` or similar to:
# - render the table of expenses
# - highlight selected row
# - show total this month
# - listen for key events

RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
CYAN = "\033[36m"



def c(text, color):
    return f"{color}{text}{RESET}"


menu = (
    f"[{c('a', YELLOW)}] Add   "
    f"[{c('e', YELLOW)}] Edit   "
    f"[{c('d', YELLOW)}] Delete   "
    f"[{c('f', YELLOW)}] Filter   "
    f"[{c('m', YELLOW)}] Monthly   "
    f"[{c('q', YELLOW)}] Quit"
)


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


def format_row(cols, widths):
    # cols: ["#1", "Coffee", "morning coffee", "2.75 JOD", "food", "2025-10-29"]
    # widths: [4, 15, 35, 10, 15, 12]
    padded = []
    for value, w in zip(cols, widths):
        padded.append(str(value)[:w].ljust(w))
    return "  ".join(padded)


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
        print(
            f"                   Expense Tracker Summary v{VERSION} | {summary['custom_date']}                   ")
        print(
            c(f"Total this month ({summary['month']}): {format_currency(summary['total_this_month'])}", GREEN))
        print("=====================================================================")

        # 2. Show current expenses (list view)
        expenses = get_all_expenses()
        if not expenses:
            print(c("No expenses recorded yet.", YELLOW))
        else:
            print(format_row(
                ["ID", "TITLE", "DESCRIPTION", "AMOUNT", "CATEGORY", "DATE"],
                [4, 15, 35, 10, 15, 12]
            ))

            print("-" * 100)
            for e in expenses:
                print(format_row(
                    [f"#{e.id}", e.title, e.description,
                        f"{e.amount:.2f} JOD", e.category, e.date],
                    [4, 15, 35, 10, 15, 12]
                ))

        # 3. Menu
        print(f'\n{menu}')
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
                print(c("Invalid amount. Must be a number.", RED))
                continue

            expense = add_expense(title, description, amount, category)
            print(
                c(f"Added #{expense.id}: {expense.title} ({format_currency(expense.amount)})", GREEN))

        elif choice == "e":
            try:
                expense_id = int(input("Enter ID to edit: ").strip())
            except ValueError:
                print(c("Invalid ID.", RED))
                input("Press Enter to continue...")
                continue

            # show menu of fields
            print(c("What do you want to change?", YELLOW))
            print("1) Title")
            print("2) Description")
            print("3) Amount")
            print("4) Category")
            print("5) Date")

            field_choice = input("Choose a number: ").strip()

            # map user choice -> field name
            if field_choice == "1":
                field = "title"
                new_value = input("New title: ").strip()

            elif field_choice == "2":
                field = "description"
                new_value = input("New description: ").strip()

            elif field_choice == "3":
                field = "amount"
                new_value = input("New amount: ").strip()

            elif field_choice == "4":
                field = "category"
                new_value = input("New category: ").strip()

            elif field_choice == "5":
                field = "date"
                new_value = input("New date (YYYY-MM-DD): ").strip()

            else:
                print(c("Invalid choice.", RED))
                input("Press Enter to continue...")
                continue

            # try to update
            ok = update_expense(expense_id, field, new_value)

            if ok:
                print(c("Expense updated successfully.", GREEN))
            else:
                print(c("Failed to update. Check the ID or field.", RED))

            input("Press Enter to continue...")

        elif choice == "d":
            id_str = input("Enter ID to delete: ").strip()
            try:
                expense_id = int(id_str)
            except ValueError:
                print(c("Invalid ID. Must be a number.", RED))
                continue

            was_deleted = delete_expense(expense_id)
            if was_deleted:
                print(c(f"Deleted expense #{expense_id}.", GREEN))
            else:
                print(c(f"No expense with ID {expense_id} found.", RED))

        elif choice == "f":
            cat = input("Category name: ").strip()
            filtered = filter_expenses_by_category(cat)

            if not filtered:
                print(c(f"No expenses found for '{cat}'.", YELLOW))
            else:
                print(f"\nFiltered by '{cat}':")
                print(format_row(
                    ["ID", "TITLE", "DESCRIPTION", "AMOUNT", "CATEGORY", "DATE"],
                    [4, 15, 35, 10, 15, 12]
                ))

                print("-" * 100)
                for e in filtered:
                    print(format_row(
                        [f"#{e.id}", e.title, e.description,
                         f"{e.amount:.2f} JOD", e.category, e.date],
                        [4, 15, 35, 10, 15, 12]
                    ))
                input("Press Enter to continue...").strip()

        elif choice == "m":
            print("================ Monthly Summary ================")
            print(f"{c('Month:', RED)} {c(summary['custom_date'], GREEN)}")
            print(f"\n{c('Total spent: ', RED)} {c(format_currency(summary['total_this_month']), GREEN)}")
            print(f"{c('Transactions: ', RED)} {c(len(expenses), GREEN)}")
            print("\nSpending by category:")
            print("--------------------------------")
            top_categories = summary["top_categories_this_month"]
            for cat, amount in top_categories:
                print(f"\n{c(cat.ljust(12), CYAN)} : {c(f'{amount:>6.2f} JOD', GREEN)}")
            input("\nPress Enter to continue...").strip()
        else:
            print(c("Unknown choice. Please use a/e/d/f/m/q.", RED))
