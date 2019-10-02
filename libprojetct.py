memberData = dict()
bookData = dict()
m_id = 101
b_id = 201


def repeat():
    choice = input("Continue Y/N: ")
    if choice == 'y':
        return True
    elif choice == 'n':
        main_menu()


def main_menu():
    print("Library Management System\n"
          "1. Add Member\n"
          "2. Add Book\n"
          "3. Book Borrowing\n"
          "4. Book Returning\n"
          "5. Member Status\n"
          "6.  Book Status\n"
          "7. Exit")
    choice = int(input("Enter Choice: "))
    if choice == 1:
        member_store()
    elif choice == 2:
        book_store()
    elif choice == 3:
        book_borrowing()
    elif choice == 4:
        book_returning()
    elif choice ==5:
        member_status()
    elif choice ==6:
        book_status()
    elif choice == 7:
        return


def member_store():
    global m_id, memberData
    name = input("Member Name: ")
    memberData.update({m_id: [name, []]})
    m_id += 1
    check = repeat()
    if check is True:
        member_store()


def book_store():
    global bookData, b_id
    name = input("Book Name: ")
    qty = int(input("Book Quantity: "))
    bookData.update({b_id: [name, qty]})
    b_id += 1
    check = repeat()
    if check is True:
        book_store()


def book_borrowing():
    global memberData, bookData
    m_id = int(input("Member Id: "))
    if m_id in memberData:
        name = input("Book Name: ")
        for b_id, b_name_qty in bookData.items():
            if b_name_qty[0] == name:
                if b_name_qty[1] > 0:
                    memberData[m_id][1].append(b_name_qty[0])
                    bookData[b_id][1] -= 1
                    print(memberData)
                    print(bookData)
                    break
                else:
                    print("Book Out of Stock")
                    check = repeat()
                    if check is True:
                        book_borrowing()
        else:
            print("Book Not Present")
            check = repeat()
            if check is True:
                book_borrowing()
        check = repeat()
        if check is True:
            book_borrowing()
    else:
        print("Member Not Valid")
        check = repeat()
        if check is True:
            book_borrowing()


def book_returning():
    global memberData, bookData
    m_id = int(input("Member Id: "))
    if m_id in memberData:
        if len(memberData[m_id][1]) > 0:
            name = input("Book Name: ")
            if name in memberData[m_id][1]:
                    for b_id, b_name_qty in bookData.items():
                        if b_name_qty[0] == name:
                            bookData[b_id][1] += 1
                            memberData[m_id][1].remove(name)
                            print(memberData)
                            print(bookData)
                        break
            else:
                print("book not borrowing")
                check = repeat()
                if check is True:
                    book_returning()
        else:
            print("Book not borrowing")
            check = repeat()
            if check is True:
                book_returning()
    else:
        print("Member Not Valid")
        check = repeat()
        if check is True:
            book_borrowing()
    check = repeat()
    if check is True:
        book_borrowing()


def member_status():
    global memberData
    m_id = int(input("Member Id: "))
    if m_id in memberData:
            print("Member Name: ", memberData[m_id][0])
            print("Allowed Book Name: ", memberData[m_id][1])
            check = repeat()
            if check is True:
                member_status()


def book_status():
    global bookData,memberData
    b_id = int(input("Book Id: "))
    if b_id in bookData:
        print("Book name:", bookData[b_id][0])
        print("Books left is:",bookData[b_id][1])
        for m_id,m_name in memberData.items():           #here we use for loop coz ek user k pas ek se zada books hosakte h
                print("Member id:", memberData[m_id][0])   #for k sath ek parameter pass nhi krna qki ek param tuple return krta h
                check = repeat()
                if check is True:
                    book_status()


main_menu()