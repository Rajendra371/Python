#dictionary-> it always comes in key value form

student={
    'name':'Rajendra Shrestha',
    'age': 24,
    'gender': 'Male',
    'address':'Kathmandu'
}
print(student)
print(student['name'])

d={}
d['name']='Ram Shrestha'
d['address']='Pokhara'
print(d)

d.update({'address':'hetauda'})
print(d)


#keys() -> it only print all the keys of the dictionary

print(student.keys())


#value-> it only print all the value of dictionary

print(student.values())

#nested dictionary

test={'key1':{'nestkey':{'subnestkey':'final result'}}}
print(test['key1'])
print(test['key1']['nestkey'])
print(test['key1']['subnestkey']['final result'])