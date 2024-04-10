class A:
    def display(self):
        print("A")
class B(A):
    def display1(self):
        print("B")
a=A()
b=B()
a.display()
b.display()
b.display1()