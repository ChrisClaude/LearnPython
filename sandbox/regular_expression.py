import re

# A RegEx, or Regular Expression, is a sequence of characters that forms
# a search pattern.
# RegEx can be used to check if a string contains the specified search pattern.

# Search the string to see if it starts with "The" and ends with "Spain"
"""txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
"""
# RegEx Functions
# The re module offers a set of functions that allows us to search a string for a match

# Function      	Description
# findall   :	    Returns a list containing all matches
# search    :   	Returns a Match object if there is a match anywhere in the string
# split     :    	Returns a list where the string has been split at each match
# sub       :      	Replaces one or many matches with a string

# The findall() Function
"""stri = "The rain in Spain"
x = re.findall("ai", stri)
print(x)
"""
# # If no matches are found, an empty list is returned

# The search() Function
# # The search() function searches the string for a match, and returns a Match object if there is a match.
# # If there is more than one match, only the first occurrence of the match will be returned

# Search for the first white-space character in the string:
"""stri = "The rain in Spain"
x = re.search("\s", stri)

print("The first white-space character is located in position:", x.start())
"""
# If no matches are found, the value None is returned
"""stri = "The rain in Spain"
x = re.search("Portugal", stri)
print(x)
"""

# The split() Function
# The split() function returns a list where the string has been split at each match
"""stri = "The rain in Spain"
x = re.split("\s", stri)
print(x)
"""

# You can control the number of occurrences by specifying the maxsplit parameter
"""stri = "The rain in Spain"
x = re.split("\s", stri, 1)
print(x)"""

# The sub() Function
# The sub() function replaces the matches with the text of your choice
"""stri = "The rain in Spain"
x = re.sub("\s", "9", stri)
print(x)
"""
# You can control the number of replacements by specifying the count parameter
"""stri = "The rain in Spain"
x = re.sub("\s", "9", stri, 2)
print(x)"""

# Match Object
# A Match Object is an object containing information about the search and the result.
"""stri = "The rain in Spain"
x = re.search("ai", stri)
print(x)  # this will print an object
"""
# The Match object has properties and methods used to retrieve information about the search, and the result:
#
# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match

# Print the position (start- and end-position) of the first match occurrence.
# The regular expression looks for any words that starts with an upper case "S"
"""stri = "The rain in Spain"
x = re.search(r"\bS\w+", stri)
print(x.span())
"""

# Print the string passed into the function
"""stri = "The rain in Spain"
x = re.search(r"\bS\w+", stri)
print(x.string)
"""

# Print the part of the string where there was a match.
# The regular expression looks for any words that starts with an upper case "S":
stri = "The rain in Spain"
x = re.search(r"\bS\w+", stri)
print(x.group())
