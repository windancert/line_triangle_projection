#include <format>
#include <iostream>
#include "MyTriangle.h"
#include "MyUtil.h"


void MyTriangle::create(Vector3d p1_arg, Vector3d p2_arg, Vector3d p3_arg, bool vis1, bool vis2, bool vis3, Vector3d up_arg, MyLight& light_n, MyCamera& cam)
{
    FLOATING_POINT_ACCURACY = 1.0e-6;
    id = getID();
    p1 = cam.project(p1_arg);
    p2 = cam.project(p2_arg);
    p3 = cam.project(p3_arg);
    up = up_arg;

    det_normal_and_o();

    ls[0] = MyLine(id, p1, p2, MyColor(255), vis1);
    ls[1] = MyLine(id, p2, p3, MyColor(255), vis2);
    ls[2] = MyLine(id, p3, p1, MyColor(255), vis3);

    for (int i = 0; i < 3; i++) {
        lines.push_back(ls[i]);
    }

    ///set_light(light_n);
    shading = n.dot(light_n.getNormalizedDirection());
    if (shading > 0) {
        shading = 0;
    }
    else {
        shading = -shading;
    }

}

void MyTriangle::det_normal_and_o()
{
    Vector3d s = p2 - p1;
    Vector3d t = p3 - p2;
    n = s.cross(t);
    n.normalize();
    o = n.dot(p1);
    cout << "det_normal_and_o: n " << n << " o " << o << "\n";
}


MyTriangle::MyTriangle(Vector3d p1_arg, Vector3d p2_arg, Vector3d p3_arg, bool vis1, bool vis2, bool vis3, Vector3d up_arg, MyLight& light_n, MyCamera& cam)
{
    create(p1_arg, p2_arg, p3_arg, vis1, vis2, vis3, up_arg, light_n, cam);
}

MyTriangle::MyTriangle(Vector3d p1, Vector3d p2, Vector3d p3, Vector3d up, MyLight& light_n, MyCamera& cam)
{
    create(p1, p2, p3, true, true, true, up, light_n, cam);
}

void MyTriangle::draw(MySvg svg)
{
    for (int i = 0; i < 3; i++) {
        ls[i].draw(svg);
    }
}

void MyTriangle::draw_normal(MySvg svg)
{
    Vector3d c = center();
    Vector3d cn = n * 50;
    svg.line(MyColor(255,0,0).str(), 1, c[0], c[1], cn[0], cn[1]);
}

string MyTriangle::str()
{
    //return format("id {} n {} o {}", id, n, o);
    return string("roland");
}



bool MyTriangle::equals(MyTriangle& t)
{
    return id == t.id;
}

Vector3d MyTriangle::center()
{
    Vector3d c = (p1 + p2 + p3) / 3.0;
    return c;
}

double MyTriangle::triangleAreaXY(Vector3d p1, Vector3d p2, Vector3d p3)
{
    return abs((p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1])) / 2.0);
}

//if include_edge is false : if the point is on the edge, is NOT inside. 
//if include_edge is true  : if the point is on the edge, is inside. 
bool MyTriangle::insideTriangleXY(Vector3d p, bool include_edge)
{
    double area = triangleAreaXY(p1, p2, p3);
    double area1 = triangleAreaXY(p, p2, p3);
    double area2 = triangleAreaXY(p1, p, p3);
    double area3 = triangleAreaXY(p1, p2, p);
    if (!include_edge) {
        if ((area1 <= FLOATING_POINT_ACCURACY) || (area2 <= FLOATING_POINT_ACCURACY) || (area3 <= FLOATING_POINT_ACCURACY))
        {
            return false;
        }
    }
    return ((abs(area1 + area2 + area3) - area) <= FLOATING_POINT_ACCURACY * area);
    return false;
}

double MyTriangle::getZ(double x, double y)
{
    if (n[2] != 0) {
        return (o - n[0] * x - n[1] * y) / n[2];
    }
    return 0;

}


/***
* add for all lines in this triangle the intersections in 3d
*/
void MyTriangle::addTriangleIntersectXYZ(MyTriangle& triangle)
{
    if (triangle.id != id) {
        for (MyLine line : lines) {
            // https://en.wikipedia.org/wiki/Line%E2%80%93plane_intersection
            Vector3d p0 = ls[0].ps[0];
            Vector3d l0 = line.ps[0];
            Vector3d l = line.get_direction();
            double teller = (p0 - l0).dot(n);
            double noemer = l.dot(n);
            if (abs(noemer) > FLOATING_POINT_ACCURACY) {
                double d = teller / noemer;
                Vector3d p = l0 + l * d;
                if (insideTriangleXY(p, true) && (d < 1.0) && (d > 0.0)) {
                    line.addSplitter(d);
                }
            }
        }
    
    }
}

/**
* For each line in this triangle add obscuratoin by other triangle.
*/
void MyTriangle::addTriangleObscuration(MyTriangle& triangle)
{
    if (triangle.id != id) {
        for (MyLine line : lines) {
            addTriangleObscuration(triangle, line);
            for (MyLine split_line : line.split_lines) {
                addTriangleObscuration(triangle, split_line);
            }
        }
    }
}

int MyTriangle::getNoVisLines()
{
    int no_vis_lines = 0;
    for (MyLine line : lines) {
        no_vis_lines += line.getNoVisibleLines();
    }
    return no_vis_lines;
}

void MyTriangle::addTriangleObscuration(MyTriangle& triangle, MyLine& line) {
    Vector3d p = line.ps[0] + line.get_direction() * 0.5;
    double tz = getZ(p[0], p[1]);

    if (insideTriangleXY(p, false) && floatSmallerThenRelative(p[2], tz, 100 * FLOATING_POINT_ACCURACY)) {
        line.visible = false;
    }
}

void MyTriangle::addHatches()
{
    double hatch_min = 5;
    double hatch_grad = 15;

    double dothtis = n.dot(Vector3d(0, 0, 1));
    if (n.dot(Vector3d(0, 0, 1)) <= 0) {
        cout << " out "<< n << " "  << dothtis << "\n";
        return;
    }


    Vector3d left = p1;
    if (p2[0] < left[0]) left = p2;
    if (p3[0] < left[0]) left = p3;
    Vector3d right = p1;
    if (p2[0] > right[0]) right = p2;
    if (p3[0] > right[0]) right = p3;

    Vector3d bottom = p1;
    if (p2[1] < bottom[1]) bottom = p2;
    if (p3[1] < bottom[1]) bottom = p3;
    Vector3d top = p1;
    if (p2[1] > top[1]) top = p2;
    if (p3[1] > top[1]) top = p3;

    // make a square around the triangle
    Vector3d sqr_bl;
    sqr_bl[0] = left[0];
    sqr_bl[1] = bottom[1];
    Vector3d sqr_tr = Vector3d();
    sqr_tr[0] = right[0];
    sqr_tr[1] = top[1];



    //Vector3d view_dir = Vector3d.sub(cam_pos, look_at).normalize();
    //Vector3d side_dir = up.cross(view_dir).normalize();
    //Vector3d e = view_dir.cross(side_dir).normalize();

    // https://www.tutorialspoint.com/Check-whether-a-given-point-lies-inside-a-Triangle
    double hatch_spacing = hatch_min + shading * hatch_grad; //pixels, to be replaced with shading
    double hatch_start = sqr_bl[0] - fmod(sqr_bl[0], hatch_spacing);
    cout << " hatch_start " << hatch_start << "\n";
    for (double x = hatch_start; x < sqr_tr[0]; x += hatch_spacing) {
        Vector3d b = Vector3d(x, bottom[1] - FLOATING_POINT_ACCURACY, 0);
        b[2] = getZ(b[0], b[1]);
        Vector3d t = Vector3d(x, top[1] + FLOATING_POINT_ACCURACY, 0);
        t[2] = getZ(t[0], t[1]);


        MyLine hatch_line = MyLine(id, b, t);

        vector<Vector3d> intersections;  // intersectes within the square/triangle
        for (int i = 0; i < 3; i++) {
            Vector3d intersect;
            if (hatch_line.getLineIntersectionXY(ls[i], intersect)) {
                bool is_in = insideTriangleXY(intersect, true);
                if (is_in) {
                    intersections.push_back(intersect);
                }
            }
        }

        if (intersections.size() == 3) {
            Vector3d delta = (intersections[0] - intersections[1]);
            if (floatEqualsRelative(0, delta.norm(), FLOATING_POINT_ACCURACY)) {
                intersections.erase(intersections.begin() + 1);
            } else {
                intersections.erase(intersections.begin() + 2);
            }
        }

        if (intersections.size() == 2) {
            lines.push_back(MyLine(id, intersections[0], intersections[1], MyColor(255)));
        }
    }


}

