#ifndef SQUARE_H
#define SQUARE_H

#ifdef __APPLE_CC__
#include <GLUT/glut.h>
#else
#include <GL/glut.h>
#endif

// Draw a filled square centered at (cx, cy) with given side length and color
void drawSquare(float cx, float cy, float side,
                float r, float g, float b);

// Draw a square outline
void drawSquareOutline(float cx, float cy, float side,
                       float r, float g, float b, float lineWidth = 2.0f);

#endif
