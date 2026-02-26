#include "circle.h"

void drawCircle(float cx, float cy, float radius,
                float r, float g, float b, int segments) {
    glColor3f(r, g, b);
    glBegin(GL_POLYGON);
    for (int i = 0; i < segments; i++) {
        float theta = 2.0f * M_PI * float(i) / float(segments);
        glVertex2f(cx + radius * cosf(theta), cy + radius * sinf(theta));
    }
    glEnd();
}

void drawCircleOutline(float cx, float cy, float radius,
                       float r, float g, float b, float lineWidth, int segments) {
    glColor3f(r, g, b);
    glLineWidth(lineWidth);
    glBegin(GL_LINE_LOOP);
    for (int i = 0; i < segments; i++) {
        float theta = 2.0f * M_PI * float(i) / float(segments);
        glVertex2f(cx + radius * cosf(theta), cy + radius * sinf(theta));
    }
    glEnd();
}
