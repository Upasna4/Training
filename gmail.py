email="upasna"
pswd=1234
loop1=True
while(loop1):
    id=input("input your email id")
    if(email==id):
        loop2=True
        while(loop2):
            pwd=int(input("input password"))
            if(pswd==pwd):
                print("welcome")
                loop1=False
                break
            else:
                print("invalid pswd")
                continue
    else:
     print("invalid email")

