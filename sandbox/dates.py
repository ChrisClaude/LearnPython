import datetime

# Display the current date
"""x = datetime.datetime.now()
print(x)"""

# #Return the year and name of weekday
"""myyear = "We are in {}"
print(myyear.format(x.year))
print(x.strftime("%A"))
"""

"""x = datetime.datetime(2020, 5, 17)
print(x)"""

# The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone),
# but they are optional, and has a default value of 0, (None for timezone).

# The strftime() Method: this is a method of a datetime object for formatting date objects into
# readable, it takes one parameter, format, to specify the format of the returned string
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))
# look at a reference of legal format code here -> https://www.w3schools.com/python/python_datetime.asp
# or https://docs.python.org/2/library/datetime.html
