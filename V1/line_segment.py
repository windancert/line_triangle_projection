# This Python file uses the following encoding: utf-8

from abc import ABC, abstractmethod

from points import Point2D, Point3D


class AbstractLineSegment(ABC):
    # Class for a line segment
    # The points of the line segment are: start + t * end
    # for t between 0 and 1
    def __init__(self, start, end):
        if start.dimension != end.dimension:
            raise Exception(f"Mismatched start and end dimensions {start.dimension} != {end.dimension}")
        self._start = start
        self._end = end

    @property
    def dimensionality(self):
        return self._start.dimension

    @property
    def start(self):
        return self._start

    @property
    def end(self):
        return self._end

    def evaluate(self, t):
        if t < 0 or t > 1:
            raise ValueError(f"Parameterization is only valid for 0<=t<=1, actual t={t}")
        return self._start + t * (self._end - self._start)

    @abstractmethod
    def intersect(self, other):
        pass


class LineSegment2D(AbstractLineSegment):
    def __init__(self, start, end):
        if not isinstance(start, Point2D) or not isinstance(end, Point2D):
            raise Exception("LineSegment2D can only be created using Point2D")
        super().__init__(start, end)

    def intersect(self, other):
        # Algorithm:
        # 1) Find t values when intersecting lines (not segments) using
        #    s1 + t1*e1 = s2 + t2*e2
        #    this is equivalent to
        #    t1 (e1x-s1x) - t2 (e2x-s2x) = s2x-s1x     ==>     alpha*t1 + beta*t2 = gamma
        #    t1 (e1y-s1y) - t2 (e2y-s2y) = s2y-s1y     ==>     delta*t1 + epsilon*t2 = zeta
        # 2) Check if t1 and t2 are between 0 and 1
        if not isinstance(other, LineSegment2D):
            raise TypeError("Intersection")

        alpha = self._end.x - self._start.x
        beta = -(other._end.x - other._start.x)
        gamma = other._start.x - self._start.x
        delta = self._end.y - self._start.y
        epsilon = -(other._end.y - other._start.y)
        zeta = other._start.y - self._start.y

        determinant = alpha * epsilon - beta * delta

        lines_are_parallel = abs(determinant) < 1e-12
        if lines_are_parallel:
            return None

        t1 = (gamma*epsilon - beta*zeta)/determinant
        t2 = (alpha*zeta - gamma*delta)/determinant

        if (0.0 <= t1 <= 1.0) and (0.0 <= t2 <= 1.0):
            # Points should be the same, for symmetry we return average
            return 0.5 * (self.evaluate(t1) + other.evaluate(t2))

        return None


class LineSegment3D(AbstractLineSegment):
    def __init__(self, start, end):
        if not isinstance(start, Point3D) or not isinstance(end, Point3D):
            raise Exception("LineSegment3D can only be created using Point3D")
        super().__init__(start, end)

    def project(self, projection):
        return LineSegment2D(projection.project(self._start), projection.project(self._end))

    def intersect(self, other):
        raise NotImplementedError("Intersection for 3D line segments not yet implemented")

