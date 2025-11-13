#to declare
# students=dict()
students = {'name':'hanna', 'age':26, 'sec':'B'}
print(len(students))# length
print(students['name']) #accessing the element
students['last_name']='kebede' #adding an item
students['first_name']= "yakob" #update
print ('f_name' in students) #checking key in dic
students.pop('first_name')# to remove 
print(students.keys()) # to print the values as list
print(students)