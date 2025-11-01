age =int(input('enter age: '))
if(age > 18):
     print('adult')

elif(age==18):
     print('pass')
else:
    print('underage')


password=input('enter password: ')
if(password.isupper()):
    print('false')

elif(password.islower()):
    print('false')
elif(password.isdigit()):
    print('false')
elif(password.isalpha()):
    print('false')
else:
    print('pass')

