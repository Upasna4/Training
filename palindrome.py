num=123
rem=0
store=num
while num>0:
    rem=rem*10+num%10
    num=num//10
    print(rem)
if(store==rem):
        print("palindrome")
else:
        print("not palindrome")
