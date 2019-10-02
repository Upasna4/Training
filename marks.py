phy=int(input("enter marks of phy"))
chem=int(input("enter marks of chem"))
maths=int(input("enter marks of maths"))
bio=int(input("enter marks of bio"))
eng=int(input("enter marks of eng"))
sum=phy+chem+maths+bio+eng
percent=sum/500*100
print("total marks=",sum)
print("percentage is=",percent)
if(percent>=80):
    print("A")
elif (percent>=60):
    print("B")
elif (percent>=40):
    print("C")
else:
    print("Fail")
    

