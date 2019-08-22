# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
#
# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
#
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     print(x)

# Looping Through a String
# for x in "banana":
#     print(x)

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     print(x)
#     if x == "banana":
#         break

# for x in fruits:
#     if x == "banana":
#         continue
#     print(x)

# for x in range(6):
#     print(x)

# Using the start parameter:
# for x in range(2, 6):
#     print(x)

# Increment the sequence with 3 (default is 1):
# for x in range(2, 30, 3):
#     print(x)

# The else keyword in a for loop specifies a block of code to be executed when the loop is finished
# for x in range(6):
#     print(x)
# else:
#     print("Finally finished!")

# Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)
