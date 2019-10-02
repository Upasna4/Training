memberData = {}
bookData = {}
borrowData = {}
m_id = 101
b_id = 201
print("Library Management System\n"
          "1.Add Member\n"
          "2.Add Book\n"
          "3.Book Borrowing\n"
          "4.Book Returning\n"
          "5.Member Status\n"
          "6.Book Status\n"
          "7.Exit")
while True:
    choice = int(input("Enter Choice: "))
    if choice == 1:
        print("Add Member Program")
        loop1=True
        while(loop1):
            name = input("Member Name: ")
            memberData.update({m_id: name})           #updates value of key and val
            print("Member Added. Member id is: ", m_id)
            m_id += 1                  #incrementing value of m_id
            while (True):
                choice = input("Add more member (Y/N): ").lower().strip()
                if choice == 'y':
                    break
                elif choice == 'n':
                    loop1 = False
                    break
                else:
                    print("invalid choice")
                    loop1=False
                    continue
    elif choice == 2:
        print("Add Book Program")
        while True:
            name = input("Book Name: ")
            qty = int(input("enter quantity"))
            bookData.update({b_id: [name, qty]})           #dict ko update krna
            print("Book Added. Book id is: ", b_id)
            b_id += 1
            choice = input("Add more member (Y/N): ").lower().strip()
            if choice == 'y':
                continue
            elif choice == 'n':
                break
    elif choice == 3:
            print("Book Borrowing Program")
            while True:
                m_id = int(input("Member id: "))
                if m_id in memberData:                                       #checks if member id in present in memberData dict
                    b_name = input("Book Name: ")
                    for b_id, b_name_qty in bookData.items():     #when we want both key and value
                        if b_name_qty[0] == b_name:      #indexing is done coz we have a list here..at [0] we have name in list
                            if b_name_qty[1] > 0:         #here we compare quantity as it is on 1st index..we see whether it is >0 or not
                                borrowData.update({m_id: b_id})         #update dict
                                bookData[b_id][1] -= 1          #decrement quantity of books
                                break
                            else:
                                print("Book out of stock")
                        else:
                            print("Book not present")
                choice = input("Add more member (Y/N): ").lower().strip()
                if choice == 'y':
                    continue
                elif choice == 'n':
                    break
    elif choice == 4:
            print("Book Returning Program")
            m_id = int(input("Member Id: "))
            name = input("Book Name: ")
            for b_id, b_name in borrowData.items():
                if b_name == name:
                    bookData[b_id][1] += 1
                    borrowData.pop(m_id)       #person is returning book so book will pop from borrowData dict
                    borrowData.update({m_id: b_id})       #dict is updated
                    break
                else:
                    print("Book not present")

            choice = input("Add more member (Y/N): ").lower().strip()
            if choice == 'y':
                continue
            elif choice == 'n':
                break
    elif choice == 5:
            print("Member Status Program")
            m_id = int(input("Member Id: "))
            if m_id in memberData:         #to check mem status we check m_id is in memberData and borrowData or not
                if m_id in borrowData:        #if b_id is in borrowData then borrowData m se b_id nikalo
                    b_id = borrowData[m_id]                   #bid nikal ra h dict m se
                    print("Member Name: ", memberData[m_id])             #the value of this key is name
                    print("Allow Book Name: ", bookData[b_id][0])        #the val of this is bookname
    elif choice == 6:
            print("Book Status Program")
            b_id = int(input("Book Id: "))
            for m_id, m_name in memberData.items():   #valuefetch
                if b_id in borrowData:
                    b_id = borrowData[m_id]
                    print("Member name:",memberData[m_id])
                    print("Book name:",bookData[b_id][0])
                    print("Book issue to user:", memberData[m_id])

    elif choice == 7:
        break
    else:
        print("invalid choice")