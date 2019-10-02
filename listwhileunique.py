l=[]
n=int(input("enter range"))
c=0
while(c<n):
    item=input("enter item:")
    value=True
    for i in l:
        if i==item:
            value=False
            break
    if value==True:
        l.insert(c,item)
        c=c+1
    else:
        print("duplicate")
print(l)