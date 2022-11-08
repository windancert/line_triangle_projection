#pragma once
#include<string>
using namespace std;

class MyColor
{
public:
	MyColor(int r_arg, int g_arg, int b_arg);
	string str();
	int r;
	int g;
	int b;
private:
	int _check_color(int c);
};


