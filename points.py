# This Python file uses the following encoding: utf-8

import math
from abc import ABC, abstractmethod
from numbers import Number


class AbstractPoint(ABC):
    @property
    @abstractmethod
    def dimension(self):
        pass

    @property
    @abstractmethod
    def elements(self):
        pass

class Point2D(AbstractPoint):
    def __init__(self, x, y):
        super().__init__()
        self.__x = x
        self.__y = y

    @property
    def dimension(self):
        return 2

    @property
    def elements(self):
        return [self.__x, self.__y]

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def normalize(self):
        s = math.sqrt(self.__x**2 + self.__y**2)
        result = self/s
        return result

    def __add__(self, other):
        if not isinstance(other, Point2D):
            raise TypeError(f"Unable to add {type(other).__name__} to Point2D")
        return Point2D(self.__x + other.__x, self.__y + other.__y)

    def __sub__(self, other):
        if not isinstance(other, Point2D):
            raise TypeError(f"Unable to subtract {type(other).__name__} from Point2D")
        return Point2D(self.__x - other.__x, self.__y - other.__y)

    def __mul__(self, other):
        if not isinstance(other, Number):
            raise TypeError(f"Unable to multiply {type(other).__name__} with Point2D")
        return Point2D(other * self.__x, other * self.__y)
    __rmul__ = __mul__

    def __truediv__(self, other):
        if not isinstance(other, Number):
            raise TypeError(f"Unable to divide Point2D with {type(other).__name__}")
        return Point2D(self.__x / other, self.__y / other)

    def __floordiv__(self, other):
        if not isinstance(other, Number):
            raise TypeError(f"Unable to do integer division on Point2D with {type(other).__name__}")
        return Point2D(self.__x // other, self.__y // other)


Zero2D = Point2D(0, 0)


class Point3D(AbstractPoint):
    def __init__(self, x, y, z):
        super().__init__()
        self.__x = x
        self.__y = y
        self.__z = z

    @property
    def dimension(self):
        return 3

    @property
    def elements(self):
        return [self.__x, self.__y, self.__z]

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def z(self):
        return self.__z

    def normalize(self):
        s = math.sqrt(self.__x**2 + self.__y**2 + self.__z**2)
        result = self/s
        return result

    def __add__(self, other):
        if not isinstance(other, Point3D):
            raise TypeError(f"Unable to add {type(other).__name__} to Point3D")
        return Point3D(self.__x + other.__x, self.__y + other.__y, self.__z + other.__z)

    def __sub__(self, other):
        if not isinstance(other, Point3D):
            raise TypeError(f"Unable to subtract {type(other).__name__} to Point3D")
        return Point3D(self.__x - other.__x, self.__y - other.__y, self.__z - other.__z)

    def __mul__(self, other):
        if not isinstance(other, Number):
            raise TypeError(f"Unable to multiply {type(other).__name__} with Point3D")
        return Point3D(other * self.__x, other * self.__y, other * self.__z)
    __rmul__ = __mul__

    def __truediv__(self, other):
        if not isinstance(other, Number):
            raise TypeError(f"Unable to divide Point3D with {type(other).__name__}")
        return Point3D(self.__x / other, self.__y / other, self.__z / other)

    def __floordiv__(self, other):
        if not isinstance(other, Number):
            raise TypeError(f"Unable to do integer division on Point3D with {type(other).__name__}")
        return Point3D(self.__x // other, self.__y // other, self.__z // other)


Zero3D = Point3D(0, 0, 0)
