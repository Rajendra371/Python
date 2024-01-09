# lambda expression allow us to create anonymous function. This basically means we can quickly make ad-hoc function without needding to properly define the function using keyword 'def'
#old

# def square (num):return num**2
square=lambda num:num**2
result=square(5)
print(result)

#filter
numbers=[1,2,3,4,5,6,7,8,9,10]
check=list(filter(lambda num: num%2==0, numbers))
print(check)
