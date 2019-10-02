a=input("enter no")
b=input("enter no")
if a.isnumeric() is True and b.isnumeric() is True:
    print(int(a)+int(b))
else:
    print("invalid val")