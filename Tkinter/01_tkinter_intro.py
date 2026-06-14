import tkinter as tk
from tkinter import UNDERLINE

# Create Main Window
window = tk.Tk()
window.title("Hello Tkinter")
window.minsize(500, 500)

# Label
label = tk.Label(
    window,
    text="Enter something below",
    font=("Arial", 16, UNDERLINE)
)
label.pack(pady=20)

# Function
def function_entry():
    input_text = entry.get()

    if input_text.strip() == "":
        label.config(text="Please enter some text!")
    else:
        label.config(text=input_text)
        entry.delete(0, tk.END)  # Clear entry after submission

# Entry Box
entry = tk.Entry(window, width=30, font=("Arial", 12))
entry.pack(pady=10)

# Put cursor in entry box automatically
entry.focus()

# Button
button = tk.Button(
    window,
    text="Click Me",
    command=function_entry,
    font=("Arial", 12)
)
button.pack(pady=10)

# Run Application
window.mainloop()