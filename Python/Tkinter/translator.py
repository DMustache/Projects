from tkinter import Tk
from tkinter import Entry
from tkinter import Button
from tkinter import Label
from tkinter import Frame
from tkinter import OptionMenu
from tkinter import StringVar
from tkinter import TOP
from tkinter import LEFT
from tkinter import RIGHT

from googletrans import Translator

root = Tk()

root['bg'] = '#fafafa'
root.title('MyTranslator')
root.geometry('450x300')

root.resizable(width=False, height=False)

frame_top = Frame(root, bg='#1a73e8', bd=5)
frame_top.place(relx=0.05, rely=0, relwidth=0.9, relheight=0.15)

frame_bottom = Frame(root, bg='#1a73e8', bd=5)
frame_bottom.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.8)

LANGUAGESPL = [
    'Русский',
    'Английский'
]

variablePL = StringVar(root)
variablePL.set(LANGUAGESPL[1])

LANGUAGESTL = [
    'Русский',
    'Английский'
]

variableTL = StringVar(root)
variableTL.set(LANGUAGESTL[0])

PhraseLang = OptionMenu(frame_top, variableTL, *LANGUAGESPL)
PhraseLang.place(relx=0.1)

RevButton = Button(frame_top, text='Rotate lang')
RevButton.place(relx=0.45)

TranslatedLang = OptionMenu(frame_top, variablePL, *LANGUAGESTL)
TranslatedLang.place(relx=0.65)

root.mainloop()