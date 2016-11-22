#!/usr/bin/python3

#gui_accrem for secuure
#developed by Isaak Cherdak

import tkinter
from tkinter import messagebox
from db import *

window_rem_acc = None

def key_rem_window(event):
    global window_rem_acc
    window_rem_acc.destroy()

def secuure_accrem():

    global window_rem_acc

    bcolor = '#9ACAEE'

    window_rem_acc = tkinter.Toplevel()
                
    natwidth = window_rem_acc.winfo_screenwidth() # get native resolutions
    natheight = window_rem_acc.winfo_screenheight()

    window_rem_acc.configure(background = bcolor)
    window_rem_acc.geometry(("%dx%d") % (natwidth / 2,natheight / 2)) # start with a window
    window_rem_acc.title("Remove Account")
    window_rem_acc.bind('<Key>', key_rem_window)


