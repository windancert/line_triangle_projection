import java.util.LinkedHashSet;


class MyTriangle {
  MyLine[] ls;
  PVector p1, p2, p3, n, up;  // plane : nx*x + ny*y + nz*z = o
  float   o;
  color   c;
  float   shading;
  int     id;
  int triangleAreaXY_counter;
  


  MyTriangle(PVector p1, PVector p2, PVector p3, boolean vis1, boolean vis2, boolean vis3, PVector up, MyLight light_n, ArrayList<MyLine> lines, MyCamera cam) {

    this.id = getID();
    this.p1 = cam.project(p1);
    this.p2 = cam.project(p2);
    this.p3 = cam.project(p3);
    this.up = up;
    
    this.triangleAreaXY_counter = 0;

    det_normal_and_o();

    this.ls = new MyLine[3];
    ls[0] = new MyLine(this, this.p1, this.p2, color(255), vis1);
    ls[1] = new MyLine(this, this.p2, this.p3, color(255), vis2);
    ls[2] = new MyLine(this, this.p3, this.p1, color(255), vis3);

    for (int i = 0; i < 3; i++) {
      lines.add(ls[i]);
    }

    c = color(random(255), random(255), random(255));

    set_light(light_n);
  }

  MyTriangle(PVector p1, PVector p2, PVector p3, PVector up, MyLight light_n, ArrayList<MyLine> lines, MyCamera cam) {
    this(p1, p2, p3, true, true, true, up, light_n, lines, cam);
  }

  void draw() {
    for (int i = 0; i < 3; i++) {
      ls[i].draw();
    }
  }

  void draw_normal(){
    stroke(255,0,0);
    PVector c = center();
    PVector cn = PVector.add(c,n.mult(50));
    line(c.x, c.y, cn.x, cn.y );
  }

  void draw3D() {
    beginShape();
    fill(c);
    vertex(p1.x, p1.y, p1.z);
    vertex(p2.x, p2.y, p2.z);
    vertex(p3.x, p3.y, p3.z);

    endShape();
  }


  String toString() {
    return "t: id: "+ id + " n " + n + " o: " + o ;
  }

  boolean equals(MyTriangle t){
    return this.id == t.id; 
    
  }


  float triangleAreaXY(PVector p1, PVector p2, PVector p3) {
    this.triangleAreaXY_counter ++;
    return abs((p1.x*(p2.y-p3.y) + p2.x*(p3.y-p1.y)+ p3.x*(p1.y-p2.y))/2.0);
  }

  //if include_edge is false : if the point is on the edge, is NOT inside. 
  //if include_edge is true  : if the point is on the edge, is inside. 
  boolean insideTriangleXY(PVector p, boolean include_edge) {
    float area = triangleAreaXY(p1, p2, p3);
    float area1 = triangleAreaXY(p, p2, p3);
    float area2 = triangleAreaXY(p1, p, p3);
    float area3 = triangleAreaXY(p1, p2, p);
    if (!include_edge) {
      if ((area1 <= FLOATING_POINT_ACCURACY) || (area2 <= FLOATING_POINT_ACCURACY) || (area3 <= FLOATING_POINT_ACCURACY))
      {
        return false;
      }
    }
    return ((abs(area1+area2+area3) - area) <= FLOATING_POINT_ACCURACY * area);
  }


  void det_normal_and_o() {
    PVector s = PVector.sub(p2, p1);
    PVector t = PVector.sub(p3, p2);
    n = s.cross(t ).normalize();
    o = n.dot(p1);
  }

  PVector center() {
    return new PVector().add(p1).add(p2).add(p3).mult(1.0/3.0);
  }

  /**
   * #TODO DIT IS NOG NIET GOED>
   */
  MyLine planePlaneIntersect(MyTriangle pl2) {
    //https://mathemerize.com/equation-of-plane-passing-through-intersection-of-two-planes/
    //https://www.youtube.com/watch?v=O6O_64zIEYI

    PVector v = n.cross( pl2.n);

    float o1 = o;
    float o2 = pl2.o;
    PVector n1 = n;
    PVector n2 = pl2.n;

    if ( PVector.sub(n1, n2).dot(1, 1, 1) < FLOATING_POINT_ACCURACY) {
      println("Parallel");
      return null;
    }

    MyLine l;
    if ((abs(n1.x) < FLOATING_POINT_ACCURACY) && (abs(n1.y) < FLOATING_POINT_ACCURACY)) {
      // we cannot take z = 0; so we take y = 0
      println("plane 1 parallel z plane");
      float teller = o1 - o2 + n2.dot(v) - n1.dot(v);
      float noemer = n1.x - (n2.x * n1.z) / n2.z;
      float px = teller / noemer;
      float pz = (o2 - n2.dot(v) - n2.x*px ) / n2.z;

      PVector p = new PVector(px, 0, pz);
      l = new MyLine(this, v, p, color(255, 0, 0), 5, true);
      println("found line : " +l);
    } else {
      // z = 0
      println("plane 1 crosses z plane");

      float teller = o1 - o2 + n2.dot(v) - n1.dot(v);
      float noemer = n1.x - (n2.x * n1.y) / n2.y;
      float px = teller / noemer;
      float py = (o2 - n2.dot(v) - n2.x*px ) / n2.y;

      PVector p = new PVector(px, py, 0);
      l = new MyLine(this, v, p, color(255, 0, 0), 5, true);
      println("found line : " +l);
    }

    return l;
  }

  float getZ(float x, float y) {
    if (n.z != 0) {
      return (o - n.x*x - n.y*y)/n.z;
    }
    return 0;
  }

  void set_light(MyLight l) {
    shading = n.dot(l.getNormalizedDirection());
    if (shading > 0) {
      shading = 0;
    } else {
      shading = -shading;
    }
    
  }

  ArrayList<MyLine> getHatches() {

    ArrayList<MyLine> hatches = new ArrayList<MyLine>();
    float hatch_min = 5;
    float hatch_grad = 15;

    if (this.n.dot(new PVector(0,0,1)) <= 0) {
      // no need to hatch the backside of a vertex
      return hatches;
    }


    PVector left = p1;
    if (p2.x < left.x) left = p2;
    if (p3.x < left.x) left = p3;
    PVector right = p1;
    if (p2.x > right.x) right = p2;
    if (p3.x > right.x) right = p3;

    PVector bottom = p1;
    if (p2.y < bottom.y) bottom = p2;
    if (p3.y < bottom.y) bottom = p3;
    PVector top = p1;
    if (p2.y > top.y) top = p2;
    if (p3.y > top.y) top = p3;

    // make a square around the triangle
    PVector sqr_bl = new PVector();
    sqr_bl.x = left.x;
    sqr_bl.y = bottom.y;
    PVector sqr_tr = new PVector();
    sqr_tr.x = right.x;
    sqr_tr.y = top.y;



    //PVector view_dir = PVector.sub(cam_pos, look_at).normalize();
    //PVector side_dir = up.cross(view_dir).normalize();
    //PVector e = view_dir.cross(side_dir).normalize();

    // https://www.tutorialspoint.com/Check-whether-a-given-point-lies-inside-a-Triangle
    float hatch_spacing =  hatch_min + shading*hatch_grad; //pixels, to be replaced with shading
    float hatch_start = sqr_bl.x - sqr_bl.x % hatch_spacing;
    for (float x = hatch_start; x < sqr_tr.x; x += hatch_spacing) {
      PVector b = new PVector(x, bottom.y - FLOATING_POINT_ACCURACY, 0);
      b.z = getZ(b.x, b.y);
      PVector t = new PVector(x, top.y + FLOATING_POINT_ACCURACY, 0);
      t.z = getZ(t.x, t.y);


      MyLine hatch_line = new MyLine(this, b, t);

      ArrayList<PVector> i_is = new ArrayList<PVector>();  // intersectes within the square/triangle
      for (int i = 0; i < 3; i ++) {
        PVector is = hatch_line.getLineIntersectionXY(this.ls[i]);
        if (is != null) {
          boolean is_in = insideTriangleXY(is, true);
          if (is_in) {
            i_is.add(is);
          }
        }
      }

      if ( i_is.size() == 3) {
        // remove duplicate: probably  a triangle corner
        LinkedHashSet<PVector> hashSet = new LinkedHashSet<>(i_is);
        i_is = new ArrayList<>(hashSet);
      }

      if (i_is.size() == 2) {
        hatches.add(new MyLine(this, i_is.get(0), i_is.get(1), color(255)));
      }
    }
    
    return hatches;
  }
}
