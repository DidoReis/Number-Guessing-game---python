import random

def number_guessing():
    # Generate a random number between 1 and 100 as the secret number
    secret_number = random.randint(1, 100)
    # Initialize the variable to keep track of the number of attempts
    attempts = 0

    # Print the welcome message
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")

    # Start a loop to allow the user to make guesses
    while True:
        try:
            # Prompt the user to input a guess
            guess = int(input("Take a guess: "))
            # Increment the number of attempts
            attempts += 1
            # Check if the guess is out of the valid range
            if guess < 1 or guess > 100:
                print("Invalid guess! Please enter a number between 1 and 100")
            # Check if the guess is lower than the secret number
            elif guess < secret_number:
                print("Too low! Try again")
            # Check if the guess is higher than the secret number
            elif guess > secret_number:
                print("Too high! Try again")
            else:
                # If the guess is equal to the secret number, the player has won
                # Display a congratulatory message along with the number of attempts
                print(f"Congratulations! You guessed the number in {attempts} attempts")
                break
        except ValueError:
            # Handle the case when the user enters a non-integer value
            print("Invalid input. Please enter a valid number.")

# Call the number_guessing function to start the game
number_guessing()
