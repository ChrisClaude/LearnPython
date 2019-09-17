# A function is a block of code which only runs when it is called.
#
# You can pass data, known as parameters, into a function.
#
# A function can return data as a result.

# #Creating a Function
# In Python a function is defined using the def keyword


# def my_function():
#     print("Hello from a function")
#
#
# #Calling a Function
# my_function()


# #Parameters
# def my_function(fname):
#     print(fname + " Claude")
#
#
# my_function("Email")
# my_function("Tobias")
# my_function("Linus")

# #Default Parameter Value
# def my_function(country="Norway"):
#     print("I am from " + country)
#
#
# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")

# #Passing a List as a Parameter
# def my_function(food):
#     for x in food:
#         print(x)
#
#
# fruits = ["apple", "banana", "cherry"]
#
# my_function(fruits)

# #Return Values
# def my_function(x):
#     return 5 * x
#
#
# print(my_function(3))
# print(my_function(5))
# print(my_function(9))

# #Keyword Arguments
# def my_function(child3, child2, child1):
#     print("The youngest child is " + child3)
#
#
# my_function(child1="Emil", child2="Tobias", child3="Linus")
# Note: The phrase Keyword Arguments are often shortened to kwargs in Python documentations.

# #Arbitrary Arguments
# If you do not now how many arguments that will be passed into your function, add a * before the parameter name in the
# function definition.
#
# This way the function will receive a tuple of arguments, and can access the items accordingly:
# def my_function(*kids):
#     print("The youngest child is " + kids[2])
#
#
# my_function("Emil", "Tobias", "Linus")

# Recursion
def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
tri_recursion(6)
