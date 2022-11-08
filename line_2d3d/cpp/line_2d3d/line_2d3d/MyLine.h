#pragma once
#include<vector>
#include<string>
#include <Eigen/Dense>
using Eigen::Vector3d;
using namespace std;

#include "MyColor.h"
#include "MyTriangle.h"
#include "MySvg.h"

class MyLine
{
private:
    Vector3d ps;
    MyTriangle parent;
    vector<double> splitters;
    MyColor c;
    int thickness;
    bool visible;
    vector<MyLine> split_lines;
public:
    MyLine(const MyLine & l);
    MyLine(MyTriangle t, Vector3d p1, Vector3d p2);
    MyLine(MyTriangle t, Vector3d p1, Vector3d p2, bool visible);
    MyLine(MyTriangle t, Vector3d p1, Vector3d p2, MyColor c);
    MyLine(MyTriangle t, Vector3d p1, Vector3d p2, MyColor c, bool visible);
    MyLine(MyTriangle t, Vector3d p1, Vector3d p2, MyColor c, int thickness, bool visible);
    void draw(MySvg svg);
    void addSplitter(double splitter);
    int generateSplitLines();
    int recombineLines();
    int getNoVisibleLines();
    Vector3d addLineIntersectionXY(MyLine l2);
    Vector3d getLineIntersectionXY(MyLine l2);
    Vector3d addGetLineIntersectionXY(MyLine l2, bool add_splitter);
    Vector3d addTriangleIntersectXYZ(MyTriangle triangle_arg);
    vector<Vector3d> addTriangleObscuration(MyTriangle triangle);
    Vector3d get_direction();

};

