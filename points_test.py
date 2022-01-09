from unittest import TestCase

from points import Point2D, Point3D

class Point2D_test(TestCase):
    def test_properties(self):
        p = Point2D(1.0, 2.5)

        self.assertEqual(1.0, p.x)
        self.assertEqual(2.5, p.y)

    def test_addition(self):
        p1 = Point2D(2.75, 4.0)
        p2 = Point2D(-1.25, 1)
        s = p1 + p2

        self.assertIsInstance(s, Point2D)
        self.assertEqual(1.5, s.x)
        self.assertEqual(5.0, s.y)

    def test_subtraction(self):
        p1 = Point2D(2.75, 4.0)
        p2 = Point2D(-1.25, 1)
        s = p1 - p2

        self.assertIsInstance(s, Point2D)
        self.assertEqual(4.0, s.x)
        self.assertEqual(3.0, s.y)

    def test_multiplication(self):
        p = Point2D(3.5, -2.75)

        for left in [2, 2.0]:
            product = left * p
            self.assertIsInstance(product, Point2D)
            self.assertEqual(7.0, product.x)
            self.assertEqual(-5.5, product.y)

        for right in [-2, -2.0]:
            product = p * right
            self.assertIsInstance(product, Point2D)
            self.assertEqual(-7.0, product.x)
            self.assertEqual(5.5, product.y)


class Point3D_test(TestCase):
    def test_properties(self):
        p = Point3D(1.0, 2.5, -3.25)

        self.assertEqual(1.0, p.x)
        self.assertEqual(2.5, p.y)
        self.assertEqual(-3.25, p.z)

    def test_addition(self):
        p1 = Point3D(2.75, 4.0, -1.25)
        p2 = Point3D(-1.25, 1, 1.25)
        s = p1 + p2

        self.assertIsInstance(s, Point3D)
        self.assertEqual(1.5, s.x)
        self.assertEqual(5, s.y)
        self.assertEqual(0, s.z)

    def test_subtraction(self):
        p1 = Point3D(2.75, 4.0, -1.25)
        p2 = Point3D(-1.25, 1, 1.25)
        s = p1 - p2

        self.assertIsInstance(s, Point3D)
        self.assertEqual(4.0, s.x)
        self.assertEqual(3.0, s.y)
        self.assertEqual(-2.5, s.z)

    def test_multiplication(self):
        p = Point3D(3.5, -2.75, 11.75)

        for left in [2, 2.0]:
            product = left * p
            self.assertIsInstance(product, Point3D)
            self.assertEqual(7.0, product.x)
            self.assertEqual(-5.5, product.y)
            self.assertEqual(23.5, product.z)

        for right in [-2, -2.0]:
            product = p * right
            self.assertIsInstance(product, Point3D)
            self.assertEqual(-7.0, product.x)
            self.assertEqual(5.5, product.y)
            self.assertEqual(-23.5, product.z)
