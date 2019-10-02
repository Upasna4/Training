l=[]
l.append(5)
print(l)
l.append(3)
print(l)

l=[1,2,3]
l1=[4,5]
l1.append(l)
print(l1)

l2=[4,5,[1,2,3]]
print(l2[2])

print(l2[2][1])

l=[1,2,3]
l2=[4,5,6]
l.extend(l)

l=[1,2,3]
l.pop()
print(l)

l=[1,2,3]
l.pop(1)
print(l)

l=[1,2,3,'A','B','D',True]
l.remove('A')
print(l)

l=[1,2,3]
a=l.pop()
print(a)

l=[1,2,3,1,4,2,3,5,6,1,2,1]
v=l.count(1)
print(v)

l=[1,2,3,1,4,2,3,5,6,1,2,1]
v=l.index(2)
print(v)

l=[1,2,3,1,4,2,3,5,6,1,2,1]
a=l.index(2,2)
print(a)
b=l.index(2,2)
print(b)
c=l.index(2,2,2)
print(c)


