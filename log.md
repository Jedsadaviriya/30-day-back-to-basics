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

get comfortable writing my own functions. things that return a value instead of just printing. ~2-3 hours today, busy schedule so a lighter day.

What I built:

### functions

1. add() and is_even(). is_even took me 3 tries. first I tried to cram an if/else and an assignment inside return(...) which is invalid, then I hit the print()-returns-None trap (boole = print(True) stores None not True), then landed on is_even = True / return is_even. after that realized the whole thing is just return x % 2 == 0 with no if/else at all [ts-2-1-week1.py](day2\ts-2-1-week1.py)

### projects

2. fizzbuzz(n). my initial thought was actually correct, use three variable but then I scrapped the idea for some reason. first attempt used `if a & b:` thinking it meant "a and b are both zero" — didn't realize & is bitwise AND on the actual values, not a combined boolean check. fixed it by adding a third variable c = n % 15 and checking that directly. also hit the None trap again here with return print("FizzBuzz") before catching it myself [p-2-fizzbuzz.py](projects\p-2-fizzbuzz.py)
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

## Day 3 — 3.July.2026

Goal:

start the Week 1 carryover, string manipulation by hand, no built-in shortcuts (no [::-1], no .count(), no reversed()). late-night session, short on time and honestly short on brainpower, got through exactly one of the three exercises.

What I built:

### functions

1. reverse_string(s). reverses a string manually with a loop instead of slicing. simple on paper, took me five separate bugs to get right [ts-3-1-week1.py](day3\ts-3-1-week1.py)

Where I got stuck:

this was a slow, frustrating one. at one point I was just staring at it going "I can't think, tell me what happens in my code." five distinct bugs on one tiny function, fixed one at a time, in this order:

1. put return inside the loop, so it bailed after the first character instead of processing the whole string
2. indexed into the wrong variable. used stringrange (which is len(s), an integer) instead of s, so it wasn't indexable
3. IndexError: string index out of range. started the range at len(s) instead of len(s) - 1. classic length vs. last-valid-index off-by-one
4. put results = "" inside the loop, so the accumulator reset to empty every pass and only the last character survived. moved it above the loop
5. strategy mismatch. looping backward (range(len-1, -1, -1)) but prepending with results = char + results. backward+prepend cancels out. reversing needs either forward+prepend or backward+append. fixed to results = results + char to match the backward loop

then even with a correct function, calling reverse_string("hi") on its own printed nothing when run as a script. had to wrap it in print(reverse_string("hi"))

What I understand now that I didn't this morning:

1. return and print() are not the same job. return hands a value back to the caller silently, print() is what actually shows it. yesterday's bug was the opposite direction (return print(x) giving back None from inside the function), today it was the missing print() on the calling side. same lesson from both ends now
2. reversing by hand only works if the iteration direction and the accumulation direction agree. forward+prepend or backward+append, never mixed
3. length and last index are off by one. range for walking a string backward is len(s) - 1 down to -1, not len(s)
4. where you initialize an accumulator matters. inside the loop resets it every pass, it has to live above the loop
5. five precise things all had to line up for one simple loop to work. good reminder that "simple" and "easy" aren't the same thing

Not finished — carrying into tomorrow:

1. count vowels (no .count()) and palindrome check. didn't reach either tonight, ran out of time. still the last items on the Week 1 MVP checklist

## Skipped — 4-6.July.2026

took a few days off, birthday. logging it as skipped instead of pretending it didn't happen or renumbering. the day count keeps going by session, not by calendar, so the next working session is still Day 4.

## Day 4 — 7.July.2026

Goal:

close out the Week 1 carryover (vowel count + palindrome, still no built-in shortcuts), then start something bigger. ended up rolling straight into a contact book project.

What I built:

### functions

1. vowelcounter(s). counts vowels in a string by walking it and checking membership against a vowels list. returns an int, the sentence building happens outside at the call site [ts-4-1-week1.py](day4\ts-4-1-week1.py)
2. is_palindrome(s). reuses Day 3's reverse_string() and compares the reverse to the original, returns a boolean. had to copy-paste reverse_string in instead of importing it, because Python module names can't have dashes and my daily files are named like ts-3-1-week1.py [ts-4-2-week1.py](day4\ts-4-2-week1.py)

### projects

3. contact book. nested dict (name goes to {phone, email}), built to be command-loop driven instead of hardcoded. got all four CRUD functions done and tested by hand: add_contact (case-insensitive key, with a y/n/else overwrite-or-cancel loop if the name already exists), lookup_contact (returns the nested dict or a "doesn't exist" string), delete_contact (uses del to actually remove the key), list_contacts (builds a list of "name: info" strings). the command loop that ties them together is not done yet [p-4-contactbook.py](projects\p-4-contactbook.py)

also wrote a throwaway joke function is_forever_love(p1, p2) mid-session, case-insensitive name check using and/or. got the operator precedence right first try. not saved, just messing around.

Where I got stuck:

1. is vs in vs == confusion, over and over. showed up in the vowel counter, again in palindrome, and again in the contact book. resolution time got shorter each round though, so it's sinking in
2. the return-vs-print bug is still following me. hit x = print(...) again in the vowel counter, in lookup_contact's else branch, and in the side quest. caught them faster each time
3. palindrome with in gave me false confidence. tests "passed" because a string is always a substring of itself, so it looked correct for the wrong reason. only caught it by testing a partial-overlap case like "abcabc". switched to ==
4. add_contact had input() sitting outside the confirmation while loop, so the re-prompt never actually re-asked. same category as Day 3's return-inside-loop, a placement/scope mistake not a syntax one
5. assumed setting a contact to "" would delete it. it just blanks the value and leaves the key. that's how I found out about del
6. list_contacts was the messy one. went through return-inside-loop (only returned the first contact), then overwriting one results variable each pass, then a doubling bug (results = results + results), before landing on results = [] before the loop plus .append() each pass

What I understand now that I didn't this morning:

1. is vs in vs == are three different questions. identity vs membership vs value equality. is on small strings/ints seems to work because of interning, right up until it silently doesn't, so it's the wrong tool for "are these equal"
2. nested dictionaries. a dict value can be another dict, and you reach into it by chaining like contacts["alice"]["phone"]
3. dicts are mutable and passed by reference. modifying a dict inside a function is visible outside without returning anything, different from reassigning a plain int or string
4. del removes a key entirely, setting a value to "" only blanks it
5. for key in contacts iterates the keys by default, .items() gives you key and value together
6. a y/n validation loop only works if the input() is inside the loop. asked once before the loop, bad input traps you with no way to fix it

Not finished — carrying into tomorrow:

1. the contact book command loop, the add/lookup/delete/list/quit dispatch that turns the four functions into an actual runnable program. that's the remaining piece
