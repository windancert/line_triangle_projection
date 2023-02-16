import java.util.*;

XML xml;

Vector<Vector<PVector>> paths;


void setup() {
  size(1400,1400);
  xml = loadXML("../line_2d3d/cpp/line_2d3d/line_2d3d/svg_pathed.svg");
  //xml = loadXML("roland.svg");
  XML[] children = xml.getChildren("path");
  
  paths = new Vector<Vector<PVector>>();
  
  for (int i = 0; i < children.length; i++) {
    String content = children[i].getString("d");
    content = content.replace("M", "");
    content = content.replace("L", "");
    content = content.replace("\n", " ");
    content = content.trim();
    Vector<PVector> pvs = new Vector<PVector>();
    paths.add(pvs);
    StringTokenizer tokens = new StringTokenizer(content, " ");
    while(tokens.hasMoreTokens()){
        Float x =  Float.parseFloat(tokens.nextToken());
        Float y =  Float.parseFloat(tokens.nextToken());
        Float c = random(0,255);
        PVector p = new PVector(x,y,c);
        pvs.add(p);
        
    }
    println("");
    
  }
}

int slow_draw_index = 1;
void draw() {
  clear();
  background(255,255,255);
  textSize(100);
  fill(0,0,0);
  text(""+slow_draw_index, 120,120);
  int draw_counter = 0;
  int path_counter = 0;
  outer:
  for(Vector<PVector> path : paths) {
    
    Enumeration<PVector> path_it = path.elements();
    PVector p1 = path_it.nextElement();
    stroke(color(127*(path_counter%3),127*((path_counter+1)%3),127*((path_counter+2)%3)));
    while (path_it.hasMoreElements()) {
       PVector p2 = path_it.nextElement();

       line(p1.x, p1.y, p2.x, p2.y);
       
       p1= p2;
       draw_counter ++;
       if (draw_counter == slow_draw_index) {
         slow_draw_index ++;
         break outer;
       }
    }
    path_counter++;
  }
  delay(500);
  
}

// Sketch prints:
// 0, Capra hircus, Goat
// 1, Panthera pardus, Leopard
// 2, Equus zebra, Zebra
