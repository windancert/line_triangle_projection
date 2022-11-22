#include <vector>

#include "MyScenes.h"

using namespace std;

extern void block(Vector3d p, Vector3d ribes, vector<MyTriangle>& my_triangles, MyLight light_n, MyCamera cam);


void test_scene(vector<MyTriangle>& my_triangles, MyLight my_light, MyCamera cam){

    Vector3d up = Vector3d(0, 1, 0);

    my_triangles.push_back(MyTriangle(Vector3d(0, 400, 0), Vector3d(400, 0, 0), Vector3d(-40, 0, 0), up, my_light,  cam));
    my_triangles.push_back(MyTriangle(Vector3d(260, 40, 240), Vector3d(-240, -40, 220), Vector3d(-100, 200, -200), up, my_light,  cam));

}

void plane_scene(vector<MyTriangle>& my_triangles, MyLight my_light, MyCamera cam) {
    Vector3d up = Vector3d(0, 1, 0);
    my_triangles.push_back(MyTriangle(Vector3d(0, 400, 0), Vector3d(400, 0, 0), Vector3d(0, 0, 0), up, my_light, cam));

}


void blocks_scene_0(vector<MyTriangle>& my_triangles, MyLight my_light, MyCamera cam){

    Vector3d ribes = Vector3d(250, 290, 320);
    int i = 0;
    int j = 0;
    int k = 0;

    Vector3d p = Vector3d(ribes[0] * i * 2.0, ribes[1] * j * 2.0, ribes[2] * k * 2.0);
    block(p, ribes, my_triangles,  my_light, cam);

}

void blocks_scene_1(vector<MyTriangle>& my_triangles, MyLight my_light, MyCamera cam) {

    Vector3d ribes = Vector3d(50, 190, 250);
    for (int i = -1; i < 2; i++) {
        for (int j = -1; j < 2; j++) {
            for (int k = -1; k < 2; k++) {
                Vector3d p = Vector3d(ribes[0] * i * 2.0, ribes[1] * j * 2.0, ribes[2] * k * 2.0);
                block(p, ribes, my_triangles, my_light, cam);
            }
        }
    }

}



void block(Vector3d p, Vector3d ribes, vector<MyTriangle>& my_triangles, MyLight light_n, MyCamera cam) {

    Vector3d rx = Vector3d(ribes[0], 0, 0);
    Vector3d ry = Vector3d(0, ribes[1], 0);
    Vector3d rz = Vector3d(0, 0, ribes[2]);

    Vector3d A = p;
    Vector3d B = p + rx;
    Vector3d C = p + rx + ry;
    Vector3d D = p + ry;

    Vector3d E = p + rz;
    Vector3d F = p + rz + rx;
    Vector3d G = p + rz + rx + ry;
    Vector3d H = p + rz + ry;

    Vector3d x = Vector3d(1, 0, 0);
    Vector3d y = Vector3d(0, 1, 0);
    Vector3d z = Vector3d(0, 0, 1);

    my_triangles.push_back(MyTriangle(A, B, F, true, true, false, z, light_n, cam));
    my_triangles.push_back(MyTriangle(F, E, A, true, true, false, z, light_n, cam));

    //my_triangles.push_back(MyTriangle(G, C, D, true, true, false, z, light_n, cam));
    //my_triangles.push_back(MyTriangle(D, H, G, true, true, false, z, light_n, cam));

    //my_triangles.push_back(MyTriangle(F, B, C, false, true, false, y, light_n, cam));
    //my_triangles.push_back(MyTriangle(C, G, F, false, true, false, y, light_n, cam));

    //my_triangles.push_back(MyTriangle(H, D, A, false, true, false, y, light_n, cam));
    //my_triangles.push_back(MyTriangle(A, E, H, false, true, false, y, light_n, cam));

    //my_triangles.push_back(MyTriangle(A, D, C, false, false, false, x, light_n, cam));
    //my_triangles.push_back(MyTriangle(C, B, A, false, false, false, x, light_n, cam));

    //my_triangles.push_back(MyTriangle(E, F, G, false, false, false, x, light_n, cam));
    //my_triangles.push_back(MyTriangle(G, H, E, false, false, false, x, light_n, cam));
}
