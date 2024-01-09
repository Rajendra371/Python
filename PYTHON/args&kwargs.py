# *args ; when function parameter starts with a asterisk, it allow for an arbitrary number of argument and the function takes them in as a tuple of values


def demoFunction(*args):
    return sum(args)

result=demoFunction(10,20,30,40,50)
print(result)

# **kwargs -> it builds a dictionary of key value pair
def demo(**kwargs):
    if 'fruit' in kwargs:
        print(f'my favorite fruit is {kwargs['fruit']}')
    else:
        print('not a favorite fruit')

demo(fruit='apple')



