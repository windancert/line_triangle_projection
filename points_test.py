# This Python file uses the following encoding: utf-8

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

    def test_dot(self):
        p1 = Point2D(-1, 2)
        p2 = Point2D(4, 5)

        self.assertEqual(p1.dot(p2), 6)
        self.assertEqual(p2.dot(p1), 6)

    def test_unary_minus(self):
        p = Point2D(1.0, 0.25)
        m = -p

        self.assertEqual(-p.x, m.x)
        self.assertEqual(-p.y, m.y)


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

    def test_normalize(self):
        p = Point3D(2, -3, 6)
        n = p.normalize()

        self.assertAlmostEqual(p.x / 7, n.x, delta=1.0e-12)
        self.assertAlmostEqual(p.y / 7, n.y, delta=1.0e-12)
        self.assertAlmostEqual(p.z / 7, n.z, delta=1.0e-12)

    def test_dot(self):
        p1 = Point3D(-1, 2, 4.5)
        p2 = Point3D(4, 5.5, 4)

        self.assertEqual(p1.dot(p2), 25)
        self.assertEqual(p2.dot(p1), 25)

    def test_cross(self):
        a = Point3D(1, -2, 3)
        b = Point3D(2, 4, -9)
        c = a.cross(b)

        self.assertEqual(6, c.x)
        self.assertEqual(15, c.y)
        self.assertEqual(8, c.z)

    def test_cross_basis_vectors(self):
        e1 = Point3D(1, 0, 0)
        e2 = Point3D(0, 1, 0)
        e3 = Point3D(0, 0, 1)

        for first, second, expected in [(e1, e2, e3),
                                        (e2, e3, e1),
                                        (e3, e1, e2),
                                        (e2, e1, -e3),
                                        (e3, e2, -e1),
                                        (e1, e3, -e2)]:
            result = first.cross(second)
            self.assertAlmostEqual(expected.x, result.x, delta=1.0e-12)
            self.assertAlmostEqual(expected.y, result.y, delta=1.0e-12)
            self.assertAlmostEqual(expected.z, result.z, delta=1.0e-12)

    def test_unary_minus(self):
        p = Point3D(1.0, 0.25, -2)
        m = -p

        self.assertEqual(-p.x, m.x)
        self.assertEqual(-p.y, m.y)
        self.assertEqual(-p.z, m.z)
