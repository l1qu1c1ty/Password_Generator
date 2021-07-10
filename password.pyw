from tkinter import *
from tkinter import messagebox
import random
import webbrowser

def generate():
    try:
        text2 = entry2.get()
        length = entry1.get()
        password = ''.join( [ random.SystemRandom().choice(all) for _ in range(int(length))])
        if not (text2 == ""):
                entry2.delete(0,END)
        if not (length == ""): 
                entry2.insert(0,password)
    except:
        messagebox.showinfo("Warning!","Enter the numeric value.")

def clear():  
   text2 = entry2.get()
   if text2 == "":
       messagebox.showinfo("Warning!","Sections are already empty.")
   entry2.delete(0,END)

def selection():
    global all
    if (var1.get() == 1) and (var2.get() == 0) and (var3.get() == 0) and (var4.get() == 0):  
        all = numbers
    
    elif (var1.get() == 0) and (var2.get() == 1) and (var3.get() == 0) and (var4.get() == 0): 
        all = lower
    
    elif (var1.get() == 0) and (var2.get() == 0) and (var3.get() == 1) and (var4.get() == 0): 
        all = upper
    
    elif (var1.get() == 0) and (var2.get() == 0) and (var3.get() == 0) and (var4.get() == 1): 
        all = symbols
    
    elif (var1.get() == 1) and (var2.get() == 1) and (var3.get() == 0) and (var4.get() == 0): 
        all = numbers + lower

    elif (var1.get() == 1) and (var2.get() == 1) and (var3.get() == 1) and (var4.get() == 0): 
        all = numbers + lower + upper
    
    elif (var1.get() == 1) and (var2.get() == 0) and (var3.get() == 1) and (var4.get() == 0): 
        all = numbers + upper

    elif (var1.get() == 1) and (var2.get() == 0) and (var3.get() == 0) and (var4.get() == 1):
        all = numbers + symbols
    
    elif (var1.get() == 0) and (var2.get() == 1) and (var3.get() == 1) and (var4.get() == 0): 
        all = lower + upper
    
    elif (var1.get() == 0) and (var2.get() == 1) and (var3.get() == 1) and (var4.get() == 1):
        all = lower + upper + symbols

    elif (var1.get() == 0) and (var2.get() == 0) and (var3.get() == 1) and (var4.get() == 1): 
        all = upper + symbols
    
    elif (var1.get() == 0) and (var2.get() == 1) and (var3.get() == 0) and (var4.get() == 1):
        all = lower + symbols

    elif (var1.get() == 1) and (var2.get() == 0) and (var3.get() == 1) and (var4.get() == 1):
        all = numbers + upper + symbols
    
    elif (var1.get() == 1) and (var2.get() == 1) and (var3.get() == 0) and (var4.get() == 1): 
        all = numbers + lower + symbols

    elif (var1.get() == 1) and (var2.get() == 1) and (var3.get() == 1) and (var4.get() == 1): 
        all = numbers + lower + upper + symbols
    
    elif var5.get() == 1:
        all = numbers + lower + upper + symbols
    
    else:
        messagebox.showinfo("Warning!","All Checkbox Empty!")

def callback(url):
    webbrowser.open_new(url)

root = Tk()
root.geometry("400x250")
root.title("Password Generator")
root.configure(background="#050505")
root.resizable(width=False, height=False)

numbers = "1234567890"
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "!'^+%&/()?=.,~@${*}[;]\_-"
all = numbers + lower + upper + symbols

lbl1 = Label(root,text="Password Length:",fg="#01d9f8",bg="#050505")
entry1 = Entry(root,width=42)
lbl2 = Label(root,text="Your Password:",fg="#01d9f8",bg="#050505")
entry2 = Entry(root,width=42)
btn1 = Button(root,text="generate",fg="blue",width=10,command=generate)
btn2 = Button(root,text="clear",fg="red",width=10,command=clear)

lbl1.place(x=10,y=10)
entry1.place(x=120,y=10)
lbl2.place(x=10,y=40)
entry2.place(x=120,y=40)
btn1.place(x=120,y=80)
btn2.place(x=220,y=80)

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()

check1 = Checkbutton(root, text='Number',variable=var1, onvalue=1, offvalue=0, command=selection,fg="#09ff08",bg="#050505").place(x=10,y=120)
check2 = Checkbutton(root, text='Lower',variable=var2, onvalue=1, offvalue=0, command=selection,fg="#09ff08",bg="#050505").place(x=10,y=140)
check3 = Checkbutton(root, text='Upper',variable=var3, onvalue=1, offvalue=0, command=selection,fg="#09ff08",bg="#050505").place(x=10,y=160)
check4 = Checkbutton(root, text='Symbols',variable=var4, onvalue=1, offvalue=0, command=selection,fg="#09ff08",bg="#050505").place(x=10,y=180)
check5 = Checkbutton(root, text='All',variable=var5, onvalue=1, offvalue=0, command=selection,fg="#09ff08",bg="#050505").place(x=10,y=200)

link1 = Label(root,text="Follow Me Github",fg="#0155ff",bg="#050505",cursor="hand2")
link1.bind("<Button-1>",lambda e: callback("https://github.com/melihcan1376"))
link1.place(x=140,y=220)

mainloop()