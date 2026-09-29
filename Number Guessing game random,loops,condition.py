import random

def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 9
    
    print("Welcome to the Number Guessing Game! You have 9 attempts.")
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
        except ValueError:
            print("Invalid input! Please enter a whole number.")
            continue
            
        attempts += 1
        if guess == secret_number:
            print(f"Correct! You guessed it in {attempts} attempts!")
            break
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")
            
    if attempts == max_attempts and guess != secret_number:
        print(f"Game Over! The number was {secret_number}.")

if __name__ == "__main__":
    play_game()
