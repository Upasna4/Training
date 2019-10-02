l=[1,2,4,5,3,2,6,1,4,7,2,9,8,10]
length=len(l)
while(length>0):
    for i in l:
        countvalue=l.count(i)
        if countvalue>1:
            indexvalue=l.index(i)
            n_indexvalue=l.index(i,indexvalue+1)
            l.pop(n_indexvalue)
            break
        length=length-1
print(l)