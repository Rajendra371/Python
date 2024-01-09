myfile=open('test.txt')
print(myfile)

#read the file content

print(myfile.read())

#if we want to print the paragraph from certain index number then do the following using seek()

myfile.seek(6)
print(myfile.read())

#readLines(): it will return list of the lines in the file
myfile.seek(0)
print(myfile.readlines())
myfile.close()

#to write to an existing file

wfile=open('test.txt','w')
print(wfile)

wfile.write('this is inserted from programming')
wfile.write('\n this is the second inserted text from program')
wfile.close()

#create a new file using w if the file is not exist

newFile=open('python.txt','w')
print(newFile)
newFile.write('this is inserted from the programming')
newFile.write('\n this is new inserted')

newFile=open('python.txt','r')
print(newFile.read())
newFile.close()


# append()-> a+ : this will create the new file
#open(filename.txt,'a+')

file=open('xyz.txt','a+')
print(file)
file.write('this is append mode file')


#delete
import os
print(os.remove('hello.txt'))


