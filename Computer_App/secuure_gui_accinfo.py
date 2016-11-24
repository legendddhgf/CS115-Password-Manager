#!/usr/bin/python3

#gui_accinfo for secuure
#developed by Isaak Cherdak

import tkinter
from tkinter import messagebox
from db import *
from secuure_gui_accadd import secuure_accadd
from secuure_gui_accrem import secuure_accrem
from secuure_gui_accwebinfo import secuure_accwebinfo

window_info = None
acc_user = None

def secuure_accinfo(user_str):
    global acc_user
    global window_info

    acc_user = user_str
    bcolor = '#9ACAEE'
    window_info = tkinter.Toplevel()

    natwidth = window_info.winfo_screenwidth() # get native resolutions
    natheight = window_info.winfo_screenheight()

    window_info.configure(background = bcolor)
    window_info.geometry(("%dx%d") % (natwidth / 2,natheight / 2)) # start with a window
    window_info.title("Account Information for '%s'" % (user_str))
    window_info.bind('<Key>', map_list_account_info_key)

    #get accounts
    button_usernames = []

    """ new """
    """"""
    data = getPasswordsForUser(acc_user)
    for info in data:
        button_usernames.append(tkinter.Button(window_info, text =
            info[2], command =
            lambda: secuure_accwebinfo(acc_user, info[2])))
    """"""

    for index in range(0, len(button_usernames)):
        button_user = button_usernames[index]
        button_user.grid(row = index, column = 0)

    # need to do this for every button (add account, remove account, etc)
    blank_labels = [] # how to artificially make space
    num_spaces = 10
    space_start = 2
    for i in range(0, num_spaces):
        blank_labels.append(tkinter.Label(window_info, text = ' ',
            background = bcolor))
        blank_labels[i].grid(row  = 0, column = space_start + i)

    button_add = tkinter.Button(window_info, text = "Add Account",
        command = add_but_cmd)
    button_remove = tkinter.Button(window_info,
        text = "Remove Account", command = rem_but_cmd)
    button_refresh = tkinter.Button(window_info,
        text = "Refresh Info", command = refresh_info)
            
    button_add.grid(row = 0, column = space_start + num_spaces)
    button_remove.grid(row = 1, column = space_start + num_spaces)
    button_refresh.grid(row = 2, column = space_start + num_spaces)

def add_but_cmd():
    global acc_user
    global window_info
    #window_info.destroy()
    win_temp = secuure_accadd(acc_user)
    #win_temp.wm_protocol("WM_DELETE_WINDOW", secuure_accinfo(acc_user))


def rem_but_cmd(): # because remove needs arguments
    global acc_user
    global window_info
    #window_info.destroy()
    secuure_accrem(acc_user)

def refresh_info():
    global window_info
    global acc_user
    window_info.destroy()
    secuure_accinfo(acc_user)

def map_list_account_info_key(event):
    global window_info
    if (len(event.char) == 1 and ord(event.char) == 27):
        window_info.destroy()
