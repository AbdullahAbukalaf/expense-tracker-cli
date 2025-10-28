import sys
from commands import (
    add_expense,
    delete_expense,
    get_all_expenses,
    get_summary,
    filter_expenses_by_category,
)
from ui import (
    print_added,
    print_list,
    print_deleted,
    print_summary,
    run_app
)
USAGE = """
Expense Tracker CLI
Usage:
  python main.py add "title" "description" amount category
  python main.py list
  python main.py delete <id>
  python main.py summary
  python main.py category <name>
"""


def main():
    run_app()
    # args = sys.argv[1:]  # everything after 'python main.py ...'

    # if not args:
    #     print(USAGE)
    #     return

    # command = args[0].lower()

    # # ADD
    # if command == "add":
    #     if len(args) < 5:
    #         print("Error: 'add' requires title, description, amount, and category.")
    #         print(USAGE)
    #         return
    #     title = args[1]
    #     description = args[2]
    #     amount_str = args[3]
    #     try:
    #         amount = float(amount_str)
    #     except ValueError:
    #         print("Error: Amount must be a number.")
    #         return
    #     category = args[4]
    #     expenes = add_expense(title, description, amount, category)
    #     print_added(expenes)
    #     return

    # # List
    # if command == "list":
    #     expenses = get_all_expenses()
    #     print_list(expenses)
    #     return
    
    # # DELETE
    # if command == "delete":
    #     if len(args) < 2:
    #         print("Error: 'delete' requires an ID.")
    #         return
        
    #     try:
    #         id = int(args[1])
    #     except ValueError:
    #         print("Error: ID must be an integer.")
    #         return
        
    #     result = delete_expense(id)
    #     print_deleted(result,id)
    #     return
        
    # # SUMMARY
    # if command == "summary":
    #     if len(args) < 1:
    #         print(USAGE)
    #         return
        
    #     data = get_summary()
    #     print_summary(data)
    #     return
    
    # # CATEGORY
    # if command == "category":
    #     if len(args) < 2:
    #         print("Error: 'categoty' requires an name.")
    #         return
    #     category = args[1]
    #     expenses = filter_expenses_by_category(category)
    #     print_list(expenses)
    #     return
    
    # if command == "tui":
    #     run_app()
    #     return
        
    
    # print(f"Unknown command: {command}")
    # print(USAGE)
    

if __name__ == "__main__":
    main()
