num1=int(input("input a no"))
num2=int(input("input a no"))
num3=int(input("input a no"))
num4=int(input("input a no"))
if(num1>num2) and (num1>num3) and (num1>num4):
    print(num1)
elif(num2>num3) and (num2>num4):
    print(num2)
elif(num3>num4):
    print(num3)
else:
    print(num4)