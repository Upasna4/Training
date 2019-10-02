
t=()
t=tuple()

t=(1)
print(type(t))

t=(1,2)
print(type(t))

l=[1,2,3,4,5]
t=tuple(l)
print(t)

l=[1,2,3,4,5,1,7,8,9,10]
t=tuple(l[2:7])
print(t)

l=[1,2,3,4,5,1,7,8,9,10]
l2=l[2:7]                #slicingoperator
t=tuple(l2)
print(t)

l=tuple(l)
print(l)
print(type(l))

t=list(t)
print(t)

a=5
print(a)
del a

t=(1,2,3,4)
print(t)
a,b,c,d=t
print(a)
print(b)
print(c)
print(d)

l=[1,2,3,4,5,6,7,8,9,10]
a1,a2,a3=l[4:7]

