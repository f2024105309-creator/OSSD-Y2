import tkinter as tk
from tkinter import messagebox

def message():
    messagebox.showinfo("Test", "Test Message")

root = tk.Tk()
root.title("Message Box")
root.geometry("300x200")

tk.Button(root, text="Message", command=message).pack(pady=50)

root.mainloop()