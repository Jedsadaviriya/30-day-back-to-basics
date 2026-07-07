# palindrome checker
# if the word in reverse is the same as normal word then it's a palindrome
# it should return a boolean
def reverse_string(s):
    stringrange = len(s)
    results = ""
    for i in range(stringrange - 1, -1, -1):
        char = s[i]
        results = results + char
    return results

def is_palindrome(s):
    reverse = reverse_string(s)
    result = ""
    if reverse == s:
        result = True
    else:
        result = False
    return result

result = is_palindrome("racecar")
result1 = is_palindrome("fish")
print(f"result is {result}, and result1 is {result1}")