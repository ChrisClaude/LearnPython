# String literals in python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello".

# #Multiline Strings
# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""

# a = '''Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua.'''
#
# print(a)

# strings in Python are arrays of bytes representing unicode characters
# Get the character at position 1 (remember that the first character has the position 0)

# a = "Hello, World!"
# print(a[1])

# Substring. Get the characters from position 2 to position 5 (not included)
# b = "Hello, World!"
# print(b[2:5])

# #The strip() method removes any whitespace from the beginning or the end
# a = " Hello, World! "
# print(a.strip())  # returns "Hello, World!"

# #The len() method returns the length of a string
# a = "Hello, World!"
# print(len(a))

# #The lower() method returns the string in lower case
# a = "Hello, World!"
# print(a.lower())

# #The upper() method returns the string in upper case
# a = "Hello, World!"
# print(a.upper())

# #The replace() method replaces a string with another string
# a = "Hello, World!"
# print(a.replace("World", "Python"))

# #The split() method splits the string into substrings if it finds instances of the separator
# a = "Hello, World!"
# print(a.split(","))  # returns ['Hello', ' World!']

# ##STRING FORMAT
# Use the format() method to insert numbers into strings
# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want {} pieces of item {} for {} dollars."
# print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
