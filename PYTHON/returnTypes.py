def check(num):
    if num % 2 == 0:
        return "even number"
    else:
        return "odd number"


result = check(15)
print(result)


def total(num):
    sum=0
    for n in num:
        if n%2==0:
            sum+=n
        return sum
        

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = total(numbers)
print(result)

# membership operators

list1 = ["a", "b", "c", "d"]
print("a" in list1)
print("b" in list1)
print("c" in list1)
print("d" not in list1)



#character count

def count_vowels(word):
    vowels=['A','I','O','E','U','a','e','i']
    count=0
    for letter in word:
        if letter in vowels:
            count+=1
            return count



text='Welcome'
result= count_vowels(text)
print('the number of vowels are :',result)

#count even number







