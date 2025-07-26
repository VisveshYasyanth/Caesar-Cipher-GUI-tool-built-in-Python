import tkinter as tk
from tkinter import messagebox

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            offset = shift if mode == 'encrypt' else -shift
            result += chr((ord(char) - start + offset) % 26 + start)
        else:
            result += char
    return result

def encrypt_message():
    try:
        shift = int(shift_entry.get())
        message = message_entry.get()
        encrypted = caesar_cipher(message, shift, 'encrypt')
        result_label.config(text=f"Encrypted: {encrypted}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer.")

def decrypt_message():
    try:
        shift = int(shift_entry.get())
        message = message_entry.get()
        decrypted = caesar_cipher(message, shift, 'decrypt')
        result_label.config(text=f"Decrypted: {decrypted}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer.")

# Tkinter Window Setup
window = tk.Tk()
window.title("Caesar Cipher Encrypt/Decrypt")
window.geometry("600x400")
window.configure(bg="black")

# Styling variables
font_style = ("Copperplate Gothic Bold", 18)
font_color = "#A52A2A"

# Widgets
title_label = tk.Label(window, text="Caesar Cipher Tool", font=("Copperplate Gothic Bold", 28), fg=font_color, bg="white")
title_label.pack(pady=10)

message_label = tk.Label(window, text="Enter your message:", font=font_style, fg=font_color, bg="white")
message_label.pack()

message_entry = tk.Entry(window, font=font_style, fg=font_color, bg="white", width=40, insertbackground=font_color)
message_entry.pack(pady=5)

shift_label = tk.Label(window, text="Enter shift value:", font=font_style, fg=font_color, bg="white")
shift_label.pack()

shift_entry = tk.Entry(window, font=font_style, fg=font_color, bg="white", width=10, insertbackground=font_color)
shift_entry.pack(pady=5)

encrypt_button = tk.Button(window, text="Encrypt", command=encrypt_message, font=font_style, fg=font_color, bg="white", borderwidth=5)
encrypt_button.pack(pady=10)

decrypt_button = tk.Button(window,relief="flat", text="Decrypt", command=decrypt_message, font=font_style, fg=font_color, bg="white", borderwidth=5)
decrypt_button.pack()

result_label = tk.Label(window, text="", font=font_style, fg=font_color, bg="white")
result_label.pack(pady=20)


# Run the application
window.mainloop()