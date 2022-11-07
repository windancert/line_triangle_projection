#pragma once
#include <vector>
#include<string>

using namespace std;

class MySvg
{
public:
	MySvg();
    void create(double width, double height);
    void finalize();
    void translate(double x, double y);
    void line(string color, int strokewidth, double x1, double y1, double x2, double y2);
    string str();
    void save(string path);
private:
    vector<string> svg_list;
    double width;
    double height;
    double tx;
    double ty;
	void __add_to_svg(string text);
    void _translate(double* x, double* y);

};

