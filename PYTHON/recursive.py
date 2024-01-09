#recursive function->function that call it self
def fact(n):
         return 1
     else:
         return n*fact(n-1)
     
     n=int(input('enter a number to get its factorial:'))
f=fact(n)
print(f)