import unittest
import math


class TestSquare(unittest.TestCase):

    def test_reading_side(self):
        s = Square(4)
        self.assertEqual(s.get_side(), 4)

    def test_reading_area(self):
        s = Square(4)
        self.assertEqual(s.get_area(), 16)

    def test_reading_diagonal(self):
        s = Square(4)
        self.assertAlmostEqual(s.get_diagonal(), 4 * math.sqrt(2))

    def test_reading_perimeter(self):
        s = Square(4)
        self.assertEqual(s.get_perimeter(), 16)

    def test_setting_side(self):
        s = Square(2)
        s.set_side(5)
        self.assertEqual(s.get_side(), 5)
        self.assertEqual(s.get_perimeter(), 20)

    def test_setting_perimeter(self):
        s = Square(2)
        s.set_perimeter(20)
        self.assertEqual(s.get_side(), 5)
        self.assertEqual(s.get_area(), 25)

    def test_setting_area(self):
        s = Square(2)
        s.set_area(36)
        self.assertEqual(s.get_side(), 6)
        self.assertEqual(s.get_perimeter(), 24)

    def test_setting_diagonal(self):
        s = Square(2)
        s.set_diagonal(10 * math.sqrt(2))
        self.assertAlmostEqual(s.get_side(), 10)
        self.assertAlmostEqual(s.get_perimeter(), 40)