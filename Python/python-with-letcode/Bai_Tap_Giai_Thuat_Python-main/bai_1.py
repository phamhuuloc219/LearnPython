import os
import tkinter as tk
from PIL import Image, ImageTk

app = tk.Tk()
app.title("Wanted!")
app.configure(bg="#FBFBD0")

current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, "image", "1.png")

wanted_text = tk.Label(app, text="WANTED", font=("Times New Roman", 50))
wanted_text.pack()

cat_image_pil = Image.open(image_path)
cat_image = ImageTk.PhotoImage(cat_image_pil)

cat = tk.Label(app, image=cat_image)
cat.pack()

app.mainloop()
