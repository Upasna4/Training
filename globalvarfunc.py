x=5
def update():
    global x             #global var ko func k andr declare krege to use global
    x=x+5
    print(x)
print(x)        #initially x ki val is 5
update()        #updates value of x to 10
print(x)         #now x has val of 10