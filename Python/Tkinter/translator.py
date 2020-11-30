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
root.geometry('300x250')

root.resizable(width=False, height=False)

def 

frame_top = Frame(root, bg='#1a73e8', bd=5)
frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)

frame_bottom = Frame(root, bg='#1a73e8', bd=5)
frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1)

phraseField = Entry(frame_top, bg='white', font=30)
phraseField.pack()

langIndex = ['English', 'Русский']
langIndex.sort()
variable = StringVar(root)
variable.set(langIndex[0])
PhraseLang = OptionMenu(frame_top, variable, *langIndex)
PhraseLang.place()

btn = Button(frame_top, text='Translate')
btn.pack()
root.bind('<Return>', lambda event=None: btn.invoke())

info = Label(frame_bottom, text='Translate info', bg='#1a73e8', font=40)
info.pack()

root.mainloop()