# tuples are immutable
names = ('hanna', 'alex', 1, 2, 3, 4.6)
print(type(names))

# convert tuple to list
newlist = list(names)
newlist[0] = 'alem'  
print(newlist)

# slicing
print(names[0:2])

# convert back to tuple
new_tuple = tuple(newlist)  
print(new_tuple)
