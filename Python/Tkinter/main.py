import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame()
label1 = tk.Label(master=frame1, text='frame1')
frame1.pack()

frame2 = tk.Frame()
label2 = tk.Label(master=frame2, text='frame2')
frame2.pack()

window.mainloop()