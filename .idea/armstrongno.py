a=153
rem=0
check=0
store=a
while(a>0):
    rem=a%10
    check=check+rem**3
    a=a//10
if(check ==store):
    print("an armstrong number")
else:
    print("not an armstrong number")