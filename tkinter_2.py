from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("800x500")
lbf=LabelFrame(root,text="Label frame")
lbf.pack(fill=BOTH,expand=YES,padx=10,pady=10)
lsbx=Listbox(lbf)
lsbx.pack(pady=15)
for i in range(0,20):
    lsbx.insert(END,i)
def delete():
    lsbx.delete(ANCHOR)
btn=Button(lbf,text="Delete",command=delete)
btn.pack()
btn1=Button(lbf,text="Select",command=lambda : print(lsbx.get(ANCHOR)))
btn1.pack()
mb=Menubutton(lbf,text="Menu")
mb.menu=Menu(mb)
mb["menu"]=mb.menu
mb.menu.add_command(label="option 1")
mb.menu.add_command(label="option 2")
mb.pack()
messagebox.showerror("error","Error")
root.mainloop()