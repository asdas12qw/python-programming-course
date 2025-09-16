"""
Write a Python class Rectangle with:

Private attributes for length and width
Methods to calculate area (getArea()) and perimeter getPerimeter())
A method to check if it's a square (isSquare())

"""

class rectangle:
    def __init__(self,lenght,width):
        self.__lenght = lenght
        self.__width = width

    def getArea(self):
        area = self.__lenght * self.__width
        return f"Area={area}"
    
    def getperamiter(self):
        peramiter = 2* (self.__lenght + self.__width)
        return f"peramiter = {peramiter}"
    
    def isSquare(self):
        if self.__width == self.__lenght :
            return F"This rectangle is square idiot!"
        else:
            return f"This rectangle is Not square idiot!"
rectangle = rectangle(10,15)
print(rectangle.getArea())
print(rectangle.getperamiter())
print(rectangle.isSquare())
