import tkinter as tk
from tkinter import ttk
from tkinter import UNDERLINE

window = tk.Tk()
window.title("Hello Tkinter")
window.minsize(500, 500)

# Label
label = ttk.Label(window, text="Have a nice day!",padding=10)
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

#Separator
sep=ttk.Separator(orient="horizontal")
sep.pack(fill="x", pady=10)
#Text
text=tk.Text(height=5,width=25)
text.pack()
text.focus()
text.insert("1.0","Hello, Welcome to the Text Widget")
text_data=text.get("1.0", "end")
print(text_data)
def text_fuction():
    text_data=text.get("1.0", "end")
    print(text_data)
text_data_button=ttk.Button(window,text="Get Data", command=text_fuction)
text_data_button.pack()
# text["state"] = "disabled"

# enable_button=ttk.Button(window, text="Enable", command=lambda: text.config(state="normal"))
# enable_button.pack()

## Checkbox widget
# check_option=tk.IntVar()
check_option=tk.StringVar()
def check_option_task():
    print(check_option.get())
check_button=ttk.Checkbutton(text="Agree with T&C", variable=check_option, command=check_option_task,onvalue="Yes",offvalue="No")
check_button.pack(pady=10)


## Radio Button
def get_radio_value():
    print(radio_value.get())
radio_value=tk.StringVar()
option_1=ttk.Radiobutton(text="Male",variable=radio_value,value="Male",command=get_radio_value)
option_1.pack(pady=10)
option_2=ttk.Radiobutton(text="Female",variable=radio_value,value="Female",command=get_radio_value)
option_2.pack(pady=10)


window.mainloop() 