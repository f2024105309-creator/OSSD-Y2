from scrapper import get_cars_data
import tkinter as tk
from tkinter import ttk

def set_textarea(data):
    textarea.delete(1.0, tk.END)

    if not data:
        textarea.insert(tk.END, "No data found!")
        status_label.config(text="No results")
        return

    for car in data:
        textarea.insert(tk.END, f"Name: {car['name']} | Price: {car['price']}\n")

    status_label.config(text="Results loaded successfully")

def search():
    status_label.config(text="Searching...")
    root.update()
    data = get_cars_data(dropdown.get())
    set_textarea(data)

def clear_text():
    textarea.delete(1.0, tk.END)
    status_label.config(text="Cleared")

# MAIN WINDOW
root = tk.Tk()
root.title("Car Price Scraper")
root.geometry("650x450")

# TITLE
title = tk.Label(root, text="🚗 Car Price Finder", font=("Arial", 18, "bold"))
title.pack(pady=10)

# FRAME
frame = tk.Frame(root)
frame.pack(pady=10)

# DROPDOWN
car_manufact = ['toyota', 'honda', 'suzuki']
dropdown = ttk.Combobox(frame, values=car_manufact, state="readonly", width=20)
dropdown.current(0)
dropdown.grid(row=0, column=0, padx=10)

# BUTTONS
search_button = tk.Button(frame, text="Search", command=search, bg="green", fg="white")
search_button.grid(row=0, column=1, padx=5)

clear_button = tk.Button(frame, text="Clear", command=clear_text, bg="red", fg="white")
clear_button.grid(row=0, column=2, padx=5)

# TEXT AREA + SCROLLBAR
text_frame = tk.Frame(root)
text_frame.pack(pady=10)

scrollbar = tk.Scrollbar(text_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

textarea = tk.Text(text_frame, height=15, width=70, yscrollcommand=scrollbar.set)
textarea.pack()

scrollbar.config(command=textarea.yview)

# STATUS LABEL
status_label = tk.Label(root, text="Ready", fg="blue")
status_label.pack(pady=5)

root.mainloop()