import json


def add_expense(expenses):
     expense_category = input("Enter expense category:")
     expense_amount = float(input("Enter expense amount:"))
     if expense_category not in expenses:
         expenses[expense_category] = expense_amount
     else:
         expenses[expense_category] += expense_amount

def view_summary(expenses):
    total_expenses = 0
    for expense_category in expenses:
        print(f"{expense_category} $ {expenses[expense_category]:.2f}")
        total_expenses += expenses[expense_category]
    print(f"Total expenses: {total_expenses:.2f}")

def save_expenses(expenses):
    with open('expenses.json', 'w') as outfile:
        json.dump(expenses, outfile)

def load_expenses():
    try:
        with open('expenses.json', 'r') as infile:
            expenses = json.load(infile)
    except FileNotFoundError:
        expenses = {}
    return expenses


def main():
    expenses = load_expenses()


    choice = input("(A)dd Expense \n(V)iew Summary \n(C)lear Expenses \n(Q)uit\n").upper()

    while choice != 'Q':
        if choice == 'A':
            add_expense(expenses)
            save_expenses(expenses)

        elif choice == 'V':
            view_summary(expenses)
        elif choice == 'C':
            confirm = input("Are you sure? This will delete all expenses. (Y/N)\n").upper()
            if confirm == 'Y':
                expenses.clear()
                save_expenses(expenses)
                print("Expenses cleared.")
        else:
            print("Please enter valid choice")
        choice = input("(A)dd Expense \n(V)iew Summary \n(C)lear Expenses \n(Q)uit\n").upper()




if __name__ == '__main__':
    main()

