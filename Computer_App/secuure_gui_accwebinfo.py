#!/usr/bin/python3

#gui_accrem for secuure
#developed by Isaak Cherdak

import tkinter
from tkinter import messagebox
from db import *

window_web_info = None
acc_user = None

def key_web_window(event):
    global window_web_info
    if (len(event.char) != 1):
        return
    if (ord(event.char) == 27):
        window_web_info.destroy()

def secuure_accwebinfo(user_str, website_str):

    global window_web_info
    global acc_user
    acc_user = user_str

    bcolor = '#9ACAEE'

    window_web_info = tkinter.Toplevel()
                
    natwidth = window_web_info.winfo_screenwidth() # get native resolutions
    natheight = window_web_info.winfo_screenheight()

    window_web_info.configure(background = bcolor)
    window_web_info.geometry(("%dx%d") % (natwidth / 2,natheight / 2)) # start with a window
    window_web_info.title("Info for ")
    window_web_info.bind('<Key>', key_rem_window)

    data = getPasswordsForUser(acc_user)
    label_website = None
    label_user = None
    label_pass = None
    label_notes = None
    for info in data:
        if (info[2] != website_str):
            continue
        label_website = tkinter.Label(window_web_info, text =
            info[2], width = 8, background = bcolor)
        label_user = tkinter.Label(window_web_info,
                text = info[0], background = bcolor)
        break
    
 
def update_website_info(u, w):
    global window_web_info
    global acc_user

    removeEntry(u, w)
    window_web_info.destroy()
    secuure_accrem(acc_user)

