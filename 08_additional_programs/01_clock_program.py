# CLOCK PROGRAM

# from time import strftime
# from tkinter import *
# from tkinter.ttk import *
#
# root = Tk()
# root.title('Digital SoftUni Clock')
#
# def clock():
#     tick = strftime('%H:%M:%S %p')
#     label.config(text=tick)
#     label.after(1000, clock)
#
# label = Label(root, font=('sans', 100), background='black', foreground='red')
# clock()
# mainloop()

from time import strftime
from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('Digital SoftUni Clock')

def clock():
    time_str = strftime('%H:%M:%S %p')  # Clearer variable name
    label.config(text=time_str)
    label.after(1000, clock)  # Fixed `after` method

label = Label(root, font=('sans', 100), background='black', foreground='orange')  # Fixed class name
label.pack(anchor='center')  # Ensure the label is displayed

clock()
root.mainloop()  # Use `root.mainloop()` instead of `mainloop()`