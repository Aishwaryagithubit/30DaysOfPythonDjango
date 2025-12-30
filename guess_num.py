import random
secret_number = random.randint(1, 100)

print("Welcome to the Number Guessing Game")
while True:
    guess = int(input("Enter your guess: "))
    
    if guess < secret_number:
        print("Too low,Try again.")
    elif guess > secret_number:
        print("Too high,Try again.")
    else:
        print("Congratulations! You guessed the number correctly")
        break
