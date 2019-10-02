import csv


def main_menu():
    print("1.REGISTRATION\n 2.LOGIN")
    choice = int(input("enter choice "))
    if choice == 1:
        register()
    elif choice == 2:
        login()
    else:
        exit()


def register():
    print("user registration page")
    name = input("enter name ")
    email = input("enter email ")
    password = input("enter password ")
    f = open("C:/Users/Hp/Desktop/register1.csv", 'a')
    f.write("%s,%s,%s\n"%(name,email,password))
    f.close()
    print("user registered")
    ch = input("registration continue y/n ")
    if ch == 'y':
        register()
    elif ch == 'n':
        main_menu()
    else:
        exit()


def login():
    print("login page")
    email = input("enter email ")
    data = csv.reader(open("C:/Users/Hp/Desktop/register1.csv"), delimiter=",")
    data = list(data)
    email_id = False
    password_id = False
    for i in data:
        if email == i[1]:
            email_id = True
            break
    if email_id == True:
        password=input("enter password ")
        for j in data:
            if password == j[2]:
                password_id = True
                break
        if password_id == True:
            print("user logged in")
        else:
            print("incorrect password")


main_menu()