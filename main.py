import unittest
import math


def classify_triangle(a, b, c):

    if a == b == c:
        return 'Equilateral triangle'
    elif (a == b or a == c or b == c) and (a*a + b*b == c*c):
        return 'Isosceles right triangle'
    elif (a == b or a == c or b == c) and (a*a + c*c == b*b):
        return 'Isosceles right triangle'
    elif (a == b or a == c or b == c) and (c*c + b*b == a*a):
        return 'Isosceles right triangle'
    elif a == b or a == c or b == c:
        return 'Isosceles triangle'
    elif (a != b or a != c or b != c) and (a*a + b*b == c*c):
        return 'Scalene right triangle'
    elif (a != b or a != c or b != c) and (a*a + c*c == b*b):
        return 'Scalene right triangle'
    elif (a != b or a != c or b != c) and (c*c + b*b == a*a):
        return 'Scalene right triangle'
    elif (a != b or a != c or b != c) and (a + b > c and a + c > b and b + c > a):
        return 'Scalene triangle'
    else:
        return 'Not a valid triangle'


def run_classify_triangle(a, b, c):
    print('classifyTriangle (', a, ',', b, ',', c, ') = ', classify_triangle(a, b, c), sep="")


class TestTriangles(unittest.TestCase):

    def test_rightTriangles(self):
        self.assertEqual(classify_triangle(3, 4, 5), 'Scalene right triangle')

    def test_nonRight(self):
        self.assertEqual(classify_triangle(1, 1, 3), 'Isosceles triangle')
        self.assertEqual(classify_triangle(1, 1, 1), 'Equilateral triangle')
        self.assertEqual(classify_triangle(7, 12, 15), 'Scalene triangle')

    def test_invalid(self):
        self.assertEqual(classify_triangle(3, 5, 9), 'Not a valid triangle')


if __name__ == '__main__':

    unittest.main(exit=True)



