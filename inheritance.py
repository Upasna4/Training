class A:
    def method_1(self):
        print("Method of class A")

class B(A):
    def method_2(self):
        print("method of class B")      #multilevel inheritance

class C(B):
    def method_3(self):
        print("method of class C")

obj=C()
obj.method_1()



class A:
    def method_1(self):
        print("method of class A")

class B:
    def method_2(self):
        print("method of class B")

class C(A,B):
    def method_3(self):
        print("method of class C")            #multiple inheritance

obj=C()
obj.method_1()



