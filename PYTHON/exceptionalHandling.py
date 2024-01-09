#try-> test a block of code for error
#except-> let you handle the error
#else-> lets you execute code when there is no error
#finally=> lets you execute code, regardless of the result of the try except

try:
    print('Hello')
except:
    print('error')
    
    
try:
    print(xyz)
except:
    print('error occur')
    
#many exception

try:
    print(hello)
    
except NameError:
    
    print('variable hello is not declare') 
except:
    print('exception occur')
finally:
    print('code execution complete')

try:
    print(20)
    
except:
    print('error')
else:
    print('error not occur')
    
#raise exception

a=20
if a>10:
    raise Exception('number is grater than 10 is not allowed')