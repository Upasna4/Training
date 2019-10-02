# class Demo:   #declaration of class
#     define="This is a demo class"     #its attr
#
# obj=Demo()           #creating object obj of class Demo
# print(obj.define)        #calling object
# class Demo:                             # declaration of class
#     define = "This is a demo class"
#
#     def show(self):      #here we use self coz this define attr is outside func n we want to use it inside func
#         print(self.define)
#
# obj=Demo()
#
# obj.show()


# class Demo:
#     def show(self):
#         name=input("enter name")
#         print(name)
#
#
# obj=Demo()
# obj.show()
#
# obj1=Demo()
# obj1.show()


# class Demo:
#     name="Attribute"
#     def show(self):
#         name="method attribute"
#         print(name)               #here this shows name=method attribute because inside func uska he parameter cal hog
#
#
# obj=Demo()
# obj.show()

#
# class Demo:
#     name="Attribute"
#     def show(self):
#         name="method attribute"
#         print(self.name)
#
#
# obj=Demo()
# obj.show()


# class Demo:
#     name="Attribute"
#     def show(self):
#         self.name="method attribute"
#         print(self.name)
#
#
# obj=Demo()
# obj.show()



# class Demo:
#     name="Attribute"
#     def show(self):
#         print(self.name)
#
#     def change(self):
#         self.name="new value"
#
# obj=Demo()
# obj.show()
# obj.change()
# obj.show()


# class Record:
#     def detail(self):
#         self.name="user"    #here we r using self because we r using this name n age in another method
#         self.age=34
#     def show(self):
#         print(self.name)
#         print(self.age)
#
# obj=Record()
# obj.detail()
# obj.show()


class Record:
    def detail(self):
        self.name="user"    #here we r using self because we r using this name n age in another method
        self.age=34
    def show_detail(self):
        print(self.name,self.age)

obj=Record()
obj.detail()    #here if we r not calling this
obj.show_detail()


# class Record:
#     def __init__(self):     #constructor made
#         print("this is a constructor")
#
#     obj=Record()



class Record:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
         print(self.name,self.age)


obj=Record("user",32)
obj.show()

obj=Record("upasna",45)
obj.show()


# class Record:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def show(self):
#         print(self.name,self.age)
#
#
# obj=Record("user",32)
# print(obj.name)
# obj.show()
#
# obj=Record("upasna",45)
# print(obj.age)
# obj.show()











