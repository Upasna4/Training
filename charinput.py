ch=input("enter any character")
if (ch<='9' and ch>='0'):
    print("number")
elif(ch<='z' and ch>='a'):
    if(ch=='a' or ch=='e' or ch=='i' or ch=='u' or ch == 'o'):
        print("Vowel")
    else:
        print("consonant")
elif(ch<='Z' and ch>='A'):
    print("Capital Alpha")
    if (ch == 'A' or ch == 'E' or ch == 'I' or ch == 'U' or ch =='O'):
        print("vowel")
    else:
        print("consonant")
else:
    print("Symbol")