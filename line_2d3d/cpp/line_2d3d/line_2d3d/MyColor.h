#pragma once
#include<string>
using namespace std;

class MyColor
{
public:
	MyColor(int r_arg = -1, int g_arg = -1 , int b_arg = -1);
	string str();
	int r;
	int g;
	int b;
private:
	int _check_color(int c);
};


