'''
Password Generator
    by Melih Can
        Python 3 Tkinter
            Thanks for using my app.
'''
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import random
import webbrowser

def generate(): # Password Generate
    try:
        text = entry1.get()
        text2 = entry2.get()
        length = entry1.get()
        password = ''.join( [ random.SystemRandom().choice(all) for _ in range(int(length))])
        if not (text2 == ""):
                entry2.delete(0,END)
        if not (text == ""): 
                entry2.insert(0,password)
    except:
        messagebox.showinfo("Warning!","Enter the numeric value.")

<<<<<<< HEAD
def clear():  # Entry Clear
   text2 = entry2.get()
   if text2 == "":
       messagebox.showinfo("Warning!","Sections are already empty.")
   entry2.delete(0,END)

def print_selection():  # Checkbox Combination
    global all
    if (var1.get() == 1) and (var2.get() == 0) and (var3.get() == 0) and (var4.get() == 0):   #1
        all = numbers
    
    elif (var1.get() == 0) and (var2.get() == 1) and (var3.get() == 0) and (var4.get() == 0): #2
        all = lower
    
    elif (var1.get() == 0) and (var2.get() == 0) and (var3.get() == 1) and (var4.get() == 0): #3
        all = upper
    
    elif (var1.get() == 0) and (var2.get() == 0) and (var3.get() == 0) and (var4.get() == 1): #4
        all = symbols
    
    elif (var1.get() == 1) and (var2.get() == 1) and (var3.get() == 0) and (var4.get() == 0): #5
        all = numbers + lower

    elif (var1.get() == 1) and (var2.get() == 1) and (var3.get() == 1) and (var4.get() == 0): #6
        all = numbers + lower + upper
    
    elif (var1.get() == 1) and (var2.get() == 0) and (var3.get() == 1) and (var4.get() == 0): #7
        all = numbers + upper

    elif (var1.get() == 1) and (var2.get() == 0) and (var3.get() == 0) and (var4.get() == 1): #8
        all = numbers + symbols
    
    elif (var1.get() == 0) and (var2.get() == 1) and (var3.get() == 1) and (var4.get() == 0): #9
        all = lower + upper
    
    elif (var1.get() == 0) and (var2.get() == 1) and (var3.get() == 1) and (var4.get() == 1): #10
        all = lower + upper + symbols

    elif (var1.get() == 0) and (var2.get() == 0) and (var3.get() == 1) and (var4.get() == 1): #11
        all = upper + symbols
    
    elif (var1.get() == 0) and (var2.get() == 1) and (var3.get() == 0) and (var4.get() == 1): #12
        all = lower + symbols

    elif (var1.get() == 1) and (var2.get() == 0) and (var3.get() == 1) and (var4.get() == 1): #13
        all = numbers + upper + symbols
    
    elif (var1.get() == 1) and (var2.get() == 1) and (var3.get() == 0) and (var4.get() == 1): #14
        all = numbers + lower + symbols

    elif (var1.get() == 1) and (var2.get() == 1) and (var3.get() == 1) and (var4.get() == 1): #15
        all = numbers + lower + upper + symbols
    
    elif var5.get() == 1:
        all = numbers + lower + upper + symbols

=======
def clear():
    text  = entry1.get()
    text2 = entry2.get()
    if (text or text2) == "":
        messagebox.showinfo("Warning!","Sections are already empty.")
    entry1.delete(0,END)
    entry2.delete(0,END)
>>>>>>> 402bb6d3ff0ff4628db46c13f58973c73bb4e20f

def callback(url):
    webbrowser.open_new(url)

root = Tk()
root.geometry("400x400")
root.title("Password Generator")
root.configure(background="#314169")
root.resizable(width=False, height=False)

numbers = "1234567890"
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "!'^+%&/()?=.,~@${*}[;]\_-"
all = numbers + lower + upper + symbols

label1 = Label(root,text="Password Length:",fg="yellow",bg="#314169").pack()

entry1 = Entry(root)
entry1.pack(ipadx=50)

space1 = Label(root,fg="yellow",bg="#314169").pack()

label2 = Label(root,text="Your Password:",fg="yellow",bg="#314169").pack()

entry2 = Entry(root,text="")
entry2.pack(ipadx=50)

space2 = Label(root,fg="yellow",bg="#314169").pack()

button1 = Button(root,text="generate",fg="blue",command=generate)
button1.pack()

space3 = Label(root,fg="yellow",bg="#314169").pack()

button2 = Button(root,text="clear",fg="red",command=clear).pack()

space4 = Label(root,fg="yellow",bg="#314169").pack()

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()

check1 = Checkbutton(root, text='Number',variable=var1, onvalue=1, offvalue=0, command=print_selection,fg="#090b03",bg="#314169").pack()
check2 = Checkbutton(root, text='Lower',variable=var2, onvalue=1, offvalue=0, command=print_selection,fg="#090b03",bg="#314169").pack()
check3 = Checkbutton(root, text='Upper',variable=var3, onvalue=1, offvalue=0, command=print_selection,fg="#090b03",bg="#314169").pack()
check4 = Checkbutton(root, text='Symbols',variable=var4, onvalue=1, offvalue=0, command=print_selection,fg="#090b03",bg="#314169").pack()
check5 = Checkbutton(root, text='All',variable=var5, onvalue=1, offvalue=0, command=print_selection,fg="#090b03",bg="#314169").pack()

space5 = Label(root,fg="yellow",bg="#314169").pack()
link1 = Label(root,text="Follow Me Github",fg="yellow",bg="#314169",cursor="hand2")
link1.pack()
link1.bind("<Button-1>",lambda e: callback("https://github.com/melihcan1376"))

mainloop()
