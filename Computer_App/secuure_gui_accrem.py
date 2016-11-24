#!/usr/bin/python3

#gui_accrem for secuure
#developed by Isaak Cherdak

import tkinter
from tkinter import messagebox
from db import *

window_rem_acc = None
acc_user = None

def key_rem_window(event):
    global window_rem_acc
    if (len(event.char) != 1):
        return
    if (ord(event.char) == 27):
        window_rem_acc.destroy()

def secuure_accrem(user_str):

    global window_rem_acc
    global acc_user
    acc_user = user_str

    bcolor = '#9ACAEE'

    window_rem_acc = tkinter.Toplevel()
                
    natwidth = window_rem_acc.winfo_screenwidth() # get native resolutions
    natheight = window_rem_acc.winfo_screenheight()

    window_rem_acc.configure(background = bcolor)
    window_rem_acc.geometry(("%dx%d") % (natwidth / 2,natheight / 2)) # start with a window
    window_rem_acc.title("Remove Account")
    window_rem_acc.bind('<Key>', key_rem_window)

    data = getPasswordsForUser(acc_user)
    button_websites = []
    for info in data:
        button_websites.append(tkinter.Button(window_rem_acc, text =
            info[2], width = 8, command =
            (lambda: delete_website_info(info[0], info[2]))))
        button_websites[len(button_websites) - 1].grid(row =
                len(button_websites) - 1, column = 0)
    
 
def delete_website_info(u, w):
    global window_rem_acc
    global acc_user

    removeEntry(u, w)
    window_rem_acc.destroy()
    secuure_accrem(acc_user)

