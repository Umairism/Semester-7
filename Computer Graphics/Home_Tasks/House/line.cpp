#include "line.h"

void drawLine(float x1, float y1, float x2, float y2,
              float r, float g, float b, float lineWidth) {
    glColor3f(r, g, b);
    glLineWidth(lineWidth);
    glBegin(GL_LINES);
        glVertex2f(x1, y1);
        glVertex2f(x2, y2);
    glEnd();
}
