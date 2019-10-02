a=123
rem=0
store=0
while a>0:
    rem=a%10
    store=store*10+rem
    a=a//10
print(store)

