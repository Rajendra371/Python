from abc import ABC,abstractmethod


class Polygon(ABC):
    @abstractmethod
    def area(self):
        pass
    
    
class Triangle(Polygon):
    def __init__(self, b, h): 
        self.b=b
        self.h=h
        
    def area(self):
        return 1/2*self.b*self.h
    
    
class Rectangle(Polygon):
    def __init__(self, l, b) :
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b
        
    
x=Triangle(5,10)
print(x.area())


y=Rectangle(20,30)
print(y.area())