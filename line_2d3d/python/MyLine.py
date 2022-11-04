from __future__ import annotations
from typing import List
from MyUtils import *
from MyCamera import *
from MyColor import *
from MyTriangle import *
import numpy as np
from MyUtils import *


class MyLine :
#   PVector[] ps;
#   MyTriangle parent;
#   FloatList splitters;
#   color c;
#   int thickness;
#   boolean visible;
#   ArrayList<MyLine> split_lines;

#   MyLine(MyLine l) {
#     this(l.parent, l.ps[0], l.ps[1], l.c, l.thickness, l.visible);
#   }

#   MyLine(MyTriangle t, PVector p1, PVector p2) {
#     this(t, p1, p2, randColor(), 1, true);
#   }
#   MyLine(MyTriangle t, PVector p1, PVector p2, boolean visible) {
#     this(t, p1, p2, randColor(), 1, visible);
#   }

#   MyLine(MyTriangle t, PVector p1, PVector p2, color c) {
#     this(t, p1, p2, c, 1, true);
#   }
#   MyLine(MyTriangle t, PVector p1, PVector p2, color c, boolean visible) {
#     this(t, p1, p2, c, 1, visible);
#   }

  def __init__(self, t:MyTriangle, p1:tuple[float,float,float], p2:tuple[float,float,float], c:MyColor=MyColor(100), thickness:int=1, visible:bool = True) :
    self.parent = t
    self.ps = (p1,p2)
    self.c = c
    self.thickness = thickness
    self.visible = visible

    self.splitters = []
    self.split_lines = []
  
  def copy(self) -> MyLine :
    return MyLine(self.parent, self.ps[0], self.ps[1], self.c, self.thickness, self.visible)

  def draw(self, svg) :
    if (self.visible) :
        # def line(self, stroke, strokewidth, x1, y1, x2, y2):
        svg.line(str(self.c), self.thickness, self.ps[0][X], self.ps[0][Y], self.ps[1][X], self.ps[1][Y])

    for line in self.split_lines :
      line.draw(svg)

  def __str__(self) :
    return f"Line : p0:  {self.ps[0]} ; p[1]: {self.ps[1]}"
  

  def addSplitter(self, splitter:float) :
    self.splitters.append(splitter)
  


  def generateSplitLines(self) -> int:
    self.splitters.append(0)
    self.splitters.append(1)
    self.splitters.sort()

    # // generate all points for the lines.
    new_points = []
    new_points.append(self.ps[0])
    # for (int i = 0; i < splitters.size()-1; i++) {
    for i in range(len(self.splitters)- 1):
        #   PVector p = PVector.sub(ps[1], ps[0]).mult(splitters.get(i+1)).add(ps[0]);
        p = np.subtract(self.ps[1], self.ps[0])
        p = np.multiply(p, self.splitters[i+1])
        p = np.add(p, self.ps[0])
        new_points.append(p)
    

    # // generate the sub lines from the points.
    # for (int i = 0; i < new_points.size() - 1; i ++) {
    for i in range(len(new_points) - 1):
      self.split_lines.append(MyLine(self.parent, new_points[i], new_points[i+1], self.c , self.thickness, self.visible))
    

    self.visible = False
    return self.getNoVisibleLines()
  

  def recombineLines(self) -> int :
    new_lines = []

    prev_visible = False
    new_line = 0
    for line in self.split_lines :
      if not prev_visible and line.visible : 
        new_line = line.copy()
        prev_visible = True
      elif prev_visible and line.visible :
        new_line.ps = (new_line.ps[0], line.ps[1])
      elif prev_visible and not line.visible :
        new_lines.append(new_line)
        new_line = 0
        prev_visible = False
    
    if new_line != 0:
      new_lines.append(new_line)
    
    self.split_lines = new_lines

    return self.getNoVisibleLines()
  

  def getNoVisibleLines(self) -> int :
    no_vis_lines = 0
    if self.visible :
      no_vis_lines = 1
    
    for l in self.split_lines :
      no_vis_lines += l.getNoVisibleLines()
    
    return no_vis_lines
  

    #   /**
    #    * Intersection with the other line in 2 dimensions (xy)
    #    * returns [v3  : intersection point, only if within line-piece : NO Z])
    #    */
  def addLineIntersectionXY(self, l2:MyLine) :
    return self.addGetLineIntersectionXY(l2, True)
  

  def getLineIntersectionXY(self, l2:MyLine)  :
    return self.addGetLineIntersectionXY(l2, False)
  

  def addGetLineIntersectionXY(self, l2:MyLine, add_splitter:bool) :
    # // https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection

    x1 = self.ps[0][X]
    x2 = self.ps[1][X]
    y1 = self.ps[0][Y]
    y2 = self.ps[1][Y]
    x3 = l2.ps[0][X]
    x4 = l2.ps[1][X]
    y3 = l2.ps[0][Y]
    y4 = l2.ps[1][Y]

    noemer = ((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
    if (abs(noemer) > FLOATING_POINT_ACCURACY ) :
        t_teller = ((x1-x3)*(y3-y4) - (y1-y3)*(x3-x4))
        u_teller = ((x1-x3)*(y1-y2) - (y1-y3)*(x1-x2))
        t = t_teller / noemer 
        u = u_teller / noemer 

        
        p = (x1 + t*(x2-x1), y1 + t*(y2-y1) , self.ps[0][Z] + t*(self.ps[1][Z]-self.ps[0][Z]))

        if ((t >= 0) and (t <= 1) and (u >= 0) and (u <= 1)    ) :
            if (add_splitter) :
                self.addSplitter(t)
                l2.addSplitter(u)
            return True, p

    return False, 0

    #   /**
    #    * calculate intersection triangle with line.
    #    *
    #    * @param {*} line
    #    * @returns v3: point of intersection, NaN if no interserction
    #    */
  def addTriangleIntersectXYZ(self, triangle_arg:MyTriangle) :
    # // https://en.wikipedia.org/wiki/Line%E2%80%93plane_intersection
    p0 = triangle_arg.ls[0].ps[0]
    l0 = self.ps[0]
    l  = self.get_direction()
    teller = np.dot(np.subtract(p0, l0), triangle_arg.n)
    noemer = np.dot(l, triangle_arg.n)
    if (abs(noemer) > FLOATING_POINT_ACCURACY ) :
      d = teller / noemer
      p = np.add(l0, np.multiply(l, d))
      if triangle_arg.insideTriangleXY(p, True) and (d < 1.0) and (d > 0.0) :
        self.addSplitter(d)
        return True, p
    return False, 0

#   /**
#    * check and set visibility wrt the triangles. Take care of lines that are part of triangle:
#    */
  def addTriangleObscuration(self, triangle: MyTriangle) :
    p = np.add(np.multiply(self.get_direction(), 0.5), self.ps[0])  # middle of line
    tz = triangle.getZ(p[X], p[Y])
    
    if (self.parent != triangle) and (triangle.insideTriangleXY(p, False) and floatSmallerThenRelative(p[Z], tz, 100*FLOATING_POINT_ACCURACY)) :
      self.visible = False

    for split_line in self.split_lines :
      split_line.addTriangleObscuration(triangle)

  def getNoVisibleLines(self) -> int:
    no_vis_lines = 0
    if self.visible:
        no_vis_lines += 1
    for split_line in self.split_lines :
        no_vis_lines += split_line.getNoVisibleLines()
    return no_vis_lines


  def get_direction(self) -> List[float] :
    return np.subtract(self.ps[1], self.ps[0])
  