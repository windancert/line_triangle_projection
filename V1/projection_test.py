# This Python file uses the following encoding: utf-8

from unittest import TestCase

from points import Point3D, Zero3D, Point2D
from projection import GroundProjection, PerspectiveProjection

class AbstractProjectionImplementations_test(TestCase):
    def _create_implementations(self):
        return [GroundProjection(),
                PerspectiveProjection.create(Point3D(1,1,1), Zero3D, 45, 1.0, 1, 10)]

    def test_known_implementations(self):
        p = Point3D(1, 0, 0)
        for projection in self._create_implementations():
            r = projection.project(p)
            self.assertIsInstance(r, Point2D)

class PerspectiveProjection_test(TestCase):
    def test_simple(self):
        # ^
        # |
        # x  --C = (1,1,0)
        # |    |
        # |    | FOV = 90
        # |
        # |
        # o----x->
        # L = (0,0,0)
        projection = PerspectiveProjection.create(Point3D(1,1,0), Zero3D, 90, 1.0, 1.0e-6, 10)
        for source, expected in [((1, 0, 0), (0, 0)),
                                 ((0, 1, 0), (1, 0)),
                                 ((0, 0, 0), (1, 0)),
                                 ((0, 0, -1), (0, 0)),
                                 ((0, 0, 1), (0, 0))]:
            source_point = Point3D(*source)
            projected = projection.project(source_point)
            print(f"{source} => {projected}")

if __name__ == "__main__":
    import unittest
    unittest.main()