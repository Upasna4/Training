n=int(input("enter a number"))
f=0
for i in range(2,n):
    if (n%i==0):
        print("composite number")
        f=1
        break
if(f==0):
    print("prime")