# rule for the game
# if divisible by 3 then print fizz
# by 5 the buzz
# by 3 and 5(15) the fizzbuzz
# otherwise just the number

def fizzbuzz(n):
    a = n % 3
    b = n % 5
    c = n % 15
    if c == 0:
        fizzbuzz = "FizzBuzz"
        return fizzbuzz
    elif a == 0:
        fizz = "Fizz"
        return fizz
    elif b == 0:
        buzz = "Buzz"
        return buzz
    else:
        return n
    
results = fizzbuzz(15)
results1 = fizzbuzz(3)
results2 = fizzbuzz(5)
results3 = fizzbuzz(11)
print(results, results1, results2, results3)