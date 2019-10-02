
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
msg=MIMEMultipart()      #class created
msg['From']='upasnabhat13@gmail.com'
msg['To']='upasnabhat17@gmail.com'
msg['Subject']="Multipart"
filename = "myfile.txt"
with open(filename,'r') as f:
    message=MIMEText(f.read(),_subtype="txt")
    message.add_header('Content-Disposition','Attachment',filename=filename)
    msg.attach(message)
body="heyy upasna"
msg.attach(MIMEText(body,"plain"))
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('upasnabhat13@gmail.com','upsidikhu')
text=msg.as_string()
server.sendmail('upasnabhat13@gmail.com','upasnabhat17@gmail.com',text)
server.quit()
print("email sent successfully")

