import random

# Generate a random number between 1 and 100
number = random.randint(1, 100)
attempts = 0

# Start a loop that continues until the correct number is guessed
while True:
    # Get user's guess
    guess = int(input("Guess the number between 1 and 100: "))
    attempts += 1  # Count the number of attempts

    # Compare the guess with the random number
    if guess == number:
        print("Congratulations, you guessed it!")
        print(f"You took {attempts} attempts.")  # Display the number of attempts
        break  # Exit the loop since the correct number was guessed
    elif guess < number:
        print("Too low, try again.")
    else:
        print("Too high, try again.")
