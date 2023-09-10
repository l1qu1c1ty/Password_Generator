from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
from password_strength import PasswordPolicy
import random
import webbrowser
import pyperclip
import os
import sys

def generate_password():
    try:
        text2 = password_entry.get()
        length = entry1.get()

        # Check if the length is negative
        if int(length) < 1:
            messagebox.showerror("Error", "Password length cannot be neutral or negative.")
            return  # Exit the function if it's negative

        if var1.get() == 0 and var2.get() == 0 and var3.get() == 0 and var4.get() == 0:
            messagebox.showwarning("Warning!", "Select at least one character type.")
            return  # Exit the function if no checkbox is checked
        
        password = ''.join([random.SystemRandom().choice(all__char) for _ in range(int(length))])
        if not (text2 == ""):
                password_entry.delete(0,END)
        
        if not (length == ""): 
                password_entry.insert(0,password)
                messagebox.showinfo("Password","Password Created.")
        
        # Update the password strength label
        update_password_strength_label(password)

    except ValueError:
        messagebox.showerror("Warning!", "Enter a numeric value.")

def clear_password():  
   text2 = password_entry.get()
   if text2 == "":
       messagebox.showwarning("Warning!","Sections are already empty.")

   if text2 != "":
       password_entry.delete(0,END)
       messagebox.showinfo("Information","Password section has been cleared.")

def save_text():
    passwd = password_entry.get()
    if passwd != "":
        with open("password.txt","a+",encoding="utf-8") as password:
            text = f"Password: {passwd}\n"
            password.write(text)
            messagebox.showinfo("Information","Saved to password.txt file.")
    else:
        messagebox.showwarning("Warning!","Password section is empty.")

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
        messagebox.showinfo("Information","All Checkbox Empty!")

def call__charback(url):
    webbrowser.open_new(url)

def exit_application():
    response = messagebox.askquestion("Exit Application", "Do you want to exit the application?")
    if response == "yes":
        root.destroy()

def copy_to_clipboard(text):
    pyperclip.copy(text)

def copy_password():
    generated_password = password_entry.get()
    if generated_password:
        copy_to_clipboard(generated_password)
        messagebox.showinfo("Information", "Password copied to clipboard!")
    
    else:
        messagebox.showwarning("Password","Password section is empty.")


# Define the paths to your custom icons
icons = {
    "Very Weak": os.path.join(sys._MEIPASS, 'icons', 'baby.png'),
    "Weak": os.path.join(sys._MEIPASS, 'icons', 'child.png'),
    "Moderate": os.path.join(sys._MEIPASS, 'icons', 'young.png'),
    "Strong": os.path.join(sys._MEIPASS, 'icons', 'astronaut.png'),
    "Very Strong": os.path.join(sys._MEIPASS, 'icons', 'ironman.png'),
    "Impossible": os.path.join(sys._MEIPASS, 'icons', 'hacker.png'),
    "Unknown": os.path.join(sys._MEIPASS, 'icons', 'alien.png'),
}

policy = PasswordPolicy.from_names(
    entropybits=30,
    strength=0.66,
    length=12,  # min length: 8
    uppercase=2,  # need min. 2 uppercase letters
    numbers=2,  # need min. 2 digits
    special=2,  # need min. 2 special characters
    nonletters=2,  # need min. 2 non-letter characters (digits, specials, anything)
)

# Define the password strength levels
strength_levels = {
    0: "Very Weak",
    1: "Weak",
    2: "Moderate",
    3: "Strong",
    4: "Very Strong",
    5: "Impossible",
    "Unknown": "Unknown"  # Make sure you have an "Unknown" icon in your 'icons' dictionary
}

# Define colors for each strength level
strength_colors = {
    "Very Weak": "red",
    "Weak": "orange",
    "Moderate": "yellow",
    "Strong": "lightgreen",
    "Very Strong": "lightgreen",
    "Impossible": "lightgreen",
    "Unknown": "black",
}

# Update the icon based on password strength
def update_password_strength_label(password):
    strength_hint = password_strength_hint(password)
    password_strength_var.set(f"Password ==> {strength_hint}")
    password_strength_label.config(fg=strength_colors.get(strength_hint, "black"))
    show_icon_label(strength_hint)

def password_strength_hint(password):
    result = policy.test(password)
    
    # Calculate the strength level based on the number of failed policy checks
    strength_level = max(5 - len(result), 0)
    return strength_levels.get(strength_level, "Unknown")

def show_icon_label(strength_hint):
    # Modify this function to show the appropriate icon based on strength_hint
    icon_label.config(image=icon_images.get(strength_hint, icon_images["Unknown"]))
    icon_label.place(x=400, y=110)

# Function to toggle password visibility
def toggle_password_visibility():
    global password_visible
    password_visible = not password_visible
    
    if password_visible:
        password_entry.config(show="")
        show_password_checkbox.config(image=hide_icon)
    else:
        password_entry.config(show="*")
        show_password_checkbox.config(image=show_icon)


root = Tk()
root.geometry("550x550")
root.title("Password Generator")
root.configure(background="#6002fd")
root.resizable(width=False, height=False)

# Create a StringVar to store the password strength hint
password_strength_var = StringVar()
password_strength_var.set("")

# Create PhotoImage objects for "Show" and "Hide" icons
show_icon = PhotoImage(file=os.path.join(sys._MEIPASS, 'icons', 'show.png'))
hide_icon = PhotoImage(file=os.path.join(sys._MEIPASS, 'icons', 'hide.png'))

# Initialize a variable to track password visibility
password_visible = False

# Create a Label for showing/hiding the password
show_password_checkbox = Label(root, image=show_icon, bg="#6002fd", cursor="hand2")
show_password_checkbox.bind("<Button-1>", lambda e: toggle_password_visibility())
show_password_checkbox.place(x=485, y=65)

# Load the icons into PhotoImage objects
icon_images = {strength: PhotoImage(file=path) for strength, path in icons.items()}

# In your GUI code, you can set the initial image and update it based on password strength
icon_label = Label(root, image=icon_images["Very Weak"], fg="#f5e001", bg="#6002fd")


password_strength_label = Label(root, textvariable=password_strength_var, fg="#1ae001", bg="#6002fd")
password_strength_label.place(x=220, y=120)

unchecked_image = PhotoImage(file=os.path.join(sys._MEIPASS, 'icons', 'unchecked.png'))
checked_image = PhotoImage(file=os.path.join(sys._MEIPASS, 'icons', 'checked.png'))

numbers = "1234567890"
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "!'^+%&/()?=.,~@${*}[;]\_-₺€"
all__char_char = numbers + lower + upper + symbols


lbl1 = Label(root,text="Password Length:",fg="white",bg="#6002fd")
lbl2 = Label(root,text="Your Password:",fg="white",bg="#6002fd")
lbl3 = Label(root,text="Password Strength:",fg="white",bg="#6002fd")

entry1 = Entry(root,width=36, fg="blue", bg="white")
password_entry = Entry(root,width=36, fg="blue", bg="white", show="*")

icon = PhotoImage(file=os.path.join(sys._MEIPASS, 'icons', 'password.png'))

btn1 = Button(root,text="Generate Password\t",fg="green", width=200, image=icon, compound='left', command=generate_password)

icon2 = PhotoImage(file=os.path.join(sys._MEIPASS, 'icons', 'clear.png'))

btn2 = Button(root,text="Clear Password\t",fg="purple", width=200, image=icon2, compound='left', command=clear_password)

icon3 = PhotoImage(file=os.path.join(sys._MEIPASS, 'icons', 'text.png'))

btn3 = Button(root,text="Save 'txt' File\t",fg="blue", width=200, image=icon3, compound='left', command=save_text)

icon4 = PhotoImage(file=os.path.join(sys._MEIPASS, 'icons', 'exit.png'))

exit_button = Button(root, text="Exit Application\t", fg="red", width=200, image=icon4, compound='left', command=exit_application)

icon5 = PhotoImage(file=os.path.join(sys._MEIPASS, 'icons', 'clipboard.png'))

copy_button = Button(root, text="Copy to Clipboard\t", fg="blue", width=200, image=icon5, compound='left', command=copy_password)

lbl1.place(x=60,y=20)

entry1.place(x=190,y=20)

lbl2.place(x=60,y=70)

password_entry.place(x=190,y=70)

lbl3.place(x=60,y=120)

btn1.place(x=220,y=180)
btn2.place(x=220,y=230)
btn3.place(x=220,y=280)
copy_button.place(x=220, y=330)
exit_button.place(x=220, y=380)

image = PhotoImage(file=os.path.join(sys._MEIPASS, 'icons', 'icon48.png'))
image_label = Label(root, image=image, bg="#6002fd")
image_label.place(x=1,y=1)

image2 = PhotoImage(file=os.path.join(sys._MEIPASS, 'icons', 'icon2-48.png'))
image2_label = Label(root, image=image2, bg="#6002fd")
image2_label.place(x=1,y=50)


image3 = PhotoImage(file=os.path.join(sys._MEIPASS, 'icons', 'github64.png'))
image3_label = Label(root, image=image3, bg="#6002fd",cursor="hand2")
image3_label.bind("<Button-1>",lambda e: call__charback("https://github.com/l1qu1c1ty"))
image3_label.place(x=230,y=450)

image4 = PhotoImage(file=os.path.join(sys._MEIPASS, 'icons', 'numbers32.png'))
image4_label = Label(root, image=image4, bg="#6002fd")
image4_label.place(x=10,y=230)

image5 = PhotoImage(file=os.path.join(sys._MEIPASS, 'icons', 'alpha32.png'))
image5_label = Label(root, image=image5, bg="#6002fd")
image5_label.place(x=10,y=260)

image6 = PhotoImage(file=os.path.join(sys._MEIPASS, 'icons', 'alpha2-32.png'))
image6_label = Label(root, image=image6, bg="#6002fd")
image6_label.place(x=10,y=290)

image7 = PhotoImage(file=os.path.join(sys._MEIPASS, 'icons', 'asterisk32.png'))
image7_label = Label(root, image=image7, bg="#6002fd")
image7_label.place(x=10,y=320)

image8 = PhotoImage(file=os.path.join(sys._MEIPASS, 'icons', 'tick32.png'))
image8_label = Label(root, image=image8, bg="#6002fd")
image8_label.place(x=10,y=350)

image9 = PhotoImage(file=os.path.join(sys._MEIPASS, 'icons', 'strength.png'))
image9_label = Label(root, image=image9, bg="#6002fd")
image9_label.place(x=1 ,y=110)

root.iconbitmap(os.path.join(sys._MEIPASS, 'icons', 'icon100.ico'))

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()

check1_label = Label(root, text="Digits", fg="white", bg="#6002fd")
check1_checkbox = Label(root, image=unchecked_image, bg="#6002fd", cursor="hand2")
check1_checkbox.bind("<Button-1>", lambda e: toggle_check(var1, check1_checkbox))
check1_label.place(x=50, y=235)
check1_checkbox.place(x=110, y=230)

check2_label = Label(root, text="Lower", fg="white", bg="#6002fd")
check2_checkbox = Label(root, image=unchecked_image, bg="#6002fd", cursor="hand2")
check2_checkbox.bind("<Button-1>", lambda e: toggle_check(var2, check2_checkbox))
check2_label.place(x=50, y=265)
check2_checkbox.place(x=110, y=260)

check3_label = Label(root, text="Upper", fg="white", bg="#6002fd")
check3_checkbox = Label(root, image=unchecked_image, bg="#6002fd", cursor="hand2")
check3_checkbox.bind("<Button-1>", lambda e: toggle_check(var3, check3_checkbox))
check3_label.place(x=50, y=295)
check3_checkbox.place(x=110, y=290)

check4_label = Label(root, text="Symbols", fg="white", bg="#6002fd")
check4_checkbox = Label(root, image=unchecked_image, bg="#6002fd", cursor="hand2")
check4_checkbox.bind("<Button-1>", lambda e: toggle_check(var4, check4_checkbox))
check4_label.place(x=50, y=325)
check4_checkbox.place(x=110, y=320)

check5_label = Label(root, text="All", fg="white", bg="#6002fd")
check5_checkbox = Label(root, image=unchecked_image, bg="#6002fd", cursor="hand2")
check5_checkbox.bind("<Button-1>", lambda e: toggle_check(var5, check5_checkbox))
check5_label.place(x=50, y=355)
check5_checkbox.place(x=110, y=350)

link1 = Label(root,text="Follow Me Github",fg="white",bg="#6002fd",cursor="hand2")
link1.bind("<Button-1>",lambda e: call__charback("https://github.com/l1qu1c1ty"))
link1.place(x=200,y=520)

mainloop()