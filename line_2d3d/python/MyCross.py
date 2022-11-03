
from typing import List
from MyColor import *
from MyTriangle import *
from svg import *
from MyUtils import *


class MyCross :
#   PVector p;
#   color   c;
#   int     thickness;

  def __init__(self, p:List[float], c:MyColor, thickness) :
    self.c = c
    self.p = p
    self.thickness = thickness
  

  def draw(self, svg) :

    svg.line(str(self.c), self.thickness, self.p[X]-10, self.p[Y]-10, self.p[X]+10, self.p[Y]+10)
