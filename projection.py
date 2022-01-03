from abc import ABC, abstractmethod


class AbstractProjection(ABC):
    @abstractmethod
    def project(self, point_in_3d):
        pass
