from tkinter import *

root = Tk()

root.title('Calculator')
root.geometry('300x400')

output = Entry(root,width=300)
output.place(x=0.5,y=0.5)

#for displaying the numbers before the arithmatic operation
def display(input):
    current = output.get()
    output.delete(0, END)
    output.insert(0, str(current) + str(input))


def clear():
    output.delete(0, END)


def add():
    first_number = output.get()
    global first
    first = float(first_number)
    global arith
    arith = 'add'
    output.delete(0,END)


def subtract():
    first_number = output.get()
    global first
    first = float(first_number)
    global arith
    arith = 'subtract'
    output.delete(0, END)


def multiply():
    first_number = output.get()
    global first
    first = float(first_number)
    global arith
    arith = 'multiply'
    output.delete(0, END)


def divide():
    first_number = output.get()
    global first
    first = float(first_number)
    global arith
    arith = 'divide'
    output.delete(0, END)


def negate():
    number = output.get()
    opposite_sign = -(float(number))
    output.delete(0, END)
    output.insert(0,opposite_sign)


def result():
    second = float(output.get())
    if arith == 'add':
        res = first + second
    elif arith == 'subtract':
        res = first - second
    elif arith == 'multiply':
        res = first * second
    elif arith == 'divide':
        res = first / second

    output.delete(0,END)
    output.insert(0,res)


button1 = Button(root, text='1', height=4, width=8, command=lambda: display(1))
button2 = Button(root, text='2', height=4, width=8, command=lambda: display(2))
button3 = Button(root, text='3', height=4, width=8, command=lambda: display(3))

button4 = Button(root, text='4', height=4, width=8, command=lambda: display(4))
button5 = Button(root, text='5', height=4, width=8, command=lambda: display(5))
button6 = Button(root, text='6', height=4, width=8, command=lambda: display(6))

button7 = Button(root, text='7', height=4, width=8, command=lambda: display(7))
button8 = Button(root, text='8', height=4, width=8, command=lambda: display(8))
button9 = Button(root, text='9', height=4, width=8, command=lambda: display(9))

button0 = Button(root, text='0', height=4, width=8, command=lambda: display(0))
button_plus = Button(root, text='+', height=4, width=8, command=add)
button_minus = Button(root, text='-', height=4, width=8, command=subtract)
button_x = Button(root, text='x', height=4, width=8, command=multiply)
button_div = Button(root, text='/', height=4, width=8, command=divide)
button_equal = Button(root, text='=', height=4, width=19, command=result)
button_clear = Button(root, text='clear', height=4, width=19, command=clear)
button_float = Button(root, text='.', height=4, width=8, command=lambda: display('.'))
button_negate = Button(root, text='+/-', height=4, width=8, command=negate)


#grid

button7.place(x=0, y=25)
button8.place(x=75, y=25)
button9.place(x=150, y=25)
button_x.place(x=225, y=25)

button4.place(x=0, y=100)
button5.place(x=75, y=100)
button6.place(x=150, y=100)
button_minus.place(x=225, y=100)

button1.place(x=0, y=175)
button2.place(x=75, y=175)
button3.place(x=150, y=175)
button_plus.place(x=225, y=175)

button_negate.place(x=0, y=250)
button0.place(x=75, y=250)
button_float.place(x=150, y=250)
button_div.place(x=225,y=250)

button_clear.place(x=0,y=325)
button_equal.place(x=150, y=325)


root.mainloop()