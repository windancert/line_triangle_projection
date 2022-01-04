from abc import abstractmethod

from line_segment import LineSegment2D, LineSegment3D
from points import Point3D, Point2D


class BaseTriangle:
    # Baseclass for a triangle

    def __init__(self, one, two, three):
        for p in [one, two, three]:
            if not isinstance(p, (Point2D, Point3D)):
                raise TypeError("A triangle must be created using Point3D points")
        if len({one.dimension, two.dimension, three.dimension}) != 1:
            raise ValueError("")
        self._one = one
        self._two = two
        self._three = three

    @property
    @abstractmethod
    def boundary(self):
        pass


class Triangle2D(BaseTriangle):
    def __init__(self, one, two, three):
        for p in [one, two, three]:
            if not isinstance(p, Point2D):
                raise TypeError("A Triangle2D must be created using Point2D points")
        super().__init__(one, two, three)

    @property
    def boundary(self):
        return [LineSegment2D(self._one, self._two), LineSegment2D(self._two, self._three),
                LineSegment2D(self._three, self._one)]

class Triangle3D(BaseTriangle):
    def __init__(self, one, two, three):
        for p in [one, two, three]:
            if not isinstance(p, Point3D):
                raise TypeError("A Triangle3D must be created using Point3D points")
        super().__init__(one, two, three)

    @property
    def boundary(self):
        return [LineSegment3D(self._one, self._two), LineSegment3D(self._two, self._three),
                LineSegment3D(self._three, self._one)]

    def project(self, projection):
        return Triangle2D(projection.project(self._one), projection.project(self._two),
                          projection.project(self._three))