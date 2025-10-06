# Personal Finance Manager 
import json
from datetime import datetime

DATA_FILE = "transactions.json"

# Base Transaction class
class Transaction:
    def __init__(self, amount, description="", date=None):
        self.amount = amount
        self.description = description
        self.date = date or datetime.today().strftime("%Y-%m-%d")

    @staticmethod
    def validate_amount(amount):
        try:
            amt = float(amount)
            if amt <= 0:
                raise ValueError
            return amt
        except ValueError:
            print("Invalid amount!")
            return None

    def __str__(self):
        return f"{self.date} | {self.__class__.__name__:<7} | Rs.{self.amount:>10.2f} | {self.description}"

# Child classes
class Income(Transaction):
    pass

class Expense(Transaction):
    pass

# Finance Manager
class FinanceManager:
    def __init__(self):
        self.transactions = self.load_transactions()

    def load_transactions(self):
        try:
            with open(DATA_FILE, "r") as f:
                content = f.read().strip()
                if not content:
                    return []
                data = json.loads(content)
                transactions = []
                for t in data:
                    if t["type"] == "Income":
                        tr = Income(t["amount"], t["description"], t["date"])
                    else:
                        tr = Expense(t["amount"], t["description"], t["date"])
                    transactions.append(tr)
                return transactions
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_transactions(self):
        data_to_save = []
        for t in self.transactions:
            data_to_save.append({
                "type": t.__class__.__name__,
                "amount": t.amount,
                "description": t.description,
                "date": t.date
            })
        with open(DATA_FILE, "w") as f:
            json.dump(data_to_save, f, indent=4)

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        self.save_transactions()
        print(f"\n{transaction.__class__.__name__} of Rs.{transaction.amount:.2f} added.")

    def show_transactions(self):
        if not self.transactions:
            print("\nNo transactions found.")
            return
        print("\n ________  All Transactions ______________")
        print(f"{'Date':<12} | {'Type':<7} | {'Amount':>10} | Description")
        print("-"*50)
        for t in self.transactions:
            print(t)
        print(f"\nTotal Transactions: {len(self)}")

    def __len__(self):
        return len(self.transactions)

    @classmethod
    def total_income(cls, transactions):
        return sum(t.amount for t in transactions if isinstance(t, Income))

    @classmethod
    def total_expense(cls, transactions):
        return sum(t.amount for t in transactions if isinstance(t, Expense))

    def show_summary(self):
        total_inc = FinanceManager.total_income(self.transactions)
        total_exp = FinanceManager.total_expense(self.transactions)
        balance = total_inc - total_exp
        print("\n____________  Finance Summary  ________________")
        print(f"{'Total Income':<15}: Rs.{total_inc:,.2f}")
        print(f"{'Total Expense':<15}: Rs.{total_exp:,.2f}")
        print(f"{'Balance':<15}: Rs.{balance:,.2f}")
        print("="*30)


# Main program
def main():
    manager = FinanceManager()
    print("Welcome to Personal Finance Manager")

    while True:
        print("\nMenu:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Show All Transactions")
        print("4. Show Finance Summary")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            amt = None
            while amt is None:
                amt_input = input("Enter income amount (Rs.): ").strip()
                amt = Transaction.validate_amount(amt_input)
            desc = input("Enter description (optional): ").strip()
            income = Income(amt, desc)
            manager.add_transaction(income)

        elif choice == "2":
            amt = None

            while amt is None:
                amt_input = input("Enter expense amount (Rs.): ").strip()
                amt = Transaction.validate_amount(amt_input)
            desc = input("Enter description (optional): ").strip()
            expense = Expense(amt, desc)
            manager.add_transaction(expense)

        elif choice == "3":
            manager.show_transactions()

        elif choice == "4":
            manager.show_summary()

        elif choice == "5":
            print("Exit Personal Finance Manager. Stay financially smart.")
            break
        else:
            print("Invalid choice. Try again.")


main()


