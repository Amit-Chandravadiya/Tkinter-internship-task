from tkinter import *
from tkinter import messagebox
from hashlib import blake2b
from Database import *
import sending_email 
import random

class Choose:
    def __init__(self, top):
        self.root = top
        self.root.title("LogIn / Registration")
        self.root.geometry("300x250")
        btn = Button(self.root,text="Login",height=2,width=8,cursor="hand",command=self.Login)
        btn.pack(pady=50)
        btn1 = Button(self.root,text="Register",height=2,width=8,cursor="hand",command=self.Registration)
        btn1.pack(pady=10)

    def Login(self):
        global instus,instlogpwd
        self.log=Toplevel()
        self.log.geometry("400x200")
        self.log.title("Login")
        lbf=LabelFrame(self.log,text="LOGIN")
        lbf.pack(fill=BOTH,expand=YES,padx=10,pady=10)

        # User 
        user=Label(lbf,text="      E-mail",font=("Arial",16))
        user.place(x=50,y=12)
        instus=Entry(lbf)
        instus.place(x=140,y=12)

        # Password
        passwd=Label(lbf,text="Password",font=("Arial",16))
        passwd.place(x=50,y=42)
        instlogpwd = Entry(lbf,show="*")
        instlogpwd.place(x=140,y=42)

        
        # Submit Button
        submitbtn=Button(lbf,text="LOGIN",cursor="hand",command=self.Validatorlog)
        submitbtn.place(x=140,y=90)


        # forget password button
        frgtbtn=Button(lbf,text="FORGOT PASSWORD",cursor="hand",command=self.forgot_pass)
        frgtbtn.place(x=140,y=120)

    def Validatorlog(self):
        if instus.get() == "" or instlogpwd.get() == "":
            messagebox.showwarning("Empty fields","All fields are necessary")
            instus.delete(0,END)
            instlogpwd.delete(0,END)
        else:
            passwd=blake2b(str(instlogpwd.get()).encode()).hexdigest()
            check=collection.find_one({"email":str(instus.get()),"password":passwd})
            if check!=None:
                sending_email.choose_mail("Login",str(instus.get()))
                self.home()
                self.log.destroy()
                
            else:
                messagebox.showwarning("Error","Invalid user or password")
                instus.delete(0,END)
                instlogpwd.delete(0,END)

    def forgot_pass(self):
        self.log.destroy()
        self.fog=Toplevel()
        self.fog.geometry("500x200")
        self.fog.title("Password Recovery")
        lbf=LabelFrame(self.fog,text="E-mail Verification")
        lbf.pack(fill=BOTH,expand=YES,padx=10,pady=10)
        user=Label(lbf,text="      E-mail",font=("Arial",16))
        user.place(x=70,y=60)
        global instfgus
        instfgus=Entry(lbf)        
        instfgus.place(x=160,y=60)
        frgtbtn=Button(lbf,text="VERIFY",cursor="hand",command=self.verify_email)
        frgtbtn.place(x=200,y=100)
        


        
                    
    def verify_email(self):
            if instfgus.get() !="":
                check=collection.find_one({"email":str(instfgus.get())})
                self.fgem=check['email']
                if check!=None:
                    global OTP
                    OTP=random.randint(1111,9999)
                    sending_email.choose_mail("Otp",self.fgem,OTP)
                    self.fog.destroy()
                    self.otp=Toplevel()
                    self.otp.geometry("500x200")
                    self.otp.title("OTP verification")
                    lbf=LabelFrame(self.otp,text="OTP-VERIFICATION")
                    lbf.pack(fill=BOTH,expand=YES,padx=10,pady=10)
                    otplbl=Label(lbf,text="Enter OTP ",font=("Arial",16))
                    otplbl.place(x=70,y=60)
                    global instotp
                    instotp=Entry(lbf)
                    instotp.place(x=160,y=60)
                    frgtbtn=Button(lbf,text="VERIFY",cursor="hand",command=self.verify_OTP)
                    frgtbtn.place(x=200,y=100)
                    print(OTP)
                else:
                    messagebox.showwarning("Invalid Email","User doesn't exist ! please do registration first.")
                    instfgus.delete (0,END)      
    def verify_OTP(self):
        if OTP == int(instotp.get()):
            print("OTP verified !")
            self.otp.destroy()
            self.reset=Toplevel()
            self.reset.geometry("340x250")
            self.reset.title("RESET")
            lbf=LabelFrame(self.reset,text="RESET-PASSWORD")
            lbf.pack(fill=BOTH,expand=YES,padx=10,pady=10)
            passwd=Label(lbf,text="Password",font=("Arial",16))
            passwd.place(x=70,y=30)
            global instfgpwd,instfgcpwd
            instfgpwd=Entry(lbf,show="*")
            instfgpwd.place(x=70,y=60)
            cpasswd=Label(lbf,text="Confirm Password",font=("Arial",16))
            cpasswd.place(x=70,y=90)
            instfgcpwd=Entry(lbf,show="*")
            instfgcpwd.place(x=70,y=120)
            submit=Button(lbf,text="RESET",cursor="hand",command=self.reset_pass)
            submit.place(x=70,y=160)
            
        else:
            messagebox.showwarning("Invalid OTP","Invalid OTP entered ! please enter correct OTP")
            instotp.delete (0,END)    
            
    def reset_pass(self):

        if instfgcpwd.get() == "" or  instfgpwd.get() == "":
            messagebox.showwarning("Error","All fields are mandetory. They cannot be left empty !")
            instfgpwd.delete(0,END)
            instfgcpwd.delete(0,END)
        elif instfgcpwd.get() == instfgpwd.get():
            newpass=blake2b(str(instfgcpwd.get()).encode()).hexdigest()
            print(newpass)
            check=collection.update_one({"email":self.fgem},{"$set": {"password":newpass}})
            print(check.raw_result)
            sending_email.choose_mail("Reset",self.fgem)
            messagebox.showinfo("INFO","Password has been succesfully reset")
            self.reset.destroy()
        else:
            messagebox.showwarning("Error","Password and Confirm password doesn't match")
            instfgpwd.delete(0,END)
            instfgcpwd.delete(0,END)




    
    def home(self):
        hom=Toplevel()
        hom.geometry("1350x800")
        hom.title("Welcome !")


    def Registration(self):
        self.new=Toplevel()
        self.new.geometry("670x300")
        self.new.title("Registration")
        lbf=LabelFrame(self.new,text="REGISTRATION")
        lbf.pack(fill=BOTH,expand=YES,padx=10,pady=10)
        global instnm,instage,instcpwd,instem,instpwd,instph

        # Name 
        name=Label(lbf,text="Name",font=("Arial",16))
        name.place(x=40,y=12)
        instnm=Entry(lbf)
        instnm.place(x=90,y=12)

        # Email
        email=Label(lbf,text="E-mail",font=("Arial",16))
        email.place(x=340,y=12)
        instem=Entry(lbf)
        instem.place(x=390,y=12)

        # Age
        age=Label(lbf,text="Age",font=("Arial",16))
        age.place(x=40,y=60)
        instage = Entry(lbf)
        instage.place(x=90,y=60)

        # Phonenumber
        phno=Label(lbf,text="Phone",font=("Arial",16))
        phno.place(x=340,y=60)
        instph=Entry(lbf)
        instph.place(x=390,y=60)
        print("Registration Done Successfully !")

        # password
        passwd=Label(lbf,text="Password",font=("Arial",16))
        passwd.place(x=40,y=108)
        instpwd = Entry(lbf,show="*")
        instpwd.place(x=40,y=138)

        # confirm password
        cnfpasswd=Label(lbf,text="Confirm Password",font=("Arial",16))
        cnfpasswd.place(x=340,y=108)
        instcpwd = Entry(lbf,show="*")
        instcpwd.place(x=340,y=138)
        
        # Submit , Reset button
        submitbtn=Button(lbf,text="REGISTER",cursor="hand",command=self.Validator)
        submitbtn.place(x=190,y=200)
        resetbtn=Button(lbf,text="RESET",cursor="hand",command=self.Reset)
        resetbtn.place(x=360,y=200)
        


    def Reset(self):
        instnm.delete(0,END)
        instph.delete(0,END)
        instage.delete(0,END)
        instem.delete(0,END)
        instpwd.delete(0,END)
        instcpwd.delete(0,END)
        print("this function has been called !")
    
    def Validator(self):
        if instnm.get() == "" or instage.get() == "" or instpwd.get() == "" or instph.get() == "" or instem.get() == "" or instcpwd.get() == "" :
            messagebox.showerror("Error","All fields are mandetory ! They cannot be empty")
        elif instpwd.get() != instcpwd.get():
            print(type(instpwd.get()))
            messagebox.showerror("Invalid Password","Password doesn't match")
            instpwd.delete(0,END)
            instcpwd.delete(0,END)
        else:
            self.Database_conn()
            if self.check==None:
                sending_email.choose_mail("Register",str(instem.get()))
                messagebox.showinfo("Reg. Registration ","Registration done successfully !")
                self.new.destroy()
                    

    def Database_conn(self):
        pa=str(instcpwd.get()).encode()
        passhashed=blake2b(pa).hexdigest()
        self.check=db.users.find_one({'email':instem.get()})
        if self.check==None:
            document={
                'name':str(instnm.get()),
                'email':str(instem.get()),
                'age':str(instage.get()),
                'phone':str(instph.get()),
                'password':passhashed
            }
            collection.insert_one(document)
            
        elif self.check!=None:
            messagebox.showinfo("Invalid Info","This user already exist !")
            self.Reset()
        


    



if __name__ == "__main__":
    root = Tk()
    C = Choose(root)
    root.mainloop()
