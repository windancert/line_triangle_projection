from svg import *
from MyCamera import *
from MyLight import *
from MyScenes import *
from MyColor import *
from MyCross import *


y_rotation = 0


def get_no_lines(lines) :
  no_vis_lines = 0
  for line in lines :
      no_vis_lines += line.getNoVisibleLines()
  return no_vis_lines

def main() :
    my_cam = MyCamera((-10,-8,-11), (0,0,0), (0,1,0), 0.9)
    my_light = MyLight((100,50,0), (0,0,0), my_cam)

    # //testlist();
    
    lines = []
    triangles = []
    crosses = []

    # test_scene(triangles, lines, my_light, my_cam)
    # blocks_scene_0(triangles, lines, my_light, my_cam)
    blocks_scene_1(triangles, lines, my_light, my_cam)

    print(f"no lines : basic shapes : {get_no_lines(lines)}")

    for triangle in triangles :
      hatches = triangle.getHatches()
      # print(f"no hatches {len(hatches)}")
      lines.extend(triangle.getHatches())
    
    print(f"no lines : add hatching : {get_no_lines(lines)}")
    
    # //lines.addAll(triangles.get(1).getHatches());
    # //ArrayList<MyLine> hatches = triangles.get(1).getHatches();
    # //lines.addAll(hatches);
    # //hatches = triangles.get(0).getHatches();
    # //lines.addAll(hatches);
    

    
    # //// PLANE PLANE intersections
    # //for (MyTriangle t1 : triangles) {
    # //  int t1_i = triangles.indexOf(t1);
    # //  for (int i = t1_i+1; i < triangles.size(); i++) {
    # //    MyTriangle t2 = triangles.get(i);
    # //    if (t1 != t2) {
    # //      MyLine l = t1.planePlaneIntersect (t2);
    # //      test_l = l;
    # //      if (l != null) {
    # //        //lines.add(l);
    # //      }
          
    # //    }
    # //  }
    # //}
    
    # // LINE LINE INTERSECTIONS 2D
    for l1 in lines :
      l1_i = lines.index(l1)
      i = l1_i+1
      while i < len(lines):
        l2 = lines[i]
        if l1 != l2:
          is_intersect, intersect = l1.addLineIntersectionXY(l2) 
          if is_intersect :
            new_cross = MyCross(intersect, MyColor(100,0,0), 1)
            crosses.append(new_cross)
        i += 1
      
    
    print(f"Line line intersections : no crosses : {len(crosses)}")
  
    # // LINE PLANE INTERSECTIONS 3D
    for line in lines :
      for triangle in triangles :
        is_intersect, intersect = line.addTriangleIntersectXYZ(triangle)
        if is_intersect :
          crosses.append(MyCross(intersect, MyColor(0,255,0), 1))
    print(f"line plane intersections : no crosses :  {len(crosses)}")
  
    # // GENERATE ALL LINE SPLITS, WHICH BECOME SUBLINES IN LINES 
    print(f"no lines :  {len(lines)}")
    no_lines = 0
    for l1 in lines :
        no_lines += l1.generateSplitLines()
    
    print(f"no lines after splits : {no_lines}")
    
#    // GENERATE THE LINE OBSCURATION, SETING THE VISIBILITY OF THE SUBLINES
# DEZE DUURT LANG IN PYTHON
    for line in lines :
      for triangle in triangles :
        if line.parent != triangle :
          line.addTriangleObscuration(triangle)
    print(f"no visibile lines after triangle obscuration : {get_no_lines(lines)}")
    
    # // RECOMBINE WHERE POSSIBLE THE LINES
    no_lines = 0
    for line in lines :
      no_lines += line.recombineLines()
    
    print(f"no visibile lines after recombination : {get_no_lines(lines)}")





# void draw() {
#   if(1==frameCount) surface.setLocation(10,10);
#   if (mousePressed && (mouseButton == LEFT)) {
#     y_rotation -= 0.1;
#   } else if (mousePressed && (mouseButton == RIGHT)) { 
#       y_rotation += 0.1;
#       println (y_rotation);
#   }
#   if (keyPressed) {
#     if (key == 'r') {
#       y_rotation = 0;
#     }
#   }

#    clear();
#    background(255);
  
#   if (draw_mode == P3D) {
#     pushMatrix();
#     translate(width/2, height/2);
#     rotateY(y_rotation);
#     for (MyTriangle t : triangles) {
#       t.draw3D();      
#     }
#     popMatrix();
    
#   } else {
  
    width = 1400
    height = 1400
    svg = SVG()
    svg.create(width, height)

    svg.translate(width/2, height/2)

    for l in lines :
      l.draw(svg)
   
    for t in triangles :
    #   //t.draw_normal();      
        pass
    
    for cross in crosses : 
        # cross.draw(svg)
        pass

    svg.finalize()
    try:
        svg.save("svg.svg")
    except IOError as ioe:
        print(ioe)


main()