## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    #pass

    def echo(self):
        print "I'm an 'Animal'"

## ??
class Dog(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

    def echo(self):
        print "I'm a 'Dog'"
        super( Dog, self).echo()

## ??
class Cat(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

    def echo(self):
        print "I'm a 'Cat'"

## ??
class Person(object):

    def __init__(self, name):
        ## ??
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

    def echo(self):
        print "I'm a 'Person'"

## ??
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary

    def echo(self):
        print "I'm an 'Employee'"

## ??
class Fish(object):

    def echo(self):
        print "I'm a 'Fish'"

## ??
class Salmon(Fish):

    def echo(self):
        print "I'm a 'Salmon'"

## ??
class Halibut(Fish):

    def echo(self):
        print "I'm an 'Fish'"


## rover is-a Dog
rover = Dog("Rover")
print "Dog.echo()"
rover.echo()

## ??
satan = Cat("Satan")
print "Cat.echo()"
satan.echo()

## ??
mary = Person("Mary")
print "Person.echo()"
mary.echo()

## ??
mary.pet = satan

## ??
frank = Employee("Frank", 120000)
print "Employee.echo()"
frank.echo()

## ??
frank.pet = rover

## ??
flipper = Fish()
print "Fish.echo()"
flipper.echo()

## ??
crouse = Salmon()
print "Salmon.echo()"
crouse.echo()

## ??
harry = Halibut()
print "Halibut.echo()"
harry.echo()
