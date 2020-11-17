# Use this to take notes on the Edpuzzle video. Try each example rather than just watching it - you will get much more out of it!
#  None
'''
student = {'name': 'John', 'age': '25', 'courses': ['Math', 'Compsci']}
print(student['courses'])
'''

'''
student = {'name': 'John', 'age': '25', 'courses': ['Math', 'Compsci']}
print(student.get('name'))
'''

'''
student = {'name': 'John', 'age': '25', 'courses': ['Math', 'Compsci']}
print(student.get('phone','Not Found'))
'''

'''
student = {'name': 'John', 'age': '25', 'courses': ['Math', 'Compsci']}
student.update({'name': 'Jane', 'age': '26', 'phone': '555-5555'})
print(student)
'''

'''
student = {'name': 'John', 'age': '25', 'courses': ['Math', 'Compsci']}
print(student.items())
'''

'''
student = {'name': 'John', 'age': '25', 'courses': ['Math', 'Compsci']}
for key, value in student.items'()
    print(key, value)
''