d={}
print(type(d))

d={1:1,2:7}
print(type(d))

d=dict()
print(d)

d=dict({1:2,2:4})
print(d)

d={1:2,2:3,4:5}
d={1:'a','a':5,0.5:True}
d={'a':[1,2,3,4],2:('a','b')}

d={1:2,2:3,4:5}
print(d[1])

for i in d:
    print(i)

d={'a':[1,2,3,4],2:('a','b')}
for i in d:                  #returnskeys
    print(i)
for i in d:                 #returnsvalue
    print(d[i])
    for j in d[i]:
        print(j)           #toprinttuplelinebyline

d={}
d[1]='hello'
d[1]='bye'
print(d)                  #ifinonekeywegive2valueslast

d={}
n=int(input("enter range:"))
for i in range(n):
    key=input("key name:")
    value=input("value:")
    d[key]=value
print(d)                            #usersekeynvaluelena

#dictionaryfunctions
d={1:2,2:4,5:6,'a':7}
print(d.keys())

