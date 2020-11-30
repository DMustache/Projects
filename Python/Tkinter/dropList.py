from tkinter import Tk
from tkinter import OptionMenu
from tkinter import StringVar
from tkinter import Listbox
from tkinter import END

root = Tk()

OPTIONS = [
    'jen',
    'feb',
    'mar'
]

variable = StringVar(root)
variable.set(OPTIONS[0])

w = OptionMenu(root, variable, *OPTIONS)
w.pack()

# root = Tk()
# root.wm_geometry("%dx%d+%d+%d" % (400, 150, 20, 40))
# listbox_items = ['Раз', 'Два', 'Три']


# def select_item(event):
#     value = (listbox.get(listbox.curselection()))
#     print(value)


# listbox = Listbox(root, width=40, height=5, font=('times', 13))
# listbox.bind('<<ListboxSelect>>', select_item)
# listbox.place(x=15, y=15)

# for item in listbox_items:
#     listbox.insert(END, item)
root.mainloop()