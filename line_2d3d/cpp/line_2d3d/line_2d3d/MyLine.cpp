#include "MyLine.h"
#include "MyUtil.h"
#include <cmath>

void MyLine::create(int parent_id, Vector3d p1, Vector3d p2, MyColor c_arg, int thickness_arg, bool visible_arg)
{
    parentId = parent_id;
    FLOATING_POINT_ACCURACY = 1.0e-10;
    ps[0] = p1;
    ps[1] = p2;
    c = c_arg;
    thickness = thickness_arg;
    visible = visible_arg;

}



MyLine::MyLine()
{
    create(-1, Vector3d(), Vector3d(), MyColor(), 1, false);
}

MyLine::MyLine(const MyLine& l)
{
	create(l.parentId, l.ps[0], l.ps[1], l.c, l.thickness, l.visible);
}

MyLine::MyLine(int parent_id, Vector3d p1, Vector3d p2)
{
    create(parent_id, p1, p2, MyColor(), 1, true);
}

MyLine::MyLine(int parent_id, Vector3d p1, Vector3d p2, bool visible)
{
    create(parent_id, p1, p2, MyColor(), 1, visible);
}

MyLine::MyLine(int parent_id, Vector3d p1, Vector3d p2, MyColor c)
{
    create(parent_id, p1, p2, c, 1, true);
}

MyLine::MyLine(int parent_id, Vector3d p1, Vector3d p2, MyColor c, bool visible)
{
    create(parent_id, p1, p2, c, 1, visible);
}

MyLine::MyLine(int parent_id, Vector3d p1, Vector3d p2, MyColor c, int thickness, bool visible)
{
    create(parent_id, p1, p2, c, thickness, visible);
}

void MyLine::draw(MySvg &svg)
{
    if (visible) {
        svg.line(c.str(), thickness, ps[0][0], ps[0][1], ps[1][0], ps[1][1]);
    }
    for (MyLine line : split_lines) {
        line.draw(svg);
    }
}

void MyLine::addSplitter(double splitter)
{
    splitters.push_back(splitter);
}

int MyLine::generateSplitLines()
{
    splitters.push_back(0);
    splitters.push_back(1);
    sort(splitters.begin(), splitters.end());
    

    // generate all points for the lines.
    vector<Vector3d> new_points;
    new_points.push_back(ps[0]);
    for (int i = 0; i < splitters.size() - 1; i++) {
        //PVector p = PVector.sub(ps[1], ps[0]).mult(splitters.get(i + 1)).add(ps[0]);
        Vector3d p = (ps[1] - ps[0]) * splitters[i + 1] + ps[0];
        new_points.push_back(p);
    }

    // generate the sub lines from the points.
    for (int i = 0; i < new_points.size() - 1; i++) {
        split_lines.push_back(MyLine(parentId, new_points[i], new_points[i + 1], c, visible));
    }

    visible = false;
    return getNoVisibleLines();
}

int MyLine::recombineLines()
{
    vector<MyLine> new_lines ;

    bool prev_visible = false;
    MyLine* new_line = 0;
    for (MyLine &line : split_lines) {
        if (!prev_visible && line.visible) {
            new_line = new MyLine(line);
            prev_visible = true;
        }
        else if (prev_visible && line.visible) {
            new_line->ps[1] = line.ps[1];
        }
        else if (prev_visible && !line.visible) {
            new_lines.push_back(*new_line);
            delete new_line;
            new_line = 0;
            prev_visible = false;
        }
    }
    if (new_line != 0) {
        new_lines.push_back(*new_line);
    }
    split_lines = new_lines;

    return getNoVisibleLines();
}

int MyLine::getNoVisibleLines()
{
    int no_vis_lines = 0;
    if (visible) {
        no_vis_lines = 1;
    }
    for (MyLine l : split_lines) {
        no_vis_lines += l.getNoVisibleLines();
    }
    return no_vis_lines;
}

bool MyLine::addLineIntersectionXY(MyLine l2, Vector3d & intersection)
{
    return addGetLineIntersectionXY(l2, true, intersection);
}

bool MyLine::getLineIntersectionXY(MyLine l2, Vector3d& intersection)
{
    return addGetLineIntersectionXY(l2, false, intersection);
}

bool MyLine::addGetLineIntersectionXY(MyLine l2, bool add_splitter, Vector3d& intersection)
{
    // https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
    double x1 = ps[0][0];
    double x2 = ps[1][0];
    double y1 = ps[0][1];
    double y2 = ps[1][1];
    double x3 = l2.ps[0][0];
    double x4 = l2.ps[1][0];
    double y3 = l2.ps[0][1];
    double y4 = l2.ps[1][1];

    double noemer = ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4));
    if (abs(noemer) > FLOATING_POINT_ACCURACY) {
        double t_teller = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4));
        double u_teller = ((x1 - x3) * (y1 - y2) - (y1 - y3) * (x1 - x2));
        double t = t_teller / noemer;
        double u = u_teller / noemer;

        Vector3d p = Vector3d();
        p[0] = x1 + t * (x2 - x1);
        p[1] = y1 + t * (y2 - y1);
        p[2] = ps[0][2] + t * (ps[1][2] - ps[0][2]);

        if ((t >= 0) && (t <= 1) && (u >= 0) && (u <= 1)) {
            if (add_splitter) {
                addSplitter(t);
                l2.addSplitter(u);
            }
            intersection = p;
            return true;
        }
    }
    return false;
}



Vector3d MyLine::get_direction()
{
    
    return ps[1] - ps[0];
}





