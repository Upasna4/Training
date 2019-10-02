memberdict={}
bookdict={}
borrowdict={}
m_id=1
b_id=11
print("1.add member\n""2.add book\n""3.book borrowing\n""4.book returning\n""5.member status\n""6.book status\n""7.exit")
while True:
    choice=int(input("enter choice"))
    if choice==1:
        print("member adding program")
        loop1=True
        while(loop1):
            m_name=(input("enter member name"))
            memberdict.update({m_id:m_name})
            print("member id is",m_id)
            m_id+=1
            while(True):
                ch=input("add more member  y/n")
                if ch =='y':
                    continue
                elif choice == 'n':
                    loop1=False
                    break
                else:
                    print("invalid choice")
                    loop1=False
                    continue



