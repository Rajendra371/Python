#if
#if else
#if elif else
# num=int (input('enter any numeric value :'))
# if num%2==0:
#     print(num,'is an even number')
# else:
#     print(num,' is an odd number')
    
    
x=15
y=20
z=25

if x>y and x>z:
    print('x is grater number than y and z')
elif y>x and y>z:
    print('y is grater number x and z')
else:
    print('z is grater')
    
    
#leap year

year=int(input('enter year with century :'))
if year%4==0 and year%100!=0 or year%400==0:
    print(f'{year}is a leap year')
else:
    print(f'{year} is is not leap year ')
    
num1=int(input('enter any number'))
if num1%5==0 and num1%3==0:
    print(f'{num1} is is divider if 3 and 5')
else:
    print('invalid')
    
    
    
