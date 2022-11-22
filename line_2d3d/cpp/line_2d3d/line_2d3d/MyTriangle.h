#pragma once
#include<vector>
#include<string>
#include <Eigen/Dense>
using Eigen::Vector3d;
using namespace std;

#include "MyColor.h"
#include "MyLine.h"
#include "MyCamera.h"
#include "MyLight.h"
#include "MySvg.h"

class MyTriangle
{
private:
    double FLOATING_POINT_ACCURACY;
    void create(Vector3d p1_arg, Vector3d p2_arg, Vector3d p3_arg, bool vis1, bool vis2, bool vis3, Vector3d up_arg, MyLight& light_n, MyCamera& cam);
    void det_normal_and_o();
    bool equals(MyTriangle& t);
    Vector3d center();
    double triangleAreaXY(Vector3d p1, Vector3d p2, Vector3d p3);
    MyLine ls[3];
    vector<MyLine> lines;
    Vector3d n, up, right;  // plane : nx*x + ny*y + nz*z = o
    Vector3d p[3];
    double   o;
    MyColor   c;
    double   shading;
    void addTriangleObscuration(MyTriangle& triangle, MyLine& line);
    void addHatching3D(Vector3d up);
public:
    int     id;
    MyTriangle(Vector3d p1_arg, Vector3d p2_arg, Vector3d p3_arg, bool vis1, bool vis2, bool vis3, Vector3d up_arg, MyLight& light_n, MyCamera& cam);
    MyTriangle(Vector3d p1, Vector3d p2, Vector3d p3, Vector3d up, MyLight& light_n, MyCamera& cam);
    bool insideTriangleXY(Vector3d po, bool include_edge);
    double getZ(double x, double y);
    void draw(MySvg &svg);
    void draw_normal(MySvg svg);
    string str();
    void addHatches();
    int addLineLineIntersectionXY(MyTriangle& triangle);
    int addTriangleIntersectXYZ(MyTriangle & triangle);
    void addTriangleObscuration(MyTriangle& triangle);
    void generateSplitLines();
    void recombineLines();


    int getNoVisLines();

};
