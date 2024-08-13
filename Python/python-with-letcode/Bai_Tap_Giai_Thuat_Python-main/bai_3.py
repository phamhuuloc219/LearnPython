import tkinter as tk
from tkinter import ttk

def draw_meme(event=None):
    meme_canvas.delete("all")
    meme_canvas.create_image(0, 0, anchor="nw", image=image)
    meme_canvas.create_text(
        20, 20, text=top_text.get(), 
        fill=color.get(), 
        font=(font.get(), int(size.get())),
        anchor="nw") 
    meme_canvas.create_text(
        20, 320, text=bottom_text.get(), 
        fill=color.get(),
        font=(font.get(), int(size.get())),
        anchor="nw") 

def color_changed(event):
    draw_meme()

def font_changed(event):
    draw_meme()

def size_changed(event):
    draw_meme()

app = tk.Tk()
app.title("Meme Generator")

# Top Text
top_text_label = ttk.Label(app, text="Top Text:")
top_text_label.grid(row=0, column=0, padx=10, pady=5)
top_text = ttk.Entry(app)
top_text.grid(row=0, column=1, padx=10, pady=5)
top_text.insert(0, "Hello")
top_text.bind("<KeyRelease>", draw_meme)

# Bottom Text
bottom_text_label = ttk.Label(app, text="Bottom Text:")
bottom_text_label.grid(row=1, column=0, padx=10, pady=5)
bottom_text = ttk.Entry(app)
bottom_text.grid(row=1, column=1, padx=10, pady=5)
bottom_text.insert(0, "Word")
bottom_text.bind("<KeyRelease>", draw_meme)

# Color
color_label = ttk.Label(app, text="Text Color:")
color_label.grid(row=2, column=0, padx=10, pady=5)
color = ttk.Combobox(
    app, values=["black", "white", "red", "green", "blue", "orange"], state="readonly")
color.grid(row=2, column=1, padx=10, pady=5)
color.set("green")
color.bind("<<ComboboxSelected>>", color_changed)

# Font
font_label = ttk.Label(app, text="Font:")
font_label.grid(row=3, column=0, padx=10, pady=5)
font = ttk.Combobox(
    app, values=["times new roman", "verdana", "courier", "impact"], state="readonly")
font.grid(row=3, column=1, padx=10, pady=5)
font.set("times new roman")  # Set default font
font.bind("<<ComboboxSelected>>", font_changed)

# Size
size_label = ttk.Label(app, text="Text Size:")
size_label.grid(row=4, column=0, padx=10, pady=5)
size = ttk.Scale(app, from_=20, to=50, orient="horizontal")
size.grid(row=4, column=1, padx=10, pady=5)
size.bind("<Motion>", size_changed)

# Meme Canvas
image = tk.PhotoImage(file="./image/1.png")
meme_canvas = tk.Canvas(app, width=image.width(), height=image.height())
meme_canvas.grid(row=5, columnspan=2, padx=10, pady=10)

draw_meme()

app.mainloop()
