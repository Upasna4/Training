#data types
x = "hello" #str i,e string
x1 = 20 #init i,e int
x2 = 2.3 #float i,e float , decimal
x3 = 1j #complex ,i,e complex
x4 = ["1","2","5"] #list i,e array js
x5 = ("1","2","3") # tuple i,e array php
x6 = range(6) # range
x7 = {"name" : "John", "age" : 36} # dict i,e json
x8 = {"apple", "banana", "cherry"} # set
x9 = frozenset({"apple", "banana", "cherry"}) # frozenset
x10 = True # False # bool i,e boolen but in capital
x11 = b"Hello" # byte
x12 = bytearray(5)
x13 = memoryview(bytes(5))
print x
print type(x11)
print x13
print x12
#random
import random

print(random.randrange(1,930330))

#casting
a = 1
print(type(a))
a = float(a)
print type(a)
a = complex(a)
print type(a)


a = "Hello World!"
print a[0]
#slicing
print(a[2:5])

#negative 
print(a[-8:-1])
#string length
print(len(a))
#strip
a = "Hello World I am with space "
print (a.strip())
#lower
print a.lower()
#upper case
print a.upper()
#replace
print a.replace("I", "U") #same as java script
#spilt
a = "Hello, World!"
print(a.split(","))
#check string
print "He" in a

#check string not in
print "He" not in a
#string cancatinate
a = "Hello"
b = "World"
print a + " " + b
#format
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#bool
print bool("abc")
print bool(123)
print bool(["apple", "cherry", "banana"])

# bit wise operator
x = 5 #101
y = 3 #011

#OR
print(x | y) #111
#AND
print(x & y) #001
#XOR
print (x ^ y) #110
#NOT
print(~x) #
#left shift
print(x<<1) #1010
#right shift
print (x >> 1) #10









