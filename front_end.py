from tkinter import *

win = Tk()
win.wm_title("Net Income DB V.0.1")
def get_selected_row():
    pass

l1 = Label(win, text='Date')
l1.grid(row=0, column=0)

l2 = Label(win, text='Earnings')
l2.grid(row=0, column=2)

l3 = Label(win, text='Groceries')
l3.grid(row=1, column=0)

l4 = Label(win, text='Entertainment')
l4.grid(row=1, column=2)

l5 = Label(win, text='Clothes')
l5.grid(row=2, column=0)

l6 = Label(win, text='Books')
l6.grid(row=2, column=2)


date_text = StringVar()
e1 = Entry(win, textvariable=date_text)
e1.grid(row=0, column=1)

earn_text = StringVar()
e2 = Entry(win, textvariable=earn_text)
e2.grid(row=0, column=3)

gro_text = StringVar()
e3 = Entry(win, textvariable=gro_text)
e3.grid(row=1, column=1)

ent_text = StringVar()
e4 = Entry(win, textvariable=ent_text)
e4.grid(row=1, column=3)

clo_text = StringVar()
e5 = Entry(win, textvariable=clo_text)
e5.grid(row=2, column=1)

book_text = StringVar()
e6 = Entry(win, textvariable=book_text)
e6.grid(row=2, column=3)

list = Listbox(win, height=8, width=35)
list.grid(row=3, column=0, rowspan=9, columnspan=2)

sb= Scrollbar(win)
sb.grid(row=3, column=2, rowspan=9)

list.bind("<<ListboxSelection>>", get_selected_row)

b1 = Button(win, text='Add', width=12, pady=5)
b1.grid(row=3, column=3)

b2 = Button(win, text='Search', width=12, pady=5)
b2.grid(row=4, column=3)

b3 = Button(win, text='Delete', width=12, pady=5)
b3.grid(row=5, column=3)

b4 = Button(win, text='View all', width=12, pady=5)
b4.grid(row=6, column=3)

b5 = Button(win, text='Close', width=12, pady=5, command=win.destroy)
b5.grid(row=7, column=3)

win.mainloop()