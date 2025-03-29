import random
import time

def display_welcome_message():
    print("Welcome to the Number Guessing Game!")
    print("I have selected a random number between 1 and 100.")
    print("Your goal is to guess the number in as few attempts as possible.")
    print("Good luck!\n")

def get_random_number():
    return random.randint(1, 100)

def get_user_guess():
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def give_feedback(guess, target):
    if guess < target:
        print("Too low! Try again.")
    elif guess > target:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number!")

def play_game():
    target_number = get_random_number()
    attempts = 0
    start_time = time.time()

    while True:
        guess = get_user_guess()
        attempts += 1
        give_feedback(guess, target_number)

        if guess == target_number:
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"You guessed the number in {attempts} attempts!")
            print(f"It took you {elapsed_time:.2f} seconds.")
            break

def main():
    display_welcome_message()
    play_game()
    while True:
        play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
        if play_again == "yes":
            print("\nStarting a new game...\n")
            play_game()
        elif play_again == "no":
            print("Thank you for playing! Goodbye!")
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

if __name__ == "__main__":
    main()