




void test_scene( ArrayList<MyTriangle> my_triangles, ArrayList<MyLine> my_lines, MyLight my_light, MyCamera cam) {

  PVector up = new PVector(0,1,0); 
  
  my_triangles.add(new MyTriangle(new PVector(    0, 400, 0), new PVector( 400, 0, 0), new PVector(  -40, 0, 0), up, my_light, my_lines, cam));
  my_triangles.add(new MyTriangle(new PVector(260, 40, 240), new PVector(-240, -40, 220), new PVector( -100, 200, -200), up, my_light, my_lines, cam));

}


void blocks_scene_0( ArrayList<MyTriangle> my_triangles, ArrayList<MyLine> my_lines, MyLight my_light, MyCamera cam) {

  PVector ribes =  new PVector(250,290,320);
  int i = 0;
  int j = 0;
  int k = 0;
  
  PVector p = new PVector(ribes.x * i * 2.0, ribes.y * j * 2.0, ribes.z * k * 2.0);
  block(p, ribes , my_triangles, my_lines, my_light, cam);
  
}

void blocks_scene_1( ArrayList<MyTriangle> my_triangles, ArrayList<MyLine> my_lines, MyLight my_light, MyCamera cam) {
  
  PVector ribes =  new PVector(50,190,250);
  for (int i = -1; i < 2; i++) {
    for (int j = -1; j < 2; j++) {
      for (int k = -1; k < 2; k++) {
        PVector p = new PVector(ribes.x * i * 2.0, ribes.y * j * 2.0, ribes.z * k * 2.0);
        block(p, ribes , my_triangles, my_lines, my_light, cam);
      }
    }
  }
  
}



void block( PVector p, PVector ribes, ArrayList<MyTriangle> my_triangles, ArrayList<MyLine> my_lines, MyLight light_n, MyCamera cam) {
 
    PVector rx = new PVector(ribes.x, 0, 0);
    PVector ry = new PVector(0, ribes.y, 0);
    PVector rz = new PVector(0, 0, ribes.z);
    
    PVector A = new PVector().add(p);
    PVector B = new PVector().add(p).add(rx);
    PVector C = new PVector().add(p).add(rx).add(ry);
    PVector D = new PVector().add(p).add(ry);
  
    PVector E = new PVector().add(p).add(rz);
    PVector F = new PVector().add(p).add(rz).add(rx);
    PVector G = new PVector().add(p).add(rz).add(rx).add(ry);
    PVector H = new PVector().add(p).add(rz).add(ry);
    
    PVector x = new PVector(1,0,0);
    PVector y = new PVector(0,1,0);
    PVector z = new PVector(0,0,1);
  
    my_triangles.add(new MyTriangle(A,B,F, true,true,false,z, light_n, my_lines, cam));
    my_triangles.add(new MyTriangle(F,E,A, true,true,false,z, light_n, my_lines, cam));
    
    my_triangles.add(new MyTriangle(G,C,D, true,true,false,z, light_n, my_lines, cam));
    my_triangles.add(new MyTriangle(D,H,G, true,true,false,z, light_n, my_lines, cam));
  
    my_triangles.add(new MyTriangle(F,B,C, false,true,false,y, light_n, my_lines, cam));
    my_triangles.add(new MyTriangle(C,G,F, false,true,false,y, light_n, my_lines, cam));

    my_triangles.add(new MyTriangle(H,D,A, false,true,false,y, light_n, my_lines, cam));
    my_triangles.add(new MyTriangle(A,E,H, false,true,false,y, light_n, my_lines, cam));

    my_triangles.add(new MyTriangle(A,D,C, false,false,false,x, light_n, my_lines, cam));
    my_triangles.add(new MyTriangle(C,B,A, false,false,false,x, light_n, my_lines, cam));

    my_triangles.add(new MyTriangle(E,F,G, false,false,false,x, light_n, my_lines, cam));
    my_triangles.add(new MyTriangle(G,H,E, false,false,false,x, light_n, my_lines, cam));
}
