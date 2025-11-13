number=int(input("enter your Number: "))
if(number % 2==1):
    print('weird')
elif(number % 2==0 and number>=2 and number<=5):
    print('Not weird')
elif(number % 2==0 and number>=6 and number<=20):
    print('Weird')
elif(number % 2==0 and number>=20):
    print('Not weird')
    