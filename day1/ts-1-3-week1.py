while True:  # True dictates that the while loop is active
    try:
        print("the loop stops if you give me the correct number(it's 67, 69, 420 or 8)")
        correctnum = int(input("What is the correct number? : "))
        if correctnum in [67, 69, 420, 8]:
            break
        else:
            print("this is not the correct number, did you even read?")
    except ValueError:
        print("This is not a number")
print("that's right ", correctnum, " was the correct number, good job you can read")