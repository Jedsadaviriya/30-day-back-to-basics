# fahrenheit to celcius calculator
print("This is a fahrenheit and celcius calculator! do you want f to c or c to f?(enter f-c or c-f)")
while True:
    convertfrom = input("f-c or c-f?: ")
    if convertfrom == ("f-c"):
        print("This is the Fahrenheit to Celcius calculator!")
        while True:
            try:
                temp = float(input("What is your Temperature in Fahrenheit?: "))
                ttc = ((temp - 32) * (5 / 9))
                print("The Temperature in Celcius is: ", ttc, "°C")
                break
            except ValueError:
                print("This is not a number or the format is incorrect try, 32 or 32.5")
        break
    elif convertfrom == ("c-f"):
        print("This is the Celcius to Fahrenheit calculator!")
        while True:
            try:
                temp = float(input("What is your Temperature in Celcius?: "))
                ttc = ((temp * (9/5)) + 32 )
                print("The Temperature in Fahrenheit is: ", ttc, "°F")
                break
            except ValueError:
                print("This is not a number or the format is incorrect try, 0 or 4.5")
        break
    else:
        print("this is not an option, do you even read?")
print("end of calculation")


