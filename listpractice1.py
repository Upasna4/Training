x=[4,5,3,2]
x.append(6)
print(x)
x.append(7)
print(x)

ldir=dir(list)
for i in ldir:
    print(i)

s=0
for i in x:
    s=s+i
print(" = ",s)

