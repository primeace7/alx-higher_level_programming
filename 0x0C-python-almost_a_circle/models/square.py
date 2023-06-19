#!/usr/bin/python3

'''
Define a square shape implementation
'''

from .rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                elif i ==2:
                    self.x = args[i]
                elif i ==3:
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
        items = {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
        return items
