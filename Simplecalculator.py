#Simple calculator 
while True:
    #Display menu
    print("\n Simple Calculator")
    print("1. Add")
    print("2. Subtract ")
    print("3. Multiply ")
    print("4. Divide ")
    print("5. Exit")
    
    #get user input
    choice = int(input("Please enter the choice: "))

    if choice == 5:
        print("Exiting... Goodbye")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    match choice:
        case 1: 
            print(f"Result: {num1 + num2}")
        case 2:
            print(f"Result: {num1 - num2}")
        case 3:
            print(f"Result: {num1 * num2}")
        case 4:
            if num2!=0:
                print(f"Result: {num1 / num2}")
            else:
                print("Error: Division by zero not allowed")    
        case default:
            print("Invalid choice")
