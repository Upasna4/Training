#a=open("myfile.txt",'x')          #create file
 # a.close()

# a=open("my.txt",'r')
# print(a.read())            #read file
# a.close()

# print(a.readline())     #shows first line only

b=open("asd.txt",'w')       #creates and writes to a file..if a file is already present it will add content to the file otherwise a file is created
value="hello world"
value1="first line"
b.write(value+'\n'+value1)
b.close()


