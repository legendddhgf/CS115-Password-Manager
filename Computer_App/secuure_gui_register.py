#!/usr/bin/python3

#gui_register for secuure
#developed by Isaak Cherdak

import tkinter
from tkinter import messagebox
from db import *

window_reg = None
field_fname = None
field_lname = None
field_username = None
field_pass = None
field_confpass = None

def secuure_register():
    global window_reg
    global field_username
    global field_pass
    global field_fname
    global field_lname
    global field_confpass

    bcolor = '#9ACAEE'

    window_reg = tkinter.Toplevel()

    natwidth = window_reg.winfo_screenwidth() # get native resolutions
    natheight = window_reg.winfo_screenheight()
 
    window_reg.configure(background = bcolor)
    window_reg.geometry(("%dx%d") % (natwidth / 2,natheight / 2)) # start with a window
    window_reg.title("Register Account")
    window_reg.bind('<Key>', map_reg_key)

    label_blank = tkinter.Label(window_reg, text = '', background =
            bcolor)

    button_submit = tkinter.Button(window_reg, text = "Submit",
            width = 10, height = 3, command =
            submit_account_registration)

    field_fname = tkinter.Entry(window_reg, bd = 5)
    field_lname = tkinter.Entry(window_reg, bd = 5)
    field_username = tkinter.Entry(window_reg, bd = 5)
    field_pass = tkinter.Entry(window_reg, bd = 5, show = '*')
    field_confpass = tkinter.Entry(window_reg, bd = 5, show = '*')
            
    label_fname = tkinter.Label(window_reg, text = "First Name",
            background = bcolor)
    label_lname = tkinter.Label(window_reg, text = "Last Name",
            background = bcolor)
    label_username = tkinter.Label(window_reg, text = "User Name",
            background = bcolor)
    label_pass = tkinter.Label(window_reg, text = "Password",
            background = bcolor)
    label_confpass = tkinter.Label(window_reg,
            text = "Confirm Password", background = bcolor)
            
    field_fname.grid(row = 0, column = 1) # trying to organize
    field_lname.grid(row = 1, column = 1)
    field_username.grid(row = 2, column = 1)
    field_pass.grid(row = 3, column = 1)
    field_confpass.grid(row = 4, column = 1)
        
    label_fname.grid(row = 0, column = 0)
    label_lname.grid(row = 1, column = 0)
    label_username.grid(row = 2, column = 0)
    label_pass.grid(row = 3, column = 0)
    label_confpass.grid(row = 4, column = 0)

    label_blank.grid(row = 5, column = 1)

    button_submit.grid(row = 6, column = 1)

def submit_account_registration():
    global window_reg
    global field_username
    global field_pass
    global field_fname
    global field_lname
    global field_confpass
    if (len(field_username.get()) == 0 or
            len(field_pass.get()) == 0 or
            len(field_fname.get()) == 0 or
            len(field_lname.get()) == 0):
        messagebox.showerror("Account Registration Error",
                "No fields can be empty")
        return

    if (field_confpass.get() != field_pass.get()):
        messagebox.showerror("Account Registration Error", "Passwords" +
                " do not match")
        return
            
    user_str = field_username.get()
    pass_str = field_pass.get()
    fname_str = field_fname.get()
    lname_str = field_lname.get()
            
    print ("Adding user '%s' with password '%s'" % (user_str, pass_str))
    addToUserTable(user_str, pass_str, "fname", "lname")

    window_reg.destroy()

            
def map_reg_key(event): # only called through register_account()
    global window_reg
    if (len(event.char) != 1):
        return
    if (ord(event.char) == 27):
        window_reg.destroy()
    return
