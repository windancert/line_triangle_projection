from numbers import Number


class Point2D:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def dimension(self):
        return 2

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __add__(self, other):
        if not isinstance(other, Point2D):
            raise TypeError(f"Unable to add {type(other).__name__} to Point2D")
        return Point2D(self.__x + other.__x, self.__y + other.__y)

    def __sub__(self, other):
        if not isinstance(other, Point2D):
            raise TypeError(f"Unable to subtract {type(other).__name__} to Point2D")
        return Point2D(self.__x - other.__x, self.__y - other.__y)

    def __mul__(self, other):
        if not isinstance(other, Number):
            raise TypeError(f"Unable to multiply {type(other).__name__} with Point2D")
        return Point2D(other * self.__x, other * self.__y)
    __rmul__ = __mul__


Zero2D = Point2D(0, 0)


class Point3D:
    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z

    @property
    def dimension(self):
        return 3

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def z(self):
        return self.__z

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


Zero3D = Point3D(0, 0, 0)
