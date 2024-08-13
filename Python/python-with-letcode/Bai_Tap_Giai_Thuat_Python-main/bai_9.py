import tkinter as tk
from tkinter import messagebox

contacts = {}

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()

    if name:
        contacts[name] = {'Số điện thoại': phone, 'Email': email}
        update_contact_list()
        messagebox.showinfo("Thông báo", f"Liên lạc {name} đã được thêm vào danh bạ.")
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Cảnh báo", "Vui lòng nhập tên liên lạc.")

def view_contact():
    selected_contact = contact_listbox.get(tk.ACTIVE)
    if selected_contact:
        contact_info = f"Số điện thoại: {contacts[selected_contact]['Số điện thoại']}\nEmail: {contacts[selected_contact]['Email']}"
        messagebox.showinfo(selected_contact, contact_info)
    else:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn một liên lạc từ danh sách.")

def update_contact_list():
    contact_listbox.delete(0, tk.END)
    for name in contacts:
        contact_listbox.insert(tk.END, name)

# Tạo giao diện Tkinter
root = tk.Tk()
root.title("Danh Bạ Liên Lạc")

# Tên
name_label = tk.Label(root, text="Tên:")
name_label.grid(row=0, column=0, sticky="E")
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

# Số điện thoại
phone_label = tk.Label(root, text="Số điện thoại:")
phone_label.grid(row=1, column=0, sticky="E")
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1)

# Email
email_label = tk.Label(root, text="Email:")
email_label.grid(row=2, column=0, sticky="E")
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1)

# Nút Thêm Liên Lạc
add_button = tk.Button(root, text="Thêm Liên Lạc", command=add_contact)
add_button.grid(row=3, column=0, columnspan=2, pady=10)

# Danh sách liên lạc
contact_listbox = tk.Listbox(root)
contact_listbox.grid(row=4, column=0, columnspan=2, pady=5)
update_contact_list()

# Nút Xem Liên Lạc
view_button = tk.Button(root, text="Xem Liên Lạc", command=view_contact)
view_button.grid(row=5, column=0, columnspan=2, pady=5)

root.mainloop()
