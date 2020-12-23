from tkinter import Tk
from tkinter import messagebox
from tkinter import Canvas
from tkinter import Frame
from tkinter import Label
from tkinter import Entry
from tkinter import Button
import requests

root = Tk()

def get_weather():
    try:
        city = cityField.get()

        key = '797261b25ff6a499d71adea747c337cf'
        url = 'http://api.openweathermap.org/data/2.5/weather'

        params = {'APPID': key, 'q': city, 'units': 'metric'}
        result = requests.get(url, params=params)
        weather = result.json()

        info['text'] = f'{str(weather["name"])}: {weather["main"]["temp"]}'
    except:
        info['text'] = f'Unexpected error!'

root['bg'] = '#fafafa'
root.title('Weather control')
root.geometry('300x250')

root.resizable(width=False, height=False)

frame_top = Frame(root, bg='#ffb700', bd=5)
frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)

frame_bottom = Frame(root, bg='#ffb700', bd=5)
frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1)

cityField = Entry(frame_top, bg='white', font=30)
cityField.pack()

btn = Button(frame_top, text='Watch weather', command=get_weather)
btn.pack()
root.bind('<Return>', lambda event=None: btn.invoke())

info = Label(frame_bottom, text='Weather info', bg='#ffb700', font=40)
info.pack()

root.mainloop()
