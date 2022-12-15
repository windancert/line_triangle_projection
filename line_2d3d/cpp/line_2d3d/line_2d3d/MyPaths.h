#pragma once
#include "MyLine.h"
class MyPaths
{

private:
	MyColor c;
	int thickness;
	int removeDoubleLines(vector<MyLine>& visible_lines);
	vector<list<Vector3d>> paths_list;
public:
	MyPaths(vector<MyLine> &visible_lines);
	void draw(MySvg& svg);
	int getNoPaths();
	int getNoLines();

};

