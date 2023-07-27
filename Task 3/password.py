import random
import string
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def generate_button_clicked():
    try:
        password_length = int(length_entry.get())
        if password_length <= 0:
            raise ValueError("Password length should be greater than 0.")
        else:
            password = generate_password(password_length)
            generated_password_entry.config(state="normal")
            generated_password_entry.delete(0, tk.END)
            generated_password_entry.insert(0, password)
            generated_password_entry.config(state="readonly", bg="green")
    except ValueError as e:
        messagebox.showerror("Error", str(e))


def reset_button_clicked():
    user_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)
    generated_password_entry.config(state="normal", bg="white")
    generated_password_entry.delete(0, tk.END)
    generated_password_entry.config(state="readonly")


def copy_button_clicked():
    generated_password = generated_password_entry.get()
    if generated_password:
        root.clipboard_clear()
        root.clipboard_append(generated_password)
        messagebox.showinfo(
            "Copied", "Generated password copied to clipboard!")


# Create the main tkinter window
root = tk.Tk()
root.title("Password Generator")

# Create and pack the GUI elements
user_label = tk.Label(root, text="User:")
user_label.pack(pady=5)

user_entry = tk.Entry(root)
user_entry.pack(pady=5)

length_label = tk.Label(root, text="Password Length:")
length_label.pack(pady=5)

length_entry = tk.Entry(root)
length_entry.pack(pady=5)

generate_button = tk.Button(
    root, text="Generate Password", command=generate_button_clicked)
generate_button.pack(pady=10)

generated_password_label = tk.Label(root, text="Generated Password:")
generated_password_label.pack(pady=5)

generated_password_entry = tk.Entry(root, state="readonly", bg="white")
generated_password_entry.pack(pady=5)

reset_button = ttk.Button(root, text="Reset", command=reset_button_clicked)
reset_button.pack(side=tk.LEFT, padx=5, pady=10)

copy_button = ttk.Button(root, text="Copy", command=copy_button_clicked)
copy_button.pack(side=tk.RIGHT, padx=5, pady=10)

# Start the tkinter event loop
root.mainloop()
