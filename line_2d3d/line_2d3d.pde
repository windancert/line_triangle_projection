float FLOATING_POINT_ACCURACY = 1.0e-2;

ArrayList<MyTriangle> triangles; 
ArrayList<MyLine> lines;
ArrayList<MyCross> crosses; 

MyLine test_l;

//String draw_mode = P3D;
String draw_mode = P2D;
float y_rotation = 0;

color randColor() {
  //return color(random(255), random(255), random(255));
  return color(255);
}

void setup() {
    size(1400,1400, draw_mode);

    
    //testlist();
    
    lines = new ArrayList<MyLine>();
    
    triangles = new ArrayList<MyTriangle>();
    //triangles.add(new MyTriangle(new PVector(115,110,-20), new PVector(-20,110,110), new PVector(110,-20,110), lines));
    //triangles.add(new MyTriangle(new PVector(  0,  0,  0), new PVector(200,200,  0), new PVector(  0,200,200), lines)); 

    triangles.add(new MyTriangle(new PVector(  -40,  0,  0), new PVector( 400,  0,   0), new PVector(    0,400,  0), lines)); 
    triangles.add(new MyTriangle(new PVector(260,  40,240), new PVector(-240, -40, 220), new PVector( -100,200,-200), lines));

    ArrayList<MyLine> hatches = triangles.get(1).getHatches();
    lines.addAll(hatches);
     hatches = triangles.get(0).getHatches();
    lines.addAll(hatches);
    

    crosses = new ArrayList<MyCross>();
    
    
    //// PLANE PLANE intersections
    //for (MyTriangle t1 : triangles) {
    //  int t1_i = triangles.indexOf(t1);
    //  for (int i = t1_i+1; i < triangles.size(); i++) {
    //    MyTriangle t2 = triangles.get(i);
    //    if (t1 != t2) {
    //      MyLine l = t1.planePlaneIntersect (t2);
    //      test_l = l;
    //      if (l != null) {
    //        //lines.add(l);
    //      }
          
    //    }
    //  }
    //}
    
    // LINE LINE INTERSECTIONS
    for (MyLine l1 : lines) {
      int l1_i = lines.indexOf(l1);
      for (int i = l1_i+1; i < lines.size(); i++) {
        MyLine l2 = lines.get(i);
        if (l1 != l2) {
         PVector intersect = l1.addLineIntersectionXY(l2) ;
          if (intersect != null) {
            crosses.add(new MyCross(intersect, #FF0000, 1));
          }
        }
      }
    }
    println("LINE LINE : no crosses : " + crosses.size());
  
    // LINE PLANE INTERSECTIONS
    for (MyLine line : lines) {
      for (MyTriangle triangle : triangles) {
        PVector intersect = line.addTriangleIntersect3D(triangle);
        if (intersect != null) {
          crosses.add(new MyCross(intersect,#00FF00,1));
          //new_lines.add(new MyLine(line.ps[0], intersect, randColor()));
          //new_lines.add(new MyLine(intersect, line.ps[1], randColor()));
        }
        else {
           //new_lines.add(line); 
        }
      }
    }
    println("no crosses : " + crosses.size());
  
    println("no lines : " + lines.size());
    ArrayList<MyLine> new_lines = new ArrayList<MyLine>();
    new_lines = new ArrayList<MyLine>();
    for (MyLine l1 : lines) {
        new_lines.addAll(l1.splitLine());
      
    }
    println("no new_lines : " + new_lines.size());
    

    lines = new_lines;
    for (MyLine line : lines) {
      for (MyTriangle triangle: triangles) {
        if (line.parent != triangle) {
          PVector p = line.addTriangleObscuration(triangle);
          //crosses.add(new MyCross(p,#0000FF,1));
        }
      }
    }

}


void draw() {
  
  if (mousePressed && (mouseButton == LEFT)) {
    y_rotation -= 0.1;
  } else if (mousePressed && (mouseButton == RIGHT)) { 
      y_rotation += 0.1;
      println (y_rotation);
  }
  if (keyPressed) {
    if (key == 'r') {
      y_rotation = 0;
    }
  }

    clear();
    background(0);

  
  if (draw_mode == P3D) {
    pushMatrix();
    translate(width/2, height/2);
    rotateY(y_rotation);
    for (MyTriangle t : triangles) {
      t.draw3D();      
    }
    popMatrix();
    
  } else {
  
    translate(width/2, height/2);
    strokeWeight(1);
    stroke(255);
    //t1.draw();  
    //t2.draw();
    for (MyLine l : lines) {
      l.draw();
    }
    
    if (test_l != null) {
      test_l.draw();
    }
    
    stroke(255, 0, 0);
    for (MyCross cross : crosses) {
      //cross.draw();
      
    }
  }
    
  noLoop();
}
