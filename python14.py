k=0
for i in range(0,4):
    for j in range(i,4):
        print(end=" ")
    d=k
    k=d+i
    for j in range(0,i+1):
        print(k,end="")
        k-=1
    k=d+i+1
    print()