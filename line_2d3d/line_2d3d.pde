import processing.svg.*;

float FLOATING_POINT_ACCURACY = 1.0e-6;

ArrayList<MyTriangle> triangles; 
ArrayList<MyLine> lines;
ArrayList<MyCross> crosses; 

MyLine test_l;

//String draw_mode = P3D;
String draw_mode = P2D;
float y_rotation = 0;

color randColor() {
  //return color(random(255), random(255), random(255));
  return color(0,0,0);
}

void setup() {
    size(1400,1300, draw_mode);

    MyCamera my_cam = new MyCamera(new PVector(-10,-8,-11), new PVector(0,0,0), new PVector(0,1,0), 0.9);
    MyLight my_light = new MyLight(new PVector(100,50,0), new PVector(0,0,0), my_cam);

    //testlist();
    
    lines = new ArrayList<MyLine>();
    triangles = new ArrayList<MyTriangle>();
    

    test_scene(triangles, lines, my_light, my_cam);
     //blocks_scene_0(triangles, lines, my_light, my_cam);
     //blocks_scene_1(triangles, lines, my_light, my_cam);

    for (MyTriangle triangle : triangles) {
      lines.addAll(triangle.getHatches());
    }
    
    
    
    //lines.addAll(triangles.get(1).getHatches());
    //ArrayList<MyLine> hatches = triangles.get(1).getHatches();
    //lines.addAll(hatches);
    //hatches = triangles.get(0).getHatches();
    //lines.addAll(hatches);
    

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
    
    // LINE LINE INTERSECTIONS 2D
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
  
    // LINE PLANE INTERSECTIONS 3D
    for (MyLine line : lines) {
      for (MyTriangle triangle : triangles) {
        PVector intersect = line.addTriangleIntersectXYZ(triangle);
        if (intersect != null) {
          crosses.add(new MyCross(intersect, #00FF00, 1));
        }
      }
    }
    println("no crosses : " + crosses.size());
  
    // GENERATE ALL LINE SPLITS, WHICH BECOME SUBLINES IN LINES 
    println("no lines : " + lines.size());
    int no_lines = 0;
    for (MyLine l1 : lines) {
        no_lines += l1.generateSplitLines();
    }
    println("no lines after splits : " + no_lines);
    
   // GENERATE THE LINE OBSCURATION, SETING THE VISIBILITY OF THE SUBLINES
    for (MyLine line : lines) {
      for (MyTriangle triangle: triangles) {
        if (line.parent != triangle) {
          ArrayList<PVector> ps = line.addTriangleObscuration(triangle);
          //crosses.addAll(new MyCross(ps,#0000FF,1));
        }
      }
    }
    println("no visibile lines after triangle obscuration : " + no_lines);
    
    // RECOMBINE WHERE POSSIBLE THE LINES
    no_lines = 0;
    for (MyLine line : lines) {
      no_lines += line.recombineLines();
    }
    println("no visibile lines after recombination : " + no_lines);

    int triangleAreaXY_counter_calls = 0;
    for (MyTriangle triangle : triangles) {
      triangleAreaXY_counter_calls += triangle.triangleAreaXY_counter;
    }
    println("triangleAreaXY_counter_calls : " + triangleAreaXY_counter_calls);


}


void draw() {
  if(1==frameCount) surface.setLocation(10,10);
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
   background(255);
  
  if (draw_mode == P3D) {
    pushMatrix();
    translate(width/2, height/2);
    rotateY(y_rotation);
    for (MyTriangle t : triangles) {
      t.draw3D();      
    }
    popMatrix();
    
  } else {
    beginRecord(SVG, "filename.svg");
 
  
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
    
    for (MyTriangle t : triangles) {
      //t.draw_normal();      
    }
    
    stroke(255, 0, 0);
    for (MyCross cross : crosses) {
      //cross.draw();
      
    }
    endRecord();
  }

    
  noLoop();
}
