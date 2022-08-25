

class MyCamera {
  private PMatrix3D cam_mat;
  
  MyCamera(PVector cam_pos, PVector look_at, PVector up) {
    PVector view_dir = PVector.sub(cam_pos, look_at).normalize();
    PVector side_dir = up.cross(view_dir).normalize();
    PVector e = view_dir.cross(side_dir).normalize();
    cam_mat =  new PMatrix3D(side_dir.x, side_dir.y, side_dir.z, -side_dir.dot(cam_pos),
                             e.x, e.y, e.z, -e.dot(cam_pos),
                             view_dir.x, view_dir.y, view_dir.z, -view_dir.dot(cam_pos),
                             0, 0, 0, 1);
                     
  }
  
  PVector project(PVector v3){
    PVector v3_p = this.cam_mat.mult(v3, null);
    return v3_p;

  }
  
  void console_print() {
   println("cam_mat ");                         
   println( " " + cam_mat.m00 + " " + cam_mat.m01 + " " + cam_mat.m02 + " " + cam_mat.m03 );                         
   println( " " + cam_mat.m10 + " " + cam_mat.m11 + " " + cam_mat.m12 + " " + cam_mat.m13 );                         
   println( " " + cam_mat.m20 + " " + cam_mat.m21 + " " + cam_mat.m22 + " " + cam_mat.m23 );                         
   println( " " + cam_mat.m30 + " " + cam_mat.m31 + " " + cam_mat.m32 + " " + cam_mat.m33 );    
  }  
  
}

    
