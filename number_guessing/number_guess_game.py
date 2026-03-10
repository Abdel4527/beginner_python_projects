from random import randint
from logo import logo

EASY_LIVES = 10
HARD_LIVES = 5


def print_separator():
    print("-" * 45)


def check_answer(user_guess, answer, lives):
    if user_guess > answer:
        print("  Too high! Try a lower number.")
        lives -= 1
    elif user_guess < answer:
        print("  Too low! Try a higher number.")
        lives -= 1
    else:
        print(f"\n  Correct! The answer was {answer}.")
    return lives


def set_difficulty():
    print_separator()
    while True:
        difficulty = input("  Choose difficulty  [easy / hard]: ").strip().lower()
        if difficulty == "easy":
            print(f"  You have {EASY_LIVES} attempts. Good luck!\n")
            return EASY_LIVES
        elif difficulty == "hard":
            print(f"  You have {HARD_LIVES} attempts. Good luck!\n")
            return HARD_LIVES
        else:
            print("  Invalid choice. Please type 'easy' or 'hard'.")


def get_guess():
    while True:
        try:
            guess = int(input("  Your guess: "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("  Please enter a number between 1 and 100.")
        except ValueError:
            print("  That's not a valid number. Try again.")


def play_game():
    answer = randint(1, 100)
    lives = set_difficulty()
    attempts_used = 0

    while lives > 0:
        print_separator()
        print(f"  Attempts remaining: {lives}")
        user_guess = get_guess()
        attempts_used += 1

        lives = check_answer(user_guess, answer, lives)

        if user_guess == answer:
            print_separator()
            print(f"  You won in {attempts_used} attempt(s)!")
            print_separator()
            return True

        if lives == 0:
            print_separator()
            print(f"  You ran out of attempts! The number was {answer}.")
            print_separator()
            return False

        if lives == 1:
            print(f"  Warning: only 1 attempt left!")
        elif lives <= 3:
            print(f"  Hint: the number is between 1 and 100.")


def main():
    print(logo)
    print("  Welcome to the Number Guessing Game!")
    print("  I'm thinking of a number between 1 and 100.")

    wins = 0
    losses = 0

    while True:
        result = play_game()
        if result:
            wins += 1
        else:
            losses += 1

        print(f"  Score  ->  Wins: {wins}  |  Losses: {losses}")
        print_separator()
        again = input("  Play again? [yes / no]: ").strip().lower()
        if again not in ("yes", "y"):
            print_separator()
            print(f"  Thanks for playing! Final score: {wins}W / {losses}L")
            print_separator()
            break
        print("\n")


main()
