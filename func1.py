def prime():

    n = int(input("enter a number"))
    f=0
    for i in range(1,n):
        f = 0
        for j in range(2, i):
            if (i % j == 0):
                f = 1
                break
        if(f==0):
            print(i," ")

prime()
#print(p)