




void test_scene( ArrayList<MyTriangle> my_triangles, ArrayList<MyLine> my_lines, PVector light_n) {

  my_triangles.add(new MyTriangle(new PVector(  -40, 0, 0), new PVector( 400, 0, 0), new PVector(    0, 400, 0), light_n, my_lines));
  my_triangles.add(new MyTriangle(new PVector(260, 40, 240), new PVector(-240, -40, 220), new PVector( -100, 200, -200), light_n, my_lines));

}




void blocks_scene_1( ArrayList<MyTriangle> my_triangles, ArrayList<MyLine> my_lines, PVector light_n) {
  
  block(new PVector(50,70,90), new PVector(150,170,190), my_triangles, my_lines, light_n);
  
}



void block( PVector p, PVector ribes, ArrayList<MyTriangle> my_triangles, ArrayList<MyLine> my_lines, PVector light_n) {
 
    PVector rx = new PVector(ribes.x, 0, 0);
    PVector ry = new PVector(0, ribes.x, 0);
    PVector rz = new PVector(0, 0, ribes.x);
    
    PVector A = new PVector().add(p);
    PVector B = new PVector().add(p).add(rx);
    PVector C = new PVector().add(p).add(rx).add(ry);
    PVector D = new PVector().add(p).add(ry);
  
    PVector E = new PVector().add(p).add(rz);
    PVector F = new PVector().add(p).add(rz).add(rx);
    PVector G = new PVector().add(p).add(rz).add(rx).add(ry);
    PVector H = new PVector().add(p).add(rz).add(ry);
  
    my_triangles.add(new MyTriangle(A,B,F, light_n, my_lines));
    my_triangles.add(new MyTriangle(F,E,A, light_n, my_lines));
    
    my_triangles.add(new MyTriangle(B,F,C, light_n, my_lines));
    my_triangles.add(new MyTriangle(C,G,F, light_n, my_lines));

    my_triangles.add(new MyTriangle(C,D,G, light_n, my_lines));
    my_triangles.add(new MyTriangle(D,H,G, light_n, my_lines));
  
    my_triangles.add(new MyTriangle(A,D,H, light_n, my_lines));
    my_triangles.add(new MyTriangle(A,H,E, light_n, my_lines));

    my_triangles.add(new MyTriangle(A,D,C, light_n, my_lines));
    my_triangles.add(new MyTriangle(A,C,B, light_n, my_lines));

    my_triangles.add(new MyTriangle(E,F,G, light_n, my_lines));
    my_triangles.add(new MyTriangle(E,G,H, light_n, my_lines));
}
