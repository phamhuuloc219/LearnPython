import tkinter as tk
import random

class FloodItGame:
    def __init__(self, master, rows, cols):
        self.master = master
        self.rows = rows
        self.cols = cols
        self.colors = ["red", "green", "blue", "yellow", "magenta", "cyan"]
        self.board = [[random.choice(self.colors) for _ in range(cols)] for _ in range(rows)]
        self.target_color = self.board[0][0]

        self.create_widgets()

    def create_widgets(self):
        # Tạo một Canvas để vẽ bảng trò chơi
        self.canvas = tk.Canvas(self.master, width=self.cols * 50, height=self.rows * 50)
        self.canvas.pack()

        # Vẽ bảng trò chơi ban đầu
        self.draw_board()

        # Gán sự kiện nhấp chuột cho Canvas
        self.canvas.bind("<Button-1>", self.on_click)

    def draw_board(self):
        # Xóa tất cả các đối tượng trên Canvas
        self.canvas.delete("all")

        # Vẽ từng ô trên bảng với kích thước 50x50 pixel
        for row in range(self.rows):
            for col in range(self.cols):
                x1, y1 = col * 50, row * 50
                x2, y2 = x1 + 50, y1 + 50
                color = self.board[row][col]
                # Vẽ hình chữ nhật (ô) với màu sắc được chọn
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")

    def flood_fill(self, row, col, replacement_color):
        # Thuật toán "flood fill" để thay đổi màu sắc của các ô liên quan
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return
        if self.board[row][col] == self.target_color:
            self.board[row][col] = replacement_color
            self.flood_fill(row + 1, col, replacement_color)
            self.flood_fill(row - 1, col, replacement_color)
            self.flood_fill(row, col + 1, replacement_color)
            self.flood_fill(row, col - 1, replacement_color)

    def on_click(self, event):
        # Xử lý sự kiện khi người chơi nhấp chuột vào ô trên bảng
        col = event.x // 50
        row = event.y // 50
        replacement_color = self.board[row][col]
        # Áp dụng thuật toán flood fill từ ô gốc (0, 0) với màu sắc được chọn
        self.flood_fill(0, 0, replacement_color)
        # Vẽ lại bảng sau khi thay đổi màu sắc
        self.draw_board()

if __name__ == "__main__":
    # Tạo một cửa sổ giao diện đồ họa Tkinter
    root = tk.Tk()
    root.title("Flood-It")
    # Tạo một đối tượng trò chơi Flood-It với bảng 10x10
    game = FloodItGame(root, rows=10, cols=10)
    # Bắt đầu vòng lặp sự kiện Tkinter
    root.mainloop()
