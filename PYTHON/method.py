# method are the function define inside the body of class


class Circle:
    pi = 3.14  # class variable


# automatically invoked function for object and it is invoked when an object is create from the class


def __init__(self, radius=5):
    self.radius = radius  # instance variable
    self.area = Circle.pi * radius * radius


# defining the own method
def setRadius(self, newRadius):
    self.radius = newRadius
    self.area = self.pi * newRadius * newRadius


c = Circle()
print("the area is:", c.area)


# calling the function
c.setRadius()
print("new radius is:", c.radius)
print(
    "the new area is:",
)
