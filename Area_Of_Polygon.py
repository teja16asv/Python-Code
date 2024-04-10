from abc import ABC
class polygon(ABC):
    def area():
        pass
class triangle(polygon):
    def area(self):
        b=int(input("Enter the breadth of triangle: "))
        h=int(input("Enter the height of triangle: "))
        a=int(1/2*b*h)
        print("The area of triangle is: ",a)
class square(polygon):
    def area(self):
        s=int(input("Enter the side of the square: "))
        print("The area of square is: ",s*s)
t=triangle()
t.area()
s=square()
s.area()