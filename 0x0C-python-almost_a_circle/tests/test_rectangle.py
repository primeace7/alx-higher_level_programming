import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_init(self):
        self.rectangle1 = Rectangle(7, 5, 1, 1, 6)
        self.assertEqual(self.rectangle1.id, 6)

        self.rectangle2 = Rectangle(7, 5, 1, 1, 34)
        self.assertEqual(self.rectangle2.id, 34)

    def test_init2(self):
        with self.assertRaises(TypeError):
            self.rectangle1 = Rectangle('width', 5, 1, 1)
            self.rectangle2 = Rectangle(7, 'height', 1, 1)
            self.rectangle3 = Rectangle(7, 5, ['x'], 1)
            self.rectangle4 = Rectangle(7, 5, 1, ('y',))

        with self.assertRaises(ValueError):
            self.rectangle1 = Rectangle(-7, 5, 1, 1)
            self.rectangle2 = Rectangle(7, -5, 1, 1)
            self.rectangle3 = Rectangle(7, 5, -1, 1)
            self.rectangle4 = Rectangle(7, 5, 1, -1)
            self.rectangle5 = Rectangle(0, 5, 1, 1)
            self.rectangle6 = Rectangle(7, 0, 1, 1)

    def test_attribute_setters(self):
        self.rectangle1 = Rectangle(9, 5, 1, 1, 6)

        self.rectangle1.width = 8
        self.assertEqual(str(self.rectangle1), '[Rectangle] (6) 1/1 - 8/5')

        self.rectangle1.height = 4
        self.assertEqual(str(self.rectangle1), '[Rectangle] (6) 1/1 - 8/4')

        self.rectangle1.x = 2
        self.assertEqual(str(self.rectangle1), '[Rectangle] (6) 2/1 - 8/4')

        self.rectangle1.y = 3
        self.assertEqual(str(self.rectangle1), '[Rectangle] (6) 2/3 - 8/4')

        self.rectangle1.id = 98
        self.assertEqual(str(self.rectangle1), '[Rectangle] (98) 2/3 - 8/4')

    def test_attribute_setters2(self):
        self.rectangle1 = Rectangle(6, 8, 4, 4, 55)

        with self.assertRaises(TypeError):
            self.rectangle1.width = 22.5
            self.rectangle1.width = 'eight'
            self.rectangle1.height = [5, 6]
            self.rectangle1.height = (9,7)
            self.rectangle1.y = 6.7
            self.rectangle1.width = (5,6)

        with self.assertRaises(ValueError):
            self.rectangle1width = -8
            self.rectangle1.height = -22
            self.rectangle1.x = -7
            self.rectangle1.y = -1
            self.rectangle1.width = 0
            self.rectangle1.height = 0

    def test_attribute_getter(self):
        self.rectangle1 = Rectangle(12, 7, 2, 3, 41)

        self.assertEqual(self.rectangle1.width, 12)
        self.assertEqual(self.rectangle1.height, 7)
        self.assertEqual(self.rectangle1.x, 2)
        self.assertEqual(self.rectangle1.y, 3)
        self.assertEqual(self.rectangle1.id, 41)

    def test_area(self):
        self.rectangle_1 = Rectangle(8, 5, 1, 1)
        area1 = self.rectangle_1.area()
        self.assertEqual(area1, 40)

        self.rectangle_2 = Rectangle(7, 6, 1, 1, 3)
        area2 = self.rectangle_2.area()
        self.assertEqual(area2, 42)

    def test_str(self):
        self.rectangle_1 = Rectangle(9, 6, 2, 3, 8)
        rect1 = str(self.rectangle_1)
        self.assertEqual(rect1, '[Rectangle] (8) 2/3 - 9/6')

        self.rectangle_2 = Rectangle(8, 4, 1, 3, 65)
        rect2 = str(self.rectangle_2)
        self.assertEqual(rect2, f'[Rectangle] (65) 1/3 - 8/4')

    def test_update_0(self):
        self.rectangle_1 = Rectangle(5, 6, 2, 2, 54)
        str_rectangle_1 = str(self.rectangle_1)
        self.assertEqual(str_rectangle_1, '[Rectangle] (54) 2/2 - 5/6')

        self.rectangle_1.update(77)
        self.assertEqual(str(self.rectangle_1), '[Rectangle] (77) 2/2 - 5/6')

        self.rectangle_1.update(77, 7)
        self.assertEqual(str(self.rectangle_1), '[Rectangle] (77) 2/2 - 7/6')

        self.rectangle_1.update(77, 7, 10)
        self.assertEqual(str(self.rectangle_1), '[Rectangle] (77) 2/2 - 7/10')

        self.rectangle_1.update(77, 7, 10, 4)
        self.assertEqual(str(self.rectangle_1), '[Rectangle] (77) 4/2 - 7/10')

        self.rectangle_1.update(77, 7, 10, 4, 5)
        self.assertEqual(str(self.rectangle_1), '[Rectangle] (77) 4/5 - 7/10')

    def test_update_1(self):
        self.rectangle_1 = Rectangle(6, 7, 2, 2, 33)

        self.rectangle_1.update(width=14)
        self.assertEqual(str(self.rectangle_1), '[Rectangle] (33) 2/2 - 14/7')

        self.rectangle_1.update(height=10, id=51)
        self.assertEqual(str(self.rectangle_1), '[Rectangle] (51) 2/2 - 14/10')

        self.rectangle_1.update(width=15, height=11, x=3, y=7, id=89)
        self.assertEqual(str(self.rectangle_1), '[Rectangle] (89) 3/7 - 15/11')

    def test_to_dictionary(self):
        self.rec1 = Rectangle(width=9, height=12, id=88, x=3, y=4)
        dictionary1 = {'id': 88, 'width': 9, 'height': 12, 'x': 3, 'y': 4}
        rec1_dict = self.rec1.to_dictionary()

        self.assertDictEqual(dictionary1, rec1_dict)
        self.assertEqual(len(dictionary1), 5)
