from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title('Ceas')

def time():
    string = strftime('%D ''' '%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)

lbl = Label(root, font=('calibri', 109, 'bold'),
            background='purple',
            foreground='white')

lbl.pack(anchor='center')
time()
mainloop()