from tkinter import *
from tkinter import messagebox
import tkinter
top=Tk()
top.title("New Application")
top.geometry("350x200")
frm=LabelFrame(top,text="Login Form",padx=10,pady=10)
name=Label(frm,text="UserName")
name.place(x=18,y=20)
entername=Entry(frm)
entername.place(x=90,y=20)
name=Label(frm,text="Password")
name.place(x=20,y=50)
enterpass=Entry(frm,show="*")
enterpass.place(x=90,y=50)
def log_details():
    v1=str(enterpass.get())
    v2=str(entername.get())
    print(v1)
    print(v2)
    messagebox.showinfo(message="Login Successfull !")
    entername.delete(0,v2.__len__())
    enterpass.delete(0,v1.__len__())
btn=Button(frm,text="Login",command=log_details)
btn.place(x=90,y=80)
top.resizable(False,False)
frm.pack(fill=BOTH,expand=YES,padx=15,pady=15)
top.mainloop()