from tkinter import Tk
from tkinter import Entry
from tkinter import Button
from tkinter import Label
from tkinter import Frame
from googletrans import Translator

root = Tk()

def translation():
    phrase = phraseField.get()
    translator = Translator()
    result = translator.translate(phrase)
    if(result.src == 'en'):
        result = translator.translate(phrase, dest='ru')
        info['text'] = result.text

    elif(result.src == 'ru'):
        result = translator.translate(phrase, dest='en')
        info['text'] = result.text

root['bg'] = '#fafafa'
root.title('MyTranslator')
root.geometry('300x250')

root.resizable(width=False, height=False)

frame_top = Frame(root, bg='#1a73e8', bd=5)
frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)

frame_bottom = Frame(root, bg='#1a73e8', bd=5)
frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1)

phraseField = Entry(frame_top, bg='white', font=30)
phraseField.pack()

btn = Button(frame_top, text='Translate', command=translation)
btn.pack()
root.bind('<Return>', lambda event=None: btn.invoke())

info = Label(frame_bottom, text='Translate info', bg='#1a73e8', font=40)
info.pack()

root.mainloop()