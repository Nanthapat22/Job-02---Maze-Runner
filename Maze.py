import os
import time

class Maze:
    def __init__(self) -> None:
        self.maze = [
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", " ", " ", " ", "X", " ", "X"],
            ["X", " ", "X", " ", "X", " ", " "],
            ["X", " ", "X", " ", "X", " ", "X"],
            ["X", " ", "X", " ", " ", " ", "X"],
            ["X", " ", "X", "X", "X", "X", "X"],
        ]
        self.player = Pos(5, 1)
        self.end = Pos(2, 6)
        self.maze[self.player.y][self.player.x] = "P"
        self.maze[self.end.y][self.end.x] = "E"

    def is_in_bound(self, y, x):
        return 0 <= y < len(self.maze) and 0 <= x < len(self.maze[0])

    def print_maze(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("\n\n\n")
        for row in self.maze:
            for col in row:
                print(col, " ", end="")
            print("")
        print("\n\n\n")

    def print_end(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("\n\n\n")
        print(">>>>> ยินดีด้วยครับ!!! <<<<<")
        print("\n\n\n")

    def move_up(self):
        next_move = Pos(self.player.y - 1, self.player.x)
        if self.is_in_bound(next_move.y, next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.player.y][self.player.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.player = next_move
                time.sleep(0.25)
                return True
            elif self.maze[next_move.y][next_move.x] == "E":
                self.print_end()
                return False
        return False

    def move_down(self):
        next_move = Pos(self.player.y + 1, self.player.x)
        if self.is_in_bound(next_move.y, next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.player.y][self.player.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.player = next_move
                time.sleep(0.25)
                return True
            elif self.maze[next_move.y][next_move.x] == "E":
                self.print_end()
                return False
        return False

    def move_left(self):
        next_move = Pos(self.player.y, self.player.x - 1)
        if self.is_in_bound(next_move.y, next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.player.y][self.player.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.player = next_move
                time.sleep(0.25)
                return True
            elif self.maze[next_move.y][next_move.x] == "E":
                self.print_end()
                return False
        return False

    def move_right(self):
        next_move = Pos(self.player.y, self.player.x + 1)
        if self.is_in_bound(next_move.y, next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.player.y][self.player.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.player = next_move
                time.sleep(0.25)
                return True
            elif self.maze[next_move.y][next_move.x] == "E":
                self.print_end()
                return False
        return False

class Pos:
    def __init__(self, y, x) -> None:
        self.y = y
        self.x = x

m = Maze()
m.print_maze()

u, r, d = 1, 1, 1

while u <= 4:
    if m.move_up():
        m.print_maze()
        u += 1

u = 1
while r <= 2:
    if m.move_right():
        m.print_maze()
        r += 1

r = 1
while d <= 3:
    if m.move_down():
        m.print_maze()
        d += 1

d = 1
while r <= 2:
    if m.move_right():
        m.print_maze()
        r += 1

r = 1
while u <= 2:
    if m.move_up():
        m.print_maze()
        u += 1

u = 1
while r <= 1:
    if m.move_right():
        m.print_maze()
        r += 1

r = 1
