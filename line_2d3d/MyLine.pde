


class MyLine {
  PVector[] ps;
  MyTriangle parent;
  FloatList splitters;
  color c;
  int thickness;
  boolean visible;

  MyLine(MyTriangle t, PVector p1, PVector p2) {
    this(t, p1, p2, randColor(), 1, true);
  }
  MyLine(MyTriangle t, PVector p1, PVector p2, boolean visible) {
    this(t, p1, p2, randColor(), 1, visible);
  }

  MyLine(MyTriangle t, PVector p1, PVector p2, color c) {
    this(t, p1, p2, c, 1, true);
  }
  MyLine(MyTriangle t, PVector p1, PVector p2, color c, boolean visible) {
    this(t, p1, p2, c, 1, visible);
  }

  MyLine(MyTriangle t, PVector p1, PVector p2, color c, int thickness, boolean visible) {
    parent = t;
    ps = new PVector[2];
    ps[0] = p1;
    ps[1] = p2;
    this.c = c;
    this.thickness = thickness;
    this.visible = visible;

    splitters = new FloatList();
  }

  void draw() {
    if (visible) {
      stroke(c);
      strokeWeight(thickness);
  
      line(ps[0].x, ps[0].y, ps[1].x, ps[1].y );
    }
  }

  String toString() {
    return "Line : p0: " + ps[0] + " ;p[1]: " + ps[1];
  }

  void addSplitter(float splitter) {
    splitters.append(splitter);
  }


  ArrayList<MyLine> splitLine() {
    splitters.append(0);
    splitters.append(1);
    splitters.sort();

    ArrayList<PVector> new_points = new ArrayList<PVector>();
    new_points.add(ps[0]);
    for (int i = 0; i < splitters.size()-1; i++) {
      PVector p = PVector.sub(ps[1], ps[0]).mult(splitters.get(i+1)).add(ps[0]);
      new_points.add(p);
    }

    ArrayList<MyLine> lines = new ArrayList<MyLine>();
    for (int i = 0; i < new_points.size() - 1; i ++) {
      lines.add(new MyLine(this.parent, new_points.get(i), new_points.get(i+1), this.visible));
    }

    return lines;
  }


  /**
   * find intersection point if it is KNOWN that the lines intersect
   */
  //PVector findIntersection3D(MyLine l2) {

  //}

  /**
   * Intersection with the other line in 2 dimensions (xy)
   * returns [v3  : intersection point, only if within line-piece : NO Z])
   */
  PVector addLineIntersectionXY(MyLine l2) {
    return addGetLineIntersectionXY(l2, true);
  }
  
  PVector getLineIntersectionXY(MyLine l2) {
    return addGetLineIntersectionXY(l2, false);
  }
  
  PVector addGetLineIntersectionXY(MyLine l2, boolean add_splitter) {
    // https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
    float x1 = this.ps[0].x;
    float x2 = this.ps[1].x;
    float y1 = this.ps[0].y;
    float y2 = this.ps[1].y;
    float x3 = l2.ps[0].x;
    float x4 = l2.ps[1].x;
    float y3 = l2.ps[0].y;
    float y4 = l2.ps[1].y;

    float noemer = ((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4));
    if (Math.abs(noemer) > FLOATING_POINT_ACCURACY ) {
      float t_teller = ((x1-x3)*(y3-y4) - (y1-y3)*(x3-x4));
      float u_teller = ((x1-x3)*(y1-y2) - (y1-y3)*(x1-x2));
      float t = t_teller / noemer ;
      float u = u_teller / noemer ;

      PVector p = new PVector();
      p.x = x1 + t*(x2-x1);
      p.y = y1 + t*(y2-y1);
      p.z = ps[0].z + t*(ps[1].z-ps[0].z);

      if ((t >= 0) && (t <= 1) && (u >= 0) && (u <= 1)    ) {
        if (add_splitter) {
          this.addSplitter(t);
          l2.addSplitter(u);
        }
        return p;
      }
    }

    return null;
  }

  /**
   * calculate intersection triangle with line.
   *
   * @param {*} line
   * @returns v3: point of intersection, NaN if no interserction
   */
  PVector addTriangleIntersect3D(MyTriangle triangle_arg) {
    // https://en.wikipedia.org/wiki/Line%E2%80%93plane_intersection
    PVector p0 = triangle_arg.ls[0].ps[0];
    PVector l0 = this.ps[0];
    PVector l  = this.get_direction();
    float teller = PVector.dot(PVector.sub(p0, l0), triangle_arg.n);
    float noemer = PVector.dot(l, triangle_arg.n);
    if (abs(noemer) > FLOATING_POINT_ACCURACY ) {
      float d = teller / noemer;
      PVector p = PVector.add(l0, PVector.mult(l, d));
      if (triangle_arg.insideTriangleXY(p, true) && (d < 1.0) && (d > 0.0)) {
        this.addSplitter(d);
        return p;
      }
    }
    return null;
  }

  /** 
   * check and set visibility wrt the triangles. Take care of lines that are part of triangle: 
   */
  PVector addTriangleObscuration(MyTriangle triangle) {
    PVector p = PVector.add(PVector.mult(get_direction(), 0.5), ps[0]);
    if ((triangle.insideTriangleXY(p, false)) && (p.z  < triangle.getZ(p.x, p.y))) {
        visible = false;
    }
    
    return p;
  }


  PVector get_direction() {
    return PVector.sub(this.ps[1], this.ps[0]);
  }
  

}
