#pragma once
#define FLOATING_POINT_ACCURACY (1.0e-10)

extern bool floatEqualsRelative(double A, double B, double acc);
extern bool doubleGT(double A, double B, double acc);
extern bool doubleST(double A, double B, double acc);

extern bool floatSmallerThenRelative(double A, double B, double acc);

extern int ID_counter;
extern int getID();


