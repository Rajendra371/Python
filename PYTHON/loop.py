#loop-> repeatation/iteration

number=[10,20,30,40,50]
for num in number:
    print(num,end="")
print('\n')

text='hello python'
for letter in text:
    print(letter, end="")

print('\n')
for i in range(1,10):
    print(i,end="")
    print('\t')
    
print('\n')
for x in range(1,21):
    if x%2==0:
        print(x,end="")
        print('\t')
    
    
#break

fruits=['apple', 'mango', 'banana', 'cherry']
for f in fruits:
    if f=='banana':
        break
    print(f)
    
#continue
for f in fruits:
    if f=='mango':
        continue
    print(f)
    
    
    
#WHILE LOOP
j=1
while(j<=10):
    print(j, end="")
    print('\t')
    j+=1
    
    