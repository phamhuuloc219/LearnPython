import tkinter as tk
from tkinter import colorchooser

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Paint App")

        self.pen_color = "black"

        self.canvas = tk.Canvas(root, bg="white", width=800, height=600)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        self.setup_menu()

        self.old_x = None
        self.old_y = None

        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

    def setup_menu(self):
        menu_bar = tk.Menu(self.root)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_canvas)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.destroy)

        menu_bar.add_cascade(label="File", menu=file_menu)

        color_menu = tk.Menu(menu_bar, tearoff=0)
        color_menu.add_command(label="Choose Color", command=self.choose_color)

        menu_bar.add_cascade(label="Color", menu=color_menu)

        self.root.config(menu=menu_bar)

    def paint(self, event):
        x, y = event.x, event.y
        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x, self.old_y, x, y, width=2, fill=self.pen_color, capstyle=tk.ROUND, smooth=tk.TRUE)

        self.old_x = x
        self.old_y = y

    def reset(self, event):
        self.old_x = None
        self.old_y = None

    def new_canvas(self):
        self.canvas.delete("all")

    def choose_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.pen_color = color

if __name__ == "__main__":
    root = tk.Tk()
    paint_app = PaintApp(root)
    root.mainloop()
