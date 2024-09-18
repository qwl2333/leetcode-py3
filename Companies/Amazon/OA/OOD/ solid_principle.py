'''
SOLID https://realpython.com/solid-principles-python/

1. Single-Responsibility Principle
One class has only one responsbility as express through its methods

class FileManager:
    def read
    def write
    def compress
    def decompress

this is against Single-Responsibility Principle
updated to:

class FileManager:
    def read
    def write

class ZipFileManager:
    def compress
    def decompress


2. Open-Closed Principle
(classes, modules, functions, etc) are open for extension but close for modification

class Shape:
    def __init__(self, shape_type, **kwargs):
        self.shape_type = shape_type
        if self.shape_type == "rectangle":
            self.width = kwargs["width"]
            self.height = kwargs["height"]
        elif self.shape_type == "circle":
            self.radius = kwargs["radius"]

    def calculate_area(self):
        if self.shape_type == "rectangle":
            return self.width * self.height
        elif self.shape_type == "circle":
            return pi * self.radius**2

If we want to add a new shape besides rectangle and circle, let's say square.
Adding it by add elif statement is against Open-Closed Principle.
One possible solution is,
class Shape(ABC):
    def __init__(self, shape_type):
        self.shape_type = shape_type

    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("circle")
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius**2

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("rectangle")
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        super().__init__("square")
        self.side = side

    def calculate_area(self):
        return self.side**2

        
3. Liskov Substitution Principle (父可被子换)
Subtypes must be substitutable for their base types. 

For example, if you have a piece of code that works with a Shape class, 
then you should be able to substitute that class with any of its subclasses, 
such as Circle or Rectangle, without breaking the code.



4. Interface Segregation Principle (ISP) 
If a class doesn't use particular methods or attributes, 
then those methods and attributes should be segregated into more specific classes.

from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def fax(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass

class OldPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in black and white...")

    def fax(self, document):
        raise NotImplementedError("Fax functionality not supported")

    def scan(self, document):
        raise NotImplementedError("Scan functionality not supported")

class ModernPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in color...")

    def fax(self, document):
        print(f"Faxing {document}...")

    def scan(self, document):
        print(f"Scanning {document}...")

OldPrinter does not use fax and scan, need to change to
class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

class Fax(ABC):
    @abstractmethod
    def fax(self, document):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass

class OldPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in black and white...")

class NewPrinter(Printer, Fax, Scanner):
    def print(self, document):
        print(f"Printing {document} in color...")

    def fax(self, document):
        print(f"Faxing {document}...")

    def scan(self, document):
        print(f"Scanning {document}...")

      
5. Dependency Inversion Principle
abstraction should not depend on details. Details should depend on abstractions.

class FrontEnd:
    def __init__(self, back_end):
        self.back_end = back_end

    def display_data(self):
        data = self.back_end.get_data_from_database()
        print("Display data:", data)

class BackEnd:
    def get_data_from_database(self):
        return "Data from the database"

这里不好是因为FrontEnd depend on a concrete class BackEnd to get data from database. 如果现在换成api取数据怎么办
也许可以在FrontEnd class 里面加一个method, 但是违背了open-closed principle因为修改了FrontEnd class. 所以最好是depend on
abstraction, 用一个DataSource interface来代替concrete class

class FrontEnd:
    def __init__(self, data_source):
        self.data_source = data_source

    def display_data(self):
        data = self.data_source.get_data()
        print("Display data:", data)

class DataSource(ABC):
    @abstractmethod
    def get_data(self):
        pass

class Database(DataSource):
    def get_data(self):
        return "Data from the database"

class API(DataSource):
    def get_data(self):

'''