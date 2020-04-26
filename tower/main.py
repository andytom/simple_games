#!/usr/bin/env python3

BOLD = "\033[1m"
DIM = "\033[2m"
END = "\033[0m"

TOWERS = {
    "": """
      _      
     | |     
     | |     
     | |     
     | |     
_____| |_____
""",
    "123": """
      _      
     | |     
    _|_|_    
   |_____|   
  |_______|  
_|_________|_
""",
    "23": """
      _      
     | |     
     | |     
   __|_|__   
  |_______|  
_|_________|_
""",
    "12": """
      _      
     | |     
     | |     
    _|_|_    
   |_____|   
__|_______|__
""",
    "13": """
      _      
     | |     
     | |     
    _|_|_    
  _|_____|_  
_|_________|_
""",
    "1": """
      _      
     | |     
     | |     
     | |     
    _|_|_    
___|_____|___
""",
    "2": """
      _      
     | |     
     | |     
     | |     
   __|_|__   
__|_______|__
""",
    "3": """
      _      
     | |     
     | |     
     | |     
  ___|_|___  
_|_________|_
""",
}


class HanoiTowers:
    def __init__(self):
        self.left = [1, 2, 3]
        self.middle = []
        self.right = []
        self.moves = 0

    def show_towers(self):
        left_tower = TOWERS.get("".join([str(i) for i in self.left]))
        middle_tower = TOWERS.get("".join([str(i) for i in self.middle]))
        right_tower = TOWERS.get("".join([str(i) for i in self.right]))

        output = zip(*[i.split("\n") for i in [left_tower, middle_tower, right_tower]])
        for i in output:
            print("".join(i))

    def get_tower(self, msg):
        full_msg = f"{msg} [L]eft, [M]iddle or [R]ight: "
        while True:
            tower = input(full_msg).lower()
            if tower.startswith("l"):
                return self.left
            elif tower.startswith("m"):
                return self.middle
            elif tower.startswith("r"):
                return self.right
            else:
                print(f"'{tower}' is not a valid choice")

    def make_move(self):
        while True:
            src = self.get_tower("Which tower should we move from")
            dest = self.get_tower("Which tower should we move to")

            if src == dest:
                print("Can't move from and to the same tower")
            elif len(src) == 0:
                print("No disks to move off that tower")
            elif len(dest) and src[0] > dest[0]:
                print(f"Cannot move {src[0]} on top of {dest[0]}")
            else:
                disk = src.pop(0)
                dest.insert(0, disk)
                return

    def play(self):
        print(f"{BOLD}Move all the disks to the Right Tower!{END}")
        while True:
            self.show_towers()
            if self.right == [1, 2, 3]:
                print(f"{BOLD}You have won, it took you {self.moves} move(s)!${END}")
                break
            self.make_move()
            self.moves += 1


if __name__ == "__main__":
    again = True
    while again:
        game = HanoiTowers()
        game.play()
        again = not input("Play again? [Yn] ").lower().startswith("n")
