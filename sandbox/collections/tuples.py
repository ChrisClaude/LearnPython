# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.

thistuple = ("apple", "banana", "cherry")
# print(thistuple)

# print(thistuple[1])  # Access Tuple Items

# Once a tuple is created, you cannot change its values. Tuples are unchangeable.
# thistuple[4] = 'pineapple' # this will give an error

# Loop Through a Tuple

# for x in thistuple:
#     print(x)

# Check if Item Exists
# if "apple" in thistuple:
#     print("Yes, 'apple' is in the fruits tuple")

# Tuple Length
# print(len(thistuple))

# Once a tuple is created, you cannot add items to it. Tuples are unchangeable.

# Tuples are unchangeable, so you cannot remove items from it, but you can delete the tuple completely
# del thistuple
# print(thistuple)  # this will raise an error because the tuple ?no longer exists

# The tuple() Constructor
# It is also possible to use the tuple() constructor to make a tuple.
# thistuple = tuple(("apple", "banana", "cherry", "pineapple"))  # note the double round-brackets
# print(thistuple)

# Method	Description
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found
