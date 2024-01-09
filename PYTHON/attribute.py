#attribute-> characteristics or properties of an object

#define class

class Employee:
    def __init__(self, full_name, age, address):
        #defining the attribute
        self.name=full_name
        self.age=age
        self.address=address
        

#instances of class ot it is known as object
obj_emp=Employee(full_name='jon smith', age=23, address='kathmandu')


#to access the attribute from the class do like this
print(obj_emp.name)
print(obj_emp.age)
print(obj_emp.address)



class Car:
    def __ini__(self, brand_name, model, color):
        self.brand=brand_name
        self.model=model
        self.color=color

          
        
obj_ve=Car(brand_name='BMW', model=2024, color='white')
print(obj_ve.brand)
print(obj_ve.model)
print(obj_ve.color)
