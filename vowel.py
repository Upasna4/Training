vowel=input("enter any string")
v=0
c=0
for i in vowel:

    if(i=='a' or i=='e' or i=='i' or i=='o' or i== 'u'):
        print(i)
        v=v+1
    else:
        c=c+1

print("total vowels",v)
print("total consonants",c)


