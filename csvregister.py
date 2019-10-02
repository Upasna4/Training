import csv

while True:
    print("1.Registration\n2.Login")

    choice = int(input("select option:"))

    if choice == 1:
        while True:
            print("User Registration Page")
            name = input("Enter name:")
            email = input("Enter email")
            password = input("Enter password")
            f = open("C:/Users/Hp/Desktop/register.csv", 'a')
            f.write("%s, %s, %s" % (name, email, password))
            f.close()
            print("user registered")
            ch = input("Registration Continue Y/N")
            if ch == 'y':
                continue
            else:
                break

    elif choice == 2:
        print("Login Page")
        email = input("enter email id")
        data = csv.reader(open("C:/Users/Hp/Desktop/register.csv"), delimiter=",")
        data = list(data)
        email_id = False
        password_id = False
        for i in data:
            if email == i[1]:
                email_id = True
                break
        if email_id == True:
            password = input("enter password")
            for j in data:
                if password == j[2]:
                    password_id = True
                    break
            if password_id == True:
                print("User successfully logged in")
            else:
                print("incorrect password")