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
        '''
        init doc is above
        all arg descriptions are in the class docstring
        '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''
        getter for the width attribute of Rectangle instance

        Args(for setter):
        num(int): the value to set the Rectangle instance's width to

        Raises(for setter):
        TypeError: num is not an int type
        ValueError: num <= 0
        '''
        return self.__width

    @width.setter
    def width(self, num):
        '''
        setter doc is in getter method
        all arg descriptions are in the getter
        '''
        if not isinstance(num, int):
            raise TypeError('width must be an integer')
        if num <= 0:
            raise ValueError('width must be > 0')

        self.__width = num

    @property
    def height(self):
        '''
        getter for the height attribute of Rectangle instance

        Args(for setter):
        val(int): the value to set the Rectangle instance's height to

        Raises(for setter):
        TypeError: val is not an int type
        ValueError: val <= 0
        '''
        return self.__height

    @height.setter
    def height(self, val):
        '''
        setter doc is in getter method
        all arg descriptions are in the getter
        '''
        if not isinstance(val, int):
            raise TypeError('height must be an integer')
        elif val <= 0:
            raise ValueError('height must be > 0')
        self.__height = val

    @property
    def x(self):
        '''
        getter for the x coordinate of Rectangle instance

        Args(for setter):
        val(int): the value to set the Rectangle instance's x coordiante to

        Raises(for setter):
        TypeError: val is not an int type
        ValueError: val < 0
        '''
        return self.__x

    @x.setter
    def x(self, val):
        '''
        setter doc is in getter method
        all arg descriptions are in the getter
        '''
        if not isinstance(val, int):
            raise TypeError('x must be an integer')
        elif val < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = val

    @property
    def y(self):
        '''
        getter for the y coordinate of Rectangle instance

        Args(for setter):
        val(int): the value to set the Rectangle instance's y coordiante to

        Raises(for setter):
        TypeError: val is not an int type
        ValueError: val < 0
        '''
        return self.__y

    @y.setter
    def y(self, val):
        '''
        setter doc is in getter method
        all arg descriptions are in the getter
        '''
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
        '''
        update the attributes of a Rectangle instance
        The corresponding attributes are assigned from args or kwargs
        '''
        if len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.__width = args[i]
                elif i == 2:
                    self.__height = args[i]
                elif i == 3:
                    self.__x = args[i]
                elif i == 4:
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
        f1 = f'[Rectangle] ({self.id}) {self.__x}/{self.__y}'
        return f'{f1} - {self.__width}/{self.__height}'

    def to_dictionary(self):
        '''
        Convert a Rectangle instance to dictionary equivalent

        Returns:
        (dict): a dictionary equivalent of the Rectangle instance
        '''
        (dict): a dictionary equivalent containing all the instance details
        items = {'id': self.id, 'width': self.__width}
        items2 = {'height': self.__height, 'x': self.__x, 'y': self.__y}
        items |= items2
        return items
