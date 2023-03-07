import java.util.*;



Vector<Vector<PVector>> paths;

float my_delay_ms = 10;

boolean paused =  false;
int slow_draw_index = 1;

void setup() {
  size(1400,1400);
  
  //XML xml = loadXML("../line_2d3d/cpp/line_2d3d/line_2d3d/svg_pathed.svg");
  //XML xml = loadXML("triangle_cube1.svg");
  XML xml = loadXML("plot_face.svg");

  paths = new Vector<Vector<PVector>>();
  int no_points = getData(xml);
  println("paths : " + paths.size());
  println("points : " + no_points);
  //slow_draw_index = no_points-10000;
  
}

int getData(XML xml){
  int no_points = 0 ;
  for (XML xml_child : xml.getChildren()){
    
   
    if (xml_child.getName() == "path"){
    
      String content = xml_child.getString("d");
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
          PVector p = new PVector(x,y);
          pvs.add(p);
          no_points ++;
          
      }
      println("");
    } else if (xml_child.getName() == "g") {
      no_points += getData(xml_child);
    }
  }
  return no_points;
}


void keyPressed() {
  println(" KEY : " + key);
    if (key == 'p') {
    paused = !paused;
  } else if ((key == '=') || (key == '+')) {
        my_delay_ms = 0.9 * my_delay_ms;
  } else if (key =='-') {
    my_delay_ms = 1.1 * my_delay_ms;
  } else if (key == ']') {
    slow_draw_index ++;
  } else if (key == '[') {
    slow_draw_index --;
  }
  
}


void draw() {

  
    clear();
    background(255,255,255);
    textSize(100);
    fill(0,0,0);
    int draw_counter = 0;
    int path_counter = 0;
    int path_line_counter = 1;
    PVector p1 = null;
    PVector p2 = null;
    outer:
    for(Vector<PVector> path : paths) {
      path_line_counter=1;
      stroke(color(155*((path_counter)%3), 155*((path_counter+1)%3),  155*((path_counter+2)%3)));
      Enumeration<PVector> path_it = path.elements();
      p1 = path_it.nextElement();
      
      while (path_it.hasMoreElements()) {
         p2 = path_it.nextElement();
         line(p1.x, p1.y, p2.x, p2.y);
         draw_counter ++;
         if (draw_counter == slow_draw_index) {
           if (!paused) {
             slow_draw_index ++;
           }
           break outer;
         }
         p1 = p2;
         path_line_counter++;
      }
      path_counter++;
      
    }
    textSize(25);
    text("line      "+slow_draw_index, 120,100);
    text("path      "+path_counter, 120,150);
    text("path line "+path_line_counter, 120,200);
    
    text("p1 "+p1.x + " : " + p1.y, 120,250);
    text("p2 "+p2.x + " : " + p2.y, 120,300);

  
  delay((int) my_delay_ms);
  
}

// Sketch prints:
// 0, Capra hircus, Goat
// 1, Panthera pardus, Leopard
// 2, Equus zebra, Zebra
