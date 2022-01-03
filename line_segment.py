from points import Point2D, Point3D


class LineSegment:
    # Class for a line segment
    # The points of the line segment are: start + t * end
    # for t between 0 and 1

    def __init__(self, start, end):
        if not isinstance(start, (Point2D, Point3D)) or not isinstance(end, (Point2D, Point3D)):
            raise Exception("Start and end of line segment must be specified as Point2D or Point3D")
        if start.dimension != end.dimension:
            raise Exception(f"Mismatched start and end dimensions {start.dimension} != {end.dimension}")
        self.__start = start
        self.__end = end

    @property
    def dimensionality(self):
        return self.__start.dimension

    def evaluate(self, t):
        if t < 0 or t > 1:
            raise ValueError(f"Parameterization is only valid for 0<=t<=1, actual t={t}")
        return self.__start + t * (self.__end - self.__start)

    def project(self, projection):
        return LineSegment(projection.project(self.__start), projection.project(self.__end))

    def intersect(self, line_segment):
        if self.dimensionality != line_segment.dimensionality:
            raise Exception(f"Mismatched dimensionality {self.dimensionality} != {line_segment.dimensionality}")

        if self.dimensionality == 2:
            return self.__intersect_2d(line_segment)
        elif self.dimensionality == 3:
            return self.__intersect_3d(line_segment)
        else:
            raise Exception(f"Unsupported dimensionality {self.dimensionality}")

    def __intersect_2d(self, other):
        # Algorithm:
        # 1) Find t values when intersecting lines (not segments) using
        #    s1 + t1*e1 = s2 + t2*e2
        #    this is equivalent to
        #    t1 (e1x-s1x) - t2 (e2x-s2x) = s2x-s1x     ==>     alpha*t1 + beta*t2 = gamma
        #    t1 (e1y-s1y) - t2 (e2y-s2y) = s2y-s1y     ==>     delta*t1 + epsilon*t2 = zeta
        # 2) Check if t1 and t2 are between 0 and 1
        alpha = self.__end.x - self.__start.x
        beta = -(other.__end.x - other.__start.x)
        gamma = other.__start.x - self.__start.x
        delta = self.__end.y - self.__start.y
        epsilon = -(other.__end.y - other.__start.y)
        zeta = other.__start.y - self.__start.y

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

    def __intersect_3d(self, line_segment):
        raise NotImplemented("Intersection of 3D lines is not yet implemented")
