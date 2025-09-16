""" 
Create a class hierarchy:

    Base class Vehicle with attributes: brand, model, year
    Derived class Car with additional attribute: number_of_doors
    Implement a method get_info() in both classes

"""

class vehicle:
    def __init__(self,brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        
    def getinfo(self,brand, model, year):
        return f"This car is{self.brand} the module is {self.model}! ({self.year})"
    
class car(vehicle):
    def __init__(self, brand, model, year, number_of_doors):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors
    
    def getinfo(self):
        return f"This is{self.brand} the module is form {self.model}! ({self.year}) have{self.number_of_doors}doors!"
Minecart = car(" Minecart" , "Minecraft", " 2014 ", " 4 ")
print(Minecart.getinfo())
