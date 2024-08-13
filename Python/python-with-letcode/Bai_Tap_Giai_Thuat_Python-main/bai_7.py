import tkinter as tk
import random

class EmojiMatchGame:
    def __init__(self, master, rows, cols):
        # Khởi tạo đối tượng trò chơi
        self.master = master
        self.rows = rows
        self.cols = cols
        self.emojis = ["😀", "😂", "😅", "😊", "😎", "🥳", "🤔", "😍", "🤩", "🥺", "😢", "😡"]
        self.board = self.create_board()  # Tạo bảng với emoji được xáo trộn
        self.selected_emojis = []  # Lưu trữ các ô đã được chọn
        self.create_widgets()  # Tạo giao diện trò chơi

    def create_board(self):
        # Tạo bảng với emoji được xáo trộn và lặp lại để tạo cặp
        emojis = (self.emojis * 2)[:self.rows * self.cols]
        random.shuffle(emojis)
        return [emojis[i:i+self.cols] for i in range(0, len(emojis), self.cols)]

    def create_widgets(self):
        # Tạo giao diện trò chơi với các nút cho mỗi ô trong bảng
        self.buttons = [[None] * self.cols for _ in range(self.rows)]

        for i in range(self.rows):
            for j in range(self.cols):
                # Tạo nút cho mỗi ô với kích thước và phương thức xử lý sự kiện nhấp chuột
                button = tk.Button(self.master, text="", font=("Arial", 12), width=4, height=2, command=lambda r=i, c=j: self.on_click(r, c))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def update_buttons(self):
        # Cập nhật nút để hiển thị emoji khi chúng được chọn hoặc ẩn đi khi chúng đã được tìm thấy
        for i in range(self.rows):
            for j in range(self.cols):
                if (i, j) not in self.selected_emojis:
                    self.buttons[i][j]["text"] = self.board[i][j]
                else:
                    self.buttons[i][j]["text"] = ""

    def on_click(self, row, col):
        # Xử lý sự kiện khi người chơi nhấp chuột vào ô
        self.selected_emojis.append((row, col))  # Lưu trữ ô đã chọn
        self.update_buttons()  # Cập nhật giao diện

        if len(self.selected_emojis) == 2:
            r1, c1 = self.selected_emojis[0]
            r2, c2 = self.selected_emojis[1]

            # Kiểm tra cặp emoji đã chọn
            if self.board[r1][c1] == self.board[r2][c2]:
                self.buttons[r1][c1]["state"] = "disabled"  # Tắt nút cho ô 1
                self.buttons[r2][c2]["state"] = "disabled"  # Tắt nút cho ô 2

            # Đặt hàm clear_selection để xóa các ô đã chọn sau 1 giây
            self.master.after(1000, self.clear_selection)

    def clear_selection(self):
        # Xóa các ô đã chọn và cập nhật giao diện
        self.selected_emojis = []
        self.update_buttons()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Emoji Match")
    game = EmojiMatchGame(root, rows=4, cols=4)  # Tạo đối tượng trò chơi với bảng 4x4
    root.mainloop()
