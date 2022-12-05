#pragma once
#include "MyLine.h"
class MyPaths
{

private:
	vector<list<MyLine>> paths_list;
public:
	MyPaths(vector<MyLine> &visible_lines);
	void draw(MySvg& svg);

};

