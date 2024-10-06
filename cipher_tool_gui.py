import tkinter as tk
from tkinter import messagebox

# Caesar Cipher encryption function
def encrypt_message():
    message = entry_message.get()
    shift = int(entry_shift.get())
    encrypted_message = ''
    
    for char in message:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_message += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_message += char  # Keep non-alphabetic characters unchanged

    result_label.config(text=f"Encrypted Message: {encrypted_message}")

# Caesar Cipher decryption function
def decrypt_message():
    message = entry_message.get()
    shift = int(entry_shift.get())
    decrypted_message = ''
    
    for char in message:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            decrypted_message += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_message += char  # Keep non-alphabetic characters unchanged

    result_label.config(text=f"Decrypted Message: {decrypted_message}")

# Hover effects for buttons
def on_enter_encrypt(e):
    btn_encrypt['background'] = '#2c6e91'
    btn_encrypt['foreground'] = '#d1e7f0'

def on_leave_encrypt(e):
    btn_encrypt['background'] = '#28527a'
    btn_encrypt['foreground'] = 'white'

def on_enter_decrypt(e):
    btn_decrypt['background'] = '#2c6e91'
    btn_decrypt['foreground'] = '#d1e7f0'

def on_leave_decrypt(e):
    btn_decrypt['background'] = '#28527a'
    btn_decrypt['foreground'] = 'white'

# Tkinter GUI setup
root = tk.Tk()
root.title("Secret Message Encryption/Decryption Tool")
root.geometry('400x300')
root.configure(bg='#4a7a8c')

# Configure grid layout to center content
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(5, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(2, weight=1)

# Title Label
title_label = tk.Label(root, text="Secret Message Tool", font=("Helvetica", 16, "bold"), bg='#4a7a8c', fg='white')
title_label.grid(row=1, column=1, pady=10)

# Labels
message_label = tk.Label(root, text="Enter Message:", font=("Helvetica", 12), bg='#4a7a8c', fg='white')
message_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")

shift_label = tk.Label(root, text="Enter Shift Value:", font=("Helvetica", 12), bg='#4a7a8c', fg='white')
shift_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")

# Entry fields
entry_message = tk.Entry(root, width=30, font=("Helvetica", 12), relief="solid", bd=1)
entry_message.grid(row=2, column=1, padx=10, pady=10)

entry_shift = tk.Entry(root, width=10, font=("Helvetica", 12), relief="solid", bd=1)
entry_shift.grid(row=3, column=1, padx=10, pady=10)

# Buttons
btn_encrypt = tk.Button(root, text="Encrypt", command=encrypt_message, bg='#28527a', fg='white', font=("Helvetica", 12, "bold"), relief="solid")
btn_encrypt.grid(row=4, column=0, padx=10, pady=10, sticky="e")

btn_decrypt = tk.Button(root, text="Decrypt", command=decrypt_message, bg='#28527a', fg='white', font=("Helvetica", 12, "bold"), relief="solid")
btn_decrypt.grid(row=4, column=1, padx=10, pady=10, sticky="w")

# Bind hover effects to buttons
btn_encrypt.bind("<Enter>", on_enter_encrypt)
btn_encrypt.bind("<Leave>", on_leave_encrypt)

btn_decrypt.bind("<Enter>", on_enter_decrypt)
btn_decrypt.bind("<Leave>", on_leave_decrypt)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12), bg='#4a7a8c', fg='white')
result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()
