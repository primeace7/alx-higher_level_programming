#!/usr/bin/python3

'''
Define a square shape implementation
    The square class inherits from the Rectangle class
'''

from .rectangle import Rectangle


class Square(Rectangle):
    '''
    Implement a square class the derives from the rectangle class

    Args:
    size(int): this is the lenght of the square. it's equivalent to
        the widht or height of the rectangle class. In fact, the size
        is set to the width attribute of the square since it derives from
        the rectangle class.
    x(int): the x coordinate of the rectangle in a cartesian plane
    y(int): the y coordinate of the rectangle in a cartesian plane
    id(int): the id number of the square

    Attributes:
    size(int): the dimension of the square
    x(int): the x coordinate of the square
    y(int): the y coordinate of the square
    id(int): the id number of the square
    '''

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'

    @property
    def size(self):
        '''
        getter for the size attribute of Square instance
            for a square instance, the size is same as the width
            or height of a rectangle instance. The setter validates
            the input using the logic of the inherited Rectangle class

        Args(for setter):
        value(int): the value to set the Square instance's size to

        Raises:
        TypeError: num is not an int type
        ValueError: num <= 0
        '''
        return self.width

    @size.setter
    def size(self, value):
        '''
        setter doc is in getter method
            all args are defined in the getter
        '''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''
        update the attributes of a Rectangle instance
            The corresponding attributes are assigned from args or kwargs
            The id, width, height, x, and y attributes can all be updated
            depending on the values passed to the function
        '''
        if len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]
                else:
                    break

        if len(kwargs) != 0 and len(args) == 0:
            for key, val in kwargs.items():
                if key == 'size':
                    self.width = val
                elif key == 'x':
                    self.x = val
                elif key == 'y':
                    self.y = val
                elif key == 'id':
                    self.id = val
                else:
                    continue

    def to_dictionary(self):
        '''
        convert a square instance to a dictionary representation

        Returns:
        (dict): a dictionary equivalent of the Square instance
        '''
        items = {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
        return items
