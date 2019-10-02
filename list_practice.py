ldir=dir(list)
for i in ldir:
    print(i)

x=[3,5,4,6]

x.remove(4)
print(x)

x.reverse()
print(x)

b=["abc","def","ghi"]
for i in b:
    for j in i:
        print(j)

x.append('7')
print(x)

# x.clear()
# print(x)

x.extend("upasna")
print(x)

#y=x.extend("upasna")
#print(y)

z=x.pop(2)
print("pop =",x)
print(z)

x.remove(6)
print("removed ",x)

#m=x.remove('6')
#print(m)

x.reverse()
print(x)

r=[6,9,4,2,7]
r.sort()
print(r)