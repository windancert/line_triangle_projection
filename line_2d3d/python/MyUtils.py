
FLOATING_POINT_ACCURACY = 1.0e-6

X = 0
Y = 1
Z = 2

def floatEqualsRelative(A, B, acc) ->bool :
    # // Calculate the difference.
    diff = abs(A - B)
    A = abs(A)
    B = abs(B)
    # // Find the largest
    largest = B if B > A else A

    if diff <= largest * acc :
        return True
    return False
    
  
   
def floatSmallerThenRelative(A, B, acc)  -> bool :
    #  // A < B --> TRUE
    # // Calculate the difference.
    fA = abs(A)
    fB = abs(B)
    # // Find the largest
    # float largest = (fB > fA) ? fB : fA;
    largest = fB if fB > fA else fA

    return A < (B - largest*acc)
    
  
   
ID_counter = 0; 
def getID() :
    global ID_counter
    ID_counter += 1
    return ID_counter

    
   
