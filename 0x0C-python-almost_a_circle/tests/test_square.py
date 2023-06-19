from models.square import Square
import unittest

class TestSquare(unittest.TestCase):
    def test_init(self):
        self.square1 = Square(7, 1, 1, 6)
        self.assertEqual(self.square1.id, 6)

        self.square2 = Square(7, 1, 1, 34)
        self.assertEqual(self.square2.id, 34)

    def test_attributes(self):
        with self.assertRaises(TypeError):
            self.square1 = Square('width', 5, 1, 1)
            self.square2 = Square(7, 'height', 1, 1)
            self.square3 = Square(7, 5, ['x'], 1)
            self.square4 = Square(7, 5, 1, ('y',))

        with self.assertRaises(ValueError):
            self.square1 = Square(-7, 5, 1, 1)
            self.square2 = Square(7, -5, 1, 1)
            self.square3 = Square(7, 5, -1, 1)
            self.square5 = Square(0, 5, 1, 1)

    def test_str(self):
        self.square_1 = Square(9, 2, 3, 8)
        sqr1 = str(self.square_1)
        self.assertEqual(sqr1, '[Square] (8) 2/3 - 9')

        self.square_2 = Square(8, 1, 3, 65)
        sqr2 = str(self.square_2)
        self.assertEqual(sqr2, f'[Square] (65) 1/3 - 8')

    def test_size(self):
        self.square1 = Square(7, 0, 0, 4)
        self.assertEqual(str(self.square1), '[Square] (4) 0/0 - 7')

        self.square1.size = 9
        self.assertEqual(str(self.square1), '[Square] (4) 0/0 - 9')

        with self.assertRaises(TypeError):
            self.square1.size = 'two'
            self.square1.size = 6.5
            self.square1.size = [7, 5]
            self.square1.size = (6,8,7)

        with self.assertRaises(ValueError):
            self.square1.size = -7
            self.square1.size = -8
            self.square1.size = 0

    def test_update(self):
        self.square1 = Square(8, 3, 3, 22)

        self.square1.update(26)
        self.assertEqual(str(self.square1), '[Square] (26) 3/3 - 8')

        self.square1.update(23, 16)
        self.assertEqual(str(self.square1), '[Square] (23) 3/3 - 16')

        self.square1.update(19, 11, 1, 1)
        self.assertEqual(str(self.square1), '[Square] (19) 1/1 - 11')

        self.square1.update(size=33, y=6, x=6, id=97)
        self.assertEqual(str(self.square1), '[Square] (97) 6/6 - 33')

        self.square1.update(y=8)
        self.assertEqual(str(self.square1), '[Square] (97) 6/8 - 33')

    def test_to_dictionary(self):
        self.square1 = Square(size=9, id=88, x=3, y=4)
        dictionary1 = {'id': 88, 'size': 9, 'x': 3, 'y': 4}
        square1_dict = self.square1.to_dictionary()

        self.assertDictEqual(dictionary1, square1_dict)
        self.assertEqual(len(dictionary1), 4)
