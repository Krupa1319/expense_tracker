import datetime
import json

# Data Storage File
DATA_FILE = "expenses.json"

# Expense Categories
CATEGORIES = ["Food", "Transportation", "Entertainment", "Miscellaneous"]

def load_expenses():
    """Load expenses from JSON file"""
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_expenses(expenses):
    """Save expenses to JSON file"""
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file)

def add_expense():
    """Add a new expense"""
    while True:
        date = input("Enter date (YYYY-MM-DD): ")
        try:
            datetime.datetime.strptime(date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount < 0:
                print("Amount cannot be negative.")
            else:
                break
        except ValueError:
            print("Invalid amount. Please enter a valid number.")

    description = input("Enter description: ")

    while True:
        category = input(f"Enter category ({', '.join(CATEGORIES)}): ").strip().title()
        if category in CATEGORIES:
            break
        else:
            print(f"Invalid category. Please select from {', '.join(CATEGORIES)}")

    expenses = load_expenses()
    if not isinstance(expenses, list):
        expenses = []
    
    expenses.append({
        "date": date,
        "amount": amount,
        "description": description,
        "category": category
    })
    save_expenses(expenses)

def view_expenses():
    """View expenses for a specific month"""
    month = input("Enter month (YYYY-MM): ")
    expenses = load_expenses()
    
    if not isinstance(expenses, list):
        expenses = []
    
    monthly_expenses = [expense for expense in expenses if isinstance(expense, dict) and 'date' in expense and expense["date"].startswith(month)]

    if monthly_expenses:
        total_expenses = sum(expense["amount"] for expense in monthly_expenses if 'amount' in expense)
        print("Monthly Expenses for", month)
        for expense in monthly_expenses:
            print(f"{expense.get('date', '')}: {expense.get('amount', 0)} ({expense.get('category', '')})")
        print("Total Expenses for", month, ":", total_expenses)
    else:
        print("No expenses found for", month)

def view_category_wise():
    """View category-wise expenditure"""
    expenses = load_expenses()
    
    if not isinstance(expenses, list):
        expenses = []
    
    category_wise = {}
    for expense in expenses:
        if isinstance(expense, dict) and 'category' in expense and 'amount' in expense:
            category = expense["category"]
            if category not in category_wise:
                category_wise[category] = 0
            category_wise[category] += expense["amount"]
    print("Category-wise Expenditure")
    for category, amount in category_wise.items():
        print(f"{category}: {amount}")

def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Category-wise Expenditure")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_category_wise()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()