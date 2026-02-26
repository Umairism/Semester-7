#ifndef TRIANGLE_H
#define TRIANGLE_H

#ifdef __APPLE_CC__
#include <GLUT/glut.h>
#else
#include <GL/glut.h>
#endif

// Draw a filled triangle given 3 vertices and an RGB color
void drawTriangle(float x1, float y1, float x2, float y2, float x3, float y3,
                  float r, float g, float b);

// Draw a triangle outline
void drawTriangleOutline(float x1, float y1, float x2, float y2, float x3, float y3,
                         float r, float g, float b, float lineWidth = 2.0f);

#endif
