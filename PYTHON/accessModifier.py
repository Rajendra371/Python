#access modifier 
#public
#private : double underscore (__) eg: self.__x
#protected underscore(_) eg: self._y


class AccessTest():
    def __init__(self, a, b, c):
        self.a=a
        self.__b=b
        self._c=c
        
    def display(self):
        print(self.a)
        print(self.__b)
        print(self._c)
        
x=AccessTest(4,5,6)
print(x.a)
#print(x.b)
print(x._c)
x.display()