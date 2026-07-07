# vowel couter
# count how many vowel comes up in a string. 
def vowelcounter(s):
    stringrange = len(s)
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for i in range(0, stringrange, 1):
        results = ""
        char = s[i]
        results = results + char
        if results in vowels:
            count += 1
    return count

result = vowelcounter("hello world!")
print(f"there were/was {result} vowels")