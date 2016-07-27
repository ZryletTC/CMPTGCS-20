from Tkinter import *
from time import strptime,strftime
from tkMessageBox import showinfo

def compute():
    global dateEnt
    date = dateEnt.get()
    weekday = strftime('%A', strptime(date, '%b %d %Y'))
    showinfo(message = '{} was a {}'.format(date,weekday))
    dateEnt.delete(0,END)


root = Tk()

label = Label(root, text='Enter date')
label.grid(row=0,column=0)

dateEnt= Entry(root)
dateEnt.grid(row=0, column=1)

button = Button(root, text='Submit', command=compute)
button.grid(row=1,column=0,columnspan=2)

root.mainloop()
