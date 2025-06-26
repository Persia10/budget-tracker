import json
import os

FILENAME = "budget_data.json"

def load_transactions():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    else:
        return []

def save_transactions(transactions):
    with open(FILENAME, "w") as file:
        json.dump(transactions, file, indent=2)

def add_transaction(transactions):
    t_type = input("Enter type (income/expense): ").strip().lower()
    if t_type not in ["income", "expense"]:
        print("Invalid type. Try again.")
        return
    description = input("Enter description: ").strip()
    amount_str = input("Enter amount: ").strip()
    try:
        amount = float(amount_str)
    except ValueError:
        print("Invalid amount. Try again.")
        return

    transaction = {
        "type": t_type,
        "description": description,
        "amount": amount
    }
    transactions.append(transaction)
    save_transactions(transactions)
    print("Transaction added!")

def show_balance(transactions):
    income = sum(t["amount"] for t in transactions if t["type"] == "income")
    expense = sum(t["amount"] for t in transactions if t["type"] == "expense")
    balance = income - expense
    print(f"\nTotal Income: ${income:.2f}")
    print(f"Total Expenses: ${expense:.2f}")
    print(f"Current Balance: ${balance:.2f}\n")

def main():
    transactions = load_transactions()
    while True:
        print("1. Add transaction")
        print("2. Show balance")
        print("3. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_transaction(transactions)
        elif choice == "2":
            show_balance(transactions)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
