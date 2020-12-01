from tkinter import *
root = Tk()

root['bg'] = '#fafafa'
root.title('Enter Check')
root.geometry('450x350')

root.resizable(width=False, height=False)

write = Text(root, width=20, height=15)
write.place(relx=0.05)

take = Text(root, width=20, height=15)
take.place(relx=0.64)

root.mainloop()