import json

# some json
natalie = '''{
    "name": "Natalie",
    "surname": "Allen",
    "age": 45,
    "address": {
        "area": "Main",
        "city": "Atlanta",
        "country": "USA"
    }
}'''

# parse natalie:
paredNatalie = json.loads(natalie)

# the result is a Python dictionary
'''print(paredNatalie['address']['country']) ''' # will print USA

employee = dict(name="John", age=30, city="Pointe-Noire")
# convert into JSON
parsedEmployee = json.dumps(employee)

# the result is a JSON string:
'''print(parsedEmployee)'''

# You can convert Python objects of the following types, into JSON strings:
# dict, list, tuple, string, int, float, True, False, None
'''print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))'''

# Convert a Python object containing all the legal data types:
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# print(json.dumps(x))

# The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.
# The json.dumps() method has parameters to make it easier to read the result
# print(json.dumps(x, indent=4))

# Use the separators parameter to change the default [default value is (", ", ": ")] separator
# print(json.dumps(x, indent=4, separators=(". ", " = ")))

# Use the sort_keys parameter to specify if the result should be sorted or not
print(json.dumps(x, indent=4, sort_keys=True))
