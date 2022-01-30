# This Python file uses the following encoding: utf-8
import math
from abc import ABC, abstractmethod

import numpy

from points import Point2D, Point3D


class AbstractProjection(ABC):
    @abstractmethod
    def project(self, point_in_3d):
        pass


class GroundProjection(AbstractProjection):
    def project(self, point_in_3d):
        return Point2D(point_in_3d.x, point_in_3d.y)

class PerspectiveProjection(AbstractProjection):
    """

    """
    # https://learnwebgl.brown37.net/08_projections/projections_perspective.html
    def __init__(self, matrix):
        if not isinstance(matrix, numpy.ndarray):
            raise Exception("matrix parameter must be an numpy.ndarray (or subtype)")
        if not matrix.shape == (4, 4):
            raise Exception(f"matrix parameter size must be 4x4, actual={matrix.shape}")
        print(f"matrix=\n{matrix}")
        self.__M = matrix

    @staticmethod
    def create(camera_location, look_at, fovy, aspect_ratio, near, far):
        #   let cam_pos = [settings.camera_x, settings.camera_y, settings.camera_z]
        #   let cam_look_at = [settings.look_at_x, settings.look_at_y, settings.look_at_z]
        #
        #   let view_matrix = lookAt4m(cam_pos, cam_look_at, [0, 0, 1])
        #   let projection_matrix = createPerspectiveUsingFrustum(settings.fov, settings.aspect, settings.near, settings.far)
        #   // let projection_matrix = perspective4m(0.4, 1) //  fovy, aspect
        #   view_projection_matrix = multiply4m(projection_matrix, view_matrix)
        frustum_matrix = PerspectiveProjection.__create_frustrum_matrix_from_fov(fovy, aspect_ratio, near, far)
        view_matrix = PerspectiveProjection.__create_view_matrix(camera_location, look_at)
        print(f"frustum_matrix=\n{frustum_matrix}")
        print(f"view_matrix=\n{view_matrix}")
        return PerspectiveProjection(frustum_matrix @ view_matrix)

    @staticmethod
    def __create_frustrum_matrix_from_fov(fovy, aspect, near, far):
        top = near*math.tan(math.radians(fovy)/2)
        bottom = -top
        right = top * aspect
        left = -right
        return PerspectiveProjection.__create_frustrum_matrix(left, right, top, bottom, near, far)

    @staticmethod
    def __create_frustrum_matrix(frustum_left, frustum_right, frustum_top, frustum_bottom,
                                 frustum_near, frustum_far):
        ft = PerspectiveProjection.__create_frustum_translation_matrix(frustum_left, frustum_right, frustum_top, frustum_bottom)
        p = PerspectiveProjection.__create_perspective_matrix(frustum_near)
        sv = PerspectiveProjection.__create_scale_view_window_matrix(frustum_left, frustum_right, frustum_top, frustum_bottom)
        z = PerspectiveProjection.__create_z_depth_map_matrix(frustum_near, frustum_far)
        return sv @ p @ z @ ft

    @staticmethod
    def __create_view_matrix(camera, look_at, up=Point3D(0, 0, 1)):
        # const lookAt4m=(a,b,d)=>{ // pos, lookAt, up
        #     const c=new Float32Array(16);
        #     b=normalize3(sub3(a,b));
        #     d=normalize3(cross3(d,b));
        #     const e=normalize3(cross3(b,d));
        #     c[0]=d[0];c[1]=e[0];c[2]=b[0];c[3]=0;
        #     c[4]=d[1];c[5]=e[1];c[6]=b[1];c[7]=0;
        #     c[8]=d[2];c[9]=e[2];c[10]=b[2];c[11]=0;
        #     c[12]=-(d[0]*a[0]+d[1]*a[1]+d[2]*a[2]);
        #     c[13]=-(e[0]*a[0]+e[1]*a[1]+e[2]*a[2]);
        #     c[14]=-(b[0]*a[0]+b[1]*a[1]+b[2]*a[2]);
        #     c[15]=1;
        #     return c;
        # }
        if (not isinstance(camera, Point3D)) or (not isinstance(look_at, Point3D) or (not isinstance(up, Point3D))):
            raise Exception("All parameters camera, look_up and up must be Point3D type")
        view_direction = (camera - look_at).normalize()
        side_direction = up.cross(view_direction).normalize()
        e = view_direction.cross(side_direction).normalize()
        return numpy.array([[side_direction.x, e.x, view_direction.x, 0],
                            [side_direction.y, e.y, view_direction.y, 0],
                            [side_direction.z, e.z, view_direction.z, 0],
                            [-side_direction.dot(camera), -e.dot(camera), -view_direction.dot(camera), 1]])

    @staticmethod
    def __create_frustum_translation_matrix(frustum_left, frustum_right, frustum_top, frustum_bottom):
        result = numpy.identity(4)
        result[3, 0] = -(frustum_left+frustum_right)/2
        result[3, 1] = -(frustum_bottom+frustum_top)/2
        return result

    @staticmethod
    def __create_perspective_matrix(frustum_near):
        result = numpy.zeros([4, 4])
        result[0, 0] = frustum_near
        result[1, 1] = frustum_near
        result[2, 2] = 1
        result[2, 3] = -1
        return result

    @staticmethod
    def __create_scale_view_window_matrix(frustum_left, frustum_right, frustum_top, frustum_bottom):
        result = numpy.identity(4)
        result[0, 0] = 2/(frustum_right-frustum_left)
        result[1, 1] = 2/(frustum_top-frustum_bottom)
        return result

    @staticmethod
    def __create_z_depth_map_matrix(frustum_near, frustum_far):
        c1 = 2 * frustum_far * frustum_near / (frustum_near - frustum_far)
        c2 = (frustum_far + frustum_near) / (frustum_far - frustum_near)
        result = numpy.zeros([4, 4])
        result[0, 0] = 1
        result[1, 1] = 1
        result[2, 2] = -c2
        result[3, 2] = c1
        result[2, 3] = -1
        return result

    def project(self, point_in_3d):
        p = numpy.array([[point_in_3d.x, point_in_3d.y, point_in_3d.z, 1]]).T
        result = self.__M @ p
        return Point2D(result[0, 0], result[1, 0])
