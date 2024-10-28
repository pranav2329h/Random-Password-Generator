import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip 
def generate_password():
    length = length_var.get()
    use_letters = letters_var.get()
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()

    character_set = ""
    if use_letters:
        character_set += string.ascii_letters
    if use_numbers:
        character_set += string.digits
    if use_symbols:
        character_set += string.punctuation

    if not character_set:
        messagebox.showerror("Selection Error", "Please select at least one character type.")
        return

    password = ''.join(random.choice(character_set) for _ in range(length))
    result_var.set(password)

def copy_to_clipboard():
    password = result_var.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard.")
    else:
        messagebox.showwarning("No Password", "Please generate a password first.")

root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("400x300")
root.config(padx=20, pady=20)
length_var = tk.IntVar(value=8)
letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)
result_var = tk.StringVar()

tk.Label(root, text="Password Length:").pack(anchor='w')
tk.Scale(root, from_=4, to_=32, orient='horizontal', variable=length_var).pack(fill='x')

tk.Checkbutton(root, text="Include Letters (A-Z)", variable=letters_var).pack(anchor='w')
tk.Checkbutton(root, text="Include Numbers (0-9)", variable=numbers_var).pack(anchor='w')
tk.Checkbutton(root, text="Include Symbols (!@#$)", variable=symbols_var).pack(anchor='w')

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)
tk.Entry(root, textvariable=result_var, width=24, font=('Arial', 12), justify='center').pack(pady=10)

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=10)

root.mainloop()
