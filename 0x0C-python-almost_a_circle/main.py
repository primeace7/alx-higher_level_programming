#!/usr/bin/python3

from models.base import Base
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(33, 3, 4, 5)
    dictionary2 = r2.to_dictionary()
    dictionary = r1.to_dictionary()
    json_dictionary = Base.to_json_string([dictionary, dictionary2])
    print(dictionary)
    print(type(dictionary))
    print(json_dictionary)
    print(type(json_dictionary))
    print(r1._name())
