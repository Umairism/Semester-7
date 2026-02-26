#include "rectangle.h"

void drawRectangle(float x1, float y1, float x2, float y2,
                   float r, float g, float b) {
    glColor3f(r, g, b);
    glBegin(GL_QUADS);
        glVertex2f(x1, y1);
        glVertex2f(x2, y1);
        glVertex2f(x2, y2);
        glVertex2f(x1, y2);
    glEnd();
}

void drawRectangleOutline(float x1, float y1, float x2, float y2,
                          float r, float g, float b, float lineWidth) {
    glColor3f(r, g, b);
    glLineWidth(lineWidth);
    glBegin(GL_LINE_LOOP);
        glVertex2f(x1, y1);
        glVertex2f(x2, y1);
        glVertex2f(x2, y2);
        glVertex2f(x1, y2);
    glEnd();
}

void drawQuad(float x1, float y1, float x2, float y2,
              float x3, float y3, float x4, float y4,
              float r, float g, float b) {
    glColor3f(r, g, b);
    glBegin(GL_QUADS);
        glVertex2f(x1, y1);
        glVertex2f(x2, y2);
        glVertex2f(x3, y3);
        glVertex2f(x4, y4);
    glEnd();
}
