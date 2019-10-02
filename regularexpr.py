import re
# data = "DS PYTHON TRAINER DS"
# find = "DS"
# result = re.match(r'DS','DS A PYTHON TRAINER DS')
# print(result)
# print(result.group())
# print(result.pos)
# print(result.start(),result.end())

# result = re.search(r'python','the python is best language,python is easy to understand.')
# print(result)
# print(result.group()) #jo pattern search kia
# print(result.pos)          #pattern will be at 0 index
# print(result.start(),result.end())       #starting and end pos..4 pe p mila aur 9 pe n mila..we write n+1


#result = re.findall(r'python','the python is best language,python is easy to understand.')
#print(result)
# print(result.group())
# print(result.pos)
# print(result.start(),result.end())

# result = re.split(r' ','Hello World,This is a split method')
# print(result)
# result[0] = "upasna"
# print(result


#result = re.sub(r'python', 'java','python is a python python powerful language')
#print(result)        #finds and replaces


pattern = re.compile('expression')
result = pattern.search('this is a regular expression')
print(result)                   #isme hum ek expr ko ek var pattern m dalege phr us var ko pas krege
print(result.group())
print(result.pos)
print(result.start(),result.end())



