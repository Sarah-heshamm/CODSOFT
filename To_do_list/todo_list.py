from tkinter import *
from tkinter import filedialog
import pickle

root = Tk()

root.title('To do list')
root.geometry('500x500')

listbox_frame = Frame(root)
listbox_frame.pack()

program_header = Label(listbox_frame, text='My To-do List',
                       font=('Rage Italic', 24, 'bold'), fg='#470505')
program_header.pack(ipadx=30)

todo_list=Listbox(listbox_frame,
                  height=8,width=30,
                  font=('Rage Italic', 20),
                  bd=0, bg='#f2d7c4', fg='#470505',
                  highlightthickness=0, selectbackground='#992626', activestyle='none')
todo_list.pack(ipadx=30,pady=20,side=LEFT,fill=BOTH)

list_scrollbar=Scrollbar(listbox_frame)
list_scrollbar.pack(side=RIGHT, fill=BOTH)

todo_list.config(yscrollcommand=list_scrollbar.set)
list_scrollbar.config(command=todo_list.yview)

todo_input=Entry(root,width=45)
todo_input.pack(ipadx=20,ipady=10,padx=5)


def add_to_list():
    new_task=todo_input.get()
    todo_list.insert(END,new_task)
    todo_input.delete(0,END)


def remove_from_list():
    todo_list.delete(ANCHOR)


def cross_from_list():
    todo_list.itemconfig(todo_list.curselection(),fg='#e8c3c3') #crossing out the selected task
    #for removing selection bar
    todo_list.selection_clear(0,END)


def uncross_from_list():
    todo_list.itemconfig(todo_list.curselection(), fg='#470505')
    #for removing selection bar
    todo_list.selection_clear(0,END)


def delete_crossed_items():
    count=0
    while count < todo_list.size():
        if todo_list.itemcget(count,'fg') == '#e8c3c3':
            todo_list.delete(todo_list.index(count))
        else:
            count+=1

#our buttons
button_frame=Frame(root)
button_frame.pack()

add_task=Button(button_frame,text='Add task',command=add_to_list)
add_task.grid(row=0,column=0,padx=5,ipady=5,pady=10)

remove_task=Button(button_frame,text='Remove Task',command=remove_from_list)
remove_task.grid(row=0,column=1,ipady=5)

cross_off_task=Button(button_frame, text='Task Done', command=cross_from_list)
cross_off_task.grid(row=0, column=2, padx=5, ipady=5)

uncross_task=Button(button_frame,text='Uncross Task',command=uncross_from_list)
uncross_task.grid(row=0,column=3,ipady=5)

delete_crossed=Button(button_frame,text='Remove Finished Tasks',command=delete_crossed_items)
delete_crossed.grid(row=0,column=4,padx=5,ipady=5)


def save_command():
    file_name=filedialog.asksaveasfilename(title='Save List' ,initialdir='C:\\Users\\sarah\\PycharmProjects\\To_do_list',
                                           filetypes=(('Dat Files','*.dat'),('All files', '*.*'))
                                           )
    if file_name.endswith('.dat'):
        pass
    else:
        file_name=f'{file_name}.dat'

    #remove crossed off tasks before saving list
    delete_crossed_items()

    #grab all tasks from list
    tasks=todo_list.get(0,END)

    #open the file
    output_file=open(file_name,'wb')
    #load the lists into the file
    pickle.dump(tasks,output_file)



def open_command():
    file_name=filedialog.askopenfilename(title='Save List',initialdir='C:\\Users\\sarah\\PycharmProjects\\To_do_list',
                                           filetypes =(('Dat Files','*.dat'),('All files', '*.*')))

    #clear list first
    clear_command()

    #open file
    input_file=open(file_name,'rb')

    #load the saved list
    tasks=pickle.load(input_file)

    #display the saved todolist
    for item in tasks:
        todo_list.insert(END,item)




def clear_command():
    todo_list.delete(0,END)


#add menu
my_menu=Menu(root)
root.config(menu=my_menu)

#creating and cascading file menu
file_menu=Menu(my_menu, tearoff=False)
my_menu.add_cascade(menu=file_menu, label='File')

#adding save and open commands
file_menu.add_command(label='Save List', command=save_command)
file_menu.add_command(label='Open List', command=open_command)
file_menu.add_separator()
file_menu.add_command(label='Clear List', command=clear_command)
file_menu.add_separator()
file_menu.add_command(label='Exit',command=exit)



root.mainloop()