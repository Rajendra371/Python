# tuple -> similar to list but immutable i.e element inside tuple cannot be changed and value are in the order and allows duplicate values

t=("apple", "mango","banana", "cherry","watermelon", "mango", "orange")
print(t)


print(len(t))

#print(t[1])

#print(t[-1, -2])

#count
print(t.count("orange"))
print(t.count("mango"))

#index()

print(t.index("cherry"))
print(t.index("mango"))

x=list(t)
print(x)


#nested list

list=[10,20,30,40,50]
list2=[5,10,15,20,25]
matrix=[list,list2]
print(matrix)

print(matrix[0][2])



