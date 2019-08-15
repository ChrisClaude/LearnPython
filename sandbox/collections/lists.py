# List is a collection which is ordered and changeable. Allows duplicate members.

thislist = ["apple", "banana", "cherry"]
# print(thislist)
# print(thislist[1])  # access item

# thislist[1] = "blackcurrant"  # change item value
# print(thislist)

# Loop through a List
# for x in thislist:
#     print(x)

# Check if item Exists
# if "apple" in thislist:
#     print("Yes, 'apple' is in the fruits list")

# List length
# print(len(thislist))

# Add Items
# thislist.append("orange")
# print(thislist)

# Add Items to specified index
# thislist.insert(1, "orange")
# print(thislist)

# Remove Item: There are several methods to remove items from a list
# thislist.remove("banana")
# print(thislist)

# The pop() method removes the specified index, (or the last item if index is not specified)
# thislist.pop()
# thislist.pop(1)
# print(thislist)

# del thislist[0]
# print(thislist)

# thislist.clear()
# print(thislist)

# Copy a List
# !!You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and
# changes made in list1 will automatically also be made in list2.
# mylist = thislist.copy()  # copies list
# print(mylist)

# mylist = list(thislist)  # copies list
# print(mylist)

# The list() Constructor
thislist2 = list(("apple", "banana", "cherry", "pineapple"))  # note the double round-brackets
print(thislist2)

# append(): Adds an element at the end of the list
# clear(): Removes all the elements from the list
# copy(): Returns a copy of the list
# count(): Returns the number of elements with the specified value
# extend(): Add the elements of a list (or any iterable), to the end of the current list
# index(): Returns the index of the first element with the specified value
# insert(): Adds an element at the specified position
# pop(): Removes the element at the specified position
# remove(): Removes the item with the specified value
# reverse(): Reverses the order of the list
# sort(): Sorts the list

