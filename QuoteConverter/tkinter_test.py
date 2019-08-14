# from tkinter import *

# root = Tk()
# root.title('Spreadsheet Editor')

# button = Button(root, text='Stop', width=25, command=root.destroy)
# button.pack()
# root.mainloop()
from tkinter import *
# import tkinter as tk

def write_slogan():
    print("Tkinter is easy to use!")

VENDORS = ['AVT Technology Solutions LLC', 'Carahsoft Technology Corp', 'Ingram Micro', 'ModTech Solutions LLC']

root = Tk()
frame = Frame(root,height=200,width=200,bg="sky blue")
frame.pack()

variable = StringVar(frame)
variable.set('Choose a vendor.')

op_menu = OptionMenu(root, variable, *VENDORS)
op_menu.pack()

# frame = tk.Frame(root)
# frame.pack()
def get_vendor():
    if variable.get()=='Choose a vendor.':
        print("Vendor name has not been chosen. Choose a vendor!")
        return None
    else:
        print("Vendor name is", variable.get())
        return variable.get()

button = Button(root, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
button.pack(side=BOTTOM)
slogan = Button(root,
                   text="OK",
                   command=get_vendor)
slogan.pack(side=BOTTOM)

root.mainloop()