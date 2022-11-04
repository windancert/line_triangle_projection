from __future__ import annotations
from typing import List
import time
FLOATING_POINT_ACCURACY = 1.0e-6

X = 0
Y = 1
Z = 2

p1 = (0,0,0)
p2 = (1,1,1)
p3 = (0,2,0)

def triangleAreaXY(p1:tuple[float,float,float], p2:tuple[float,float,float], p3:tuple[float,float,float]) :
    
    # p1x = p1[X]
    # p1y = p1[Y]
    # p2x = p2[X]
    # p2y = p2[Y]
    # p3x = p3[X]
    # p3y = p3[Y]
    a = abs(p1[X]*(p2[Y]-p3[Y]) +p2[X]*(p3[Y]-p1[Y]) + p3[X]*(p1[Y]-p2[Y]))/2.0
    return a


#   //if include_edge is false : if the point is on the edge, is NOT inside. 
#   //if include_edge is true  : if the point is on the edge, is inside. 
def insideTriangleXY(p:tuple[float,float,float], include_edge : bool) -> bool :
    area  = triangleAreaXY(p1, p2, p3)
    area1 = triangleAreaXY(p, p2, p3)
    area2 = triangleAreaXY(p1, p, p3)
    area3 = triangleAreaXY(p1, p2, p)
    if not include_edge :
        if (area1 <= FLOATING_POINT_ACCURACY) or (area2 <= FLOATING_POINT_ACCURACY) or (area3 <= FLOATING_POINT_ACCURACY) :
            return False
    ins = (abs(area1+area2+area3) - area) <= (FLOATING_POINT_ACCURACY * area)
    return ins


if __name__ == '__main__':
    start_ms = time.perf_counter()

    a = (0,1,2)
    for i in range(int(1e6)):
        insideTriangleXY(a, True )

    end_ms = time.perf_counter()
    print(f"duration : {end_ms - start_ms}")
