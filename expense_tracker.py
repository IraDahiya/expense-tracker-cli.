import json

def add_expense(expenses):
    category = input("Enter expense category: ")
    amount_str = input("Enter amount: ")
    try:
        amount = float(amount_str)
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
    expenses.append({"category": category, "amount": amount})
    print(f"Added expense: {category} - {amount}")

def remove_expense(expenses):
    if not expenses:
        print("No expenses to remove.")
        return
    print("Expenses:")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['category']} - {expense['amount']}")
    choice_str = input("Enter the number of the expense to remove: ")
    try:
        choice = int(choice_str)
        if 1 <= choice <= len(expenses):
            removed = expenses.pop(choice - 1)
            print(f"Removed expense: {removed['category']} - {removed['amount']}")
        else:
            print("Invalid choice number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def show_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return
    print("\nAll Expenses:")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['category']} - {expense['amount']}")

def show_summary(expenses):
    if not expenses:
        print("No expenses to summarize.")
        return
    summary = {}
    for expense in expenses:
        summary[expense['category']] = summary.get(expense['category'], 0) + expense['amount']
    print("\nExpense Summary by Category:")
    for category, total in summary.items():
        print(f"{category}: {total}")
    print(f"Total Expenses: {sum(summary.values())}")

def save_expenses(expenses, filename="expenses.json"):
    try:
        with open(filename, "w") as f:
            json.dump(expenses, f)
        print(f"Expenses saved to {filename}.")
    except Exception as e:
        print(f"Error saving expenses: {e}")

def load_expenses(filename="expenses.json"):
    try:
        with open(filename, "r") as f:
            expenses = json.load(f)
        print(f"Loaded expenses from {filename}.")
        return expenses
    except FileNotFoundError:
        print("No saved expenses found. Starting fresh.")
        return []
    except Exception as e:
        print(f"Error loading expenses: {e}")
        return []

def main():
    expenses = load_expenses()
    while True:
        print("\n--- Expense Tracker Menu ---")
        print("1. Add Expense")
        print("2. Remove Expense")
        print("3. Show All Expenses")
        print("4. Show Summary by Category")
        print("5. Save & Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            remove_expense(expenses)
        elif choice == '3':
            show_expenses(expenses)
        elif choice == '4':
            show_summary(expenses)
        elif choice == '5':
            save_expenses(expenses)
            print("Exiting the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

