_template:_

```javascript
## Day  —

Goal:
What I built:
Where I got stuck:
What I understand now that I didn't this morning:
```

## Day 1 — 1.July.2026

Goal:

recap the most basics of computing. how things are stored, and create simple scripts.

What I built:

### scripts

1. ask user for name, greets them, ask for 2 numbers, shows sum, difference, product and quotient of the two numbers [ts-1-1-week1.py](day1\ts-1-1-week1.py)
2. simple example for +, -, \* and /[ts-1-3-week1.py](day1\ts-1-3-week1.py)
3. Control flow, asks for a correct number to end an infinite loop, with a little bit of spice and rage bait [ts-1-4-week1.py](day1\ts-1-4-week1.py)
4. Celcius to fahrenheit vice versa calculator. [ts-1-5-week1.py](day1\ts-1-5-week1.py)
5. which year do I turn 100 calculator [ts-1-6-week1.py](day1\ts-1-6-week1.py)
6. f-string examples [ts-1-7-week1.py](day1\ts-1-7-week1.py)
7. types extraction funciton examples [ts-1-8-week1.py](day1\ts-1-8-week1.py)
8. find larger num [ts-1-9-week1.py](day1\ts-1-9-week1.py)
9. Min to hour and min conversion with modulo[ts-1-10-week1.py](day1\ts-1-10-week1.py)
10. first project. guessing randomly generated number game. [p-1-guessing-game.py](projects\p-1-guessing-game.py)

Where I got stuck:

1. string input, stuck around 5 min, I forgot about the "datatype(input("something something trallalelo trallala"))"

What I understand now that I didn't this morning:

1. try/except in Python — instead of crashing when a user
   types something wrong, I can catch the specific error
   and handle it myself
2. variables are labels pointing to a box in memory, not
   the box itself — two variables can point to the same
   box, which is why modifying one can affect the other

## Day 2 — 2.July.2026

Goal:

get comfortable writing my own functions — things that return a value instead of just printing. ~2-3 hours today, busy schedule so a lighter day.

What I built:

### functions

1. add() and is_even(). is_even took me 3 tries — first I tried to cram an if/else and an assignment inside return(...) which is invalid, then I hit the print()-returns-None trap (boole = print(True) stores None not True), then landed on is_even = True / return is_even. after that realized the whole thing is just return x % 2 == 0 with no if/else at all [ts-2-1-week1.py](day2\ts-2-1-week1.py)

### projects

2. fizzbuzz(n). first attempt used `if a & b:` thinking it meant "a and b are both zero" — didn't realize & is bitwise AND on the actual values, not a combined boolean check. fixed it by adding a third variable c = n % 15 and checking that directly. also hit the None trap again here with return print("FizzBuzz") before catching it myself [p-2-fizzbuzz.py](projects\p-2-fizzbuzz.py)
3. calculator(a, op, b). started by trying to use input() inside the function to grab the operator, then restructured to take op as a parameter instead — more testable. hit the None trap a third time in the divide-by-zero branch (err = print(...)) but caught and fixed it myself this time without it being flagged. added an else branch that returns a string for invalid operators instead of a bare return that silently gives None [p-3-calculator.py](projects\p-3-calculator.py)

Where I got stuck:

1. kept defaulting to print() inside functions instead of return — same mistake showed up 3 separate times across is_even, fizzbuzz and calculator before it fully clicked
2. confused & (bitwise AND) with checking whether two conditions are both true — used it in fizzbuzz thinking it meant something it didn't
3. named local variables the same as the function itself twice (is_even = True inside def is_even, fizzbuzz = "FizzBuzz" inside def fizzbuzz). works because of local scope but noting it as a bad habit to drop before recursion bites me
4. overwrote a test variable by reusing resultscal1 for two different calculator calls and lost the first result

What I understand now that I didn't this morning:

1. a function that returns a value is usable by the caller, a function that prints is a dead end — nothing comes back
2. print() always returns None no matter what it prints, so x = print(y) never gives you y back
3. if x % 2 == 0: return True else: return False is often just decoration around a boolean expression that already exists — could be return x % 2 == 0 directly
4. bitwise & is not the same as "both conditions are true" — need and, or an explicit check like n % 15 == 0
5. order/structure of if-elif chains matters for overlapping conditions (3 and 5 both dividing 15) — solved it with a dedicated % 15 check instead of relying on elif ordering

Not finished — carrying into tomorrow:

1. string manipulation exercises: reverse a string, count vowels, palindrome check — all without built-in shortcuts (no slicing, no .count(), no reversed()). last item left on the Week 1 MVP checklist
