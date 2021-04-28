from tkinter import *
from tkinter import messagebox
import tkinter as tk
import random
import webbrowser

def generate():
    numbers = "1234567890"
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    symbols = "!'^+%&/()?=.,~@${*}[;]\_-"

    all = numbers + lower + upper + symbols 
    try:
        length = entry1.get()
        password = "".join(random.sample(all,int(length)))
        entry2.insert(0,password)
    except:
        messagebox.showinfo("Warning!","Enter the numeric value.")

def clear():
    text  = entry1.get()
    text2 = entry2.get()
    if (text and text2) == "":
        messagebox.showinfo("Warning!","Sections are already empty.")
    entry1.delete(0,END)
    entry2.delete(0,END)

def callback(url):
    webbrowser.open_new(url)


root = Tk()
root.geometry("300x280")
root.title("Password Generator")
root.configure(background="#314169")

label1 = Label(root,text="Password Length:",fg="yellow",bg="#314169").pack()

entry1 = Entry(root)
entry1.pack()

space1 = Label(root,fg="yellow",bg="#314169").pack()

label2 = Label(root,text="Your Password:",fg="yellow",bg="#314169").pack()

entry2 = Entry(root,text="")
entry2.pack()

space2 = Label(root,fg="yellow",bg="#314169").pack()

button1 = Button(root,text="generate",command=generate)
button1.pack()

space3 = Label(root,fg="yellow",bg="#314169").pack()

button2 = Button(root,text="clear",command=clear).pack()

space4 = Label(root,fg="yellow",bg="#314169").pack()

link1 = Label(root,text="melihcan1376",fg="yellow",bg="#314169",cursor="hand2")
link1.pack()
link1.bind("<Button-1>",lambda e: callback("https://github.com/melihcan1376"))

root.mainloop()
