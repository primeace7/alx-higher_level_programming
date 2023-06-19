'''
Define a base shape implementation
'''
from models.base import Base
import unittest

class TestBase(unittest.TestCase):
    def test_init(self):
        self.base_shape1 = Base()
        self.assertEqual(self.base_shape1.id, 1)

        self.base_shape2 = Base(20)
        self.assertEqual(self.base_shape2.id, 20)

        self.base_shape3 = Base()
        self.assertEqual(self.base_shape3.id, 2)
