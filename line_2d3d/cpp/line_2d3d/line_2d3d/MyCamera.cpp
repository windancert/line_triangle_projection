#include "MyCamera.h"
using Eigen::Vector4d;


MyCamera::MyCamera(Vector3d cam_pos_arg, Vector3d look_at_arg, Vector3d up_arg, double zoom_arg)
{
	Vector3d view_dir = cam_pos_arg - look_at_arg;
	view_dir.normalize();
	Vector3d side_dir = up_arg.cross(view_dir);
	side_dir.normalize();
	Vector3d e = view_dir.cross(side_dir);
	e.normalize();

	cam_mat << side_dir[0], side_dir[1], side_dir[2], -side_dir.dot(cam_pos_arg),
		e[0], e[1], e[2], -e.dot(cam_pos_arg),
		view_dir[0], view_dir[1], view_dir[2], -view_dir.dot(cam_pos_arg),
		0, 0, 0, 1;

	cam_mat *= zoom_arg;
}

Vector3d MyCamera::project(Vector3d v3)
{
	Vector4d v4;
	v4.head(3) << v3;
	v4[3] = 0;
	Vector4d v4_p = cam_mat * v4;

	return v4.head(3);
}


//
//MatrixXd m(2, 2);
//m(0, 0) = 3;
//m(1, 0) = 2.5;
//m(0, 1) = -1;
//m(1, 1) = m(1, 0) + m(0, 1);
//std::cout << m << std::endl;
//Vector3d d3;
//d3 << 1, 2, 3;
//std::cout << d3 << std::endl;
//Vector4d d4;
//d4.head(3) << d3;
//d4[3] = 10;
//std::cout << d4 << std::endl;
