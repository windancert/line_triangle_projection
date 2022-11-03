from typing import List
from MyCamera import *
import numpy as np


class MyLight :
#   PVector pos, look_at, n_dir; 

    def __init__(self, pos:List[float], look_at:List[float], cam: MyCamera) :
        self.pos = cam.project(pos)
        self.look_at = cam.project(look_at)
        n_dir = np.subtract(self.pos, self.look_at)
        self.n_dir = n_dir / np.linalg.norm(n_dir)
        

  
    def getNormalizedDirection(self)->List[float] :
        return self.n_dir    
  
  
    def __str__(self) :
        return f"p: {self.pos} ; la: {self.look_at} ; n: {self.self}"    
