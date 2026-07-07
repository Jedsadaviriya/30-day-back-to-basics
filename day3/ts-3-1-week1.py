#reverse a string without using built-in functions
def reverse_string(s):
    stringrange = len(s)
    results = ""
    for i in range(stringrange - 1, -1, -1):
        char = s[i]
        results = results + char
    return results

print(reverse_string("hi"))