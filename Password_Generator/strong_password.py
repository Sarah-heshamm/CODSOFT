from tkinter import *
from random import randint

root = Tk()

root.title('Strong Password Generator')
root.geometry('400x300')

message = Label(root, text='Enter the required password length', font='Arial 14')
message.pack(pady=10)

length_choice = Entry(root, width=30, font='Arial 14')
length_choice.pack(ipady=10, pady=10)


# function to generate the strong password
def strongpw():
    password.delete(0,END)
    length =int (length_choice.get())
    for i in range(length):
        password.insert(i, chr(randint(33,126)))   #characters in ASCII table


#function for copying to clipboard
def copy():
    root.clipboard_clear()
    root.clipboard_append(password.get())


# hidden entry box for the generated password to be easily copied
password = Entry(root, width=30, font='Arial 14', bg='systembuttonface', bd=0)
password.pack(ipady=10, fill=BOTH, padx=10 , pady=20)

generate_button = Button(root, text='Generate Password', command=strongpw)
generate_button.pack(side=LEFT, ipadx=5, ipady=5, padx=20)

copy_button = Button(root, text='Copy to Clipboard', command=copy)
copy_button.pack(side=RIGHT, ipadx=5, ipady=5, padx=20)

root.mainloop()
