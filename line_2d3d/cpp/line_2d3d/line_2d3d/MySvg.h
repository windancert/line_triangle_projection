#pragma once
#include <vector>
#include<string>
#include <Eigen/Dense>
using Eigen::Vector3d;


using namespace std;

class MySvg
{
public:
	MySvg();
    void create(double width, double height);
    void finalize();
    void translate(double x_arg, double y_arg);
    void line(string color, int strokewidth, double x1, double y1, double x2, double y2);
    //void path(string color, int strokewidth, vector<Vector3d>& points);
    void start_path(string color, int strokewidth);
    void add_path(Vector3d points[2]);
    void end_path();
    string str();
    void save(string path);
private:
    vector<string> svg_list;
    double width;
    double height;
    double tx;
    double ty;
	void __add_to_svg(string text);
    void _translate(double& x, double& y);
    void _translate(Vector3d& p);

};

