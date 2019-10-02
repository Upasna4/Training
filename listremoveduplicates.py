l=[1,2,3,1,4,2,3,5,6,1,2]
for i in l:
    countvalue=l.count(i)
    if countvalue>1:
        indexvalue=l.index(i)
        l.pop(indexvalue)
print(l)