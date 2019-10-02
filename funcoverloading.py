def add(*a):      #single * se tuple bnta h
    print(a)
add(1)              #funcoverloading
add(1,2)
add(1,2,3)
add(1,2,3,4)

def add(*a):
    c=0
    for i in a:
        c=c+i
    print(c)                #toaddelements
add(1,2,3,4)

 #double astrisk
def dataDict(**a):
     return a
record=dataDict(name='user',age=23)                #dictiscreated
print(record)
print(record['name'])
print(record['age'])
