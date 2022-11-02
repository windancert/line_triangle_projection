from typing import List
import numpy as np

class MyCamera :

#   private PMatrix3D cam_mat;
  
  def MyCamera(self, cam_pos:List[float], look_at:List[float], up:List[float], zoom:float) :
    
    view_dir = np.sub(cam_pos, look_at)
    self.view_dir = view_dir / np.linalg.norm(view_dir)

    side_dir = np.cross(up, view_dir)
    self.side_dir = side_dir / np.linalg.norm(side_dir)

    e = np.cross(view_dir, side_dir)
    self.e = e / np.linalg.norm(e)
    cam_mat = np.array[[side_dir.x, side_dir.y, side_dir.z, -side_dir.dot(cam_pos)],
                             [e.x, e.y, e.z, -e.dot(cam_pos)],
                             [view_dir.x, view_dir.y, view_dir.z, -view_dir.dot(cam_pos)],
                             [0, 0, 0, 1]]
    # zoom = np.multiply(np.eye(4), zoom)
    cam_mat.multiply(zoom)
                     
  
  
  def project(self, v3:List(float)) ->List(float):
    v4 = v3
    v4.append(0)
    v4_p = np.multiply(self.cam_mat, v4)
    return v4_p[0:3]

  
  
  def console_print(self) :
   print("cam_mat ")                  
   print( f"  {self.cam_mat.m00:.1}  {self.cam_mat.m01:.1}  {self.cam_mat.m02:.1}  {self.cam_mat.m03:.1} "        )                
   print( f"  {self.cam_mat.m10:.1}  {self.cam_mat.m11:.1}  {self.cam_mat.m12:.1}  {self.cam_mat.m13:.1} "      )                  
   print( f"  {self.cam_mat.m20:.1}  {self.cam_mat.m21:.1}  {self.cam_mat.m22:.1}  {self.cam_mat.m23:.1} "          )               
   print( f"  {self.cam_mat.m30:.1}  {self.cam_mat.m31:.1}  {self.cam_mat.m32:.1}  {self.cam_mat.m33:.1} "   )
  
  


    
