username = input('enter your name: ')
usergender = input('enter your Gender: ')
userage = int(input('enter your age: '))
userWeight = float(input("enter your weight: "))
userheight = float(input("enter your height: "))

def BMI():
    bmi_value = userWeight / (userheight ** 2)
    return bmi_value

def BMR_male():
    return 10 * userWeight + 6.25 * userheight - 5 * userage + 5

def BMR_female():
    return 10 * userWeight + 6.25 * userheight - 5 * userage - 161

print(f"Your BMI is: {BMI()}")

if usergender.lower() == "male":
    print(f"Your BMR is: {BMR_male()}")

if usergender.lower() == "female":
    print(f"Your BMR is: {BMR_female()} ")
