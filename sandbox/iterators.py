# Lists, tuples, dictionaries, and sets are all iterable objects.
"""
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
"""

# Even strings are iterable objects, and can return an iterator
"""
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
"""

# Looping Through an Iterator
# #Iterate the values of a tuple
"""
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
    print(x)
"""

# #Iterate the characters of a string
"""
mystr = "banana"

for x in mystr:
    print(x)

# The for loop actually creates an iterator object and executes the next() method for each loop.
"""


# Create an Iterator
# #Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.)

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)
