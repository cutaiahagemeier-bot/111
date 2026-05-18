import random


def play() -> None:
    """Run a small number guessing game."""
    secret = random.randint(1, 20)
    attempts = 0

    print("Guess the secret number between 1 and 20!")

    while True:
        guess_text = input("Your guess: ").strip()
        if not guess_text.isdigit():
            print("Please type a whole number.")
            continue

        guess = int(guess_text)
        attempts += 1

        if guess < secret:
            print("Too low. Try again!")
        elif guess > secret:
            print("Too high. Try again!")
        else:
            print(f"You got it in {attempts} attempts. Nice!")
            break


if __name__ == "__main__":
    play()
