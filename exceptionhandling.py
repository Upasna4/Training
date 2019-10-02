try:
    a=int(input("enter no"))   #here agr try m error ni hua to whi chlega except ni chlega
    print(a)                        #aur agr try m error na hua toh except chlega
except ValueError:
    print("enter int val")
finally:
    print("this is finally block")      #finally tb chlega jb dono m error hoga