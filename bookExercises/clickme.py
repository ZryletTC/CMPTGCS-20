from Tkinter import *
from time import strftime, localtime, gmtime
from tkMessageBox import showinfo

def clicked():
    'print date/time'
    time = strftime('Day:  %d %b %Y\nTime: %H:%M:%S %p\n',localtime())
    print(time)

def clickmsg():
    time = strftime('Day:  %d %b %Y\nTime: %H:%M:%S %p\n',localtime())
    showinfo(message=time)


def local():
    time = strftime('Local time\nDay:  %d %b %Y\nTime: %H:%M:%S %p\n',localtime())
    print(time)

def gmt():
    time = strftime('Greenwich time\nDay:  %d %b %Y\nTime: %H:%M:%S %p\n',gmtime())
    print(time)


root = Tk()

button = Button(root, text='Local time', command=local)
button.pack()

button = Button(root, text='Greenwich time', command=gmt)
button.pack()

root.mainloop()
