from ast import PyCF_TYPE_COMMENTS
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


## Combo box
selected_country=tk.StringVar()
countries=ttk.Combobox(textvariable=selected_country,values=["Egypt","Saudi Arabia","United Arab Emirates","Kuwait"])
countries['state']="readonly"
countries.pack()
def display_country(event):
    country_label=ttk.Label(text=selected_country.get(),font="custom_font",padding=15)
    country_label.pack()
    # print(f"Selected country: {selected_country.get()}")
countries.bind("<<ComboboxSelected>>", display_country)


## List Box
food_items =["PIZZA","PASTA","ICE CREAM","SUSHI","STEAK"]
fav_food=tk.StringVar(value=food_items)
food_list=tk.Listbox(listvariable=fav_food,height=5,selectmode="extended")
food_list.pack()
def get_fav_food(event):
    food_indices=food_list.curselection()
    for index in food_indices:
        print(food_items[index])

food_list.bind("<<ListboxSelect>>", get_fav_food)


##Spin Box
counter=tk.IntVar(value=10)
def get_spinbox_value():
    print(f"Current spinbox value :{spin_box.get()}")

# spin_box=ttk.Spinbox(from_=0,to=25,textvariable=counter,wrap=True,command=get_spinbox_value)
# spin_box=ttk.Spinbox(values=(0,5,10,15,20,25),textvariable=counter,wrap=True,command=get_spinbox_value)
spin_box=ttk.Spinbox(values=tuple(range(0,100,5)),textvariable=counter,wrap=True,command=get_spinbox_value) 
spin_box.pack()
print(spin_box.get())
window.mainloop() 
 