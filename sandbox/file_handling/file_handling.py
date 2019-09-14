import os

#####################
#                   #
# Python Open File  #
#                   #
#####################
# Open a File on the Server
"""f = open("Notes.txt", "r")
print(f.read())
"""

#####################
#                   #
# Python File Read  #
#                   #
#####################

# Read Only Parts of the File
"""f = open("Notes.txt", "r")
print(f.read(6))
"""

# Read Lines
"""f = open("Notes.txt", "r")
print(f.readline())
print(f.readline())
print(f.readline())
"""
#  By calling readline() three times, you can read the three first lines
# Loop through the file line by line
"""for x in f:
    print(x)
"""
# By looping through the lines of the file, you can read the whole file, line by line

# Close Files
# It is a good practice to always close the file when you are done with it.
"""print(f.readline())
f.close()
"""
# Note: You should always close your files, in some cases, due to buffering,
# changes made to a file may not show until you close the file.

#####################
#                   #
# Python File Write #
#                   #
#####################
# To write to an existing file, you must add a parameter to the open() function:
#
# "a" - Append - will append to the end of the file
#
# "w" - Write - will overwrite any existing content

"""
f = open("testfile.txt", "a")
f.write("Now the file has more content!")
f.close()

# open and read the file after the appending:
f = open("testfile.txt", "r")
print(f.read())
"""

# Open the file "testfile.txt" and overwrite the content
"""f = open("testfile.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

# open and read the file after the appending:
f = open("testfile.txt", "r")
print(f.read())
"""

######################
#                    #
# Python Create File #
#                    #
######################

# Create a New File
# To create a new file in Python, use the open() method, with one of the following parameters:
#
# "x" - Create - will create a file, returns an error if the file exist
#
# "a" - Append - will create a file if the specified file does not exist
#
# "w" - Write - will create a file if the specified file does not exist

# Create a file called "myfile.txt"
"""
f = open("myfile.txt", "x")
print("Result: a new empty file is created!")
"""

# Create a new file if it does not exist
"""
f = open("myfile.txt", "w")  # or f = open("myfile.txt", "w")
"""

########################
#                      #
# Python Create Delete #
#                      #
########################
# To delete a file, you must import the OS module, and run its os.remove() function

"""
os.remove("demofile.txt")
print("demofile.txt removed")
"""

# Check if File exist
# To avoid getting an error, you might want to check if the file exists before you try to delete it
"""
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")
"""
# Delete Folder
os.rmdir("C:\\Users\\Christ\\Music\\KJV")
# Note: You can only remove empty folders.
