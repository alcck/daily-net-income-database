from tkinter import *
import back_end

win = Tk()
win.wm_title("Daily Net Income DB V.0.1")

selected_row = 0


def get_selected_row():
    index = list1.curselection()[0]
    selected_row = list1.get(index)
    e1.delete(0, END)
    e1.insert(END, selected_row[1])
    e2.delete(0, END)
    e1.insert(END, selected_row[2])
    e3.delete(0, END)
    e1.insert(END, selected_row[3])
    e4.delete(0, END)
    e1.insert(END, selected_row[4])
    e5.delete(0, END)
    e1.insert(END, selected_row[5])
    e6.delete(0, END)
    e1.insert(END, selected_row[6])


def view_command():
    list1.delete(0, END)
    for row in back_end.view():
        list1.insert(END, row)


def search_command():
    list1.delete(0, END)
    for row in back_end.search(date_text.get()):
        list1.insert(END, row)


def add_command():
    back_end.insert(date_text.get(), earn_int.get(), gro_int.get(), ent_int.get(), clo_int.get(), book_int.get())
    list1.delete(0, END)
    list1.insert(END,
                 (date_text.get(), earn_int.get(), gro_int.get(), ent_int.get(), clo_int.get(), book_int.get()))


def delete_command():
    back_end.delete(selected_row[0])


def calculate_command():
    list1.delete(0, END)
    n1 = earn_int.get()
    n2 = gro_int.get()
    n3 = ent_int.get()
    n4 = clo_int.get()
    n5 = book_int.get()
    x = n1 - (n2 + n3 + n4 + n5)
    e7.insert(END, x)


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

l6 = Label(win, text='Net Income')
l6.grid(row=3, column=0)

date_text = StringVar()
e1 = Entry(win, textvariable=date_text)
e1.grid(row=0, column=1)

earn_int = IntVar()
e2 = Entry(win, textvariable=earn_int)
e2.grid(row=0, column=3)

gro_int = IntVar()
e3 = Entry(win, textvariable=gro_int)
e3.grid(row=1, column=1)

ent_int = IntVar()
e4 = Entry(win, textvariable=ent_int)
e4.grid(row=1, column=3)

clo_int = IntVar()
e5 = Entry(win, textvariable=clo_int)
e5.grid(row=2, column=1)

book_int = IntVar()
e6 = Entry(win, textvariable=book_int)
e6.grid(row=2, column=3)

netincome_text = IntVar()
e7 = Entry(win, textvariable=netincome_text)
e7.grid(row=3, column=1)

list1 = Listbox(win, height=6, width=35)
list1.grid(row=3, column=0, rowspan=9, columnspan=2)

sb = Scrollbar(win)
sb.grid(row=3, column=2, rowspan=9)

list1.bind("<<ListboxSelection>>", get_selected_row)

b1 = Button(win, text='Add', width=12, pady=5, command=add_command)
b1.grid(row=3, column=3)

b2 = Button(win, text='Search', width=12, pady=5, command=search_command)
b2.grid(row=4, column=3)

b3 = Button(win, text='Delete', width=12, pady=5, command=delete_command)
b3.grid(row=5, column=3)

b4 = Button(win, text='View all', width=12, pady=5, command=view_command)
b4.grid(row=6, column=3)

b5 = Button(win, text='Calculate', width=12, pady=5, command=calculate_command)
b5.grid(row=7, column=3)

b6 = Button(win, text='Close', width=12, pady=5, command=win.destroy)
b6.grid(row=8, column=3)

win.mainloop()
