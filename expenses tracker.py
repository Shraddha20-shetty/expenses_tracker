# Function to input a new expense
def input_expense():
    try:
        amount = float(input("Enter the expense amount: $"))
        category = input("Enter the category (e.g., Food, Transport, Entertainment): ")
        description = input("Enter a short description: ")

        expense = {
            'amount': amount,
            'category': category,
            'description': description,
        }

        return expense
    except ValueError:
        print("Invalid input. Please enter a numeric value for the amount.")
        return None

# Function to display all expenses
def display_expenses(expenses):
    if not expenses:
        print("\nNo expenses recorded.")
        return

    print("\n--- All Expenses ---")
    for idx, expense in enumerate(expenses, start=1):
        print(f"{idx}. {expense['category']} | ${expense['amount']:.2f} | {expense['description']}")

# Function to analyze expenses
def analyze_expenses(expenses):
    if not expenses:
        print("\nNo expenses to analyze.")
        return

    total_spent = sum(expense['amount'] for expense in expenses)
    category_summary = {}

    for expense in expenses:
        category = expense['category']
        if category not in category_summary:
            category_summary[category] = 0
        category_summary[category] += expense['amount']

    print("\n--- Expense Analysis ---")
    print(f"Total spent: ${total_spent:.2f}")

    print("Category Summary:")
    for category, amount in category_summary.items():
        print(f"{category}: ${amount:.2f}")



def main():
    expenses = []

    while True:
        print("\n--- Expense Tracker ---")
        print("1. Input a new expense")
        print("2. Display all expenses")
        print("3. Analyze expenses")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            expense = input_expense()
            if expense:
                expenses.append(expense)
                print("Expense added successfully.")
        elif choice == '2':
            display_expenses(expenses)
        elif choice == '3':
            analyze_expenses(expenses)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")


main()