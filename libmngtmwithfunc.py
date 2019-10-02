memberData = {}
bookData = {}

m_id = 101
b_id = 201

def menu():
    print("Library Management System\n"
          "1.Add Member\n"
          "2.Add Book\n"
          "3.Book Borrowing\n"
          "4.Book Returning\n"
          "5.Member Status\n"
          "6.Book Status\n"
          "7.Exit")



def memberadd():
    global m_id
    name = input("Member Name: ")
    memberData.update({m_id: name})  # updates value of key and val
    print("Member Added. Member id is: ", m_id)
    m_id += 1

def addmorefunc():
    choice = input("Add more member (Y/N): ").lower().strip()
    if choice == 'y':
        memberadd()
        addmorefunc()
    elif choice == 'n':
        menu()
    else:
        print("invalid choice ")
        addmorefunc()


menu()
choice = int(input("enter choice"))
if choice == 1:
    print("Add Member Program")
    memberadd()
    addmorefunc()
elif choice ==2:


