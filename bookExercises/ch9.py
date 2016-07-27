from Tkinter import *
from calendar import monthrange

def cal(year,month):
    monthinfo = monthrange(year,month)

    weekdays = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

    root = Tk()
    for i in range(7):
        lbl = Label(root,text=weekdays[i])
        lbl.grid(row=0,column=i)

    for i in range(monthinfo[1]):
        lbl = Label(root,text=str(i+1))
        lbl.grid(row=(i+monthinfo[0])/7+1,column=(i+monthinfo[0])%7)

    root.mainloop()
