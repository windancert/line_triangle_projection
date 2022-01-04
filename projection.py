from abc import ABC, abstractmethod

from points import Point2D


class AbstractProjection(ABC):
    @abstractmethod
    def project(self, point_in_3d):
        pass


class GroundProjection(AbstractProjection):
    def project(self, point_in_3d):
        return Point2D(point_in_3d.x, point_in_3d.y)
