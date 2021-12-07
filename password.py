#importing libraries
import random
import pyperclip
from tkinter import *
from tkinter.ttk import *
 
#function to calculate password requirements
def requisites():
    entry.delete(0, END)
 
    # Get the length of password
    length = Variable1.get()
 
    lowercase_letter = "abcdefghijklmnopqrstuvwxyz"
    uppercase_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    numbers_symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    password = ""
 
    # if password strength selected is low
    #password will contain only lowercase letters
    if Variable.get() == 1:
        for i in range(0, length):
            password = password + random.choice(lowercase_letter)
        return password
 
    # if password strength selected is medium
    #password will contain both lowercase and uppercase letters 
    elif Variable.get() == 0:
        for i in range(0, length):
            password = password + random.choice(uppercase_letter)
        return password
 
    # if password strength selected is strong
    #pasword will contain lowercase and uppercase letters, numbers and symbols
    elif Variable.get() == 3:
        for i in range(0, length):
            password = password + random.choice(numbers_symbols)
        return password
    else:
        print("Choose an option")
 
 
#function to generate a password
def generate_password():
    password1 = requisites()
    entry.insert(10, password1)
 
#creating a GUI window
root = Tk()
Variable = IntVar()
Variable1 = IntVar()
root.title("Password Generator")
 
# create label
Random_password = Label(root, text="Password")
Random_password.grid(row=0)
entry = Entry(root)
entry.grid(row=0, column=1)
 
# create label for length of password
c_label = Label(root, text="Length")
c_label.grid(row=1)
 
#generating a password
generate_button = Button(root, text="Generate", command=generate_password)
generate_button.grid(row=0, column=3)
 
#creating radiobuttons to decide the strength of password
radio_low = Radiobutton(root, text="Low", variable=Variable, value=1)
radio_low.grid(row=1, column=2, sticky='E')

#default setting is medium password 
radio_middle = Radiobutton(root, text="Medium", variable=Variable, value=0)
radio_middle.grid(row=1, column=3, sticky='E')
radio_strong = Radiobutton(root, text="Strong", variable=Variable, value=3)
radio_strong.grid(row=1, column=4, sticky='E')
combo = Combobox(root, textvariable=Variable1)
 
#length of password
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16,
                   17, 18, 19, 20, 21, 22, 23, 24, 25,
                   26, 27, 28, 29, 30, 31, 32, "Length")
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.grid(column=1, row=1)
 
#start program 
root.mainloop()