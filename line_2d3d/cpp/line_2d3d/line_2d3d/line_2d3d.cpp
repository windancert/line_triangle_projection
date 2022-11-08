// line_2d3d.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

#include "MySvg.h"
#include "MyColor.h"
#include "MyCamera.h"
#include "MyLight.h"


int main()
{
    std::cout << "Hello line 2d 3d!\n";
    //MySvg svg = MySvg();
    //svg.create(1000, 1000);
    //MyColor c = MyColor(-50, 50, 260);
    //svg.line(c.str(), 2, 100, 100, 200, 200);
    //svg.finalize();
    //svg.save("roland.svg");


    MySvg svg = MySvg();
    svg.create(1000, 1000);

    MyCamera my_cam = MyCamera(Vector3d(-10, -8, -11), Vector3d(0, 0, 0), Vector3d(0, 1, 0), 0.9);
    MyLight my_light = MyLight(Vector3d(100, 50, 0), Vector3d(0, 0, 0), my_cam);


};

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
