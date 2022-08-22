

class MyCross {
  PVector p;
  color   c;
  int     thickness;

  MyCross(PVector p, color c, int thickness) {
    this.c = c;
    this.p = p;
    this.thickness = thickness;
  }

  void draw() {
    stroke(c);
    strokeWeight(thickness);

    line(p.x-10, p.y-10, p.x+10, p.y+10);
    line(p.x+10, p.y-10, p.x-10, p.y+10);
  }
}
