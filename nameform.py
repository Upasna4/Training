d={}
size=int(input("enter no of records"))
while size>0:
    name = input("enter name")
    m = d.get(name)
    if m == None:
        age=int(input("enter age"))
        city=input("enter city")
        d.update({name:{'age':age,'city':city}})
        size-=1
    else:
        print("key already exists")
for name in d:
    print(name)                     #nameprints
    for key,value in d[name].items():
        print("\t",key,"--",value)


