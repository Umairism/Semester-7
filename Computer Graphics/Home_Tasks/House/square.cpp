#include "square.h"

void drawSquare(float cx, float cy, float side,
                float r, float g, float b) {
    float half = side / 2.0f;
    glColor3f(r, g, b);
    glBegin(GL_QUADS);
        glVertex2f(cx - half, cy - half);
        glVertex2f(cx + half, cy - half);
        glVertex2f(cx + half, cy + half);
        glVertex2f(cx - half, cy + half);
    glEnd();
}

void drawSquareOutline(float cx, float cy, float side,
                       float r, float g, float b, float lineWidth) {
    float half = side / 2.0f;
    glColor3f(r, g, b);
    glLineWidth(lineWidth);
    glBegin(GL_LINE_LOOP);
        glVertex2f(cx - half, cy - half);
        glVertex2f(cx + half, cy - half);
        glVertex2f(cx + half, cy + half);
        glVertex2f(cx - half, cy + half);
    glEnd();
}
