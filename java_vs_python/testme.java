import java.util.Vector;
import java.lang.Math;

public class testme {

    float p1[], p2[], p3[];  // plane : nx*x + ny*y + nz*z = o
  
    testme() {
        p1 = new float[3];
        p1[0] = 0;
        p1[1] = 0;
        p1[2] = 0;
        p2 = new float[3];
        p2[0] = 1;
        p2[1] = 1;
        p2[2] = 1;
        p3 = new float[3];
        p3[0] = 0;
        p3[1] = 2;
        p3[2] = 0;

        float a[] = new float[3];
        a[0] = 0;
        a[1] = 2;
        a[2] = 3;
        for (int i = 0; i < 1e6; i++){
            insideTriangleXY(a, true );
        }


    }

	public static void main(String[] args) {
		System.out.println("Hello desde el paquete consoletest");

        long start_ms = System.currentTimeMillis();

        testme tm = new testme();

        long finish_ms = System.currentTimeMillis();
        long timeElapsed_ms = finish_ms - start_ms;

		System.out.printf("tijd genomen ms %d ", timeElapsed_ms);
	}

    float triangleAreaXY(float p1[], float p2[], float p3[]) {
        return (float)Math.abs((p1[0]*(p2[1]-p3[1]) + p2[0]*(p3[1]-p1[1])+ p3[0]*(p1[1]-p2[1]))/2.0);
      }
    
      //if include_edge is false : if the point is on the edge, is NOT inside. 
      //if include_edge is true  : if the point is on the edge, is inside. 
      boolean insideTriangleXY(float p[], boolean include_edge) {
        float FLOATING_POINT_ACCURACY = (float)1.0e-6;
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
        return (( (float)Math.abs(area1+area2+area3) - area) <= FLOATING_POINT_ACCURACY * area);
      }
}

