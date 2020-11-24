from tkinter import Tk
from tkinter import messagebox
from tkinter import Canvas
from tkinter import Frame
from tkinter import Label
from tkinter import Entry
from tkinter import Button 

root = Tk()

def btn_click():
    login = loginInput.get()
    password = passField.get()

    info_str=f'Data: {login} {password}'
    messagebox.showinfo(title='Name', message=info_str)

    #messagebox.showerror(title='Error', message='Error!')

root['bg'] = '#fafafa'
root.title('Name')
root.wm_attributes('-alpha', 0.9)
root.geometry('300x250')

root.resizable(width=False, height=False)

canvas = Canvas(root, height=300, width=250)
canvas.pack()

frame = Frame(root, bg='red')
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)

title = Label(frame, text='Solution', bg='gray', font=40)
title.pack()

btn = Button(frame, text='Button', bg='yellow', command=btn_click)
btn.pack()

loginInput = Entry(frame, bg='white')
loginInput.pack()

passField = Entry(frame, bg='white', show='*')
passField.pack()

root.mainloop()