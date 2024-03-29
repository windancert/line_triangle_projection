#include <iostream>
using namespace std;

#include "MyPaths.h"
#include "MyUtil.h"

int MyPaths::removeDoubleLines(vector<MyLine>& visible_lines)
{
    int no_lines_removed = 0;
    auto line_it = visible_lines.begin();
    while (line_it != visible_lines.end()) {
        auto line_it2 = line_it+1;
        while (line_it2 != visible_lines.end()) {
            if (*line_it2 == *line_it) {
                line_it = visible_lines.erase(line_it);
                no_lines_removed++;
                //cout << ".";
                break;
            }
            else {
                line_it2++;
            }
        }
        line_it++;
    }
    return no_lines_removed;

}

MyPaths::MyPaths(vector<MyLine> &visible_lines)
{
    // initialise variables. WIll be overwritten by first line.
    c = MyColor();
    thickness = 1;


    //Find length 0 lines, kill em.
    cout << "Culling zero length lines : from " << visible_lines.size() << " --> ";
    auto line_it = visible_lines.begin();
    while (line_it != visible_lines.end()) {
        if (floatEqualsRelative(line_it->ps[0].x(), line_it->ps[1].x(), FLOATING_POINT_ACCURACY) &&
            floatEqualsRelative(line_it->ps[0].y(), line_it->ps[1].y(), FLOATING_POINT_ACCURACY)) {
            line_it = visible_lines.erase(line_it);
        }
        else {
            line_it++;
        }
    }
    cout << visible_lines.size() << "\n";

    //Find length double lines, kill em.
    removeDoubleLines(visible_lines);
    cout << "Culling double lines to " << visible_lines.size() << "\n";

    
    bool no_more_connections_found = true;
    while (visible_lines.size() > 0) {

        if (no_more_connections_found) {
            paths_list.push_back(list<Vector3d>());        // create a line list and put it to the path list
            list<Vector3d>& point_path = paths_list.back(); // get a reference to add lines to. (avoid copying whole lists).

            auto first_line_it = visible_lines.begin();
            c = first_line_it->c;
            thickness = first_line_it->thickness;
            point_path.push_back(first_line_it->ps[0]);  // copy the points of the first line
            point_path.push_back(first_line_it->ps[1]);
            visible_lines.erase(first_line_it);            // remove it from the list, and go for the next one
        }
        else {
            no_more_connections_found = true;
        }


        list<Vector3d>& point_path = paths_list.back();
        auto check_line_it = visible_lines.begin(); // make an iterator over the visible lines
        while (check_line_it != visible_lines.end()) {
            // see if the next line connects to the start or end.
            Vector3d& start = point_path.front();       // get a reference to the front (for readability)
            Vector3d& end = point_path.back();         // get a reference to the back (for readability)


            if (floatEqualsRelative(start.x(), check_line_it->ps[0].x(), FLOATING_POINT_ACCURACY) &&
                floatEqualsRelative(start.y(), check_line_it->ps[0].y(), FLOATING_POINT_ACCURACY)) {
                // start connects to left (0) of iterated line
                point_path.push_front(check_line_it->ps[1]);
                check_line_it = visible_lines.erase(check_line_it);
                no_more_connections_found = false;
                break;
            }
            else if (floatEqualsRelative(start.x(), check_line_it->ps[1].x(), FLOATING_POINT_ACCURACY) &&
                floatEqualsRelative(start.y(), check_line_it->ps[1].y(), FLOATING_POINT_ACCURACY)) {
                // start connects to right of iterated line
                point_path.push_front(check_line_it->ps[0]);
                check_line_it = visible_lines.erase(check_line_it);
                no_more_connections_found = false;
                break;
            }
            else if (floatEqualsRelative(end.x(), check_line_it->ps[0].x(), FLOATING_POINT_ACCURACY) &&
                floatEqualsRelative(end.y(), check_line_it->ps[0].y(), FLOATING_POINT_ACCURACY)) {
                // start connects to left of iterated line
                point_path.push_back(check_line_it->ps[1]);
                check_line_it = visible_lines.erase(check_line_it);
                no_more_connections_found = false;
                break;
            }
            else if (floatEqualsRelative(end.x(), check_line_it->ps[1].x(), FLOATING_POINT_ACCURACY) &&
                floatEqualsRelative(end.y(), check_line_it->ps[1].y(), FLOATING_POINT_ACCURACY)) {
                // start connects to right of iterated line
                point_path.push_back(check_line_it->ps[0]);
                check_line_it = visible_lines.erase(check_line_it);
                no_more_connections_found = false;
                break;
            }
            else {
                check_line_it++;
            }

        }
    }
    

    return;

}

void MyPaths::draw(MySvg& svg)
{
    auto path_it = paths_list.begin();
    while (path_it != paths_list.end()){
        
        auto point_it = path_it->begin();
        svg.start_path(c.str(), thickness, *point_it);
        point_it++;
        while (point_it != path_it->end()) {
            svg.add_path(*point_it);
            point_it++;
        }
        svg.end_path();

        path_it++;
    }
}

int MyPaths::getNoPaths()
{
    return paths_list.size();
}

int MyPaths::getNoLines()
{
    int no_lines = 0;
    auto path_it = paths_list.begin();
    while (path_it != paths_list.end()) {
        no_lines += (path_it->size()-1);
        path_it++;
    }

    return no_lines;
}
    
