#ifndef CIRCLE_H
#define CIRCLE_H

#ifdef __APPLE_CC__
#include <GLUT/glut.h>
#else
#include <GL/glut.h>
#endif

#include <cmath>

// Draw a filled circle at (cx, cy) with given radius, color, and segment count
void drawCircle(float cx, float cy, float radius,
                float r, float g, float b, int segments = 100);

// Draw a circle outline
void drawCircleOutline(float cx, float cy, float radius,
                       float r, float g, float b, float lineWidth = 2.0f, int segments = 100);

#endif
