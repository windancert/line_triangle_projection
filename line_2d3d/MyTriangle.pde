import java.util.LinkedHashSet;


class MyTriangle {
  MyLine[] ls;
  PVector p1, p2, p3, n;  // plane : nx*x + ny*y + nz*z = o
  float   o;
  color   c;
  float   shading;

  MyTriangle(PVector p1, PVector p2, PVector p3, PVector light_n,  ArrayList<MyLine> lines) {
    this.p1 = p1;
    this.p2 = p2;
    this.p3 = p3;
    this.ls = new MyLine[3];
    ls[0] = new MyLine(this, p1, p2, color(255));
    ls[1] = new MyLine(this, p2, p3, color(255));
    ls[2] = new MyLine(this, p3, p1, color(255));

    for (int i = 0; i < 3; i++) {
      lines.add(ls[i]);
    }
    det_normal_and_o();

    c = color(random(255), random(255), random(255));
    
    set_light(light_n);
  }

  void draw() {
    for (int i = 0; i < 3; i++) {
      ls[i].draw();
    }
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
    return "t: n " + n + " o: " + o;
  }


  float triangleAreaXY(PVector p1, PVector p2, PVector p3) {
    return abs((p1.x*(p2.y-p3.y) + p2.x*(p3.y-p1.y)+ p3.x*(p1.y-p2.y))/2.0);
  }

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
    return ((abs(area1+area2+area3) - area) <= FLOATING_POINT_ACCURACY);
  }






  void det_normal_and_o() {
    PVector s = PVector.sub(p2, p1);
    PVector t = PVector.sub(p3, p2);
    n = s.cross(t ).normalize();
    o = n.dot(p1);
  }

  /**
   * #TODO DIT IS NOG NIET GOED>
   */
  MyLine planePlaneIntersect(MyTriangle pl2) {
    //https://mathemerize.com/equation-of-plane-passing-through-intersection-of-two-planes/
    //https://www.youtube.com/watch?v=O6O_64zIEYI

    PVector v = n.cross( pl2.n);
    println(v);
    println(this);
    println(pl2);

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
      l = new MyLine(this, v, p, color(255, 0, 0), 5);
      println("found line : " +l);
    } else {
      // z = 0
      println("plane 1 crosses z plane");

      float teller = o1 - o2 + n2.dot(v) - n1.dot(v);
      float noemer = n1.x - (n2.x * n1.y) / n2.y;
      float px = teller / noemer;
      float py = (o2 - n2.dot(v) - n2.x*px ) / n2.y;

      PVector p = new PVector(px, py, 0);
      l = new MyLine(this, v, p, color(255, 0, 0), 5);
      println("found line : " +l);
    }

    return l;
  }

  float getZ(float x, float y) {
    return (o - n.x*x - n.y*y)/n.z;
  }

  void set_light(PVector l) {
      shading = n.dot(l);
      if (shading < 0) {
          shading = 0;
      }
      println("shading " + shading);
  }
  
  ArrayList<MyLine> getHatches() {
    ArrayList<MyLine> hatches = new ArrayList<MyLine>();
    float hatch_min = 5;
    float hatch_grad = 15;


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

    // https://www.tutorialspoint.com/Check-whether-a-given-point-lies-inside-a-Triangle

    
    float hatch_spacing =  hatch_min + shading*hatch_grad; //pixels, to be replaces with shading
    for (float x = sqr_bl.x; x < sqr_tr.x; x += hatch_spacing) {
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
