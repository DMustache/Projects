from tkinter import Tk
from tkinter import Entry
from tkinter import Button
from tkinter import Label
from tkinter import Frame
from tkinter import OptionMenu
from tkinter import StringVar

from googletrans import Translator

root = Tk()

root['bg'] = '#fafafa'
root.title('MyTranslator')
root.geometry('450x300')

root.resizable(width=False, height=False)

# frame_top = Frame(root, bg='#1a73e8', bd=5)
# frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)

frame_bottom = Frame(root, bg='#1a73e8', bd=5)
frame_bottom.place(relx=0.05, rely=0, relwidth=0.9, relheight=0.8)

root.mainloop()