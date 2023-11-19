import tkinter as tk
from math import *

def evaluate(event):
    res.configure(text="Result: " + str(eval(entry.get())))

def handle_button_press(event):
    window.destroy()


window = tk.Tk()
window.title("Hello World")

tk.Label(window, text="Your Expression:").pack()
entry = tk.Entry(window)
entry.bind("event", evaluate)
entry.pack()

button = tk.Button(text="My simple app.")
button.bind("event", handle_button_press)
button.pack()

res = tk.Label(window)
res.pack()
window.mainloop()