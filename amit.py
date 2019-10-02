import mysql.connector
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

con = mysql.connector.connect(host='localhost', user='root', password='amit', database='db_new1')
obj = con.cursor()

print("Hi welcome to the website")
print("1. Login ")
print("2. Sign up")
n = int(input("What would you like to do?"))
if n == 2:
     name = input("Please enter your name")
     email = input("Please enter your email id")
     pwd = input("Please enter your password")
     city = input("Please enter your city")
     isactive = 0
     otp = random.randint(10000, 100000)
     obj.execute("INSERT INTO db_new1(name,emailid,password,city,otp,isactive)values('%s','%s','%s','%s',%s,%s)"%(name,email,pwd,city,otp,isactive))
     con.commit()
     server = smtplib.SMTP("smtp.gmail.com", 587)
     server.starttls()
     server.login('amitmadaan9595@gmail.com', '8295951610')

     msg = MIMEMultipart()
     msg['From'] = 'amitmadaan9595@gmail.com'
     msg['To'] = email
     msg['Subject'] = "Sign up confirmation"
     body = "Your otp is:"+str(otp)
     msg.attach(MIMEText(body, 'plain'))
     text = msg.as_string()
     server.sendmail(msg['From'], msg['To'], text)
     server.quit()
     o = int(input("Pls enter the otp sent to your mentioned email id to confirm sign up"))
     if (o==otp):

        obj.execute("update db_new1 set isactive='2' where emailid=email")
        '''email id='madaanamit367@gmail.com'''
        con.commit()
        print("Signed up successfully")
     else:
         print("The otp did not match, pls try again")



if(n==1):
    while(True):
        email = input("Enter your email id")
        pwd = input("Enter your password")
        obj.execute("SELECT * from db_new1 where emailid='%s'"%(email))
        data = obj.fetchall()
        print(data)
        if(len(data)>0):
            if(data[0][1]==email and data[0][2]==pwd):
                    print("Login successfull")
                    print("Welcome, "+data[0][0])
                    break
        else:
            print("Data entered is incorrect, pls try again")