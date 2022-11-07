#include "MySvg.h"
#include<string>
#include <sstream>
#include<iostream>
#include<fstream>
using namespace std;


MySvg::MySvg() {

    //"""
    //Create a few attributes with default values,
    //and initialize the templates dictionary.
    //"""

    width = 0;
    height = 0;
    tx = 0;
    ty = 0;

    

};

void MySvg::__add_to_svg(string text) {
    //"""
    //    Utility function to add element to drawing.
    //    """
    svg_list.push_back(text);
};


void MySvg::create(double width, double height) {

    //"""
    //    Adds the necessary opening element to document.
    //    """

    width = width;
    height = height;

    svg_list.clear();
    ostringstream ss;
    ss << "<svg width='%dpx' height='" << width << "px' height='" << height << "px' xmlns='http://www.w3.org/2000/svg' version='1.1' xmlns:xlink='http://www.w3.org/1999/xlink'>\n";
    __add_to_svg(ss.str());
};

void MySvg::finalize() {
    
    string s = "finalize";
    __add_to_svg(s);
};
void MySvg::translate(double tx, double ty) {
    tx = tx;
    ty = ty;
};


void MySvg::_translate(double* x, double* y) {
    *x += tx;
    *y += ty;
}

void MySvg::line(string color, int strokewidth, double x1, double y1, double x2, double y2) {

    //"""
    //    Adds a line using the method's arguments.
    //    """

    _translate(&x1, &y1);
    _translate(&x2, &y2);
    ostringstream ss;
    ss << "    <line stroke='" << color << "' stroke-width='" << strokewidth << "px' y2='" << y2 << "' x2='" << x2 << "' y1='{" << y1 << "' x1='" << x1 << "' />\n";
    __add_to_svg(ss.str());
};
      
      
string MySvg::str() {
    //
    //"""
    //    Returns the entire drawing by joining list elements.
    //    """
    //string str(svg_list.begin(), svg_list.end());
    string str = "roland";
    return(str);
};
void  MySvg::save(string path) {

    //"""
    //Saves the SVG drawing to specified path.
    //Let any exceptions propagate up to calling code.
    //"""
    fstream file;
    file.open(path, ios_base::out);

    if (!file.is_open()) {

        cout << "Unable to open the file.\n";
        return;
    }
    file << str();
    file.close();


};

