#!/usr/bin/env python3
import random

BOLD = "\033[1m"
DIM = "\033[2m"
END = "\033[0m"


class Minesweeper:
    def __init__(self):
        self.size = 10

        self.mines = set()
        num_mines = random.randint(8, 13)
        while len(self.mines) < num_mines:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            self.mines.add((x, y))

        self.flags = set()
        self.revs = set()

    def get_neighbours(self, row, column):
        neighbours = set()
        for x in range(max(0, row - 1), min(row + 2, self.size)):
            for y in range(max(0, column - 1), min(column + 2, self.size)):
                if x == row and column == y:
                    continue
                neighbours.add((x, y))
        return neighbours

    def count_neignbour_mines(self, row, column):
        neighbours = self.get_neighbours(row, column)
        neighbour_mines = neighbours.intersection(self.mines)
        return len(neighbour_mines)

    def show_board(self):
        print(" |", end="")
        print(" ".join([str(i) for i in range(self.size)]))
        print("-+", end="")
        print("-" * 2 * self.size)
        for row in range(self.size):
            print(f"{row}|", end="")
            for column in range(self.size):
                if (row, column) in self.revs or (row, column) in self.flags:
                    if (row, column) in self.flags:
                        print(f"{BOLD}F{END}", end="")
                    elif (row, column) in self.mines:
                        print(f"{BOLD}X{END}", end="")
                    else:
                        n = self.count_neignbour_mines(row, column)
                        if n:
                            print(f"{n}", end="")
                        else:
                            print(f" ", end="")
                else:
                    print(f"{DIM}#{END}", end="")
                print(" ", end="")
            print("")

    def reveal(self, row, column):
        if (row, column) in self.flags:
            print(f"row {row}, columns {column} is flagged, unflag it first")
            return
        if (row, column) in self.revs:
            return
        self.revs.add((row, column))
        if self.count_neignbour_mines(row, column) == 0:
            for (r, c) in self.get_neighbours(row, column):
                self.reveal(r, c)

    def make_move(self):
        while True:
            move = input("[F]lag, [U]nflag or [R]eval? Row, Column: ")
            # TODO - error handling
            if move == "debug":
                print(f"Mines: {self.mines}")
                print(f"Revealed: {self.revs}")
                print(f"Flagged: {self.flags}")
                return
            try:
                action, row, column = move.split()
                row, column = int(row), int(column)
            except ValueError:
                print(f"unable to parse '{move}'")
                continue

            if row < 0 or row > self.size:
                print(f"row '{row}' is invalid, should be between 0 and {self.size}")
                continue

            if column < 0 or column > self.size:
                print(
                    f"column '{column}' is invalid, should be between 0 and {self.size}"
                )
                continue

            if action.lower() == "f":
                if (row, column) in self.revs:
                    print(f"Cannot flag a square that has already been revealed")
                    continue
                self.flags.add((row, column))
                return
            elif action.lower() == "u":
                self.flags.remove((row, column))
                return
            elif action.lower() == "r":
                self.reveal(row, column)
                return
            else:
                print(f"Unknow action '{action}'")

    def play(self):
        while True:
            self.show_board()

            if self.revs.intersection(self.mines):
                print(f"{BOLD}BOOM!!!{END}")
                print(f"You lost!")
                break
            if (
                self.flags == self.mines
                and len(self.flags.union(self.revs)) == self.size * self.size
            ):
                print(f"{BOLD}You have flagged all the mines!{END}")
                print(f"{BOLD}YOU WIN!!{END}")
                break

            self.make_move()


if __name__ == "__main__":
    while True:
        game = Minesweeper()
        game.play()
        again = input("Play again? [Yn] ")
        if again.lower().startswith("n"):
            break
