# Day 1 - Python Basics
# simple program greeting user
name = input("What's your name? ")
print("Hello, " + name)


# Example of The stack
def greet():
    stackname = "Janjao"   # this lives on the stack
    print("hello" + stackname)

greet() # calls for the function
# the name is gone after the greet function is excuted

# Example of The heap
alist = [1,2,3,4,5,6,7]  # this lives on the heap, it may grow or shrink overtime


# when you write
x = 10
# python allocates a small piece of memory somewhere and creates a box.
# it can be called upon and now the the x becomes a lable or reference to that box.

a = [1,2,3]
b = a
b.append(4)
# append modifies the list adding 4 at the end of the list [1,2,3]
print(a) # it should print [1,2,3,4] out if I did things correctly 
# because a and b are both references to the same list in memory.

print(1 + 2)
