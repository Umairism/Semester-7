#include "triangle.h"

void drawTriangle(float x1, float y1, float x2, float y2, float x3, float y3,
                  float r, float g, float b) {
    glColor3f(r, g, b);
    glBegin(GL_TRIANGLES);
        glVertex2f(x1, y1);
        glVertex2f(x2, y2);
        glVertex2f(x3, y3);
    glEnd();
}

void drawTriangleOutline(float x1, float y1, float x2, float y2, float x3, float y3,
                         float r, float g, float b, float lineWidth) {
    glColor3f(r, g, b);
    glLineWidth(lineWidth);
    glBegin(GL_LINE_LOOP);
        glVertex2f(x1, y1);
        glVertex2f(x2, y2);
        glVertex2f(x3, y3);
    glEnd();
}
