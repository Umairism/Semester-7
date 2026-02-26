#ifndef RECTANGLE_H
#define RECTANGLE_H

#ifdef __APPLE_CC__
#include <GLUT/glut.h>
#else
#include <GL/glut.h>
#endif

// Draw a filled rectangle from (x1,y1) bottom-left to (x2,y2) top-right
void drawRectangle(float x1, float y1, float x2, float y2,
                   float r, float g, float b);

// Draw a rectangle outline
void drawRectangleOutline(float x1, float y1, float x2, float y2,
                          float r, float g, float b, float lineWidth = 2.0f);

// Draw a filled quadrilateral given 4 vertices and color
void drawQuad(float x1, float y1, float x2, float y2,
              float x3, float y3, float x4, float y4,
              float r, float g, float b);

#endif
