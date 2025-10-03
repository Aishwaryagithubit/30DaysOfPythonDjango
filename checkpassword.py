# Password Strength Checker
def check_password(password):
    if len(password) < 6:
        return "Weak"  
    
    letter = False
    number = False
    special = False

    for ch in password:
        if ch.isalpha():
            letter = True
        elif ch.isdigit():
            number = True
        elif ch in "!@#$%^&*()":
            special = True

    if letter and not (number or special):
        return "Weak" 
    elif letter and number and special:
        return "Strong"
    else:
        return "Medium"

# Loop until password is Medium or Strong
while True:
    user_password = input("Enter your password: ")
    strength = check_password(user_password)

    if strength == "Weak":
        print("Weak password.Try at least 6 characters and include numbers or special characters.")
    elif strength == "Medium":
        print("Medium password. Not bad, but you could make it stronger.")
        print("Password accepted!")
        break
    else:
        print("Strong password,Great job")
        print("Password accepted!")
        break


