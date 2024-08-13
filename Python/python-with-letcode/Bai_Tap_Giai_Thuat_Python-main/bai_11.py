import tkinter as tk
import random


class SnakeGame:
    def __init__(self, master, width=400, height=400, block_size=20):
        self.master = master
        self.master.title("Snake Game")
        self.width = width
        self.height = height
        self.block_size = block_size
        self.canvas = tk.Canvas(
            self.master, width=self.width, height=self.height, bg="black"
        )
        self.canvas.pack()
        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.direction = "Right"
        self.food = self.create_food()
        self.score = 0
        self.score_display = self.canvas.create_text(
            10, 10, text=f"Score: {self.score}", fill="white", anchor="nw"
        )
        self.canvas.bind_all("<Key>", self.on_key_press)
        self.master.after(100, self.update)

    def create_food(self):
        x = (
            random.randint(1, (self.width - self.block_size) / self.block_size)
            * self.block_size
        )
        y = (
            random.randint(1, (self.height - self.block_size) / self.block_size)
            * self.block_size
        )
        return self.canvas.create_oval(
            x, y, x + self.block_size, y + self.block_size, fill="red"
        )

    def move_snake(self):
        head = self.snake[0]
        if self.direction == "Up":
            new_head = (head[0], head[1] - self.block_size)
        elif self.direction == "Down":
            new_head = (head[0], head[1] + self.block_size)
        elif self.direction == "Left":
            new_head = (head[0] - self.block_size, head[1])
        elif self.direction == "Right":
            new_head = (head[0] + self.block_size, head[1])

        self.snake = [new_head] + self.snake[:-1]

    def check_collision(self):
        head = self.snake[0]
        if head in self.snake[1:]:
            return True
        if (
            head[0] < 0
            or head[0] >= self.width
            or head[1] < 0
            or head[1] >= self.height
        ):
            return True
        return False

    def check_food(self):
        head = self.snake[0]
        food_coords = self.canvas.coords(self.food)
        if head[0] == food_coords[0] and head[1] == food_coords[1]:
            self.snake.append((0, 0))  # Add a new segment to the snake
            self.canvas.delete(self.food)  # Remove the food
            self.food = self.create_food()  # Create a new food
            self.score += 1
            self.update_score()

    def update_score(self):
        self.canvas.itemconfig(self.score_display, text=f"Score: {self.score}")

    def update(self):
        if not self.check_collision():
            self.move_snake()
            self.check_food()
            self.update_snake()
            self.master.after(100, self.update)
        else:
            self.game_over()

    def update_snake(self):
        self.canvas.delete("snake")
        for segment in self.snake:
            x, y = segment
            self.canvas.create_rectangle(
                x,
                y,
                x + self.block_size,
                y + self.block_size,
                fill="green",
                tags="snake",
            )

    def on_key_press(self, event):
        key = event.keysym
        if (
            key == "Up"
            and self.direction != "Down"
            or key == "Down"
            and self.direction != "Up"
            or key == "Left"
            and self.direction != "Right"
            or key == "Right"
            and self.direction != "Left"
        ):
            self.direction = key

    def game_over(self):
        self.canvas.create_text(
            self.width / 2,
            self.height / 2,
            text="Game Over",
            fill="white",
            font=("Helvetica", 16),
            anchor="center",
        )


if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
