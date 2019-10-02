class A:
    def __init__(self):
        print("cons 1")

    def method_1(self):
        print("method 1")


class B(A):
    def __init__(self):
        A.__init__(self)   #class A cons called
        print("cons 2")

    def method_1(self):
        print("this is method 2")

obj=B()
obj.method_1()