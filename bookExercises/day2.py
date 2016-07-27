from Tkinter import *
from time import strptime,strftime
from tkMessageBox import showinfo

def compute():
    global dateEnt
    date = dateEnt.get()
    try:
        weekday = strftime('%A ', strptime(date, '%b %d, %Y'))
        dateEnt.insert(0, weekday)
    except(ValueError):
        try:
            weekday = strptime(date, '%A %b %d, %Y')
        except(ValueError):
            showinfo(message="Please use Month Day, Year format\nExample: Jun 9, 2014")
    
def clear():
    dateEnt.delete(0,END)


root = Tk()

label = Label(root, text='Enter date')
label.grid(row=0,column=0)

dateEnt= Entry(root)
dateEnt.grid(row=0, column=1)

button = Button(root, text='Submit', command=compute)
button.grid(row=1,column=0)

button = Button(root, text='Clear', command=clear)
button.grid(row=1,column=1)

root.mainloop()
