#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Rectangle:
    """
    Create a rectangle with `width` and `height` dimensions.
    """

    def __init__(self: object, width: float, height: float) -> None:
        """
        Initialize rectangle, setting width and height.

        :width: rectangle's width -> float
        :height: rectangle's height -> float
        :returns: None
        """
        self.set_width(width)
        self.set_height(height)
        self.name = 'Rectangle'

    def __str__(self: object):
        """
        Print object's information, ie, name of class, width and height
        :returns: str
        """
        return f'{self.name}(width={self.width}, height={self.height})'

    def set_width(self: object, width: int) -> None:
        """
        Set object's width

        :width: object's width
        :returns: None
        """
        self.width = width

    def set_height(self: object, height: int) -> None:
        """
        Set object's height

        :height: object's height
        :returns: None
        """
        self.height = height

    def get_area(self: object) -> int:
        """
        Get object's area
        :returns: area -> int
        """
        width = self.width
        height = self.height
        return width * height

    def get_perimeter(self: object) -> int:
        """
        Get object's perimeter
        :returns: perimeter -> int
        """
        width = self.width
        height = self.height
        return 2 * (width + height)

    def get_diagonal(self: object) -> float:
        """
        Get object's diagonal
        :returns: diagonal -> float
        """
        width = self.width
        height = self.height
        return (width ** 2 + height ** 2) ** (0.5)

    def get_picture(self: object) -> str:
        """
        Returns a string that represents the shape using lines of "*". 
        The number of lines is equal to the height and the number of "*" in each 
        line is equal to the width. If the width or height is larger than 50, 
        return the string: "Too big for picture."

        :returns: picture or message -> str
        """
        width = self.width
        height = self.height
        
        if width > 50 or height > 50:
            return 'Too big for picture.'

        msg = ''
        for line in range(0, height):
            for col in range(0, width):
                msg += '*'
            msg += '\n'

        return msg

    def get_amount_inside(self: object, shape: object) -> int:
        """
        Returns the number of times the passed in `shape` 
        could fit inside the object.

        :shape: another object to compare with -> object
        :returns: integer division of this object's area
        and `shape` area -> int
        """
        return self.get_area() // shape.get_area()
        

class Square(Rectangle):
    """
    Inherits properties from `Rectangle` object, creating a
    Square with a single side length passed in.
    """

    def __init__(self: object, side: int) -> None:
        self.set_width(side)
        self.set_height(side)
        self.name = 'Square'

    def __str__(self: object) -> None:
        """
        Print object's information, ie, name of class and side length
        :returns: str
        """
        return f'{self.name}(side={self.width})'

    def set_side(self: object, side: int) -> None:
        """
        Define both `width` and `height` attributes with `side` value.

        :side: square length
        :returns: None
        """
        self.set_width(side)
        self.set_height(side)


if __name__ == "__main__":
    rect = Rectangle(10, 5)
    print(rect.get_area())
    rect.set_height(3)
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())

    sq = Square(9)
    print(sq)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())
