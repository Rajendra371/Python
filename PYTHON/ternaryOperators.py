number=int(input('enter a number:'))
msg='Even' if number%2==0 else 'Odd'
print(msg)


a=5
b=7

# [statement_on_True] if [condition] else [statement_on_false] 
print(a,"is greater") if (a>b) else print(b,"is Greater")






#enumerate -> ut is a useful function to use with for loop

index_count=0
for letter in 'hello':
    print('at index{} the letter us {}' .format(index_count, letter))
    index_count+=1


#use above example with enumerate

for i,letter in enumerate('welcome'):
    print('at index {}the letter is {}'.format(i,letter))
    
#zip()-> you can use zip() function to quickly create a list of tuple by zipping up together two list

list1=[1,2,3,4,4,5,6,7,8,9]
list2=[10,11,12,13,14]
result=list(zip(list1,list2))
print(result)

#min and max

print(min([1,2,3,4,5,-2,-1]))
print(max([10,20,30,40, 100]))

#random
from random import shuffle
a=['a','b','c','d','e']
shuffle(a)
print(a)


from random import randint
y=randint(1,100)
print(y)
