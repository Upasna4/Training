l=[]
c=0
while(c<5):
    item=input("item")
    if item in l:
        print("duplicate")
    else:
        l.insert(c,item)
        c=c+1
print(l)