print"Hello World"


#multipld line comments
"""
This is a comment
written in 
more than just one line
"""
print("Hello, World!")

#variables
x = 1
y = 2

if x > y:
	print ("x greater than y")
else:
	print "y greater than x"

#else if
z = 3
if (x > y and x > z):
	print "X is greater than all"
elif (y > x and y > z):
	print "y greater than all"
else:
	print "Z greater than all"


# functions
def fun(x):
	print "value of x = "+str(x) #castung convert int to string

fun(x)

#loops


#while loop
i = 1
while i < 6 :
	#i = i + 1
	i += 1
print "Changed value of i = "+ str(i)

#break in while
i = 1
while i < 6 :
	i += 1
	if i == 3 :
		break

print "Changed value of i = "+ str(i)


# continue in while
i = 1
j = 1
while i < 6 :
	i += 1
 	if i == 3 :
 		continue
 	j += 1

print "Changed value of j = "+ str(j)

# else in while
i = 1
while i > 6 :
 	i += 1
else:
 	print "not even execute one time while loop"

print "Changed value of i = "+ str(i)


# for loops
fruits = ["apple", "banana", "cherry"]
for x in fruits :
  print(x)

 # break in for loop
for x in fruits :
 	if x == 'banana' :
 		break
 	print x
#continue in for loop
for x in fruits :
	if x == 'banana' :
		continue
	print x