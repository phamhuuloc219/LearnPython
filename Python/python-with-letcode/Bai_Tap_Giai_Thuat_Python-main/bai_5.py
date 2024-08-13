import tkinter as tk
import random

class Dot:
    def __init__(self, canvas, game):
        self.canvas = canvas
        self.game = game
        self.id = canvas.create_oval(0, 0, 20, 20, fill="red")
        self.canvas.move(self.id, random.randint(0, 780), random.randint(0, 580))

    def check_collision(self, other):
        coords = self.canvas.coords(self.id)
        other_coords = self.canvas.coords(other)
        return (other_coords[0] < coords[2] and other_coords[2] > coords[0] and
                other_coords[1] < coords[3] and other_coords[3] > coords[1])

class DestroyTheDotsGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Destroy the Dots")

        self.canvas = tk.Canvas(master, width=800, height=600, bg="white")
        self.canvas.pack()

        self.dots = []
        for _ in range(10):
            dot = Dot(self.canvas, self)
            self.dots.append(dot)

        self.player = self.canvas.create_rectangle(390, 290, 410, 310, fill="black")

        self.score = 0
        self.score_label = tk.Label(master, text="Score: 0", font=("Helvetica", 16))
        self.score_label.pack()

        self.master.bind("<Left>", self.move_left)
        self.master.bind("<Right>", self.move_right)
        self.master.bind("<Up>", self.move_up)
        self.master.bind("<Down>", self.move_down)

        self.game_loop()

    def move_left(self, event):
        self.canvas.move(self.player, -5, 0)
        self.check_collisions()

    def move_right(self, event):
        self.canvas.move(self.player, 5, 0)
        self.check_collisions()

    def move_up(self, event):
        self.canvas.move(self.player, 0, -5)
        self.check_collisions()

    def move_down(self, event):
        self.canvas.move(self.player, 0, 5)
        self.check_collisions()

    def check_collisions(self):
        for dot in self.dots:
            if dot.check_collision(self.player):
                self.canvas.delete(dot.id)
                new_dot = Dot(self.canvas, self)
                self.dots[self.dots.index(dot)] = new_dot
                self.increase_score()

    def increase_score(self):
        self.score += 1
        self.score_label.config(text="Score: {}".format(self.score))

    def game_loop(self):
        self.check_collisions()
        self.master.after(30, self.game_loop)

if __name__ == "__main__":
    root = tk.Tk()
    game = DestroyTheDotsGame(root)
    root.mainloop()
