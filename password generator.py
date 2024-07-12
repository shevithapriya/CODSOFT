import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password

def generate_password_button_click():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Password length must be greater than zero.")
        else:
            password = generate_password(length)
            password_var.set(password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for password length.")

def accept_password():
    username = username_entry.get().strip()
    password = password_var.get().strip()
    if username == "" or password == "":
        messagebox.showerror("Error", "Please enter a username and generate a password first.")
    else:
        messagebox.showinfo("Accepted", f"Username: {username}\nPassword: {password}")

def reset_inputs():
    username_var.set("")
    length_entry.delete(0, tk.END)
    password_var.set("")

root = tk.Tk()
root.title("Password Generator")

frame = tk.Frame(root, padx=20, pady=20, bg="#000000")
frame.pack(padx=10, pady=10)

title_text = tk.Text(frame, height=1, width=20, wrap=tk.WORD, bg="#000000", fg="#FFFFFF", relief=tk.FLAT)
title_text.insert(tk.END, "Password Generator")
title_text.config(state=tk.DISABLED)
title_text.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

username_label = tk.Label(frame, text="Enter Username:", bg="#000000", fg="#FFFFFF")
username_label.grid(row=1, column=0, padx=5, pady=5)

username_var = tk.StringVar()
username_entry = tk.Entry(frame, textvariable=username_var, width=30)
username_entry.grid(row=1, column=1, padx=5, pady=5)

length_label = tk.Label(frame, text="Enter Password Length:", bg="#000000", fg="#FFFFFF")
length_label.grid(row=2, column=0, padx=5, pady=5)

length_entry = tk.Entry(frame, width=10)
length_entry.grid(row=2, column=1, padx=5, pady=5)

generate_button = tk.Button(frame, text="Generate Password", command=generate_password_button_click, bg="#FFFFFF", fg="#000000")
generate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

password_var = tk.StringVar()
password_label = tk.Label(frame, text="Generated Password:", bg="#000000", fg="#FFFFFF")
password_label.grid(row=4, column=0, padx=5, pady=5)

password_entry = tk.Entry(frame, textvariable=password_var, width=30, state='readonly')
password_entry.grid(row=4, column=1, padx=5, pady=5)

accept_button = tk.Button(frame, text="Accept", command=accept_password, bg="#FFFFFF", fg="#000000")
accept_button.grid(row=5, column=0, padx=5, pady=10)

reset_button = tk.Button(frame, text="Reset", command=reset_inputs, bg="#FFFFFF", fg="#000000")
reset_button.grid(row=5, column=1, padx=5, pady=10)

root.mainloop()
