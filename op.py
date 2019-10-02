import os
print(os.getcwd())           #current working dir

path=os.getcwd()    #gives current working dir
print(path)

loc=__file__
print(loc)      #to check puri location

print(os.getcwd())
os.chdir("C:\\Users\\hp\\desktop")      #to change loc of rest of the files which will be made later(first method using double backslash)
print(os.getcwd())
os.chdir("C:/Users/hp/desktop")         #second method using frontslash
print(os.getcwd())

path=os.getcwd()
os.chdir("C:/Users/hp/desktop")
print(os.getcwd())
os.chdir(path)                 #third method if we have chngd loc n we want our loc back we store our orig loc in a var then we pas that var we get orig loc
print(os.getcwd())

