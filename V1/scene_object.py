# This Python file uses the following encoding: utf-8

from abc import ABC, abstractmethod


class SceneObject(ABC):
    @abstractmethod
    def get_triangles(self):
        pass
