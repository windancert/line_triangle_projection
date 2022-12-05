#include "MyPaths.h"
#include "MyPath.h"
#include "MyUtil.h"

MyPaths::MyPaths(vector<MyLine> &visible_lines)
{
    
    while (visible_lines.size() > 0) {
        paths_list.push_back(list<MyLine>());        // create a line list and put it to the path list
        list<MyLine>& line_path = paths_list.back(); // get a reference to add lines to. (avoid copying whole lists).

        auto check_line_it = visible_lines.begin(); // make an iterator over the visible lines
        line_path.push_back(*check_line_it);        // copy this line to the path start
        check_line_it = visible_lines.erase(check_line_it);         // remove it from the list

        if (visible_lines.size() > 0) {            // if there are more lines, let's check'm
            while (check_line_it != visible_lines.end()) {
                // see if the next line connects to the start or end.
                MyLine& start = line_path.front();       // get a reference to the front (for readability)
                MyLine& end = line_path.back();         // get a reference to the back (for readability)


                if (floatEqualsRelative(start.ps[0].x(), check_line_it->ps[0].x(), FLOATING_POINT_ACCURACY) &&
                    floatEqualsRelative(start.ps[0].y(), check_line_it->ps[0].y(), FLOATING_POINT_ACCURACY)) {
                    // start connects to left (0) of iterated line
                    line_path.push_back(*check_line_it);
                    check_line_it = visible_lines.erase(check_line_it);

                }
                else if (floatEqualsRelative(start.ps[0].x(), check_line_it->ps[1].x(), FLOATING_POINT_ACCURACY) &&
                    floatEqualsRelative(start.ps[0].y(), check_line_it->ps[1].y(), FLOATING_POINT_ACCURACY)) {
                    // start connects to right of iterated line
                    check_line_it->reverse();
                    line_path.push_back(*check_line_it);
                    check_line_it = visible_lines.erase(check_line_it);

                }
                else if (floatEqualsRelative(end.ps[1].x(), check_line_it->ps[0].x(), FLOATING_POINT_ACCURACY) &&
                    floatEqualsRelative(end.ps[1].y(), check_line_it->ps[0].y(), FLOATING_POINT_ACCURACY)) {
                    // start connects to left of iterated line
                    check_line_it->reverse();
                    line_path.push_back(*check_line_it);
                    check_line_it = visible_lines.erase(check_line_it);

                }
                else if (floatEqualsRelative(end.ps[1].x(), check_line_it->ps[1].x(), FLOATING_POINT_ACCURACY) &&
                    floatEqualsRelative(end.ps[1].y(), check_line_it->ps[1].y(), FLOATING_POINT_ACCURACY)) {
                    // start connects to right of iterated line
                    line_path.push_back(*check_line_it);
                    check_line_it = visible_lines.erase(check_line_it);

                }
                else {
                    check_line_it++;
                }
            }
        }
    }
    



}

void MyPaths::draw(MySvg& svg)
{
    for (list<MyLine> line_path : paths_list) {
        svg.start_path(line_path.begin()->c.str(), line_path.begin()->thickness);
        for (MyLine& line : line_path) {
            svg.add_path(line.ps);
        }
        svg.end_path();
    }
}
    
