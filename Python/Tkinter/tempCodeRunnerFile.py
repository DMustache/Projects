root['bg'] = '#000000'
root.title('Calculator')
root.geometry('300x250')

root.resizable(width=False, height=False)

entry = Frame(root, bg='yellow', width=30, height=10)
entry = LabelFrame(text='Write numbers')
entry.pack(side=TOP)

ftnum = Entry(width=7, bg='#A35151', fg='#FDFCFD', justify=CENTER, font=30)
ftnum.place()

fsnum = Entry(width=7, bg='#A35151', fg='#FDFCFD', justify=CENTER, font=30)
fsnum.place()