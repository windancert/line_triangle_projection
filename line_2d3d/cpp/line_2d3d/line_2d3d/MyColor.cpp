#include <format>
#include <cstdlib>
#include <sstream>
#include <iostream>
using namespace std;

#include "MyColor.h"

MyColor :: MyColor(int r_arg, int g_arg, int b_arg) {
    if (r_arg == -1) {
        r_arg = rand() % 256;
        g_arg = rand() % 256;
        b_arg = rand() % 256;
    }

    if (g == -1) {
        g_arg = r_arg;
        b_arg = r_arg;
    }
    r = _check_color(r_arg);
    g = _check_color(g_arg);
    b = _check_color(b_arg);

    
    
}
int MyColor::_check_color(int c) {
    if (c < 0) {
        return 0;
    }
    else if (c > 255) {
        return 255;
    }
    return c;
}
string MyColor::str() {

    return format("#{:02X}{:02X}{:02X}", r, g, b);
}




