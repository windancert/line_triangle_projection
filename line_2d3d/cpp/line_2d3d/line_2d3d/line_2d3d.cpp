// line_2d3d.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <chrono>
using namespace std::chrono;

#include "MySvg.h"
#include "MyColor.h"
#include "MyCamera.h"
#include "MyLight.h"
#include "MyTriangle.h"
#include "MyScenes.h"
#include "MyColor.h"
#include "MyPaths.h"

int getNoVisLines(vector<MyTriangle>& triangles);
void svgit(vector<MyTriangle>& triangles);
void svg_paths(MyPaths  paths);

int main()
{
    auto start = high_resolution_clock::now();

    std::cout << "Hello line 2d 3d!\n";

    //MyCamera my_cam = MyCamera(Vector3d(0, -10, 0), Vector3d(0, 0, 0), Vector3d(1, 0, 0), 0.9);
    MyCamera my_cam = MyCamera(Vector3d(-10, -8, -11), Vector3d(0, 0, 0), Vector3d(0, 1, 0), 0.9);
    MyLight my_light = MyLight(Vector3d(100, 50, 0), Vector3d(0, 0, 0), my_cam);

    vector<MyTriangle> triangles;

    test_scene(triangles, my_light, my_cam);
    //plane_scene(triangles, my_light, my_cam);
    //blocks_scene_0(triangles, my_light, my_cam);
    //blocks_scene_1(triangles, my_light, my_cam);

    cout << "No lines scene: " << getNoVisLines(triangles) << "\n";

    //
    //for (MyTriangle& triangle : triangles) {
    //    triangle.addHatches();
    //}
    
    cout << "No lines scene after hatching: " << getNoVisLines(triangles) << "\n";
    
    int no_intersects = 0;
    for (int i = 0; i < triangles.size(); i++){
        for (int j = 0; j < triangles.size(); j++) {
            no_intersects += triangles[i].addLineLineIntersectionXY(triangles[j]);
        }
    }
    cout << "No 2D LINE LINE intersects : " << no_intersects << "\n";

    // LINE PLANE INTERSECTIONS 3D
    no_intersects = 0;
    for (int i = 0; i < triangles.size(); i++) {
        for (int j = 0; j < triangles.size(); j++) {
            no_intersects += triangles[i].addTriangleIntersectXYZ(triangles[j]);
        }
    }
    cout << "No 3D LINE PLANE intersects : " << no_intersects << "\n";


    // GENERATE ALL LINE SPLITS, WHICH BECOME SUBLINES IN LINES 
    int no_lines = 0;
    for (MyTriangle& triangle : triangles) {
        triangle.generateSplitLines();
    }
    cout << "No lines scene after splitting: " << getNoVisLines(triangles) << "\n";


    // GENERATE THE LINE OBSCURATION, SETING THE VISIBILITY OF THE SUBLINES
    for (int i = 0; i < triangles.size(); i++) {
        for (int j = 0; j < triangles.size(); j++) {
            triangles[i].addTriangleObscuration(triangles[j]);
        }
    }
    cout << "No lines scene after obscuration: " << getNoVisLines(triangles) << "\n";


    // RECOMBINE WHERE POSSIBLE THE LINES
    for (MyTriangle &triangle : triangles) {
        triangle.recombineLines();
    }
    cout << "No lines scene after recomination in triangle: " << getNoVisLines(triangles) << "\n";


    vector<MyLine> all_vis_lines;
    for (MyTriangle& triangle : triangles) {
        triangle.getVisLines(all_vis_lines);
    }
    cout << "No lines : " << all_vis_lines.size() << "\n";

    // BEST F***ING TEST CODE EVAH!
    //list<MyLine> lines_list;
    //lines_list.push_back(all_vis_lines.front());
    //MyLine &line_l1 = lines_list.front();
    //line_l1.ps[0].x() = 1000000;
    //cout << line_l1.str() << "\n";
    //MyLine line_l2 = lines_list.front();
    //cout << line_l2.str() << "\n";

    //auto it = lines_list.begin();
    //while (it != lines_list.end()) {
    //    it->reverse();
    //    it->ps[0].x() = 0;
    //    it++;
    //}
    //MyLine line_l3 = lines_list.front();
    //cout << line_l3.str() << "\n";

    svgit(triangles);


    MyPaths my_paths(all_vis_lines);
    svg_paths(my_paths);
    cout << "No paths after connecting paths: " << my_paths.getNoPaths() << " with "<< my_paths.getNoLines()<<" lines\n";


    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<milliseconds>(stop - start);
    cout << "Duration : " << duration.count() << " ms\n";

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


void svgit(vector<MyTriangle>& triangles) {
    int width = 1400;
    int height = 1300;
    MySvg svg = MySvg();
    svg.create(width, height);
    svg.translate(width / 2, height / 2);

    //svg.line(MyColor().str(), 2, 10, 10, 200, 200);
    //MyColor c = MyColor(-50, 50, 260);
    //svg.line(c.str(), 2, 100, 100, 200, 200);

    int no_drawn_lines = 0;
    for (MyTriangle& triangle : triangles) {
        no_drawn_lines += triangle.draw(svg);
    }
    cout << "Drawn " << no_drawn_lines << " lines\n";

    svg.finalize();
    svg.save("svg_lined.svg");
}
void svg_paths(MyPaths  paths) {
    int width = 1400;
    int height = 1300;
    MySvg svg = MySvg();
    svg.create(width, height);
    svg.translate(width / 2, height / 2);

    //svg.line(MyColor().str(), 2, 10, 10, 200, 200);
    //MyColor c = MyColor(-50, 50, 260);
    //svg.line(c.str(), 2, 100, 100, 200, 200);

    paths.draw(svg);

    svg.finalize();
    svg.save("svg_pathed.svg");
}
int getNoVisLines(vector<MyTriangle>& triangles) {
    int no_vis_lines = 0;
    for (MyTriangle& triangle : triangles) {
        no_vis_lines += triangle.getNoVisLines();
    }
    return no_vis_lines;
}
