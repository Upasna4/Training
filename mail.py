import smtplib
server=smtplib.SMTP("smtp.gmail.com",587)
#print(server)             #server se connectivity hogye hai
server.starttls()          #start transfer layer security for sending email
server.login('upasnabhat13@gmail.com','upsidikhu')
server.sendmail('upasnabhat13@gmail.com','upasnabhat17@gmail.com','hey there')
print("email sent successfully")