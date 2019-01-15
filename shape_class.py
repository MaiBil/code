"""
Shape Area and Perimeter Classes - Create an abstract
class called Shape and then inherit from it other shapes
like diamond, rectangle, circle, triangle etc. Then have
each class override the area and perimeter functionality
to handle each shape type.
"""
from math import pi


class Shape:

    def __init__(self):
        self.area = area
        self.perimeter = perimeter

    def area(self):
        pass

    def perimeter(self):
        pass


class Rectangle(Shape):

    def __init__(self, width, hight):
        self.width = width
        self.hight = hight

    def area(self):
        return self.width*self.hight

    def perimeter(self):
        return 2 * (self.width + self.hight)


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi*((self.radius)**2)

    def perimeter(self):
        return 2*pi*self.radius


class Triangle(Shape):

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.s = (side1 + side2 + side3)/2

    def area(self):
        return (self.s*(self.s-self.side1)*(self.s-self.side2)*(self.s-self.side3))**(1/2)

    def perimeter(self):
        return self.side1 + self.side2 + self.side3


if __name__ == '__main__':
    print("We are going to calculate the perimeter or area of any of these figures: Circle, Triangle, Rectangle.")
    while True:
        while True:
            ask_shape = (input("Is your shape a Circle, a Rectangle or a Triangle? "))[0].lower()
            if ask_shape == "c" or ask_shape == "r" or ask_shape == "t":
                break
            else:
                print("That's not a valid shape! Try again ")
                continue

        if ask_shape == "c":
            rad = int(input("What's the radius of the Circle? "))
            myshape = Circle(rad)
            the_shape = "circle"
        elif ask_shape == "r":
            wid = int(input("What's the widht of the rectangle? "))
            hid = int(input("And the hight? "))
            myshape = Rectangle(wid, hid)
            the_shape = "rectangle"
        elif ask_shape == "t":
            s1 = int(input("How long is the first side of the triangle? "))
            s2 = int(input("And the second? "))
            s3 = int(input("And the third? "))
            myshape = Triangle(s1, s2, s3)
            the_shape = "triangle"

        while True:
            ask_area_or_perim = (input("Do you want to calculate the area or perimeter? "))[0].lower()
            if ask_area_or_perim == "a" or ask_area_or_perim == "p":
                break
            else:
                print("That's not a valid answer! Try again ")
                continue

        if ask_area_or_perim == "a":
            print(f"The area of your {the_shape} is {myshape.area()}\n")
        elif ask_area_or_perim == "p":
            print(f"The perimeter of your {the_shape} is {myshape.perimeter()}\n")

        again = input("Do you want to calculate another shape? Y/N ")
        if again.upper()[0] == "Y":
            continue
        else:
            break
