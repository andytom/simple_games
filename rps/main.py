#!/usr/bin/env python3
import enum
import getpass
import math
import random
import time

# -- Constants ----------------------------------------------------------------
BOLD = "\033[1m"
DIM = "\033[2m"
END = "\033[0m"


# -- Helper Funcs -------------------------------------------------------------
def compare_moves(p1, p2):
    if p1 == p2:
        return 0
    if p1 == Moves.ROCK:
        if p2 == Moves.SCISSORS:
            return 1
        else:
            return 2
    if p1 == Moves.SCISSORS:
        if p2 == Moves.PAPER:
            return 1
        else:
            return 2
    if p1 == Moves.PAPER:
        if p2 == Moves.ROCK:
            return 1
        else:
            return 2


def ai_log(msg):
    print(f"{DIM}[AI] {msg}{END}", end="", flush=True)
    for _ in range(random.randint(10, 30)):
        print(f"{DIM}.{END}", end="", flush=True)
        time.sleep(0.01)
    print(f"{DIM} OK!{END}")


# -- Classes ------------------------------------------------------------------
class Moves(enum.Enum):
    ROCK = enum.auto()
    PAPER = enum.auto()
    SCISSORS = enum.auto()


class RPS:
    def __init__(self, player1, player2, best_of=5):
        self.player1 = player1
        self.player2 = player2
        self.min_games = math.ceil(best_of / 2)
        # 0 is a draw, 1 wins for player1 and 2 wins for player2
        self.metrics = [0, 0, 0]

    def play(self):
        print(f"Playing first to {self.min_games}")
        print("")
        while self.metrics[1] < self.min_games and self.metrics[2] < self.min_games:
            print("Player 1, select your move.")
            p1 = self.player1()
            print("Player 2, select your move.")
            p2 = self.player2()

            print("")
            print(f"Player 1 plays {BOLD}{p1.name}{END},", end=" ")
            print(f"Player 2 plays {BOLD}{p2.name}{END},", end=" ")

            result = compare_moves(p1, p2)
            if result == 0:
                print(f"{BOLD}It's a Draw!{END}")
            else:
                print(f"{BOLD}Player {result} wins!{END}")
            self.metrics[result] += 1
            print("")

        winner = 1
        if self.metrics[1] < self.metrics[2]:
            winner = 2
        print(f"Player {winner} has won {self.metrics[winner]} games.")
        print(f"{BOLD}PLAYER {winner} IS THE WINNER!!!{END}")
        print("")


# -- Players ------------------------------------------------------------------
def human_player():
    cleaned_move = None
    while cleaned_move is None:
        # Use getpass here so that if we have two humans playing each other the
        # second player can't see the first player's move.
        move = getpass.getpass("[R]ock, [P]aper or [S]cissors?")
        if move.lower().startswith("r"):
            cleaned_move = Moves.ROCK
        elif move.lower().startswith("p"):
            cleaned_move = Moves.PAPER
        elif move.lower().startswith("s"):
            cleaned_move = Moves.SCISSORS
        else:
            print(f"Invalid move '{move}'")

    return cleaned_move


def computer_player():
    ai_log("Initializing Neural Networks")
    ai_log("Loading Psychological Profiles")
    ai_log("Reticulating Splines")
    ai_log("Examining Quantum State")

    return random.choice(list(Moves))


def get_player(player_id):
    player = None
    while player is None:
        selected = input(f"Player {player_id} - [H]uman or [A]I? ")
        if selected.lower().startswith("h"):
            player = human_player
        elif selected.lower().startswith("a"):
            player = computer_player
        else:
            print(f"Unknown option '{selected}'")
    return player


# -- Main ---------------------------------------------------------------------
if __name__ == "__main__":
    p1 = get_player(1)
    p2 = get_player(2)
    print("")

    if p1 == human_player or p2 == human_player:
        print(f"{BOLD}Note:{END} The input for human users will not be echoed!")
        print("Just input your move and press 'Enter'")
        print("")

    game = RPS(p1, p2)
    game.play()

    print("Total Games  : {}".format(sum(game.metrics)))
    print(f"Draws        : {game.metrics[0]}")
    print(f"Player 1 Won : {game.metrics[1]}")
    print(f"Player 2 Won : {game.metrics[2]}")
