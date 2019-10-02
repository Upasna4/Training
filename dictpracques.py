d={}
n=int(input("enter size of elements"))
for i in range(n):
    key=input("enter key")
    m = d.get(key)
    if m == None:
        val = input("enter value")
        d.update({key: val})
    else:
        print("key already exist")


