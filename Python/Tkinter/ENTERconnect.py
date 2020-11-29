from tkinter import Tk
from tkinter import Label

root = Tk()

root['bg'] = '#fafafa'
root.title('Enter Check')
root.geometry('300x250')

root.resizable(width=False, height=False)

def callback(event):
    label['text'] = 'You ptressed Enter'

root.bind('<Return>', callback)

label = Label(root, text='')
label.pack()

root.mainloop()