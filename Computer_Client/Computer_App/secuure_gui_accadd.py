#!/usr/bin/python3

#gui_accadd for secuure
#developed by Isaak Cherdak

import tkinter
from tkinter import messagebox
from db import *
from passgen import genPass

entry_user_user = None
entry_user_pass = None
entry_user_notes = None
entry_user_website = None
slider_length = None
window_add_acc = None
acc_user = None

def key_add_window(event):
    global window_add_acc
    global acc_user
    if (len(event.char) != 1):
        return
    if (ord(event.char) == 10 or ord(event.char) == 13): # enter key
        submit_account_add()
    if (ord(event.char) == 27):
        window_add_acc.destroy()

def submit_account_add():
    global entry_user_user
    global entry_user_pass
    global entry_user_website
    global entry_user_notes
    global window_add_acc
    user_user = entry_user_user.get()
    user_pass = entry_user_pass.get()
    user_website = entry_user_website.get()
    user_notes = entry_user_notes.get()

    if (len(user_user) == 0 or len(user_pass) == 0 or
            len(user_website) == 0):
        messagebox.showerror("Invalid Submission",
            "All Fields other than notes must be filled")
        return

    if (addPassForWebsite(user_user, user_pass, user_website, user_notes)):
        window_add_acc.destroy()

def secuure_accadd(user_str):
    global entry_user_user
    global entry_user_pass
    global entry_user_website
    global entry_user_notes
    global slider_length
    global window_add_acc
    global acc_user

    acc_user = user_str

    bcolor = '#9ACAEE'

    window_add_acc = tkinter.Toplevel()
                
    natwidth = window_add_acc.winfo_screenwidth() # get native resolutions
    natheight = window_add_acc.winfo_screenheight()

    window_add_acc.configure(background = bcolor)
    window_add_acc.geometry(("%dx%d") % (natwidth / 2,natheight / 2)) # start with a window
    window_add_acc.title("Add Account")
    window_add_acc.bind('<Key>', key_add_window)

    label_user_website = tkinter.Label(window_add_acc, text = "Website",
            background = bcolor)
    label_user_user = tkinter.Label(window_add_acc, text = "Username",
            background = bcolor)
    label_user_pass = tkinter.Label(window_add_acc, text = "Password",
            background = bcolor)
    label_user_notes = tkinter.Label(window_add_acc, text = "Notes",
            background = bcolor)

    entry_user_website = tkinter.Entry(window_add_acc)
    entry_user_user = tkinter.Entry(window_add_acc)
    entry_user_pass = tkinter.Entry(window_add_acc, show = '*')
    entry_user_notes = tkinter.Entry(window_add_acc,
            width = 30, relief = tkinter.GROOVE)

    button_user_add = tkinter.Button(window_add_acc, text = "Submit", command =
            submit_account_add)

    label_blank = tkinter.Label(window_add_acc, text = "", background = bcolor)

    slider_length = tkinter.Scale(window_add_acc, from_ = 8, to = 20,
            orient = tkinter.HORIZONTAL)
    var_caps = tkinter.IntVar()
    check_caps = tkinter.Checkbutton(window_add_acc,
        text = "Capitals", variable = var_caps,
        background = bcolor)
    label_blank1 = tkinter.Label(window_add_acc, text = "  ",
            background = bcolor) # spacing
    var_nums = tkinter.IntVar()
    check_nums = tkinter.Checkbutton(window_add_acc,
        text = "Nums", variable = var_nums,
        background = bcolor)
    label_blank2 = tkinter.Label(window_add_acc, text = "  ",
            background = bcolor) # spacing
    var_specs = tkinter.IntVar()
    check_specs = tkinter.Checkbutton(window_add_acc,
        text = "Special Chars", variable = var_specs,
        background = bcolor)

    label_blank3 = tkinter.Label(window_add_acc, text = "  ",
            background = bcolor)

    button_gen_pass = tkinter.Button(window_add_acc,
            text = "Randomize", command = lambda:
            newRandomPass(var_caps.get(), var_nums.get(), var_specs.get()))

    label_user_website.grid(row = 0, column = 0)
    label_user_user.grid(row = 1, column = 0)
    label_user_pass.grid(row = 2, column = 0)
    label_user_notes.grid(row = 3, column = 0)

    entry_user_website.grid(row = 0, column = 1)
    entry_user_user.grid(row = 1, column = 1)
    
    entry_user_pass.grid(row = 2, column = 1)
    slider_length.grid(row = 2, column = 2)
    check_caps.grid(row = 2, column = 3)
    label_blank1.grid(row = 2, column = 4)
    check_nums.grid(row = 2, column = 5)
    label_blank2.grid(row = 2, column = 6)
    check_specs.grid(row = 2, column = 7)
    label_blank3.grid(row = 2, column = 8)
    button_gen_pass.grid(row = 2, column = 9)

    entry_user_notes.grid(row = 3, column = 1)

    label_blank.grid(row = 4, column = 0)

    button_user_add.grid(row = 5, column = 1)

    return window_add_acc

def newRandomPass(caps, nums, specs):
    global entry_user_pass
    global slider_length
    #print ("Caps %d, nums %d, specs %d" % (caps, nums, specs))
    length = slider_length.get()
    str_pass = genPass(length, specs, caps, nums)
    entry_user_pass.delete(0, len(entry_user_pass.get())) # delete previous
                                                          # password
    entry_user_pass.insert(0, str_pass) # replace with new password
    print ("Entry: %s" % str_pass)
