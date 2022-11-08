#include "MyLight.h"



MyLight::MyLight(Vector3d pos_arg, Vector3d look_at_arg, MyCamera cam_arg) {
    pos = cam_arg.project(pos_arg);
    look_at = cam_arg.project(look_at_arg);
    n_dir = (pos - look_at);
    n_dir.normalize();

};

Vector3d MyLight::getNormalizedDirection() {
    return n_dir;
};


