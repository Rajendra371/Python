#numpy-> numerical python (+, -, %, /)
import numpy

data =[[1,2,3],[4,5,6]]
d=numpy.array(data)
print(d)
print(d.shape())

#check data type of array element
print(d.dtype)
print(type(d))


#one dimensional array
x=(10,20,30,40)
x=numpy.array(x)
print(x)

#we can specify data typw of array element explicitly using dtype

data=numpy.array([1,3,5,7],dtype='int64')
print(data)

#create array of length 5 using zeros()
a=numpy.zero(5)
print(a)

a=numpy.one(5)
print(a)

b=numpy.empty((2,3))
print(b)


#arrange()
c=numpy.arrange(10)
print(c)

#indexing
print(c[2])

#slicing
print(c[1:5])


r=numpy.array([[1., 2., 3.],[4., 5., 6.,]])
print(r)


#element wise multiplication
result=r*r
print(result)

#element wise addition
result =r+r
print(result)


#Boolean indexing
a=numpy.array([1,2,3,4,5,12,13,14,15,30,40,7])
boolean_mask=a>20
print(a[boolean_mask])


#fancy Indexing
fancy_indexing=a[[1,4,5]]
print (fancy_indexing)


#unary universal function (mul,div,power addition)
a=numpy.arrange(10)
s=numpy.sqrt(a)
print(s)

#linear algebra

x=numpy.array([[1,2,3],[4,5,6]])
y=numpy.array([[6,12],[1,5],[8,9]])
#matrix mul
result=x.dot(y)

r=numpy.dot(x,y)
print(r)

#transpose
r=numpy.transpose(x)
print(r)
