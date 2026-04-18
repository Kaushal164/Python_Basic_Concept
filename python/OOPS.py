#OOP stands for Object Oriented Programming. It is a programming paradigm that uses objects and classes to organize code.
#In OOP, we can create objects that have properties and methods. Properties are the attributes of the object, while methods are the functions that can be performed on the object.
#In python, we can create a class using the class keyword. A class is a blueprint for creating objects. We can create an object from a class by calling the class as a function.

#write a program to create a class called Car with properties like make, model, year and methods like start, stop, drive.
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def start(self):
        print("The car has started.")
        
    def stop(self):
        print("The car has stopped.")
        
    def drive(self):
        print("The car is driving.")
#creating an object of the Car class
my_car = Car("Toyota", "Camry", 2020)   
print(my_car.make) #print the make of the car
print(my_car.model) #print the model of the car
print(my_car.year) #print the year of the car
my_car.start() #call the start method
my_car.drive() #call the drive method
my_car.stop() #call the stop method

#Inheritance in OOP
#Inheritance is a fundamental concept in OOP that allows a new class (called a child class
#or subclass) to inherit properties and methods from an existing class (called a parent class or superclass). This promotes code reusability and establishes a natural hierarchical relationship between classes.
#write a program to create a class called ElectricCar that inherits from the Car class and has an additional property called battery_size and a method called charge.
class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year) #call the constructor of the parent class
        self.battery_size = battery_size
        
    def charge(self):
        print("The car is charging.")   
#creating an object of the ElectricCar class
my_electric_car = ElectricCar("Tesla", "Model S", 2021, 100)
print(my_electric_car.make) #print the make of the electric car 
print(my_electric_car.model) #print the model of the electric car
print(my_electric_car.year) #print the year of the electric car
print(my_electric_car.battery_size) #print the battery size of the electric car
my_electric_car.start() #call the start method from the parent class
my_electric_car.drive() #call the drive method from the parent class
my_electric_car.charge() #call the charge method from the ElectricCar class

#Polymorphism in OOP
#Polymorphism is a concept in OOP that allows objects of different classes to be treated
#as instances of the same class through a common interface. It enables a single function or method to work with different types of objects, allowing for flexibility and extensibility in code design.
#write a program to create a function called describe_car that takes an object of the Car class
#and prints the make, model and year of the car. Then create an object of the ElectricCar class and pass it
#to the describe_car function.
def describe_car(car):  
    print(f"Car Make: {car.make}, Model: {car.model}, Year: {car.year}")
#creating an object of the Car class
my_car = Car("Honda", "Civic", 2019)
describe_car(my_car) #call the describe_car function with the Car object
#creating an object of the ElectricCar class
my_electric_car = ElectricCar("Nissan", "Leaf", 2020, 40)
describe_car(my_electric_car) #call the describe_car function with the ElectricCar object   
        
#private and protected members in OOP
#In OOP, we can define private and protected members to restrict access to certain attributes and methods of a class. Private members are denoted by a double underscore prefix (__) and can only be accessed within the class. Protected members are denoted by a single underscore prefix (_) and can be accessed within the class and its subclasses.
#write a program to create a class called Person with a private member called __name and a protected member called _age. Then create a subclass called Student that inherits from the Person class and has a method to display the name and age of the student.
class Person:
    def __init__(self, name, age):
        self.__name = name #private member
        self._age = age #protected member
        
    def get_name(self):
        return self.__name #method to access the private member
class Student(Person):
    def display_info(self):
        print(f"Name: {self.get_name()}, Age: {self._age}") #accessing the protected member and private member through a method
#creating an object of the Student class
student = Student("Alice", 20)
student.display_info() #call the display_info method to show the name and age of the student
    
#operator overloading in OOP
#Operator overloading is a feature in OOP that allows us to define the behavior of operators (like +, -, *, etc.) for our custom classes. This means we can specify how these operators should work when applied to objects of our classes, enabling us to use them in a more intuitive and natural way.
#write a program to create a class called Vector that has two properties x and y. Then overload the + operator to add two Vector objects together.
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y) #overloading the + operator to add two Vector objects 
    def __str__(self):
        return f"Vector({self.x}, {self.y})" #method to return a string representation of the Vector object
#creating two Vector objects
vector1 = Vector(2, 3)
vector2 = Vector(4, 5)
#adding the two Vector objects using the overloaded + operator
result_vector = vector1 + vector2
print(result_vector) #print the result of adding the two Vector objects
        
#Constructor and Destructor in OOP
#A constructor is a special method in OOP that is called when an object is created. It is used to initialize the properties of the object. In python, the constructor is defined using the __init__ method. A destructor is a special method that is called when an object is destroyed. It is used to perform any cleanup operations before the object is removed from memory. In python, the destructor is defined using the __del__ method.
#write a program to create a class called Employee with a constructor that initializes the name and salary of the employee. Then create a destructor that prints a message when the object is destroyed.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def __del__(self):
        print(f"Employee {self.name} has been removed from memory.") #message to be printed when the object is destroyed
#creating an object of the Employee class
employee = Employee("John", 50000)
print(f"Employee Name: {employee.name}, Salary: {employee.salary}") #print the name and salary of the employee
del employee #destroy the employee object to trigger the destructor
    
#classes and objects in OOP
#In OOP, a class is a blueprint for creating objects. It defines the properties and methods that the objects created from the class will have. An object is an instance of a class. It is created using the class as a template and can have its own unique values for the properties defined in the class.
#write a program to create a class called Animal with properties like name and species and methods like eat and sleep. Then create an object of the Animal class and call the methods.
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def eat(self):
        print(f"{self.name} is eating.") #method to indicate that the animal is eating
        
    def sleep(self):
        print(f"{self.name} is sleeping.") #method to indicate that the animal is sleeping
#creating an object of the Animal class
    
my_animal = Animal("Leo", "Lion")
print(f"Animal Name: {my_animal.name}, Species: {my_animal.species}") #print the name and species of the animal
my_animal.eat() #call the eat method
my_animal.sleep() #call the sleep method

#data types in OOP
#In OOP, we can use various data types to define the properties of our classes. Common data types include integers, floats, strings, lists, dictionaries, and more. The choice of data type depends on the nature of the property being defined and how it will be used in the class.
#write a program to create a class called Book with properties like title, author, and pages. Then create an object of the Book class and print the properties.
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
#creating an object of the Book class
my_book = Book("To Kill a Mockingbird", "Harper Lee", 281)
print(f"Book Title: {my_book.title}, Author: {my_book.author}, Pages: {my_book.pages}") #print the properties of the book

#Encapsulation in OOP
#Encapsulation is a fundamental principle of OOP that involves bundling the data (attributes) and methods (functions) that operate on the data into a single unit, called a class. It also restricts direct access to some of the object's components, which can prevent the accidental modification of data and promote modularity and maintainability in code.
#write a program to create a class called BankAccount with properties like account_number and balance. Then create methods to deposit and withdraw money from the account, ensuring that the balance cannot go negative.
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}.")
        else:
            print("Deposit amount must be positive.")
            
    def withdraw(self, amount):
        if amount > 0:
            if self.balance - amount >= 0:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.balance}.")
            else:
                print("Insufficient funds. Withdrawal denied.")
        else:
            print("Withdrawal amount must be positive.")
#creating an object of the BankAccount class
my_account = BankAccount("123456789", 1000) 
print(f"Account Number: {my_account.account_number}, Balance: ${my_account.balance}") #print the account number and balance
my_account.deposit(500) #deposit money into the account
my_account.withdraw(200) #withdraw money from the account
my_account.withdraw(1500) #attempt to withdraw more than the balance to test the insufficient funds case

#Abstraction in OOP
#Abstraction is a principle of OOP that focuses on hiding the complex implementation details of a class and exposing only the necessary features to the user. It allows us to create a simple interface for interacting with an object while keeping the underlying complexity hidden from the user.
#write a program to create a class called Shape with an abstract method called area. Then create subclasses called Circle and Rectangle that inherit from the Shape class and implement the area method.
from abc import ABC, abstractmethod
from unicodedata import name
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass #abstract method to be implemented by subclasses
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius ** 2 #implementing the area method for Circle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height #implementing the area method for Rectangle

#creating objects of the Circle and Rectangle classes
my_circle = Circle(5)
my_rectangle = Rectangle(10, 5)

print(f"Circle Area: {my_circle.area()}") #print the area of the circle
print(f"Rectangle Area: {my_rectangle.area()}") #print the area of the rectangle        

#class and instance variables in OOP
#In OOP, class variables are shared among all instances of a class, while instance variables are unique to each instance. Class variables are defined within the class but outside any methods, while instance variables are typically defined within the constructor (the __init__ method) and prefixed with self.
#write a program to create a class called Counter with a class variable called count and an  instance variable called name. Then create a method to increment the count and print the name and count of each instance.


class Counter:
    count = 0 #class variable to keep track of the count of instances
    
    def __init__(self, name):
        self.name = name #instance variable to store the name of the instance
        Counter.count += 1 #increment the class variable count whenever a new instance is created
    def display_count(self):
        print(f"{self.name} Count: {Counter.count}") #method to display the name and count of the instance
#creating instances of the Counter class
counter1 = Counter("Counter 1")
counter2 = Counter("Counter 2")
counter1.display_count() #display the count for counter1
counter2.display_count() #display the count for counter2

#example of a class with a method that uses both class and instance variables
class Employee:
    company_name = "Tech Company" #class variable to store the company name
    
    def __init__(self, name, salary):
        self.name = name #instance variable to store the employee's name
        self.salary = salary #instance variable to store the employee's salary
        
    def display_info(self):
        print(f"Employee Name: {self.name}, Salary: ${self.salary}, Company: {Employee.company_name}") #method to display the employee's information including the class variable   
#creating an instance of the Employee class
employee1 = Employee("Alice", 70000)
employee1.display_info() #display the information of employee1

#example of a class with a method that modifies a class variable
class Counter:
    count = 0 #class variable to keep track of the count of instances
    
    def __init__(self, name):
        self.name = name #instance variable to store the name of the instance
        Counter.count += 1 #increment the class variable count whenever a new instance is created
        
    @classmethod
    def reset_count(cls):
        cls.count = 0 #class method to reset the count to zero
#creating instances of the Counter class
counter1 = Counter("Counter 1") 
counter2 = Counter("Counter 2")
print(f"Current Count: {Counter.count}") #print the current count of instances
Counter.reset_count() #reset the count using the class method
print(f"Count after reset: {Counter.count}") #print the count after resetting
    
#example understanding oops in python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age) #call the constructor of the parent class
        self.student_id = student_id
        
    def display_info(self):
        super().display_info() #call the display_info method of the parent class
        print(f"Student ID: {self.student_id}") #display the student ID
#creating an object of the Student class
student = Student("Bob", 22, "S12345")
student.display_info() #call the display_info method to show the information of the student

       
    
