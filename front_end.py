from tkinter import *

win = Tk()

l1 = Label(win, text='Date')
l1.grid(row=0, column=0)

l2 = Label(win, text='Earnings')
l2.grid(row=0, column=2)

l3 = Label(win, text='Class 1')
l3.grid(row=1, column=0)

l4 = Label(win, text='Class 2')
l4.grid(row=1, column=2)

l5 = Label(win, text='Class 3')
l5.grid(row=2, column=0)

l6 = Label(win, text='Class 4')
l6.grid(row=2, column=2)

date_text = StringVar()
e1 = Entry(win, textvariable=date_text)
e1.grid(row=0,column=1)

win.mainloop()