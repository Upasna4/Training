list=[]
n=int(input("size of list"))
for i in range(n):
    item=input("enter item")
    if len(list)==0:
        list.insert(i,item)
    else:
        for j in list:
            if j==item:
                print("duplicate")
                break
            else:
                list.insert(i,item)
                break
print(list)