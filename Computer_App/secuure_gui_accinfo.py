#!/usr/bin/python3

#gui_accinfo for secuure
#developed by Isaak Cherdak

import tkinter
from tkinter import messagebox
from db import *
from secuure_gui_accadd import secuure_accadd
from secuure_gui_accrem import secuure_accrem

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
    list_accounts = {}
    list_accounts["Admin"] = "Password"
    label_usernames = []
    label_passwords = []

    """ new """
    """"""
    data = getPasswordsForUser(acc_user)
    for info in data:
        label_usernames.append(tkinter.Label(window_info, text =
            info[0] + " : ", background = bcolor))
        label_passwords.append(tkinter.Label(window_info, text =
            info[1], background = bcolor))
    """"""

    """ old """
    """
    for key in list_accounts:
        label_usernames.append(tkinter.Label(window_info, text =
            key + " : ", background = bcolor))
        label_passwords.append(tkinter.Label(window_info, text =
            list_accounts[key], background = bcolor))
    """

    for index in range(0, len(label_usernames)):
        label_user = label_usernames[index]
        label_pass = label_passwords[index]
        label_user.grid(row = index, column = 0)
        label_pass.grid(row = index, column = 1)

    # need to do this for every button (add account, remove account, etc)
    blank_labels = [] # how to artificially make space
    num_spaces = 10
    space_start = 2
    for i in range(0, num_spaces):
        blank_labels.append(tkinter.Label(window_info, text = ' ',
            background = bcolor))
        blank_labels[i].grid(row  = 0, column = space_start + i)

    button_add = tkinter.Button(window_info, text = "Add Account",
        command = secuure_accadd)
    button_remove = tkinter.Button(window_info,
        text = "Remove Account", command = secuure_accrem)
    button_refresh = tkinter.Button(window_info,
        text = "Refresh Info", command = refresh_info)
            
    button_add.grid(row = 0, column = space_start + num_spaces)
    button_remove.grid(row = 1, column = space_start + num_spaces)
    button_refresh.grid(row = 2, column = space_start + num_spaces)

def refresh_info():
    global window_info
    global acc_user
    window_info.destroy()
    secuure_accinfo(acc_user)

def map_list_account_info_key(event):
    global window_info
    if (len(event.char) == 1 and ord(event.char) == 27):
        window_info.destroy()
