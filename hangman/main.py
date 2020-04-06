#!/usr/bin/env python3
import os
import random
import string

# -- Constants ----------------------------------------------------------------
BOLD = "\033[1m"
END = "\033[0m"

HANGED_MEN = [
    """
    +------------+
    |            |
    |            |
    |            |
    |            |
    |            |
    |            |
    |            |
    |            |
    +------------+""",
    """
    +------------+
    |            |
    |            |
    |            |
    |            |
    |            |
    |            |
    |  ________  |
    |            |
    +------------+""",
    """
    +------------+
    |            |
    |  |         |
    |  |         |
    |  |         |
    |  |         |
    |  |         |
    |  L_______  |
    |            |
    +------------+""",
    """
    +------------+
    |            |
    |  +------   |
    |  |         |
    |  |         |
    |  |         |
    |  |         |
    |  L_______  |
    |            |
    +------------+""",
    """
    +------------+
    |            |
    |  +----+-   |
    |  |    |    |
    |  |         |
    |  |         |
    |  |         |
    |  L_______  |
    |            |
    +------------+""",
    """
    +------------+
    |            |
    |  +----+-   |
    |  |    |    |
    |  |    o    |
    |  |         |
    |  |         |
    |  L_______  |
    |            |
    +------------+""",
    """
    +------------+
    |            |
    |  +----+-   |
    |  |    |    |
    |  |    o    |
    |  |    |    |
    |  |         |
    |  L_______  |
    |            |
    +------------+""",
    """
    +------------+
    |            |
    |  +----+-   |
    |  |    |    |
    |  |    o    |
    |  |   /|    |
    |  |         |
    |  L_______  |
    |            |
    +------------+""",
    """
    +------------+
    |            |
    |  +----+-   |
    |  |    |    |
    |  |    o    |
    |  |   /|\\   |
    |  |         |
    |  L_______  |
    |            |
    +------------+""",
    """
    +------------+
    |            |
    |  +----+-   |
    |  |    |    |
    |  |    o    |
    |  |   /|\\   |
    |  |   /     |
    |  L_______  |
    |            |
    +------------+""",
    """
    +------------+
    |            |
    |  +----+-   |
    |  |    |    |
    |  |    o    |
    |  |   /|\\   |
    |  |   / \\   |
    |  L_______  |
    |            |
    +------------+""",
]


class Hangman:
    def __init__(self):
        dirname = os.path.dirname(__file__)
        words_file = os.path.join(dirname, "words")
        with open(words_file) as f:
            words = f.read().lower().split()

        self.word = random.choice(words)
        self.guesses = set()

    def get_guess(self):
        while True:
            guess = input("Pick a letter: ").lower()
            if len(guess) != 1 or guess not in string.ascii_lowercase:
                print(f"'{guess}' is not a valid letter.")
            elif guess in self.guesses:
                print(f"You have already guessed '{guess}'")
            else:
                return guess

    def play(self):
        print("Let's play Hangman!")
        while True:
            incorrect_guesses = [c for c in self.guesses if c not in self.word]
            revealed_word = " ".join(
                [c if c in self.guesses else "_" for c in self.word]
            )

            print(HANGED_MEN[len(incorrect_guesses)])
            print("{:^24}".format(revealed_word))
            print("")
            if len(incorrect_guesses) > 0:
                incorrect_guesses.sort()
                print("Incorrect: {}".format(" ".join(incorrect_guesses)))
                print("")

            # The +1 here is to make sure we exit at the when we display the 0
            # chances remain sprite not on the turn after.
            if len(incorrect_guesses) + 1 == len(HANGED_MEN):
                print(f"{BOLD}You lost!{END}")
                print(f"Correct answer was {BOLD}'{self.word}'{END}.")
                break
            if revealed_word.count("_") == 0:
                print(f"{BOLD}You win!{END}")
                break
            new_guess = self.get_guess()
            self.guesses.add(new_guess)


if __name__ == "__main__":
    while True:
        game = Hangman()
        game.play()
        again = input("Play again? [Yn] ")
        if again.lower().startswith("n"):
            break
