z=[[1,2,3],[4,5,6]]
m = [[2,7,5],[8,4,5]]
s=[]
r=len(z)
c=len(z[0])
for i in range(0,r):
    x=[]
    for j in range(0,c):
        x.append(z[i][j]+m[i][j])
    s.append(x)


for i in s:
    for j in i:
        print(j,end=" ")
    print()
'''print()
s=z+m
print(" = ",s)
for i in z:
    for i in m:
        print(" = ",s)
   '''



