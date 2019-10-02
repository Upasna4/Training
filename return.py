def add():
    a=5
    b=6
    c=a+b
    print(c)
add()
value=add()
print(value)        #thisgivesnullsoweusereturn

def add():
    a=5
    b=6
    c=a+b
    return c
a=add()
print(a)