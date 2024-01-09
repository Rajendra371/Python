#set-> un-order collection of unique items

x={1, 20, 30,100,200,300,600,20,30}
print(x)
print(len(x))
print(type(x))


y=set({'a','b','c','d'})

print(y)

#update()
x.update(y)
print(x)

#discard()
y.discard('d')
print(y)

x.pop()
print(x)

a={1,2,3,4,5,6}
b={5,6,7,8,9}

c=a.difference(b)
print(c)

d=a.intersection(b)
print(d)