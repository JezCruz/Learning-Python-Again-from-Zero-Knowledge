# Python Test Games - Number Guessing Game.
print("\n=== Number Guessing Game ===\n")

secret_number = 7
guess = 0
attempts = 0

while guess != secret_number:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low!\n")
    elif guess > secret_number:
        print("Too high!\n")
    else:
        print(f"Correct! The number is {secret_number}")
        print(f"You guessed it in {attempts} attempts.")