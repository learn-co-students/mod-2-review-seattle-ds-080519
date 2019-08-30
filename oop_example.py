# declaring a class Student.  class names should always be capitalized
class Student:
    # setting a class attribute called `instances`, that initially
    # contains an empty list
    instances = []

    # declaring the constructor.  this is what is called when you create
    # a new instance of the class, e.g. `Student("Erin")`
    # in that example, "Erin" would become the parameter `name`
    def __init__(self, name):
        # setting an instance variable called `name`, assigned to the
        # parameter `name`
        self.name = name
        # modifying the `instances` class attribute, to add the current
        # instance that we're creating
        self.__class__.instances.append(self)

    # declaring the instance method to convert an instance into a string
    # this is used when you call the built-in `print` function
    def __str__(self):
        # getting the value of instance variable `name`, and returning
        # a string based on that value
        return "Student instance with name: " + self.name

    # declaring the instance method to print a greeting
    def say_hello(self):
        # getting the value of instance variable `name`, and printing
        # a string based on that value
        print("Hello my name is", self.name)

    # declaring the class method to print all of the instances
    @classmethod
    def printInstances(cls):
        # getting the value of class variable `instances`, and printing
        # them out.  this implicitly calls the __str__ method
        for instance in cls.instances:
            print(instance)

# declaring a child class that inherits from the Student class.
# note that it doesn't need to have __init__ or __str__, it just
# uses the ones from Student
class StudentWhoseNameStartsWithA(Student):
    # however it does declare say_hello, since we want this behavior
    # to be different from the parent class
    def say_hello(self):
        # first, invoke the method in the parent class (Student)
        super().say_hello()
        # then, add something custom
        print("My name starts with 'A'")

hunter = Student("Hunter")
dirk = Student("Dirk")
henok = Student("Henok")

aaron = StudentWhoseNameStartsWithA("Aaron")
allison = StudentWhoseNameStartsWithA("Allison")

print()

print("Hunter say hello")
hunter.say_hello()
print()

print("Aaron say hello")
aaron.say_hello()
print()

print("Print all instances of Student")
Student.printInstances()
print()

