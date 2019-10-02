d={1:2,2:4,5:6,'a':7}
print(d.items())
for i in d.items():    #returnsinformoftuple
    print(i)

d={1:2,2:4,5:6,'a':7}
print(d.items())
for i,j in d.items():
    print(i,j)      #doesnotintuple

d={}
d.update({1:2,2:4,3:6})
print(d)               #updateswhenempty

d={1:0,2:3,4:2}
d.update({1:2,2:4,3:6})
print(d)

d={'1':2,'2':4}
d.update({1:5})
print(d.get(2))       #to check whether this key is present or not

d={'1':2,'2':4}
n=input("key")
n1=input("value")
n2=d.get(n)                                     #user se input lekr check krna ki ke y hai ya nahi
if n2==None:
    d.update({n:n1})
else:
    print("key already exists")

d={1:0,2:3,5:7,8:5}
d.popitem()                     #removeslastelement
print(d)

d={1:0,2:3,5:6,7:4}
d.pop(2)                      #giveindextoremovekeandvalue
print(d)