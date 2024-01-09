text='python is a high level programming language'
print(text)


#cunt the number of characters in a string

print(len(text))

#indexing

print(text[0])
print(text[-1])


#slicing

print(text[2:10])
print(text[:20]) #0-19
print(text[10:])

#negative slicing 
print(text[-10:-1])


#built in string method()
# .upper()
#.lower()
#.split()->split the word from space by default

print(text.upper())
print(text.lower())
print(text.split())

print(text.split('level'))


# string formatting with placeholder

print('we are learning %s' %'python')
print('we are learning %s at %s ' %('python','dursikshya'))
