"""Console Hangman game for the CodeAlpha Python Programming tasks."""

import random

WORDS = ["python", "coding", "laptop", "function", "variable"]
MAX_INCORRECT_GUESSES = 6


def display_word(secret_word: str, guessed_letters: set[str]) -> str:
    """Return the word with unguessed letters hidden."""
    return " ".join(letter if letter in guessed_letters else "_" for letter in secret_word)


def get_letter() -> str:
    """Read and validate one alphabetic character."""
    while True:
        guess = input("Guess one letter: ").strip().lower()
        if len(guess) == 1 and guess.isalpha():
            return guess
        print("Please enter exactly one letter.")


def play_game() -> None:
    secret_word = random.choice(WORDS)
    guessed_letters: set[str] = set()
    incorrect_guesses = 0

    print("\nWelcome to Hangman!")
    print(f"The word has {len(secret_word)} letters. You can make {MAX_INCORRECT_GUESSES} incorrect guesses.")

    while incorrect_guesses < MAX_INCORRECT_GUESSES:
        print(f"\nWord: {display_word(secret_word, guessed_letters)}")
        print(f"Incorrect guesses remaining: {MAX_INCORRECT_GUESSES - incorrect_guesses}")
        guess = get_letter()

        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue

        guessed_letters.add(guess)
        if guess in secret_word:
            print("Good guess!")
            if all(letter in guessed_letters for letter in secret_word):
                print(f"\nYou won! The word was '{secret_word}'.")
                return
        else:
            incorrect_guesses += 1
            print("That letter is not in the word.")

    print(f"\nYou ran out of guesses. The word was '{secret_word}'.")


def main() -> None:
    play_game()


if __name__ == "__main__":
    main()
