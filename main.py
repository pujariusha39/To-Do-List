import tkinter
from tkinter import*
def newTask():
    task=my_entry.get()
    if task!="":
        list_box.insert(END,task)
        my_entry.delete(0,"end")
def deleteTask():
    list_box.delete(ANCHOR)

# create main window
root=Tk()
root.title("to-do-list")
root.geometry("400x350+500+200")
root.config(bg="#223441")
root.resizable(False,False)
#create widgets(frame,listbox,scrollbar,button)
frame=Frame(root)
frame.pack(pady=12)

list_box=Listbox(frame,width=35,height=10,font=("Times",10),bd=0,fg="black")
list_box.pack(side=LEFT,fill=BOTH)

task_list=["ushasri,eat an apple "]
for item in task_list :
    list_box.insert(END,item)
sb=Scrollbar(frame)
sb.pack(side=RIGHT,fill=BOTH)
list_box.config(yscrollcommand=sb.set)
sb.config(command=list_box.yview)
#my entry list
my_entry=Entry(root,font= ("times",16))
my_entry.pack(pady=18)
#space
bt_frame=Frame(root)
bt_frame.pack(pady=20)
#add button
bt=tkinter.Button(root,text="Add Task",font=("times",16),bg="#c5f776",padx=20,pady=10,command=newTask)
bt.pack(fill=BOTH,expand=True,side=LEFT)
#delete button
del_bt=tkinter.Button(root,text="Delete Task",font=("times",16),bg="#ff8b61",padx=20,pady=10,command=deleteTask)
del_bt.pack(fill=BOTH,expand=True,side=LEFT)


root.mainloop()