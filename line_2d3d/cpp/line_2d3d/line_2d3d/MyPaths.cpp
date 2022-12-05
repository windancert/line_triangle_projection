#include "MyPaths.h"
#include "MyUtil.h"

MyPaths::MyPaths(vector<MyLine> &visible_lines)
{
    
    while (visible_lines.size() > 0) {
        paths_list.push_back(list<Vector3d>());        // create a line list and put it to the path list
        list<Vector3d>& point_path = paths_list.back(); // get a reference to add lines to. (avoid copying whole lists).

        auto check_line_it = visible_lines.begin(); // make an iterator over the visible lines
        c = check_line_it->c;
        thickness = check_line_it->thickness;
        point_path.push_back(check_line_it->ps[0]);  // copy the points of the first line
        point_path.push_back(check_line_it->ps[1]);
        check_line_it = visible_lines.erase(check_line_it);         // remove it from the list, and go for the next one

        if (visible_lines.size() > 0) {            // if there are more lines, let's check'm
            while (check_line_it != visible_lines.end()) {
                // see if the next line connects to the start or end.
                Vector3d& start = point_path.front();       // get a reference to the front (for readability)
                Vector3d& end = point_path.back();         // get a reference to the back (for readability)


                if (floatEqualsRelative(start.x(), check_line_it->ps[0].x(), FLOATING_POINT_ACCURACY) &&
                    floatEqualsRelative(start.y(), check_line_it->ps[0].y(), FLOATING_POINT_ACCURACY)) {
                    // start connects to left (0) of iterated line
                    point_path.push_back(check_line_it->ps[0]);
                    check_line_it = visible_lines.erase(check_line_it);

                }
                else if (floatEqualsRelative(start.x(), check_line_it->ps[1].x(), FLOATING_POINT_ACCURACY) &&
                    floatEqualsRelative(start.y(), check_line_it->ps[1].y(), FLOATING_POINT_ACCURACY)) {
                    // start connects to right of iterated line
                    point_path.push_back(check_line_it->ps[1]);
                    check_line_it = visible_lines.erase(check_line_it);

                }
                else if (floatEqualsRelative(end.x(), check_line_it->ps[0].x(), FLOATING_POINT_ACCURACY) &&
                    floatEqualsRelative(end.y(), check_line_it->ps[0].y(), FLOATING_POINT_ACCURACY)) {
                    // start connects to left of iterated line
                    point_path.push_back(check_line_it->ps[0]);
                    check_line_it = visible_lines.erase(check_line_it);

                }
                else if (floatEqualsRelative(end.x(), check_line_it->ps[1].x(), FLOATING_POINT_ACCURACY) &&
                    floatEqualsRelative(end.y(), check_line_it->ps[1].y(), FLOATING_POINT_ACCURACY)) {
                    // start connects to right of iterated line
                    point_path.push_back(check_line_it->ps[1]);
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
    for (list<Vector3d> point_path : paths_list) {
        auto point_it = point_path.begin();
        svg.start_path(c.str(), thickness, *point_it);
        point_it++;
        while (point_it != point_path.end()) {
            svg.add_path(*point_it);
            point_it++;
        }
        svg.end_path();
    }
}

int MyPaths::getNoPaths()
{

    return paths_list.size();
}
    
