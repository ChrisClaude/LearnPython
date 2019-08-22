# A dictionary is a collection which is unordered, changeable and indexed.
# In Python dictionaries are written with curly brackets, and they have keys and values.

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
# print(thisdict)
# x = thisdict["model"]
# print(x)
# There is also a method called get() that will give you the same result
# x = thisdict.get("model")

# thisdict["year"] = 2018

# Loop Through a Dictionary
# Print all key names in the dictionary, one by one
# for x in thisdict:
#     print(x)

# print all values in the dictionary, one by one:

# for x in thisdict:
#     print(thisdict[x])

# You can also use the values() function to return values of a dictionary:
# for x in thisdict.values():
#     print(x)

# Loop through both keys and values, by using the items() function:

# for x, y in thisdict.items():
#     print(x, y,)

# if "model" in thisdict:
#     print("Yes, 'model' is one of the keys in the thisdict dictionary")

# Dictionary Length
# print(len(thisdict))

# Adding Items
# Adding an item to the dictionary is done by using a new index key and assigning a value to it

# thisdict["color"] = "red"
# print(thisdict)

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead)
# thisdict.popitem()
# print(thisdict)

# The del keyword removes the item with the specified key name
# del thisdict["model"]
# print(thisdict)

# The del keyword can also delete the dictionary completely
# del thisdict
# print(thisdict) #this will cause an error because "thisdict" no longer exists.

# thisdict.clear()
# print(thisdict)

# Copy a Dictionary
# You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1,
# and changes made in dict1 will automatically also be made in dict2.
#
# There are ways to make a copy, one way is to use the built-in Dictionary method copy().

# mydict = thisdict.copy()
# print(mydict)

# Another way to make a copy is to use the built-in method dict().
# mydict = dict(thisdict)
# print(mydict)

# Nested Dictionaries
myparent = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

# print(myparent)

# thisdict = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
# print(thisdict)

# Dictionary Methods
# Python has a set of built-in methods that you can use on dictionaries.
#
# Method	            Description
# clear()	            Removes all the elements from the dictionary
# copy()	            Returns a copy of the dictionary
# fromkeys()	        Returns a dictionary with the specified keys and values
# get()	                Returns the value of the specified key
# items()	            Returns a list containing the a tuple for each key value pair
# keys()	            Returns a list containing the dictionary's keys
# pop()	                Removes the element with the specified key
# popitem()	            Removes the last inserted key-value pair
# setdefault()	        Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	            Updates the dictionary with the specified key-value pairs
# values()	            Returns a list of all the values in the dictionary
