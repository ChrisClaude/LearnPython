import sandbox.mymodule as mx
from sandbox.random_number import numbers
import platform

# sandbox.mymodule.greeting("Jonathan")
# You can create an alias when you import a module, by using the as keyword
"""
a = mx.person1["age"]
print(a)
"""
"""
x = platform.system()
print(x)
"""

"""
x = dir(platform)
print(x)
"""

# Note: The dir() function can be used on all modules, also the ones you create yourself.
# You can choose to import only parts from a module, by using the from keyword.
print(numbers)


