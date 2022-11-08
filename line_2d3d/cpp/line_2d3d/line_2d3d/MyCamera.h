#pragma once
#include <Eigen/Dense>
using Eigen::Vector3d;
using Eigen::Matrix4d;

class MyCamera
{
private:

    Matrix4d cam_mat;
public:
    MyCamera(Vector3d cam_pos_arg, Vector3d look_at_arg, Vector3d up_arg, double zoom_arg);
    Vector3d project(Vector3d v3);

};






