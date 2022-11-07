from __future__ import annotations
from typing import List
import time
FLOATING_POINT_ACCURACY = 1.0e-6

X = 0
Y = 1
Z = 2

p1 = (0,0,0)
p1x = 0
p1y = 0
p2 = (1,1,1)
p2x = 1
p2y = 1
p3 = (0,2,0)
p3x = 0
p3y = 0


def triangleAreaXY(p1x,p1y,p2x,p2y,p3x,p3y) :
    
    a = abs(p1x*(p2y-p3y) +p2x*(p3y-p1y) +p3x*(p1y-p2y))/2.0
    return a


#   //if include_edge is false : if the point is on the edge, is NOT inside. 
#   //if include_edge is true  : if the point is on the edge, is inside. 
def insideTriangleXY(px,py, include_edge : bool) -> bool :
    area  = triangleAreaXY(p1x,p1y,p2x,p2y,p3x,p3y)
    area1 = triangleAreaXY(px,py,p2x,p2y,p3x,p3y)
    area2 = triangleAreaXY(p1x,p1y,px,py,p3x,p3y)
    area3 = triangleAreaXY(p1x,p1y,p2x,p2y,px,py)
    if not include_edge :
        if (area1 <= FLOATING_POINT_ACCURACY) or (area2 <= FLOATING_POINT_ACCURACY) or (area3 <= FLOATING_POINT_ACCURACY) :
            return False
    ins = (abs(area1+area2+area3) - area) <= (FLOATING_POINT_ACCURACY * area)
    return ins


if __name__ == '__main__':
    start_ms = time.perf_counter()

    a = (0,1,2)
    ax = 0
    ay = 1
    for i in range(int(1e6)):
        insideTriangleXY(ax,ay, True )

    end_ms = time.perf_counter()
    print(f"duration : {end_ms - start_ms}")
