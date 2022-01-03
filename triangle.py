from line_segment import LineSegment
from points import Point3D


class Triangle:
    # Class for a triangle

    def __init__(self, one, two, three):
        for p in [one, two, three]:
            if not isinstance(p, Point3D):
                raise TypeError("A triangle must be created using Point3D points")
        self.__one = one
        self.__two = two
        self.__three = three

    @property
    def boundary(self):
        return [LineSegment(self.__one, self.__two), LineSegment(self.__two, self.__three), LineSegment(self.__three, self.__one)]

