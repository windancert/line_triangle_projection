

void testlist() {
  ArrayList<Integer> il = new ArrayList<Integer>();
  
  for (int i = 0 ; i < 10; i++) {
    il.add(i);
  }
  
  for (Integer i : il) {
    print(" " + i);
  }
  println();
  
  for (Integer i : il) {
    if ((i%2) != 0) {
      il.remove(i);
      il.add(i*2);
      print(" " + i);
    }
  }
  
  for (Integer i : il) {
    print(" " + i);
  }
  println();
  
}
