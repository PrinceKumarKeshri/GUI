# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 17:13:20 2021

@author: 0526p
"""

from tkinter import *

root = Tk()
root.title('Working on Tkinter')
root.geometry('400x200')

def show():
    myLabel = Label(root, text = var.get()).pack()

var = StringVar()

#c = Checkbutton(root, text = 'Check this box, I dare you!', variable = var, onvalue = 'on', offvalue = 'off')
c = Checkbutton(root, text = 'Do you want to delete it? Click here!', variable = var, onvalue = 'Delete', offvalue = 'Not Delete')
c.deselect()
c.pack()

mybutton =  Button(root, text = 'Show selection', command = show).pack()

root.mainloop()