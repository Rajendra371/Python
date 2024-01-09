# list is a collection data types used in python, it is similar to array in other programming language . it is mutable i.e 
# element inside list can be change i.e remove or add or sort element inside list are in the order and list allows duplicate values

fruits=['apple', 'banana', 'papaya', 'cherry']
print(fruits)

#count the number of element in the list
print(len(fruits))



print(fruits[1][0])

print(fruits[1:3])

#append() ->to add new element in the list


fruits.append('orange')
print(fruits)

#pop() -> to remove last element from list by default
fruits.pop()
print(fruits)

fruits.pop(1)
print(fruits)

#remove()
fruits1=['apple', 'banana', 'papaya', 'cherry']
fruits1.remove('apple')
print(fruits1)

#clear()-> this method will empties the list
fruits2=['apple', 'banana', 'papaya', 'cherry']
fruits2.clear()
print(fruits2)


#del-> this method will delete the list completely

num=[1, 2, 3, 4]
del num
#print(num)

test=list((1, 2, 3, 4, 5))
print(test)


x=list(range(10))
print(x)

y=list(range(1,10))
print(y)

z=list(range(1,20, 2))
print(z)


nums=list(range(10,101,10))
print(nums)


#sort()
fruits.sort()
print(fruits)

fruits.sort(reverse=True)
print(fruits)

#reverse()
fruits1.reverse()
print(fruits1)