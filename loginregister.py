import os
path="C:\\Users\\hp\\Desktop"
os.chdir("C:\\Users\\hp\\Desktop\\loginreg")
name=input("enter name")
email=input("enter email")
password=input("enter password")
if os.path.isdir("emails"):
    print("folder already exists")
else:
    os.mkdir("emails")
    os.chdir("C:\\Users\\hp\\Desktop\\loginreg\\emails")
    if os.path.isdir(email):
        print("folder already exists")
    else:
        os.mkdir(email)
        os.chdir("C:\\Users\\hp\\Desktop\\loginreg\\emails\\"+email)
        if os.path.isfile(name):
            print("file already exists")
        else:
            b = open(name + ".txt", 'w')
            val = name
            val1 = email
            val2 = password
            b.write("name="+val + '\n'"email="+ val1 + '\n'"password=" +val2)
            a = open(name + ".txt", 'r')
            print(a.read())
            b.close()


