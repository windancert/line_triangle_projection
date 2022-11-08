#pragma once
#include<string>
#include <Eigen/Dense>
using Eigen::Vector3d;
using namespace std;

#include "MyCamera.h"

class MyLight
{
public :
    MyLight(Vector3d pos_arg, Vector3d look_at_arg, MyCamera cam_arg);
    Vector3d getNormalizedDirection();
private:
    Vector3d pos, look_at, n_dir;
};

