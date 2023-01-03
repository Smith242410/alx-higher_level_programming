#!/usr/bin/python3
"""Defines a class Rectangle"""

class Rectangle:
    """Represents a Rectangle"""

    def __init__(self, width=0, height=0):
    """Creates an instance of the Rectangle.

        Args:
            width (int): defines the width of the rectangle.
            height (int): defines the height of the rectangle."""
        self.width = width
        self.height = height

    @property
    """Gets the width of the Rectangle"""

    def width(self):
        return self.__width

    @width.setter
    """Sets the width of the Rectangle"""

    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    """Gets the height of the Rectangle"""

    def height(self):
        return self.__height

    @height.setter
    """Sets the value of the Rectangle"""

    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
