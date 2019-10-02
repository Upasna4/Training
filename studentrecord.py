import os
while True:
    path="C:\\Users\\hp\\Desktop"               #path dia folder ka
    os.chdir("C:\\Users\\hp\\Desktop\\Student Record")    #sbi fol ka yhi path rhna chahea
    name=input("enter name")
    qual=input("enter qualification")
    if os.path.isdir(name):                    #aisa fol present h ya nai
        print("folder already exists")
    else:
        os.mkdir(name)
    os.chdir("C:\\Users\\hp\\Desktop\\Student Record\\"+name)
    if os.path.isfile(name):
        print("file already exists")
    else:
        b = open(name+".txt", 'w')
        val=name
        val1=qual
        b.write("name=" +val+ '\n' "qual=" +val1)
        a = open(name+".txt", 'r')
        print(a.read())
        b.close()
        choice = input("Do u want to add more students (Y/N): ").lower().strip()
        if choice == 'y':
            continue
        elif choice == 'n':
            break
