a=16
v=True
for i in range(2,a):
    if a%i==0:
        print("not a prime number")
        value=False
        break
if value==True:
    print("it is a prime number")