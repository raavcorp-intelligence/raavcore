# This is a test to incorparate a TK GUI interface into the RAAV interface

from tkinter import *


def main():
    x1 = e1.get()
    print(x1)


master = Tk()
Label(master, text="Command:").grid(row=0)
master.geometry("200x200")
e1 = Entry(master)
e1.grid(row=0, column=1)
Button(master, text='Exit', command=master.quit).grid(
    row=3, column=0, sticky=W, pady=4)
Button(master, text='Send', command=main).grid(
    row=4, column=0, sticky=W, pady=4)
Button(master, text='Voice', command=main).grid(
    row=5, column=0, sticky=W, pady=4)

mainloop()
