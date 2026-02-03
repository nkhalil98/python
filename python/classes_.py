from abc import ABC, abstractmethod
from dataclasses import dataclass


# TODO: mixins
# TODO: @classmethods vs @staticmethods vs instance methods


# class definition and instantiation
# ----------------------------------

# classes are blueprints for user-defined data types
# classes define attributes and methods
# objects are instances of classes


## class definition
class Cat:
    def __init__(self, name, age):  # initializer/constructor method
        self.name = name  # instance variable/attribute
        self.age = age

    def meow(self):  # method
        print("Meow!")

    def __str__(self):  # dunder/magic method for string representation
        return f"Cat(name={self.name}, age={self.age})"


## object instantiation
tofu = Cat("Tofu", 2)
print(tofu.name)  # access attribute
tofu.meow()  # method call
print(tofu)  # __str__ method is called automatically


## __init__ and self

# The `__init__()` method is a special (magic) method that Python runs
# automatically whenever we create a new instance based on the class. The
# `self` parameter is required in the method definition (and it must come
# first) because when Python calls this method later (when creating an
# instance), the method call will automatically pass the `self` argument.

# Every method call associated with an instance automatically passes `self`,
# which is a reference to the instance itself; it gives the individual
# instance access to the attributes and methods in the class.

# Variables like `self.name` are accessible through class instances and are
# called attributes. They are also available to every method in the class.


### with __init__
class Car1:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Information: {self.year} {self.make} {self.model}")


car1 = Car1("Toyota", "Corolla", 2020)
car1.display_info()


### without __init__
class Car2:
    # still can be defined without __init__ and accessed using self
    make = ""
    model = ""
    year = 0

    def display_info(self):
        print(f"Car Information: {self.year} {self.make} {self.model}")


car2 = Car2()
car2.make = "Honda"
car2.model = "Civic"
car2.year = 2023
car2.display_info()


# class vs instance variables
# ---------------------------


class Person:
    tag = "person"  # class variable/attribute (each instance has its own copy)

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.id = None  # default value
        self._private_id = None  # protected attribute (by convention)
        self.__private_id = None  # private attribute (name mangling)

    def greet(self):
        print("Hello, my name is", self.name)

    def speak(self):
        print("I am a person")

    # getter method
    def get_id(self):
        return self.id

    # setter method
    def set_id(self, id):
        assert isinstance(id, int), "ID must be an integer"
        self.id = id

    def __str__(self):
        return f"Person(name={self.name}, age={self.age}, id={self.id})"


p = Person("Nabil", 26)
p.greet()

p.id = 1  # direct access to instance attribute
p.set_id(2)  # using setter method (good practice)
print(p.get_id())  # using getter method (good practice)

# Python is not good at enforcing encapsulation, so we can access protected and
# private attributes directly
p2 = Person("Ali", 30)  # another object instantiation
p2.id = 3
del p2.id  # delete instance attribute
p2._private_id = 4  # access protected attribute (not recommended)
p2._Person__private_id = 5  # can even access the private name-mangled attribute
p2.nationality = "USA"  # add new instance attribute

# hasattr() and getattr()
print(hasattr(p, "name"))  # True
print(getattr(p, "age"))  # 26
print(getattr(p, "nonexistent", "default"))  # default


people = [p, p2]  # list of objects
print(people)  # printed as a list of references
for person in people:
    print(person)  # __str__ method is called automatically

# OOP concepts (Inheritance, Polymorphism, Abstraction, and Encapsulation)
# ------------------------------------------------------------------------


## inheritance


# Student is a subclass (child class) of Person superclass (parent class)
class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)  # super() returns a proxy object that
        # allows us to call methods of the superclass
        self.school = school

    def study(self):
        print("I am studying")

    # method overriding
    def speak(self):
        print("I am a student")


s = Student("Nabil", 26, "MIT")
s.greet()  # method from superclass
s.speak()  # overridden method
s.study()  # method from subclass

print(issubclass(Student, Person))  # True
print(isinstance(s, Student))  # True
print(isinstance(s, Person))  # True


## composition (instances as attributes)
class University:
    def __init__(self, name, city, state):
        self.name = name
        self.city = city
        self.state = state


class MITStudent(Student):
    def __init__(self, name, age):
        super().__init__(name, age, University("MIT", "Cambridge", "MA"))


mit_student = MITStudent("Nabil", 26)
print(mit_student.school.name)  # access University attribute through Student


## polymorphism through method overriding
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Woof!")


def animal_sound(animal):
    animal.speak()


dog = Dog("Buddy", 4)
cat = Cat("Whiskers", 3)

animal_sound(dog)  # Woof!
animal_sound(cat)  # Meow!


## abstraction with abc module
class Shape(ABC):
    @abstractmethod  # subclasses must implement this method
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

    def perimeter(self):
        return 2 * 3.14 * self.radius


## encapsulation with public, protected, and private attributes
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner  # public attribute
        self._balance = balance  # protected attribute (by convention)
        self.__account_number = "123456789"  # private attribute (name mangling)

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient funds")
        else:
            self._balance -= amount

    def get_balance(self):
        return self._balance

    def get_account_number(self):
        return self.__account_number


# multiple inheritance and MRO
# ----------------------------


class A:
    pass


class B:
    pass


class C(A, B):
    pass


print(C.__bases__)  # (<class '__main__.A'>, <class '__main__.B'>)
print(
    C.__mro__
)  # (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)


# @property decorator
# -------------------


## classic getter, setter, deleter methods
class Square:
    def __init__(self, side):
        self.__side = side

    def get_side(self):
        return self.__side

    def set_side(self, value):
        if value < 0:
            raise ValueError("Side length cannot be negative")
        self.__side = value

    def del_side(self):
        print("Deleting side attribute")
        del self.__side


## using property()
class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def set_width(self, value):
        if value < 0:
            raise ValueError("Width cannot be negative")
        self.__width = value

    def del_width(self):
        print("Deleting width attribute")
        del self.__width

    def get_height(self):
        return self.__height

    def set_height(self, value):
        if value < 0:
            raise ValueError("Height cannot be negative")
        self.__height = value

    def del_height(self):
        print("Deleting height attribute")
        del self.__height

    width = property(get_width, set_width, del_width, "Width property")
    height = property(get_height, set_height, del_height, "Height property")


## using @property decorator
class Circle:  # noqa
    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        """Radius property"""
        return self.__radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self.__radius = value

    @radius.deleter
    def radius(self):
        print("Deleting radius attribute")
        del self.__radius


# method chaining
# ---------------


class Calculator:
    def __init__(self, value=0):
        self.value = value

    def add(self, x):
        self.value += x
        return self  # return self to allow chaining

    def subtract(self, x):
        self.value -= x
        return self

    def multiply(self, x):
        self.value *= x
        return self

    def divide(self, x):
        if x == 0:
            raise ValueError("Cannot divide by zero")
        self.value /= x
        return self

    def result(self):
        return self.value


calc = Calculator()
result = calc.add(5).subtract(2).multiply(4).divide(6).result()


# dataclasses
# -----------


@dataclass
class Point:
    x: float
    y: float


p1 = Point(1.0, 2.0)
p2 = Point(1.0, 2.0)

print(p1)  # Point(x=1.0, y=2.0)
print(p1 == p2)  # True (dataclasses provide value-based equality)
