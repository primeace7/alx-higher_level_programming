#!/usr/bin/python3

'''
Define a class that implements a rectangle
'''

from .base import Base


class Rectangle(Base):
    '''
    Implement a rectangle plane shape

    Args:
    x(int): the x coordinate of the rectangle
    y:(int): the y coordinante of the rectangle
    width(int): the rectangle width
    height(int): the rectangle height

    Attributes:
    x(int): the x coordinate of the rectangle
    y:(int): the y coordinante of the rectangle
    width(int): the rectangle width
    height(int): the rectangle height
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, num):
        if not isinstance(num, int):
            raise TypeError('width must be an integer')
        if num <= 0:
            raise ValueError('width must be > 0')

        self.__width = num

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, val):
        if not isinstance(val, int):
            raise TypeError('height must be an integer')
        elif val <= 0:
            raise ValueError('height must be > 0')
        self.__height = val

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        if not isinstance(val, int):
            raise TypeError('x must be an integer')
        elif val < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = val

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        if not isinstance(val, int):
            raise TypeError('y must be an integer')
        elif val < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = val

    def area(self):
        '''
        calculate rectangle area

        Returns:
        int: area of the rectangle
        '''
        return self.__width * self.__height

    def display(self):
        '''
        display the rectangle by printing #s
        '''
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for a in range(self.__x):
                print(' ', end='')
            for j in range(self.__width):
                print('#', end='')
            print()

    def update(self, *args, **kwargs):
        if len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.__width = args[i]
                elif i == 2:
                    self.__height = args[i]
                elif i ==3:
                    self.__x = args[i]
                elif i ==4:
                    self.__y = args[i]
                else:
                    break

        if len(kwargs) != 0 and len(args) == 0:
            for key, val in kwargs.items():
                if key == 'width':
                    self.__width = val
                elif key == 'height':
                    self.__height = val
                elif key == 'x':
                    self.__x = val
                elif key == 'y':
                    self.__y = val
                elif key == 'id':
                    self.id = val
                else:
                    break

    def __str__(self):
        return f'[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}'

    def to_dictionary(self):
        items = {'id': self.id, 'width': self.__width, 'height': self.__height,\
                 'x': self.__x, 'y': self.__y}
        return items
