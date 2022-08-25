
class MyLight{
  PVector pos, look_at, n_dir; 
  
  MyLight(PVector pos, PVector look_at, MyCamera cam) {
    this.pos = cam.project(pos);
    this.look_at = cam.project(look_at);
    this.n_dir = PVector.sub(this.pos, this.look_at).normalize();
    
  }
  
  PVector getNormalizedDirection() {
    return this.n_dir;    
  }
  
  String toString() {
    return ("p: " + this.pos + " ; la: " + this.look_at + " ; n: " + this.n_dir);    
  }
}
