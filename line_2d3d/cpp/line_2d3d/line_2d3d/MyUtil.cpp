#include <cmath>
#include "MyUtil.h"

 bool floatEqualsRelative(double A, double B, double acc) {
    // Calculate the difference.
    double diff = abs(A - B);
    A = abs(A);
    B = abs(B);
    // Find the largest
    double largest = (B > A) ? B : A;

    if (diff <= largest * acc)
        return true;
    return false;

}
bool doubleGT(double A, double B, double acc) {
    return (A > (B + acc));

 }
bool doubleST(double A, double B, double acc) {
    return (A < (B + acc));

}

 bool floatSmallerThenRelative(double A, double B, double acc) {
    // A < B --> TRUE
   // Calculate the difference.
    double fA = abs(A);
    double fB = abs(B);
    // Find the largest
    double largest = (fB > fA) ? fB : fA;

    return A < B - largest * acc;

}

static int ID_counter = 0;
 int getID() {
    ID_counter++;
    return ID_counter;
}

