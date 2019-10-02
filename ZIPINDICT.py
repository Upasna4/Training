l=[1,2,3,4]
l1=[5,6,7,8]
d=dict(zip(l,l1))
print(d)

l=[1,2,3,1,4]
l1=[5,6,7,8]
d=dict(zip(l,l1))
print(d)

l=[1,2,3,4]
l1=[5,6,7,8]
for i,j in zip(l,l1):
    print(i,j)