#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Rectangle:
    """Create a rectangle!"""

    def __init__(self: object, width: float, height: float) -> None:
        """
        Initialize rectangle, setting width and height.

        :width: rectangle's width -> float
        :height: rectangle's height -> float
        :returns: None
        """
        self.set_width(width)
        self.set_height(height)

    def set_width(self: object, width: float) -> None:
        """
        Set object's width

        :width: object's width
        :returns: None
        """
        self.width = width

    def set_height(self, height):
        """
        Set object's height

        :height: object's height
        :returns: None
        """
        self.height = height

    def get_area(self: object) -> float:
        """
        Get object's area
        :returns: area -> float
        """
        width = self.width
        height = self.height
        return width * height

    def get_perimeter(self: object) -> float:
        """
        Get object's perimeter
        :returns: perimeter -> float
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
            if line < height - 1:
                msg += '\n'

        return msg
        
class Square(Rectangle):
    pass

if __name__ == "__main__":
    rect = Rectangle(3, 4)
    print(rect.get_area())
    print(rect.get_perimeter())
    print(rect.get_diagonal())
    print(rect.get_picture())
