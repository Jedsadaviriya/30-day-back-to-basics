# initial creation date
# computer picks rand num betw 1 and 100
# user guess
# program says "too high", "too low" or correct
# loops until user guess correct
# when correct say how many guesses

import random

print("I will choose and number between 1 - 100 and you guess what the number is")
crrans = random.randint(1, 100)
guesses = 0
print("I choose a number now guess")
while True:
        guesses += 1
        print(f"this is guess nr.{guesses} pick a number between 1 - 100")
        try:
            guessingnr = int(input("Number: "))
            if guessingnr == crrans:
                print(f"that's right {crrans} was the number I choose. it took you {guesses} guesses")
                break
            elif guessingnr < crrans:
                print("my number is higher than your number")
            elif guessingnr > crrans:
                print("my number is lower than your number")
        except ValueError:
             print("not a number")
             guesses -= 1
       
