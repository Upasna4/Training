loop1=True
while(loop1):
    n=int(input("enter number"))
    for i in range(1,11):
        print(n*i)
    c=0
    loop2=True
    while(False):
        ch=input("continue yes or no")
        if ch=='y':
            break
        elif ch=='n':
            exit("thank u")
        else:
            print("invalid character")
            c=c+1
            if c==3:
                exit("crossed limit")