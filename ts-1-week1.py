print("Hello World!")
name = input("What is your name? ")
print("Hello " + name + ", welcome to 30 day back to basics")
print("as a quick test, can you choose 2 numbers? one at a time")
inputnum1 = float(input("Number number one: "))
inputnum2 = float(input("Number number two: "))
print("This is the sum, difference, product and quotient of your two numbers",)

print(inputnum1 + inputnum2)
print(inputnum1 - inputnum2)
print(inputnum1 * inputnum2)
try:
    print(inputnum1 / inputnum2)
except:
    print("cannot devided by 0")

