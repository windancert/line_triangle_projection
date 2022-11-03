from __future__ import annotations
from typing import List
from MyUtils import *
from MyCamera import *
from MyColor import *
from MyLine import *
import numpy as np
from MyUtils import *
from MyLight import *

class MyTriangle :
#   MyLine[] ls;
#   PVector p1, p2, p3, n, up;  // plane : nx*x + ny*y + nz*z = o
#   float   o;
#   color   c;
#   float   shading;
#   int     id;



  def __init__(self, p1:List[float], p2:List[float], p3:List[float], vis1:bool, vis2:bool, vis3:bool, up:List[float], light_n:MyLight, lines:List[MyLine], cam:MyCamera ) :

    self.id = getID()
    self.p1 = cam.project(p1)
    self.p2 = cam.project(p2)
    self.p3 = cam.project(p3)
    self.up = up

    self.det_normal_and_o()

    self.ls = [MyLine]*3
    self.ls[0] = MyLine(self, self.p1, self.p2, MyColor(255), vis1)
    self.ls[1] = MyLine(self, self.p2, self.p3, MyColor(255), vis2)
    self.ls[2] = MyLine(self, self.p3, self.p1, MyColor(255), vis3)

    for i in range(3) :
      lines.append(self.ls[i])

    self.c = MyColor()

    self.set_light(light_n)
  

  def __str__(self) :
    return f"t: if : {self.id} n  {self.n} o: {self.o}"

  def draw(self, svg) :
    for i in range(3) :
      self.ls[i].draw(svg)

  def draw_normal(self, svg) :
    c = self.center()
    cn = np.add(c,np.multiply(n, 50))
    svg.line(str(MyColor(255,0,0)), self.thickness, c[X], c[Y], cn[X], cn[Y] )

  def equals(self, t:MyTriangle) -> bool:
    return self.id == t.id


  def triangleAreaXY(self, p1:List[float], p2:List[float], p3:List[float]) :
    a = abs(p1[X]*(p2[Y]-p3[Y]) + p2[X]*(p3[Y]-p1[Y]) + p3[X]*(p1[Y]-p2[Y]))/2.0
    return a
  

#   //if include_edge is false : if the point is on the edge, is NOT inside. 
#   //if include_edge is true  : if the point is on the edge, is inside. 
  def insideTriangleXY(self, p:List[float], include_edge : bool) -> bool :
    area  = self.triangleAreaXY(self.p1, self.p2, self.p3)
    area1 = self.triangleAreaXY(p, self.p2, self.p3)
    area2 = self.triangleAreaXY(self.p1, p, self.p3)
    area3 = self.triangleAreaXY(self.p1, self.p2, p)
    if not include_edge :
      if (area1 <= FLOATING_POINT_ACCURACY) or (area2 <= FLOATING_POINT_ACCURACY) or (area3 <= FLOATING_POINT_ACCURACY) :
        return False
    ins = (abs(area1+area2+area3) - area) <= (FLOATING_POINT_ACCURACY * area)
    return ins
  

  def det_normal_and_o(self) :
    s = np.subtract(self.p2, self.p1)
    t = np.subtract(self.p3, self.p2)
    n = np.cross(s,t )
    self.n = n / np.linalg.norm(n)
    self.o = np.dot(self.n, self.p1)
  

  def center(self) -> List[float] :
    p = np.add(self.p1, self.p2)
    p = np.add(p, self.p3)
    p = np.multiply(p, (1.0/3.0))
    return p
  

#   /**
#    * #TODO DIT IS NOG NIET GOED>
#    */
#   MyLine planePlaneIntersect(MyTriangle pl2) {
#     //https://mathemerize.com/equation-of-plane-passing-through-intersection-of-two-planes/
#     //https://www[Y]outube.com/watch?v=O6O_64zIEYI

#     PVector v = n.cross( pl2.n);

#     float o1 = o;
#     float o2 = pl2.o;
#     PVector n1 = n;
#     PVector n2 = pl2.n;

#     if ( PVector.sub(n1, n2).dot(1, 1, 1) < FLOATING_POINT_ACCURACY) {
#       println("Parallel");
#       return null;
#     }

#     MyLine l;
#     if ((abs(n1[X]) < FLOATING_POINT_ACCURACY) && (abs(n1[Y]) < FLOATING_POINT_ACCURACY)) {
#       // we cannot take z = 0; so we take y = 0
#       println("plane 1 parallel z plane");
#       float teller = o1 - o2 + n2.dot(v) - n1.dot(v);
#       float noemer = n1[X] - (n2[X] * n1[Z]) / n2[Z];
#       float px = teller / noemer;
#       float pz = (o2 - n2.dot(v) - n2[X]*px ) / n2[Z];

#       PVector p = new PVector(px, 0, pz);
#       l = new MyLine(this, v, p, color(255, 0, 0), 5, true);
#       println("found line : " +l);
#     } else {
#       // z = 0
#       println("plane 1 crosses z plane");

#       float teller = o1 - o2 + n2.dot(v) - n1.dot(v);
#       float noemer = n1[X] - (n2[X] * n1[Y]) / n2[Y];
#       float px = teller / noemer;
#       float py = (o2 - n2.dot(v) - n2[X]*px ) / n2[Y];

#       PVector p = new PVector(px, py, 0);
#       l = new MyLine(this, v, p, color(255, 0, 0), 5, true);
#       println("found line : " +l);
#     }

#     return l;
#   }

  def getZ(self, x:float, y:float) -> float :
    if (self.n[Z] != 0):
       return (self.o - self.n[X]*x - self.n[Y]*y)/self.n[Z]
    else :
        return 0

  def set_light(self, l : MyLight) :
    self.shading = np.dot(self.n, l.getNormalizedDirection())
    if (self.shading > 0) :
      self.shading = 0
    else:
      self.shading = -self.shading
    

  def getHatches(self) -> List[MyLine]:
    hatches = []
    hatch_min = 5
    hatch_grad = 15

    if np.dot(self.n, (0,0,1)) <= 0 :
    #   // no need to hatch the backside of a vertex
      return hatches
    


    left = self.p1
    if (self.p2[X] < left[X]) : left = self.p2
    if (self.p3[X] < left[X]) : left = self.p3
    right = self.p1
    if (self.p2[X] > right[X]) : right = self.p2
    if (self.p3[X] > right[X]) : right = self.p3

    bottom = self.p1
    if (self.p2[Y] < bottom[Y]) : bottom = self.p2
    if (self.p3[Y] < bottom[Y]) : bottom = self.p3
    top = self.p1
    if (self.p2[Y] > top[Y]) : top = self.p2
    if (self.p3[Y] > top[Y]) : top = self.p3

    # // make a square around the triangle
    sqr_bl = [0]*2
    sqr_bl[X] = left[X]
    sqr_bl[Y] = bottom[Y]
    sqr_tr = [0]*2
    sqr_tr[X] = right[X]
    sqr_tr[Y] = top[Y]

    # // https://www.tutorialspoint.com/Check-whether-a-given-point-lies-inside-a-Triangle

    



    hatch_spacing =  hatch_min + self.shading*hatch_grad; #pixels, to be replaces with shading
    x = sqr_bl[X]
    while x < sqr_tr[X]:
      b = [x, bottom[Y] - FLOATING_POINT_ACCURACY, 0]
      b[Z] = self.getZ(b[X], b[Y])
      t = [x, top[Y] + FLOATING_POINT_ACCURACY, 0]
      t[Z] = self.getZ(t[X], t[Y])

      hatch_line = MyLine(self, b, t)

      intersects = []  #// intersectes within the square/triangle
      for i in range(3):
        is_is, i_s = hatch_line.getLineIntersectionXY(self.ls[i])
        if is_is:
          is_in = self.insideTriangleXY(i_s, True)
          if is_in:
            intersects.extend(i_s)
      
      if len(intersects) == 3 :
        # // remove duplicate: probably  a triangle corner
        hash_set = set(intersects)
        intersects = list(hash_set)
      
      
      if len(intersects) == 2 :
        hatches.extend(MyLine(self, intersects[0], intersects[1], MyColor(255)))
      

      x += hatch_spacing

    return hatches