import tkinter as tk
from tkinter import Button, Label, StringVar
from random import choice

def choose_name():
    first_names = ["Nguyễn", "Trần", "Hồ", "Lê", "Huỳnh", "Ngô"]
    last_names = ["Bình", "An", "Thiên", "Hậu", "Khánh", "Toàn"]
    spy_name = choice(first_names) + " " + choice(last_names)
    name_var.set(spy_name)

app = tk.Tk()
app.title("BÍ MẬT HÀNG ĐẦU")

title_label = Label(app, text="Nhấn nút màu đỏ để tìm tên điệp viên của bạn")
title_label.pack()

button = Button(app, text="Nói cho tôi!", command=choose_name, bg="red", font=("Arial", 14))
button.pack()

name_var = StringVar()
name_label = Label(app, textvariable=name_var, font=("Arial", 16))
name_label.pack()

app.mainloop()