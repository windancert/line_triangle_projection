import numpy as np



step = 1.4
start = -10
end = 10

def find_left(p):
    l = p - p%step
    print(f"{p } {l}")

a = np.arange(start,end,step)


find_left(3.2)
find_left(-3.2)

