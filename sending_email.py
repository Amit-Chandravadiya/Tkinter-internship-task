import smtplib as s
from email.message import EmailMessage
def choose_mail(cho,email,otp=None):
    
        try:
            smtpobj=s.SMTP("smtp.gmail.com",587)
            smtpobj.starttls()
            smtpobj.login("charusat.libg8@gmail.com","Amit(G8)")
            msg = EmailMessage()
            msg['From'] = "charusat.libg8@gmail.com"
            msg['To'] = f"{email}"
            if cho == "Login":
                msg['Subject'] = "Reg. Login activity"
                msg.set_content("this is html ! ")
                msg.add_alternative("""
                <!DOCTYPE html>
                <html>
                    <body>
                        <h1>Login activity detected in your account. If it was not you then contact administrator immediately.</h1>
                    </body>
                </html>""", subtype='html')
            elif cho == "Register":
                msg['Subject'] = "Reg. Registration"
                msg.set_content("this is html ! ")
                msg.add_alternative("""
                <!DOCTYPE html>
                <html>
                    <body>
                        <h1>Registration done successfully. You can now take full benifits of our python tkinter application</h1>
                    </body>
                </html>""", subtype='html')
            elif cho == "Otp":
                msg['Subject'] = "Reg. Password Recovery"
                msg.set_content("this is html ! ")
                msg.add_alternative("""
                <!DOCTYPE html>
                <html>
                    <body>
                        <h1>One Time Password for your password recovery is : %s. Do Not Share .</h1>
                    </body>
                </html>"""%(str(otp)), subtype='html')
            elif cho == "Reset":
                msg['Subject'] = "Reg. Password Recovery"
                msg.set_content("this is html ! ")
                msg.add_alternative("""
                <!DOCTYPE html>
                <html>
                    <body>
                        <h1>Your Password has been successfully reset. You can now login with new password .</h1>
                    </body>
                </html>""", subtype='html')

            smtpobj.send_message(msg)
            smtpobj.quit()
            print("Message sent successfully !")

        except Exception as e:
            print("Error unable to send mail !")
            print("Something went wrong !",Exception)
            # print(Exception.with_traceback())

