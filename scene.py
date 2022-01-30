# This Python file uses the following encoding: utf-8
import itertools

from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D

from line_segment import LineSegment3D
from projection import AbstractProjection
from scene_object import SceneObject


class Scene:
    def __init__(self, objects=[]):
        if any(not isinstance(o, (SceneObject, LineSegment3D)) for o in objects):
            raise TypeError("All objects must be of type LineSegment3D or SceneObject")

        self.__scene_objects = [o for o in objects if isinstance(o, SceneObject)]
        self.__lines = [o for o in objects if isinstance(o, LineSegment3D)]

    def create_3D_figure(self):
        fig = pyplot.figure()
        ax = fig.add_subplot(111, projection='3d')
        self.__draw_lines(ax, self.__get_lines_from_scene_objects(), 'b-')
        self.__draw_lines(ax, self.__lines, 'k-')
        return fig

    def create_2D_figure(self, projection):
        if not isinstance(projection, AbstractProjection):
            t = type(projection).__name__
            raise TypeError(f"Parameter transformation must be implementation of AbstractProjection, got {t}")
        lines2d_from_objects = [l.project(projection) for l in self.__get_lines_from_scene_objects()]
        lines2d_from_lines = [l.project(projection) for l in self.__lines]
        fig = pyplot.figure()
        ax = fig.add_subplot(111)
        self.__draw_lines(ax, lines2d_from_objects, 'b-')
        self.__draw_lines(ax, lines2d_from_lines, 'k-')
        return fig

    def __get_lines_from_scene_objects(self):
        triangles = itertools.chain.from_iterable(o.get_triangles() for o in self.__scene_objects)
        lines_from_triangles = itertools.chain.from_iterable(t.boundary for t in triangles)
        return lines_from_triangles

    @staticmethod
    def __draw_lines(axes, lines, style):
        for line in lines:
            axes.plot(*zip(line.start.elements, line.end.elements), style)

if __name__ == "__main__":
    from sphere import Sphere
    from line_segment import LineSegment3D
    from points import Point3D, Zero3D
    from projection import GroundProjection

    s1 = Sphere(Zero3D, 1.0, 2)
    s2 = Sphere(Point3D(3, 3, 3), 2.0, 2)
    s3 = Sphere(Point3D(8, 8, 8), 3.0, 2)
    l11 = LineSegment3D(Point3D(-2, 0, 0), Point3D(2, 0, 0))
    l12 = LineSegment3D(Point3D(0, -2, 0), Point3D(0, 2, 0))
    l21 = LineSegment3D(Point3D(0, 3, 3), Point3D(6, 3, 3))
    l22 = LineSegment3D(Point3D(3, 0, 3), Point3D(3, 6, 3))
    l31 = LineSegment3D(Point3D(4, 8, 8), Point3D(12, 8, 8))
    l32 = LineSegment3D(Point3D(8, 4, 8), Point3D(8, 12, 8))

    s = Scene([s1, s2, s3, l11, l12, l21, l22, l31, l32])

    s.create_3D_figure()
    s.create_2D_figure(GroundProjection())
    pyplot.show()
