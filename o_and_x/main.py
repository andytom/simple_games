#!/usr/bin/env python3

BOLD = "\033[1m"
DIM = "\033[2m"
END = "\033[0m"


class Game:
    def __init__(self):
        # The board is a 1-d array where the indexes match the following
        # positions in the board.
        #
        #   0 1 2
        #   3 4 5
        #   6 7 8
        #
        self.board = [None for _ in range(9)]

    def have_winner(self):
        # Check the rows
        if self.board[0] == self.board[1] == self.board[2] != None:
            return self.board[0]
        if self.board[3] == self.board[4] == self.board[5] != None:
            return self.board[3]
        if self.board[6] == self.board[7] == self.board[8] != None:
            return self.board[6]
        # Check the columns
        if self.board[0] == self.board[3] == self.board[6] != None:
            return self.board[0]
        if self.board[1] == self.board[4] == self.board[7] != None:
            return self.board[1]
        if self.board[2] == self.board[5] == self.board[8] != None:
            return self.board[2]
        # Check the diagonals
        if self.board[0] == self.board[4] == self.board[8] != None:
            return self.board[0]
        if self.board[2] == self.board[4] == self.board[6] != None:
            return self.board[2]
        # If there are no matches then we don't have a winner so return None
        return None

    def show_board(self):
        formatted = [
            f"{BOLD}{value}{END}" if value is not None else f"{DIM}{index}{END}"
            for index, value in enumerate(self.board)
        ]

        print("|".join(formatted[0:3]))
        print("-+-+-")
        print("|".join(formatted[3:6]))
        print("-+-+-")
        print("|".join(formatted[6:9]))

    def player_move(self, player):
        cleaned_move = None
        while cleaned_move is None:
            try:
                move = input(f"{player}, Select a square: ")
                move = int(move)
            except ValueError:
                print(f"'{move}' is not a valid square")
                continue
            if move < 0 or 8 < move:
                print(f"'{move}' is out of range.")
            elif self.board[move] != None:
                print(f"{move} is already taken.")
            else:
                cleaned_move = move

        self.board[cleaned_move] = player
        print("")
        self.show_board()

    def play(self):
        self.show_board()
        while True:
            self.player_move("O")
            if self.have_winner():
                print("")
                print("{} has won".format(self.have_winner()))
                break
            if self.board.count(None) == 0:
                print("")
                print("Game is a Draw")
                break

            self.player_move("X")

            if self.have_winner():
                print("")
                print("{} has won".format(self.have_winner()))
                break
            if self.board.count(None) == 0:
                print("")
                print("Game is a Draw")
                break


if __name__ == "__main__":
    try:
        while True:
            print("Starting a new game!")
            print("")
            g = Game()
            g.play()
            print("")
            again = input("Play again? [yN]")
            if not again.lower().startswith("y"):
                break
            print("")
    except (KeyboardInterrupt, EOFError):
        print("")
        print("Exiting the game.")
