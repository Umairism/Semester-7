#ifndef LINE_H
#define LINE_H

#ifdef __APPLE_CC__
#include <GLUT/glut.h>
#else
#include <GL/glut.h>
#endif

// Draw a line from (x1,y1) to (x2,y2) with given color and width
void drawLine(float x1, float y1, float x2, float y2,
              float r, float g, float b, float lineWidth = 2.0f);

#endif
