from typing import List
from MyCamera import *
from MyLight import *
from MyTriangle import *
from MyUtils import *
import numpy as np






def test_scene(self, my_triangles:List[MyTriangle], my_lines:List[MyLine], my_light:List[MyLight], cam:MyCamera) :

    up = (0,1,0)

    my_triangles.add(MyTriangle((    0, 400, 0), ( 400, 0, 0), (  -40, 0, 0), True,True,True, up, my_light, my_lines, cam))
    my_triangles.add(MyTriangle((260, 40, 240), (-240, -40, 220), ( -100, 200, -200), True,True,True, up, my_light, my_lines, cam))




def blocks_scene_0( my_triangles:List[MyTriangle], my_lines:List[MyLine], my_light:List[MyLight], cam:MyCamera) :

    ribes =  (250,290,320)
    i = 0
    j = 0
    k = 0

    p = (ribes[X] * i * 2.0, ribes[Y] * j * 2.0, ribes[Z] * k * 2.0)
    block(p, ribes , my_triangles, my_lines, my_light, cam)



def blocks_scene_1( my_triangles:List[MyTriangle], my_lines:List[MyLine], my_light:List[MyLight], cam:MyCamera) :
  
  ribes =  (50,190,250)
  for i in range(-1,2) :
    for j in range(-1,2) :
      for k in range(-1,2) :
        p = (ribes[X] * i * 2.0, ribes[Y] * j * 2.0, ribes[Z] * k * 2.0)
        block(p, ribes , my_triangles, my_lines, my_light, cam)
      
    
  





def block( p:List[float], ribes:List[float], my_triangles:List[MyTriangle], my_lines:List[MyLine], light_n:List[MyLight], cam:MyCamera) :
 
    rx = (ribes[X], 0, 0)
    ry = (0, ribes[Y], 0)
    rz = (0, 0, ribes[Z])
    
    A = list(p)
    B = np.add(p,rx)
    C = np.add(np.add(np.add(p,rx),ry), ry)
    D = np.add(p,ry)
  
    E = np.add(p,rz)
    F = np.add(np.add(p,rz),rx)
    G = np.add(np.add(np.add(p,rz),ry),ry)
    H = np.add(np.add(p,rz),ry)
    
    x = (1,0,0)
    y = (0,1,0)
    z = (0,0,1)
  
    my_triangles.append(MyTriangle(A,B,F, True,True,False,z, light_n, my_lines, cam))
    my_triangles.append(MyTriangle(F,E,A, True,True,False,z, light_n, my_lines, cam))
    
    my_triangles.append(MyTriangle(G,C,D, True,True,False,z, light_n, my_lines, cam))
    my_triangles.append(MyTriangle(D,H,G, True,True,False,z, light_n, my_lines, cam))
  
    my_triangles.append(MyTriangle(F,B,C, False,True,False,y, light_n, my_lines, cam))
    my_triangles.append(MyTriangle(C,G,F, False,True,False,y, light_n, my_lines, cam))

    my_triangles.append(MyTriangle(H,D,A, False,True,False,y, light_n, my_lines, cam))
    my_triangles.append(MyTriangle(A,E,H, False,True,False,y, light_n, my_lines, cam))

    my_triangles.append(MyTriangle(A,D,C, False,False,False,x, light_n, my_lines, cam))
    my_triangles.append(MyTriangle(C,B,A, False,False,False,x, light_n, my_lines, cam))

    my_triangles.append(MyTriangle(E,F,G, False,False,False,x, light_n, my_lines, cam))
    my_triangles.append(MyTriangle(G,H,E, False,False,False,x, light_n, my_lines, cam))

