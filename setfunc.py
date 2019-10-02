s=set()
s.add(1)
print(s)            #insertonlyoneelement

s.update({6,2,3,4,5})              #updatesset
print(s)

l=[1,2,3]
s.update(l)
print(s)

s={1,2,3,4}
s.pop()             #removesfirstelement
print(s)

s={1,2,3,4}            #removes3
s.remove(3)
print(s)

#s={1,2,3,4}
#s.remove(8)           #giveserrorwhenwepasselementwhichisnotpresent
#print(s)

s={1,2,3,4}
s.discard(8)            #doesntgiveerror
print(s)

#specialfunctions
s={1,2,3}
s1={4,5,6}
s2=s.union(s1)
print(s2)

s={1,2,3}
s1={4,5,6}
s3={7,8,9}
s2=s.union(s1.union(s2))
print(s2)

s={1,2,3}
s1={4,5,6}
s3={7,8,9}
s2=s|s1|s3
print(s2)

s={1,2,3}
s1={4,2,6}
s2=s.intersection(s1)
print(s2)


s={1,2,3}
s1={4,2,6}
s2=s&s1
print(s2)

s={1,2,3}
s1={4,2,6}
s2=s1.difference(s)
print(s2)

s={1,2,3,7}
s1={4,2,6}
s2=s-s1
print(s2)

