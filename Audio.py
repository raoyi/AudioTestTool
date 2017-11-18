#!/usr/bin/env python
# -*- coding: utf-8 -*-
#based on windows and python 2.7

from Tkinter import *
import sys
import os
import random
import winsound

ran = None
ioin = None
real = 'L'

#voice play function
def voice():
    global ran
    ran = str(random.randint(1, 9))
    winsound.PlaySound(real+ran+'.wav', winsound.SND_FILENAME)
    
#click actions
def click1():
    global ioin
    global real
    ioin = '1'
    if ioin == str(ran) and real == 'L':
        real = 'R'
        label['text'] = 'Press number:  |  Right'
        voice()
    elif ioin == str(ran) and real == 'R':
        f = open("pass.flg",'w')
        f.close()
        while True:
            if os.path.isfile('pass.flg') == True:
                sys.exit(0)
    else:
        voice()
    
def click2():
    global ioin
    global real
    ioin = '2'
    if ioin == str(ran) and real == 'L':
        real = 'R'
        label['text'] = 'Press number:  |  Right'
        voice()
    elif ioin == str(ran) and real == 'R':
        f = open("pass.flg",'w')
        f.close()
        while True:
            if os.path.isfile('pass.flg') == True:
                sys.exit(0)
    else:
        voice()
    
def click3():
    global ioin
    global real
    ioin = '3'
    if ioin == str(ran) and real == 'L':
        real = 'R'
        label['text'] = 'Press number:  |  Right'
        voice()
    elif ioin == str(ran) and real == 'R':
        f = open("pass.flg",'w')
        f.close()
        while True:
            if os.path.isfile('pass.flg') == True:
                sys.exit(0)
    else:
        voice()
    
def click4():
    global ioin
    global real
    ioin = '4'
    if ioin == str(ran) and real == 'L':
        real = 'R'
        label['text'] = 'Press number:  |  Right'
        voice()
    elif ioin == str(ran) and real == 'R':
        f = open("pass.flg",'w')
        f.close()
        while True:
            if os.path.isfile('pass.flg') == True:
                sys.exit(0)
    else:
        voice()
    
def click5():
    global ioin
    global real
    ioin = '5'
    if ioin == str(ran) and real == 'L':
        real = 'R'
        label['text'] = 'Press number:  |  Right'
        voice()
    elif ioin == str(ran) and real == 'R':
        f = open("pass.flg",'w')
        f.close()
        while True:
            if os.path.isfile('pass.flg') == True:
                sys.exit(0)
    else:
        voice()
    
def click6():
    global ioin
    global real
    ioin = '6'
    if ioin == str(ran) and real == 'L':
        real = 'R'
        label['text'] = 'Press number:  |  Right'
        voice()
    elif ioin == str(ran) and real == 'R':
        f = open("pass.flg",'w')
        f.close()
        while True:
            if os.path.isfile('pass.flg') == True:
                sys.exit(0)
    else:
        voice()
    
def click7():
    global ioin
    global real
    ioin = '7'
    if ioin == str(ran) and real == 'L':
        real = 'R'
        label['text'] = 'Press number:  |  Right'
        voice()
    elif ioin == str(ran) and real == 'R':
        f = open("pass.flg",'w')
        f.close()
        while True:
            if os.path.isfile('pass.flg') == True:
                sys.exit(0)
    else:
        voice()
    
def click8():
    global ioin
    global real
    ioin = '8'
    if ioin == str(ran) and real == 'L':
        real = 'R'
        label['text'] = 'Press number:  |  Right'
        voice()
    elif ioin == str(ran) and real == 'R':
        f = open("pass.flg",'w')
        f.close()
        while True:
            if os.path.isfile('pass.flg') == True:
                sys.exit(0)
    else:
        voice()
    
def click9():
    global ioin
    global real
    ioin = '9'
    if ioin == str(ran) and real == 'L':
        real = 'R'
        label['text'] = 'Press number:  |  Right'
        voice()
    elif ioin == str(ran) and real == 'R':
        f = open("pass.flg",'w')
        f.close()
        while True:
            if os.path.isfile('pass.flg') == True:
                sys.exit(0)
    else:
        voice()
    
if os.path.isfile('pass.flg') == True:
    os.remove('pass.flg')
    
root = Tk()
root.title('AudioTest-V1.0')
#root.geometry('534x496')

#layout
label = Label(root, text = 'Left  |  Press number:')
label.config(fg = '#EF7321', font=("Arial", 30, "bold"))
label.grid(row = 0, column = 0, columnspan = 3)

Button(root, text = '1', width = 7, height = 2, fg = '#EF7321', font=("Arial", 30, "bold"), command=click1).grid(row = 1, column = 0)
Button(root, text = '2', width = 7, height = 2, fg = '#EF7321', font=("Arial", 30, "bold"), command=click2).grid(row = 1, column = 1)
Button(root, text = '3', width = 7, height = 2, fg = '#EF7321', font=("Arial", 30, "bold"), command=click3).grid(row = 1, column = 2)

Button(root, text = '4', width = 7, height = 2, fg = '#EF7321', font=("Arial", 30, "bold"), command=click4).grid(row = 2, column = 0)
Button(root, text = '5', width = 7, height = 2, fg = '#EF7321', font=("Arial", 30, "bold"), command=click5).grid(row = 2, column = 1)
Button(root, text = '6', width = 7, height = 2, fg = '#EF7321', font=("Arial", 30, "bold"), command=click6).grid(row = 2, column = 2)

Button(root, text = '7', width = 7, height = 2, fg = '#EF7321', font=("Arial", 30, "bold"), command=click7).grid(row = 3, column = 0)
Button(root, text = '8', width = 7, height = 2, fg = '#EF7321', font=("Arial", 30, "bold"), command=click8).grid(row = 3, column = 1)
Button(root, text = '9', width = 7, height = 2, fg = '#EF7321', font=("Arial", 30, "bold"), command=click9).grid(row = 3, column = 2)

voice()

#Window centered
root.update_idletasks()
x = (root.winfo_screenwidth()-root.winfo_reqwidth())/2
y = (root.winfo_screenheight()-root.winfo_reqheight())/2
root.geometry("+%d+%d"%(x,y))

root.mainloop()
