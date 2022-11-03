from typing import List
import numpy as np
from MyUtils import *

class MyCamera :

#   private PMatrix3D cam_mat;
  
  def __init__(self, cam_pos:List[float], look_at:List[float], up:List[float], zoom:float) :
    
    view_dir = np.subtract(cam_pos, look_at)
    self.view_dir = view_dir / np.linalg.norm(view_dir)

    side_dir = np.cross(up, view_dir)
    self.side_dir = side_dir / np.linalg.norm(side_dir)

    e = np.cross(view_dir, side_dir)
    self.e = e / np.linalg.norm(e)
    a1 = [self.side_dir[X], self.side_dir[Y], self.side_dir[Z], -np.dot(self.side_dir, cam_pos)]
    a2 = [self.e[X], self.e[Y], self.e[Z], -np.dot(self.e,cam_pos)]
    a3 = [self.view_dir[X], self.view_dir[Y], self.view_dir[Z], -np.dot(self.view_dir, cam_pos)]
    a4 = [0, 0, 0, 1]
    self.cam_mat = []
    self.cam_mat.append(a1)
    self.cam_mat.append(a2)
    self.cam_mat.append(a3)
    self.cam_mat.append(a4)
    # zoom = np.multiply(np.eye(4), zoom)
    self.cam_mat = np.multiply(self.cam_mat, zoom)
  
  def project(self, v3:List[float]) -> List[float]:
    v4 = list(v3)
    v4.append(0)
    v4_p = np.dot(self.cam_mat, v4)
    
    return v4_p[0:3]
  
  def console_print(self) :
   print("cam_mat ")                  
   print( f"  {self.cam_mat.m00:.1}  {self.cam_mat.m01:.1}  {self.cam_mat.m02:.1}  {self.cam_mat.m03:.1} "        )                
   print( f"  {self.cam_mat.m10:.1}  {self.cam_mat.m11:.1}  {self.cam_mat.m12:.1}  {self.cam_mat.m13:.1} "      )                  
   print( f"  {self.cam_mat.m20:.1}  {self.cam_mat.m21:.1}  {self.cam_mat.m22:.1}  {self.cam_mat.m23:.1} "          )               
   print( f"  {self.cam_mat.m30:.1}  {self.cam_mat.m31:.1}  {self.cam_mat.m32:.1}  {self.cam_mat.m33:.1} "   )
  
  


    
