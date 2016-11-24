#!/usr/bin/python3

#gui_login for secuure
#developed by Isaak Cherdak

import tkinter
from tkinter import messagebox
from db import *
from secuure_gui_register import secuure_register
from secuure_gui_accinfo import secuure_accinfo

# global variables
root = None
userentry = None
passentry = None
window_en = None

def secuure_login():
    global root
    global userentry
    global passentry
    global window_en

    window_en = True
    bcolor = '#9ACAEE'
    createPassTable()
    userAccounts = {}# temporary users until backend is sorted out
    userAccounts["Admin"] = "Password"
        
    root = tkinter.Tk() # set root to be toplevel window
    root.title("Welcome to Secuure")
    root.configure(background = bcolor)
                
    natwidth = root.winfo_screenwidth() # get native resolutions
    natheight = root.winfo_screenheight()
            
    root.geometry(("%dx%d") % (natwidth / 2,natheight / 2)) # start with a window
                                                            # 1/4 the size of the
                                                            # screen
                
    frame_main = tkinter.Frame(root)
                
    root.bind('<Key>', mapKeyToFunc) # for most keystrokes, one function will map
                
    login_Button = tkinter.Button(root, text ="log in", width = 10, height = 3,
            command = login)
        
    userentry = tkinter.Entry(root, bd = 5)
    user_label = tkinter.Label(root, text = 'Username',
            background = bcolor)
    passentry = tkinter.Entry(root, bd = 5, show = '*') # password is hidden
    pass_label = tkinter.Label(root, text = 'Password',
            background = bcolor)
    reg_button = tkinter.Button(root, text = "Register", command =
            reg_but_cmd)
                
    blank_label = tkinter.Label(root, text = '', background =
            bcolor)
                
    reg_button.grid(row = 4, column = 1)
    blank_label.grid(row = 3, column = 100) # filling space
    login_Button.grid(row = 2, column = 1)
    userentry.grid(row = 0, column = 1) # these four need to be sized appropriately
    user_label.grid(row = 0, column = 0)
    passentry.grid(row = 1, column = 1)
    pass_label.grid(row = 1, column = 0)
                
    menubar = tkinter.Menu(root) # make menubar
    filemenu = tkinter.Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=donothing)
    filemenu.add_command(label="Open", command=donothing)
    filemenu.add_command(label="Save", command=donothing)
    filemenu.add_command(label="Save as...", command=donothing)
    filemenu.add_command(label="Close", command=donothing)
                
    filemenu.add_separator()
                        
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    editmenu = tkinter.Menu(menubar, tearoff=0)
    editmenu.add_command(label="Undo", command=donothing)
        
    editmenu.add_separator()
                
    editmenu.add_command(label="Cut", command=donothing)
    editmenu.add_command(label="Copy", command=donothing)
    editmenu.add_command(label="Paste", command=donothing)
    editmenu.add_command(label="Delete", command=donothing)
    editmenu.add_command(label="Select All", command=donothing)
                
    menubar.add_cascade(label="Edit", menu=editmenu)
    helpmenu = tkinter.Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", command=donothing)
    helpmenu.add_command(label="About...", command=donothing)
    menubar.add_cascade(label="Help", menu=helpmenu)
                
    root.config(menu=menubar) # set menubar to main window
                
    root.mainloop() # start the interface

def reg_but_cmd():
    global window_en
    window_en = False # while using a different window, disable this one
    secuure_register()
    window_en = True

def mapKeyToFunc(event):
    global window_en
    if (not window_en): # don't let people mess with this info unless active
        return
    if (len(event.char) != 1): # ie: shift is length 0
        return
    if (event.char == '\n' or event.char == '\r'):
        login()
    elif (ord(event.char) == 27): # 27 is ascii val of escape
        quit_prgrm()
    return # without a return, every key results in an error
        
def login(): # hit enter or login button
    global window_en
    global user_str
    global pass_str
    if (not window_en):
        return

    user_str = userentry.get()
    pass_str = passentry.get()
            
    #Call to login function in storage.py
    login_valid = verMasterLogin(user_str, pass_str)

    if (len(user_str) == 0 or len(pass_str) == 0):
        messagebox.showerror("Invalid Combination",
            "Neither User nor Password can be empty")
        return
        
    info_str = "Your username is %s\n" % \
        (user_str) + "Your password is %s\n" % (pass_str)
            
    if (login_valid):
        info_str += "This is a valid combination"
    else:
        info_str += "This is not a valid combination"
        
    #messagebox.showinfo("Account information", info_str)

    print(info_str)

    if (login_valid):
        secuure_accinfo(user_str)
    else:
        messagebox.showerror("Invalid Combination",
            "User/Pass combo doesn't exist")
        
def quit_prgrm(): # when you hit escape
    global root
    root.destroy()

def donothing():
    return
