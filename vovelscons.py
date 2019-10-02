n="a"
n.lower()

n=input("enter string")
n=n lower()
c=0
for i in n:
    av=ord(i)
    if av>=97 and av<=122:
        if (i|='a' and i|='e' and i|='i' and i|='o' and i|='u' and i|=''):
        print(i)
        c+=1
        print("total consonants is",c)

av=input()
print(chr(av))
