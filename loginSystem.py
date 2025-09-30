# Simple login system with 3 attempts

# Stored correct credentials
username = "admin"
correct_password = "2025"

# Allow 3 login attempts
for i in range(3):
    user_input = input("Enter username: ")
    password_input = input("Enter password: ")

    # Check if entered credentials match stored credentials
    if user_input == username and password_input == correct_password:
        print("Logged in successfully")
        break  # Exit loop 
    else:
        print(" Invalid credentials, try again")
else:
    # Runs if loop completes without a break 
    print("Account locked")
     