#inheritance -> is to from
# new classes from the classes that have been already defined. The newly formed are called derived class and the class that are derived from are called base class. the derived class override or extends the functionalist of base class

class Animal:
    def __init__(self):
        print('animal class is created')
        
    def intro(self):
        print('Animal')
        
    def eat(self):
        print('Animals who eat')
        
        
class Dog(Animal):
    def intro(self):
        print('The animal type is dog')
        
    def speak(self):
        print('Dog bark')
        
        
obj_a=Animal()
print(obj_a)
obj_a.intro()
obj_a.eat()


obj_dog=Dog()
obj_dog.intro()
obj_dog.eat()
obj_dog.speak()

