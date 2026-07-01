# ask for number, print square root
import math

while True:
    try:
        print("Square root finder, please enter a number")
        rootof = float(input("Number here: "))
        print(math.sqrt(rootof))
        break
    except ValueError:
        print("This is not a number")