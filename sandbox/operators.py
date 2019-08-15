# #IDENTITY OPERATOR: "is" and "is not"
# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object,
# with the same memory location

# x = ["apple", "banana"]
# y = ["apple", "banana"]
# z = x

# print(x is z)
# returns True because z is the same object as x

# print(x is y)
# returns False because x is not the same object as y, even if they have thew same content

# print(x == y)
# to demonstrate the difference between "is" and "==": this comparison returns True because x is equal to y

# x = ["apple", "banana"]
# y = ["apple", "banana"]
# z = x

# print(x is not z)
# returns False because z is the same object as x

# print(x is not y)
# returns True because x is not the same object as y, even if they have the same content

# print(x != y)
# to demonstrate the difference between "is not" and "!=": this comparison returns False because x is equal to y

# #Membership Operators
# Membership operators are used to test if a sequence is presented in an object

# x = ["apple", "banana"]

# print("banana" in x)

# returns True because a sequence with the value "banana" is in the list

# x = ["apple", "banana"]

# print("pineapple" not in x)

# returns True because a sequence with the value "pineapple" is not in the list

