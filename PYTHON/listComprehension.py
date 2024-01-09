#list comprehension allows us to build out the list using a different notation. you can think of it as essentially a one line for loop build inside of [] bracket.

#using for loop to calculate the square of number
for x in range(1,11):
    print(x**2)
    
    
#converting above program using list comprehension
numbers=[x**2 for x in range(1,11)]
print(numbers)

#even number
numbers=[x for x in range(1, 21) if  x%2==0]
print(numbers)

#converting c int f
c=[10,20,30,40,50,60,70,80,90,100]
f=[((9/5)*temp+32) for temp in c]
print(f)

#map
def squareFunc(num):
    return num**2
    
numbers=[2,4,6,8,10]
result= list(map(squareFunc,numbers))
print(result)


def filterFunc(num):
    return num%2==0

numbers=[1,2,3,4,5,6,7,8,9]
result=list(filter(filterFunc, numbers))
print(result)