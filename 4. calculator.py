# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 15:32:27 2021

@author: 0526p
"""
from tkinter import *

root = Tk()
root.title('Calculator Made by Me')

e = Entry(root, width = 45, borderwidth = 5)
e.grid(row = 0 , column = 0, columnspan = 3, padx = 10, pady  = 10)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    global f_num, operation
    operation = 'add'
    first_number = e.get()
    f_num = int(first_number)
    e.delete(0, END)
    
def button_subtract():
    global f_num, operation
    operation = 'subtract'
    first_number = e.get()
    f_num = int(first_number)
    e.delete(0, END)

def button_multiply():
    global f_num, operation
    operation = 'multiply'
    first_number = e.get()
    f_num = int(first_number)
    e.delete(0, END)
 
def button_division():
    global f_num, operation
    operation = 'division'
    first_number = e.get()
    f_num = int(first_number)
    e.delete(0, END)
    
def button_equal():
    second_num = e.get()
    e.delete(0, END)
    if operation == 'add':
        e.insert(0, f_num + int(second_num))
    elif operation == 'subtract':
        e.insert(0, f_num - int(second_num))
    elif operation == 'multiply':
        e.insert(0, f_num * int(second_num))
    elif operation == 'division':
        e.insert(0, f_num / int(second_num))
    
button_1 = Button(root, text = '1', padx=40, pady = 20, command = lambda: button_click(1))
button_2 = Button(root, text = '2', padx=40, pady = 20, command = lambda: button_click(2))
button_3 = Button(root, text = '3', padx=40, pady = 20, command = lambda: button_click(3))
button_4 = Button(root, text = '4', padx=40, pady = 20, command = lambda: button_click(4))
button_5 = Button(root, text = '5', padx=40, pady = 20, command = lambda: button_click(5))
button_6 = Button(root, text = '6', padx=40, pady = 20, command = lambda: button_click(6))
button_7 = Button(root, text = '7', padx=40, pady = 20, command = lambda: button_click(7))
button_8 = Button(root, text = '8', padx=40, pady = 20, command = lambda: button_click(8))
button_9 = Button(root, text = '9', padx=40, pady = 20, command = lambda: button_click(9))
button_0 = Button(root, text = '0', padx=40, pady = 20, command = lambda: button_click(0))
button_clear = Button(root, text = 'Clear', padx=80, pady = 20, command = button_clear)
button_equal = Button(root, text = '=', padx=85, pady = 20, command = button_equal)
button_add = Button(root, text = '+', padx=39, pady = 20, command = button_add)
button_subtract = Button(root, text = '-', padx=41, pady = 20, command = button_subtract)
button_multiply = Button(root, text = '*', padx=40, pady = 20, command = button_multiply)
button_division = Button(root, text = '/', padx=40, pady = 20, command = button_division)

button_1.grid(row =3 , column =0 )
button_2.grid(row =3 , column =1 )
button_3.grid(row =3 , column =2 )

button_4.grid(row =2 , column =0 )
button_5.grid(row =2 , column =1 )
button_6.grid(row =2 , column =2 )

button_7.grid(row =1 , column =0 )
button_8.grid(row =1 , column =1 )
button_9.grid(row =1 , column =2 )

button_0.grid(row =4 , column =0 )
button_clear.grid(row =4 , column =1, columnspan = 2)

button_add.grid(row =5 , column =0 )
button_equal.grid(row =5 , column =1,columnspan = 2)

button_subtract.grid(row =6 , column =0 )
button_multiply.grid(row =6 , column =1 )
button_division.grid(row =6 , column =2 )


root.mainloop()
