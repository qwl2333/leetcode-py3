'''
https://csoahelp.com/2024/08/19/%E4%BA%9A%E9%A9%AC%E9%80%8A%E9%9D%A2%E8%AF%95ood%E7%9C%9F%E9%A2%98%EF%BC%9Apizza-%E4%BB%B7%E6%A0%BC%E8%AE%A1%E7%AE%97%E5%99%A8-%E6%8A%80%E6%9C%AF%E8%A7%A3%E6%9E%90-amazon-interview/

Write a program that allows the user to calculate the price of a pizza. A pizza has:

a base
a size
toppings
Assume the system stores everything in-memory, no storage required.

clarifications:
Before jumping into the coding, some questions need to be clarified:

Size Categories: What are the specific sizes, and how are their prices scaled? Can we assume small, medium, and large, with price factors like small = 0.8x, medium = 1.5x, and large = 2x the base price?
Base Options: Will there be different options for the base, such as thin crust, thick crust, or gluten-free?
Topping Choices: Will the toppings include options like cheese, pepperoni, mushrooms, and other standard choices? Additionally, will each topping have a fixed cost?
After receiving confirmation from the interviewer, the assumptions were set as follows:

The sizes will follow a price factor, where:
Small = 0.8x the base price,
Medium = 1.5x the base price,
Large = 2x the base price.
The base options will have fixed prices:
Thin Crust = $5,
Thick Crust = $7,
Gluten-Free = $6.
Each topping will have a predefined cost:
Cheese = $2,
Pepperoni = $3,
Mushrooms = $1.5,
Onions = $1,
Olives = $1.2.

所需用到的design pattern:
decorator design pattern

class Coffee:
    def cost(self):
        return 2.0  # Base coffee price

class Milk(Coffee):
    def cost(self):
        return super().cost() + 0.5

class ChocolateSyrup(Coffee):
    def cost(self):
        return super().cost() + 0.3

class WhippedCream(Coffee):
    def cost(self):
        return super().cost() + 0.2

第一反应是用enum表示不同的types的coffee


第一反应是用enum表示不同的types的pizza
以下是不用decorator design pattern的解法
坏处是必须预先设定好所有的toppings, 中途不能更改
但是decorator design pattern可以慢慢的一个topping一个topping的加, 而且每次加完都可以算price
而且价格是enum非常反设计尝试, 因为价格会一直变
from enum import Enum

class Size(Enum):
    SMALL, MEDIUM, LARGE = 0.8, 1, 1.2

class BASE(Enum):
    THIN, THICK, GLUTEN_FREE = 1, 2, 3

class Topping(Enum):
    CHEESE, PEPPERONI, MUSHROOMS, ONIONS = 2, 3, 4, 2

class Pizza:
    def __init__(self, size: Size, base: BASE, toppings: list[Topping] = []):
        self.size = size
        self.base = base
        self.toppings = toppings
    
    def calculate_price(self) -> float:
        price = self.base
        for topping in self.toppings:
            price += topping
        
        return price * self.size
'''


# 采用 decorator design pattern
from abc import ABC, abstractmethod
from enum import Enum

class Size(Enum):
    SMALL, MEDIUM, LARGE = 0.5, 1, 1.5

class Pizza(ABC):
    def __init__(self, size, price):
        self.size = size
        self.price = price

    def get_size_factor(self) -> float:
        return float(self.size.value)

    @abstractmethod
    def get_cost(self) -> float:
        pass

class ThinCrustPizza(Pizza):
    def get_cost(self):
        return self.price * self.get_size_factor()
    
class ThickCrustPizza(Pizza):
    def get_cost(self):
        return self.price * self.get_size_factor()

class Cheese(Pizza):
    def __init__(self, price: float, pizza: Pizza):
        super().__init__(pizza.size, price)
        self.pizza = pizza

    def get_cost(self):
        return self.pizza.get_cost() + self.price * self.get_size_factor()


class Pepperoni(Pizza):
    def __init__(self, price: float, pizza: Pizza):
        super().__init__(pizza.size, price)
        self.pizza = pizza

    def get_cost(self):
        return self.pizza.get_cost() + self.price * self.get_size_factor()
    

class Mushroom(Pizza):
    def __init__(self, price: float, pizza: Pizza):
        super().__init__(pizza.size, price)
        self.pizza = pizza

    def get_cost(self):
        return self.pizza.get_cost() + self.price * self.get_size_factor()


cheese_mushroom_pizza = ThinCrustPizza(Size.MEDIUM, 5)
cheese_mushroom_pizza = Cheese(2, cheese_mushroom_pizza)
cheese_mushroom_pizza = Cheese(2, cheese_mushroom_pizza)
cheese_mushroom_pizza = Mushroom(1, cheese_mushroom_pizza)
print(cheese_mushroom_pizza.get_cost())

'''
questions to clarify:
can customers order double toppings?
can customers order a pizza without any toppings?
'''

