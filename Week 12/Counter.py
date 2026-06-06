import tkinter as tk

count = 0

def update_label():
    counter_label.config(text=str(count))

def increment():
    global count
    count += 1
    update_label()

def decrement():
    global count
    count -= 1
    update_label()

def reset():
    global count
    count = 0
    update_label()


root = tk.Tk()
root.title("Counter App")

counter_label = tk.Label(root, text="0", font=("Arial", 20))
counter_label.pack(pady=10)

tk.Button(root, text="Increment", command=increment).pack()
tk.Button(root, text="Decrement", command=decrement).pack()
tk.Button(root, text="Reset", command=reset).pack()

root.mainloop()