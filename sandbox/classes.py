# Create a Class
# class MyClass:
#     x = 5


# Create object
# p1 = MyClass()
# print(p1.x)


# The __init__() Function
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Object method
    def myfunc(self):
        print("Hello my name is " + self.name)


p2 = Person("John", 36)

print(p2.name)
print(p2.age)
p2.myfunc()

# Note: The __init__() function is called automatically every time the
# class is being used to create a new object.

# Modify Object Properties
'''p2.age = 25
print(p2.age)'''

# Delete Object Properties
'''
del p2.age
print(p2.age)  # will give an error: AttributeError
'''
# Delete Objects
'''
del p2
print(p2)  # will give an error: AttributeError
'''
