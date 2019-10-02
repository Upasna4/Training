if(5>6):
    print("5 is greater")
print("hello")

a=6
b=5
if(a>b):
    print(a,"is greater")
else:
    print(b,"is grater")

c=input("enter no")
d=input("enter no")
c=c.isnumeric()
d=d.isnumeric()
if c== True and d== True:
    print(int(c)+int(d))

m=input("enter no")
n=input("enter no")
p=m.isnumeric()
q=n.isnumeric()
if p== True and q== True:
    print(int(p)+int(q))
else:
    print("invalid input")
