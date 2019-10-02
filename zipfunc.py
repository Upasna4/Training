l=[1,2,3]
l1=[4,5,6]
l3=zip(l,l1)              #withoutmemoryobjectsoitreturnsreference
print(l3)

l=[1,2,3]
l1=[4,5,6]
l3=list(zip(l,l1))
print(l3)

l1=[1,2,3]
l2=[3,5,6,7]
l3=list(zip(l1,l2))
print(l3)