#-------------------------------------------------------------------------------
# Name:        send_email
# Purpose:
# Author:      Kiran Chandrashekhar
# Created:     09-08-2022
#-------------------------------------------------------------------------------

import ssl
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import conf

class SendEmail:
    def __init__(self):
        self.username   = conf.gmail_username
        self.password   = conf.gmail_password
        self.host       = conf.gmail_smtp_host
        self.port       = conf.port

    #---------------------------------------------------------------
    #   Send Email to the user via Gmail
    #   Recipient Email address is a Single Email address
    #   If you want to send to multiple email address, please use "," 
    #   seperated email address
    #---------------------------------------------------------------
    def send_email(self, recipient_email_address,  email_message):

        try:           
         
            msg = MIMEMultipart()
            msg['From']     = self.username
            msg['To']       = recipient_email_address
            msg['Subject']  = "Test Email"

            msg.attach(MIMEText(email_message, 'html'))

            server = smtplib.SMTP(self.host, self.port)
            
            context = ssl.create_default_context()
            server.starttls(context=context) # Secure the connection
            server.login(self.username, self.password)   # Use your Gmail username and App password here              
            server.sendmail(self.username, recipient_email_address, msg.as_string())
      
        except Exception as e:
            print(str(e))

        finally:
            server.quit()




def main():
    email_message = '''
    <p>Hi Test user, </p>
    <p>Thi is a Test email sent via an automated process in Gmail</p>
    '''
    obj = SendEmail()
    obj.send_email('kiran.cshet@gmail.com', email_message)
    
if __name__ == '__main__':
    main()
    print("Done")
