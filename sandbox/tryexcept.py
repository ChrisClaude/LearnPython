"""try:
    print(x)
except NameError:
    print("An exception occurred")
except:
    print("Something else went wrong")
else:
    print("Nothing went wrong")
    # You can use the else keyword to define a block of code to be executed
    # if no errors were raised"""

"""try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
"""

f = ""
try:
    f = open("demofile.txt")
    f.write("Lorum Ipsum")
except:
    print("Something went wrong when writing to the file")
finally:
    f.close()
