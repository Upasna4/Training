class A:
    def method_1(self):
        print("this is method 1")


class B(A):
    def method_1(self):
        super().method_1()
        print("this is method 2")

obj=B()
obj.method_1()