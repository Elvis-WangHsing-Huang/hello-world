## Animal is-a object
class Animal(object):
    pass

## Dog is Animal
class Dog(Animal):
    def __init__(self, name):
        ##
        self.name = name

##
class Cat(Animal):
    def __init__(self, name):
        ##??
        self.name = name


## Person is object
class Person(object):
    def __init__(self, name):
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is Person
class Employee(Person):
    def __init__(self, name, salary):
        ## ?? return a parent object for single inheritance
        super(Employee, self).__init__(name)
        self.salary = salary

class Fish(object):
    pass

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass

# rover is-a Dog
rover = Dog("Rover")

satan = Dog("Satan")

mary = Person("Mary")

mary.pet = satan

frank = Employee("Frank", 120000)

frank.pet = rover

flipper = Fish()

crouse = Salmon()

harry = Halibut()
