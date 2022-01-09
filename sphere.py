import itertools

from points import Point3D
from triangle import Triangle3D

# let
# X = .525731112119133606
# let
# Z = .850650808352039932
#
# let
# vdata = [ // [12][3]
# [-X, 0.0, Z], [X, 0.0, Z], [-X, 0.0, -Z], [X, 0.0, -Z],
#         [0.0, Z, X], [0.0, Z, -X], [0.0, -Z, X], [0.0, -Z, -X],
#         [Z, X, 0.0], [-Z, X, 0.0], [Z, -X, 0.0], [-Z, -X, 0.0]
# ];
# let
# tindices = [ // s[20][3]
# [0, 4, 1], [0, 9, 4], [9, 5, 4], [4, 5, 8], [4, 8, 1],
#            [8, 10, 1], [8, 3, 10], [5, 3, 8], [5, 2, 3], [2, 7, 3],
#            [7, 10, 3], [7, 6, 10], [7, 11, 6], [11, 0, 6], [0, 1, 6],
#            [6, 1, 10], [9, 0, 11], [9, 11, 2], [9, 2, 5], [7, 2, 11]];

MASTER_X = 0.525731112119133606
MASTER_Z = 0.850650808352039932

VERTEX_A = Point3D(-MASTER_X, 0.0, MASTER_Z)
VERTEX_B = Point3D(MASTER_X, 0.0, MASTER_Z)
VERTEX_C = Point3D(-MASTER_X, 0.0, -MASTER_Z)
VERTEX_D = Point3D(MASTER_X, 0.0, -MASTER_Z)
VERTEX_E = Point3D(0.0, MASTER_Z, MASTER_X)
VERTEX_F = Point3D(0.0, MASTER_Z, -MASTER_X)
VERTEX_G = Point3D(0.0, -MASTER_Z, MASTER_X)
VERTEX_H = Point3D(0.0, -MASTER_Z, -MASTER_X)
VERTEX_I = Point3D(MASTER_Z, MASTER_X, 0.0)
VERTEX_J = Point3D(-MASTER_Z, MASTER_X, 0.0)
VERTEX_K = Point3D(MASTER_Z, -MASTER_X, 0.0)
VERTEX_L = Point3D(-MASTER_Z, -MASTER_X, 0.0)

TRIANGLES = [Triangle3D(VERTEX_A, VERTEX_E, VERTEX_B), Triangle3D(VERTEX_A, VERTEX_J, VERTEX_E),
             Triangle3D(VERTEX_J, VERTEX_F, VERTEX_E), Triangle3D(VERTEX_E, VERTEX_F, VERTEX_I),
             Triangle3D(VERTEX_E, VERTEX_I, VERTEX_B), Triangle3D(VERTEX_I, VERTEX_K, VERTEX_B),
             Triangle3D(VERTEX_I, VERTEX_D, VERTEX_K), Triangle3D(VERTEX_F, VERTEX_D, VERTEX_I),
             Triangle3D(VERTEX_F, VERTEX_C, VERTEX_D), Triangle3D(VERTEX_C, VERTEX_H, VERTEX_D),
             Triangle3D(VERTEX_H, VERTEX_K, VERTEX_D), Triangle3D(VERTEX_H, VERTEX_G, VERTEX_K),
             Triangle3D(VERTEX_H, VERTEX_L, VERTEX_G), Triangle3D(VERTEX_L, VERTEX_A, VERTEX_G),
             Triangle3D(VERTEX_A, VERTEX_B, VERTEX_G), Triangle3D(VERTEX_G, VERTEX_B, VERTEX_K),
             Triangle3D(VERTEX_J, VERTEX_A, VERTEX_L), Triangle3D(VERTEX_J, VERTEX_L, VERTEX_C),
             Triangle3D(VERTEX_J, VERTEX_C, VERTEX_F), Triangle3D(VERTEX_H, VERTEX_C, VERTEX_L)]

class Sphere:
    def __init__(self, center, radius, subdivisions):
        self.__center = center
        self.__radius = radius
        self.__subdivisions = subdivisions

    def get_triangles(self):
        result = list(TRIANGLES)

        for _ in range(self.__subdivisions):
            result = itertools.chain.from_iterable(self.__subdivide_triangle(t) for t in result)

        result = [t.scale(self.__radius).translate(self.__center) for t in result]

        return result

    def __subdivide_triangle(self, triangle):

        v1, v2, v3 = triangle.vertex_1, triangle.vertex_2, triangle.vertex_3

        v12 = (v1 + v2).normalize()
        v13 = (v1 + v3).normalize()
        v23 = (v2 + v3).normalize()

        triangles = [Triangle3D(v1, v12, v13), Triangle3D(v2, v23, v12),
                     Triangle3D(v3, v13, v23), Triangle3D(v12, v23, v13)]

        return triangles


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    from points import Zero3D

    s1 = Sphere(Zero3D, 1, 0)
    s2 = Sphere(Point3D(3, 3, 3), 2, 1)
    s3 = Sphere(Point3D(8, 8, 8), 3, 2)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for triangle in itertools.chain.from_iterable(s.get_triangles() for s in [s1, s2, s3]):
        for line in triangle.boundary:
            ax.plot(*zip(line.start.elements, line.end.elements))

    plt.show()
