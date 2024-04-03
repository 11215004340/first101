#importing the random module
import random

#Generate a random number between 1 to 10
secret_number = random.randint(1, 10)

#Mximum attempts allowed
max_attempts = 3

# Function to display a welcome message
def welcome_message():
    print("\nWelcome to the Number Guessing Game!")
    print(f"You have{max_attempts} attempts to guess the correct number.")

# Function for recursive guessing
def guess_recursive(attempts_left):
    #get user input
    guess = int(input("\nGuess the number (between 1 and 10): "))

    #check if the guess is correct
    if guess == secret_number:
        print("Congratulation! you guessed the correct number!")
    else:
        print(f"wrong guess. Attempts left: {attempts_left-1}")
        if attempts_left > 1:
            #mark a recursive call for another guess
            guess_recursive(attempt_left - 1)
        else:
            print(f"\nsorry, you couldn't guess the number. The correct number was {secret_number}.")

#calling the function 
welcome_message()
guess_recursive(max_attempts)

#using id() to get memory addresses
print(f"Memory address of Secret number {secret_number} is: {id(secret_number)}")