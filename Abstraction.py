from abc import ABC
class polygon(ABC):
    def sides():
        pass
class triangle(polygon):
    def sides(self):
        print("It has three sides")
class square(polygon):
    def sides(self):
        print("It has four sides")
class pentagon(polygon):
    def sides(self):
        print("It has five sides")
t=triangle()
t.sides()
s=square()
s.sides()