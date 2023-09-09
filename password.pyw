from tkinter import *
from tkinter import messagebox
import random
import webbrowser

def generate_password():
    try:
        text2 = entry2.get()
        length = entry1.get()
        password = ''.join([random.SystemRandom().choice(all__char) for _ in range(int(length))])
        if not (text2 == ""):
                entry2.delete(0,END)
        
        if not (length == ""): 
                entry2.insert(0,password)
    except:
        messagebox.showinfo("Warning!","Enter the numeric value.")

def clear_password():  
   text2 = entry2.get()
   if text2 == "":
       messagebox.showinfo("Warning!","Sections are already empty.")
   entry2.delete(0,END)

def save_text():
    passwd = entry2.get()
    if passwd != "":
        with open("password.txt","a+") as password:
            text = f"Password: {passwd}\n"
            password.write(text)
            messagebox.showinfo("Information","Saved to password.txt file.")
            password.close()
    else:
        messagebox.showinfo("Warning!","Password section is empty.")

def toggle_check(check_var, check_label):
    if check_var.get() == 0:
        check_var.set(1)
        check_label.config(image=checked_image)
    else:
        check_var.set(0)
        check_label.config(image=unchecked_image)
    
    if check_var == var5:  # Check if the clicked checkbox is the "all__char" checkbox
        if check_var.get() == 1:
            var1.set(1)
            var2.set(1)
            var3.set(1)
            var4.set(1)
            check1_checkbox.config(image=checked_image)
            check2_checkbox.config(image=checked_image)
            check3_checkbox.config(image=checked_image)
            check4_checkbox.config(image=checked_image)
        else:
            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            check1_checkbox.config(image=unchecked_image)
            check2_checkbox.config(image=unchecked_image)
            check3_checkbox.config(image=unchecked_image)
            check4_checkbox.config(image=unchecked_image)

    selection()

def selection():
    global all__char
    if (var1.get() == 1) and (var2.get() == 0) and (var3.get() == 0) and (var4.get() == 0):  
        all__char = numbers
    
    elif (var1.get() == 0) and (var2.get() == 1) and (var3.get() == 0) and (var4.get() == 0): 
        all__char = lower
    
    elif (var1.get() == 0) and (var2.get() == 0) and (var3.get() == 1) and (var4.get() == 0): 
        all__char = upper
    
    elif (var1.get() == 0) and (var2.get() == 0) and (var3.get() == 0) and (var4.get() == 1): 
        all__char = symbols
    
    elif (var1.get() == 1) and (var2.get() == 1) and (var3.get() == 0) and (var4.get() == 0): 
        all__char = numbers + lower

    elif (var1.get() == 1) and (var2.get() == 1) and (var3.get() == 1) and (var4.get() == 0): 
        all__char = numbers + lower + upper
    
    elif (var1.get() == 1) and (var2.get() == 0) and (var3.get() == 1) and (var4.get() == 0): 
        all__char = numbers + upper

    elif (var1.get() == 1) and (var2.get() == 0) and (var3.get() == 0) and (var4.get() == 1):
        all__char = numbers + symbols
    
    elif (var1.get() == 0) and (var2.get() == 1) and (var3.get() == 1) and (var4.get() == 0): 
        all__char = lower + upper
    
    elif (var1.get() == 0) and (var2.get() == 1) and (var3.get() == 1) and (var4.get() == 1):
        all__char = lower + upper + symbols

    elif (var1.get() == 0) and (var2.get() == 0) and (var3.get() == 1) and (var4.get() == 1): 
        all__char = upper + symbols
    
    elif (var1.get() == 0) and (var2.get() == 1) and (var3.get() == 0) and (var4.get() == 1):
        all__char = lower + symbols

    elif (var1.get() == 1) and (var2.get() == 0) and (var3.get() == 1) and (var4.get() == 1):
        all__char = numbers + upper + symbols
    
    elif (var1.get() == 1) and (var2.get() == 1) and (var3.get() == 0) and (var4.get() == 1): 
        all__char = numbers + lower + symbols

    elif (var1.get() == 1) and (var2.get() == 1) and (var3.get() == 1) and (var4.get() == 1): 
        all__char = numbers + lower + upper + symbols
    
    elif var5.get() == 1:
        all__char = numbers + lower + upper + symbols
    
    else:
        messagebox.showinfo("Warning!","All Checkbox Empty!")

def call__charback(url):
    webbrowser.open_new(url)

root = Tk()
root.geometry("550x350")
root.title("Password Generator")
root.configure(background="#6002fd")
root.resizable(width=False, height=False)

unchecked_image = PhotoImage(file="icons/unchecked.png")
checked_image = PhotoImage(file="icons/checked.png")

numbers = "1234567890"
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "!'^+%&/()?=.,~@${*}[;]\_-₺€"
all__char_char = numbers + lower + upper + symbols

lbl1 = Label(root,text="Password Length:",fg="white",bg="#6002fd")
entry1 = Entry(root,width=36)
lbl2 = Label(root,text="Your Password:",fg="white",bg="#6002fd")
entry2 = Entry(root,width=36)

icon = PhotoImage(file="icons/password.png")

btn1 = Button(root,text="generate password",fg="green",width=200,image=icon, compound='left', command=generate_password)

icon2 = PhotoImage(file="icons/clear.png")

btn2 = Button(root,text="clear password\t",fg="red",width=200,image=icon2, compound='left', command=clear_password)

icon3 = PhotoImage(file="icons/text.png")

btn3 = Button(root,text="save txt file\t",fg="blue",width=200,image=icon3, compound='left', command=save_text)

lbl1.place(x=60,y=20)
entry1.place(x=190,y=20)
lbl2.place(x=60,y=70)
entry2.place(x=190,y=70)
btn1.place(x=170,y=120)
btn2.place(x=170,y=170)
btn3.place(x=170,y=220)

image = PhotoImage(file="icons/icon48.png")
image_label = Label(root, image=image, bg="#6002fd")
image_label.place(x=1,y=1)

image2 = PhotoImage(file="icons/icon2-48.png")
image2_label = Label(root, image=image2, bg="#6002fd")
image2_label.place(x=1,y=50)

image3 = PhotoImage(file="icons/github64.png")
image3_label = Label(root, image=image3, bg="#6002fd")
image3_label.place(x=230,y=260)

image4 = PhotoImage(file="icons/numbers32.png")
image4_label = Label(root, image=image4, bg="#6002fd")
image4_label.place(x=10,y=120)

image5 = PhotoImage(file="icons/alpha32.png")
image5_label = Label(root, image=image5, bg="#6002fd")
image5_label.place(x=10,y=150)

image6 = PhotoImage(file="icons/alpha2-32.png")
image6_label = Label(root, image=image6, bg="#6002fd")
image6_label.place(x=10,y=180)

image7 = PhotoImage(file="icons/asterisk32.png")
image7_label = Label(root, image=image7, bg="#6002fd")
image7_label.place(x=10,y=210)

image8 = PhotoImage(file="icons/tick32.png")
image8_label = Label(root, image=image8, bg="#6002fd")
image8_label.place(x=10,y=240)

root.iconbitmap("icons/icon100.ico")

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()

check1_label = Label(root, text="Number", fg="white", bg="#6002fd")
check1_checkbox = Label(root, image=unchecked_image, bg="#6002fd", cursor="hand2")
check1_checkbox.bind("<Button-1>", lambda e: toggle_check(var1, check1_checkbox))
check1_label.place(x=50, y=120)
check1_checkbox.place(x=110, y=115)

check2_label = Label(root, text="Lower", fg="white", bg="#6002fd")
check2_checkbox = Label(root, image=unchecked_image, bg="#6002fd", cursor="hand2")
check2_checkbox.bind("<Button-1>", lambda e: toggle_check(var2, check2_checkbox))
check2_label.place(x=50, y=150)
check2_checkbox.place(x=110, y=145)

check3_label = Label(root, text="Upper", fg="white", bg="#6002fd")
check3_checkbox = Label(root, image=unchecked_image, bg="#6002fd", cursor="hand2")
check3_checkbox.bind("<Button-1>", lambda e: toggle_check(var3, check3_checkbox))
check3_label.place(x=50, y=180)
check3_checkbox.place(x=110, y=175)

check4_label = Label(root, text="Symbols", fg="white", bg="#6002fd")
check4_checkbox = Label(root, image=unchecked_image, bg="#6002fd", cursor="hand2")
check4_checkbox.bind("<Button-1>", lambda e: toggle_check(var4, check4_checkbox))
check4_label.place(x=50, y=210)
check4_checkbox.place(x=110, y=205)

check5_label = Label(root, text="All", fg="white", bg="#6002fd")
check5_checkbox = Label(root, image=unchecked_image, bg="#6002fd", cursor="hand2")
check5_checkbox.bind("<Button-1>", lambda e: toggle_check(var5, check5_checkbox))
check5_label.place(x=50, y=240)
check5_checkbox.place(x=110, y=235)

link1 = Label(root,text="Follow Me Github",fg="white",bg="#6002fd",cursor="hand2")
link1.bind("<Button-1>",lambda e: call__charback("https://github.com/l1qu1c1ty"))
link1.place(x=200,y=320)

mainloop()