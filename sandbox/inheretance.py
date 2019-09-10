class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


# Use the Person class to create an object, and then execute the printname method:

'''
x = Person("John", "Doe")
x.printname()
'''

# Inheritance: Note: Use the pass keyword when you do not want to add
# any other properties or methods to the class.
'''
class Student(Person):
    pass


x = Student("Mike", "Olsen")
x.printname()
'''


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


x = Student("Mike", "Olsen", 2019)
x.welcome()

# If you add a method in the child class with the same name as a function in the parent class,
# the inheritance of the parent method will be overridden.
