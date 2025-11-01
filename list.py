# names=list()
# names=['hanna','alex',1,23,4.6,True]
# print(type(names))
# print(len(names))
# print(names[-6])



# list unpacking
name=['hanna','alex','abel','yakob','micky','desa']
first , second, *third, = name
print(third)
# negative indexing

#slicing
new_list= name[-4:-2]
print(new_list)

# modifying
name[0]='alem'
print(name)


#checking element in a list
print('hanna' in name)

#adding items to list
name.append('king')
print(name)


#inserting items in specific index

name.insert(2,'abebe')
print(name)


#remove.clear() clear all the element


#copying
new_list = name.copy()  

numbers=[45,46,5,4]

newest_list = numbers + name
newest_list = numbers.extend(name)

print(newest_list)
print(newest_list.count())




