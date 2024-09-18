'''
The Unix find command allows you to search for files under a given directory. 
You can specify criteria for files you are interested in.

Imagine that you need to write code in a high level language like java, that does things similar to the find command. 
I would like you to focus on 2 uses cases at first.

Find all files over 5 MB somewhere under a directory. 'size constraint'
Find all XML files somewhere under a directory. 'extension constraint'
The design should be maintainable to add new contraints. like 'name constraint' or different size/extension constraint
I would like you to create a library that lets me do this easily.

Follow up: How would you handle if some contraints should support AND, OR conditionals.


思路: 这题用到了
specification pattern: The specification pattern is a design pattern that defines a family of objects that can be combined to represent complex criteria. 
It allows you to create flexible and reusable conditions for filtering, searching, and validating data.

from abc import ABC, abstractmethod

class Specification(ABC):
    @abstractmethod
    def is_satisfied_by(self, target):
        pass

class AndSpecification(Specification):
    def __init__(self, spec1, spec2):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, target):
        return self.spec1.is_satisfied_by(target) and self.spec2.is_satisfied_by(target)

class OrSpecification(Specification):
    def __init__(self, spec1, spec2):
        self.spec1 = spec1
        self.spec2.spec2

    def is_satisfied_by(self, target):
        return self.spec1.is_satisfied_by(target) or self.spec2.is_satisfied_by(target)

class NotSpecification(Specification):
    def __init__(self, spec):
        self.spec = spec

    def is_satisfied_by(self, target):
        return not self.spec.is_satisfied_by(target)

# Example usage
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

# Concrete specifications
class PriceGreaterThan100(Specification):
    def is_satisfied_by(self, product):
        return product.price > 100

class CategoryEqualsElectronics(Specification):
    def is_satisfied_by(self, product):
        return product.category == "electronics"

# Composite specifications
expensive_electronics = AndSpecification(PriceGreaterThan100(), CategoryEqualsElectronics())
cheap_or_electronics = OrSpecification(PriceLessThan50(), CategoryEqualsElectronics())

# Filtering products
products = [
    Product("Laptop", 1200, "electronics"),
    Product("Book", 20, "books"),
    Product("Smartphone", 800, "electronics"),
    Product("T-shirt", 30, "clothing"),
]

filtered_products_expensive_electronics = filter(expensive_electronics.is_satisfied_by, products)
filtered_products_cheap_or_electronics = filter(cheap_or_electronics.is_satisfied_by, products)

'''
from abc import ABC, abstractmethod
from enum import Enum
from collections import deque
from typing import Optional

# If it is a file system, we can use FileSystemEntry to represent a common class for both File and Directory
# But to simplify we can just use a File class
class FileSystemEntry:
    def __init__(self, name: str, path: str) -> None:
        self.name = name
        self.path = path
    
    def get_full_path(self) -> str:
        return f'{self.path}/{self.name}'

class File(FileSystemEntry):
    def __init__(self, name: str, path: str, size: int, extension: str) -> None:
        super().__init__(name, path)
        self.extension = extension
        self.size = size

class Directory(FileSystemEntry):
    def __init__(self, name: str, path: str, content: Optional[list[FileSystemEntry]] = None) -> None:
        super().__init__(name, path)
        self.content = content

class Filter(ABC): # In java this would be an interface. ABCs are classes that cannot be instantiated directly but serve as blueprints for other classes. 
                   # They define a set of methods that subclasses must implement.
    @abstractmethod
    def is_matched(self, file: File):
        pass

class Operator(Enum):
    EQUAL = 0
    GREATER_THAN = 1
    LESS_THAN = 2

class SizeFilter(Filter):
    def __init__(self, operator: Operator, size: int):
        self.operator = operator
        self.size = size
    
    def is_matched(self, file: File):
        if self.operator == Operator.EQUAL:
            return file.size == self.size
        elif self.operator == Operator.GREATER_THAN:
            return file.size > self.size
        else:
            return file.size < self.size

class ExtensionFilter(Filter):
    def __init__(self, extension: str):
        self.extension = extension
    
    def is_matched(self, file: File):
        return self.extension == file.extension

class AndFilter(Filter):
    def __init__(self, filters: list[Filter]):
        self.filters = filters
    
    def is_matched(self, file: File):
        return all(f.is_matched(file) for f in self.filters)

class OrFilter(Filter):
    def __init__(self, filters: list[Filter]):
        self.filters = filters
    
    def is_matched(self, file: File):
        return any(f.is_matched(file) for f in self.filters)

class LinuxFileFinder:
    def find_filtered_files(self, root_dir: Directory, filter: Optional[Filter]) -> list[File]:
        queue = deque()
        queue.append(root_dir)
        filtered_files = []
        while queue:
            cur_dir = queue.popleft()
            for fs_entry in cur_dir.content:
                if isinstance(fs_entry, Directory):
                    queue.append(fs_entry)
                else:
                    if filter and filter.is_matched(fs_entry):
                        filtered_files.append(fs_entry)
                    elif not filter:
                        filtered_files.append(fs_entry)

        return filtered_files

root_dir = Directory('documents', 'home/user')
file1 = File('example1.xml', 'home/user/documents', 4, 'xml')
file2 = File('example2.xml', 'home/user/documents', 5, 'xml')
dir1 = Directory('monday', 'home/user/documents')
dir2 = Directory('tuesday', 'home/user/documents')
root_dir.content = [file1, file2, dir1, dir2]

file3 = File('example3.xml', 'home/user/documents/monday', 6, 'xml')
file4 = File('example4.pdf', 'home/user/documents/monday', 7, 'pdf')
dir1.content = [file3, file4]

file5 = File('example5.xml', 'home/user/documents/tuesday', 3, 'xml')
file6 = File('example6.xml', 'home/user/documents/tuesday', 7, 'xml')
dir2.content = [file5, file6]

file_finder = LinuxFileFinder()
greater_than_4 = SizeFilter(Operator.GREATER_THAN, 4)
xml_filter = ExtensionFilter('xml')
xml_files_greater_than_4 = AndFilter([xml_filter, greater_than_4])
files_filtered = file_finder.find_filtered_files(root_dir, xml_files_greater_than_4)
for file in files_filtered:
    print(f'path: {file.get_full_path()}, size: {file.size}, extension: {file.extension}')