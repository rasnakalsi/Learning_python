import tkinter as tk 
from tkinter import messagebox

def eval_compute():
    global default
    print("Inside eval_compute")
    arg1=str1.get()
    arg2=str2.get()
    if arg1.isdigit()==False:
        entry_1.focus_set()
        return
    elif arg2.isdigit==False:
        entry_2.focus_set()
        return
    
    arg1=int(arg1)
    arg2=int(arg2)

    result=0.0
    print(arg1,arg2)
    if radio_var.get() =="+":
        result=arg1+arg2
        print(result)
    elif radio_var.get()=="-":
        result=arg1-arg2
    elif radio_var.get()=="*":
        result=arg1*arg2
    else:
        result=arg1/arg2
    messagebox.showinfo("Result!!",str1.get()+radio_var.get()+str2.get()+" is "+str(result))    
    str1.set(default)
    str2.set(default)
    #focus_set  ##command to set the focus
window=tk.Tk()
window.title("Calculator")

button=tk.Button(window,text="Evaluate",command=eval_compute)

radio_var=tk.StringVar()
radio_1=tk.Radiobutton(window,text="+",variable=radio_var,value="+")
radio_2=tk.Radiobutton(window,text="-",variable=radio_var,value="-")
radio_3=tk.Radiobutton(window,text="*",variable=radio_var,value="*")
radio_4=tk.Radiobutton(window,text="/",variable=radio_var,value="/")
radio_1.select() ##Checks the radio button

default="Enter integer value"

str1=tk.StringVar()
str1.set(default)

entry_1=tk.Entry(window,textvariable=str1)
#entry_1.bind("<Key>",lambda ev: str1.set(""))

str2=tk.StringVar()
str2.set(default)
entry_2=tk.Entry(window,textvariable=str2)

entry_1.grid(column=0,row=2)
radio_1.grid(row=0,column=1)
radio_2.grid(row=1,column=1)
radio_3.grid(row=2,column=1)
radio_4.grid(row=3,column=1)
button.grid(row=5,column=1)
entry_2.grid(column=2,row=2)

window.mainloop()