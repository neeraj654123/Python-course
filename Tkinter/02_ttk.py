import tkinter as tk
from tkinter import ttk
from tkinter import UNDERLINE

window = tk.Tk()
window.title("Hello Tkinter")
window.minsize(500, 500)

# Label
label = ttk.Label(window, text="Have a nice day!")
label.config(font=("Arial", 16, UNDERLINE))
label.pack(pady=10)

# Function
def function_entry():
    input_text = entry.get()
    label.config(text=input_text)

# Entry
entry = ttk.Entry(window, width=30)
entry.pack(pady=10)

# Button
button = ttk.Button(window, text="Click Me", command=function_entry)
button.pack(pady=10)

#Quit button
quit_button = ttk.Button(window, text="Quit", command=window.destroy)
quit_button.pack(pady=10)

window.mainloop()