# Simple Banking System
balance = 0

def check_balance():
    print(f"Your current balance is: ${balance}")

# Function to deposit money
def deposit():
    global balance
    try:
        amount = float(input("Enter an amount to deposit: "))
        if amount > 0:
            balance += amount
            print(f"Deposited ${amount}. New balance: ${balance}")
        else:
            print("Please enter a positive amount.")
    except ValueError:
        print("Invalid input,Enter a number.")

# Function to withdraw money
def withdraw():
    global balance
    try:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Please enter a positive amount")
        elif amount > balance:
            print("Insufficient funds!")
        else:
            balance -= amount
            print(f"Withdrawn ${amount}. New balance: ${balance}")
    except ValueError:
        print("Invalid input,Enter a number")

# Main menu loop
while True:
    print("\n Welcome to Simple Bank System")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        check_balance()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        print("Thank you for using Simple Bank")
        break
    else:
        print("Invalid choice, please select 1-4")



