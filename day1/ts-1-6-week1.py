import datetime

print("Find out in which year you will turn 100 years old")
print("how old are you right now?")
while True:
    try:
        age = int(input("Your Age: "))
        break
    except ValueError:
        print("Not an age try again")
currentdate = datetime.datetime.now()
print("the current year is ", currentdate.year)
if age <= 100:
    year100 = currentdate.year + (100 - age)
    print("you will turn 100 in the year ", year100)
elif age >= 100:
    year100 = currentdate.year + (100 - age)
    print("you turned 100 in the year ", year100)