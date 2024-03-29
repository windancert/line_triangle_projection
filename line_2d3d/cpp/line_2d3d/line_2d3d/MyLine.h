#pragma once
#include<vector>
#include<string>
#include <Eigen/Dense>
using Eigen::Vector3d;
using namespace std;

#include "MyColor.h"
#include "MySvg.h"


class MyLine
{
private:
    vector<double> splitters;
    void create(int parent_id, Vector3d p1, Vector3d p2, MyColor c, int thickness, bool visible);
public:
    MyColor c;
    int thickness;
    int parentId;
    bool visible;
    Vector3d ps[2];
    void reverse();
    vector<MyLine> split_lines;
    MyLine();
    MyLine(const MyLine& l);
    MyLine(int parent_id, Vector3d p1, Vector3d p2);
    MyLine(int parent_id, Vector3d p1, Vector3d p2, bool visible);
    MyLine(int parent_id, Vector3d p1, Vector3d p2, MyColor c);
    MyLine(int parent_id, Vector3d p1, Vector3d p2, MyColor c, bool visible);
    MyLine(int parent_id, Vector3d p1, Vector3d p2, MyColor c, int thickness, bool visible);
    int draw(MySvg &svg);
    void addSplitter(double splitter);
    int generateSplitLines();
    int recombineLines();
    int getNoVisibleLines();
    int getVisibleLines(vector<MyLine>& vis_lines);
    bool addLineIntersectionXY(MyLine l2, Vector3d& intersection);
    bool getLineIntersectionXY(MyLine l2, Vector3d& intersection, bool infinite_line = false);
    bool addGetLineIntersectionXY(MyLine l2, bool add_splitter, Vector3d& intersection, bool infinite_line = false);
    bool getLineLineIntersection3D(MyLine l2, Vector3d& intersection);
    Vector3d get_direction();
    string str();
    bool operator==(const MyLine& l);
};

