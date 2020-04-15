#!/usr/bin/env python3
import random
from collections import namedtuple

Duck = namedtuple("Duck", ["name", "template"])

BOLD = "\033[1m"
END = "\033[0m"

HEADER = "".join([f"    {l}   " for l in "abcdefghi"])

DUCK_TEMPLATES = [
    """
    {}   
   _    
 <(.)__.
~~(___/~
    {}   
""",
    """
    {}   
   _    
 =(.)__.
~~(___/~
    {}   
""",
    """
    {}   
   _    
 >(.)__.
~~(___/~
    {}   
""",
    """
    {}   
     _  
 .__(.)>
~~\\___)~
    {}   
""",
    """
    {}   
     _  
 .__(.)=
~~\\___)~
    {}   
""",
    """
    {}   
     _  
 .__(.)<
~~\\___)~
    {}   
""",
]


class Game:
    def __init__(self):
        self.ducks = [Duck(name, random.choice(DUCK_TEMPLATES)) for name in "abcdefghi"]
        random.shuffle(self.ducks)
        self.swaps = 0

    def show_ducks(self):
        print(f"{BOLD}{HEADER}{END}", end="")
        output = zip(
            *[
                d.template.format(d.name, i).split("\n")
                for i, d in enumerate(self.ducks)
            ]
        )

        for i in output:
            print("".join(i))

    def get_duck(self, msg):
        while True:
            try:
                duck_num = input(msg)
                duck_num = int(duck_num)
                if duck_num >= 0 and duck_num < len(self.ducks):
                    return duck_num
                print(f"'{duck_num}' is not a valid duck")
            except ValueError:
                print(f"'{duck_num}' is not a valid duck")

    def play(self):
        print(f"{BOLD}Get your ducks in a row!{END}")
        while True:
            self.show_ducks()
            if "".join([d.name for d in self.ducks]) == "abcdefghi":
                print(f"It took {self.swaps} swaps, to get your ducks in a row!")
                break
            print("Which ducks should we swap?")
            x = self.get_duck("Pick a duck: ")
            y = self.get_duck("Pick another duck: ")
            self.ducks[x], self.ducks[y] = self.ducks[y], self.ducks[x]
            self.swaps += 1


if __name__ == "__main__":
    while True:
        game = Game()
        game.play()
        again = input("Play again? [Yn] ")
        if again.lower().startswith("n"):
            break
