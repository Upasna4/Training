import csv
f=open("C:/Users/Hp/Desktop/record1.csv",'w')
f.write("name,email,password\n")
f.write("upasna,user@gmail.com,1234\n")
f.write("user,user1@gmail.com,5678\n")
f.close()

file1=open("C:/Users/Hp/Desktop/record1.csv",'r')  #to read file
print(file1.read())
file1.close()

data=csv.reader(open("C:/Users/Hp/Desktop/record1.csv"),delimiter=",")   #gives reference
data=list(data)
print(data[0][2])                #prints password
