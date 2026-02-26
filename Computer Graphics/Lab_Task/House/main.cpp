
#include "rectangle.h"
#include "triangle.h"
#include "circle.h"
#include "line.h"
#include "square.h"
#include <cstdio>
#include <cstring>

bool showGrid = true;

// Walls
const float BEIGE_R = 0.82f, BEIGE_G = 0.71f, BEIGE_B = 0.55f;   // left wall
const float BROWN_R = 0.40f, BROWN_G = 0.26f, BROWN_B = 0.13f;   // right wall

// Roof
const float DARK_GRAY_R = 0.38f, DARK_GRAY_G = 0.38f, DARK_GRAY_B = 0.38f; // left roof
const float GRAY_R = 0.50f, GRAY_G = 0.50f, GRAY_B = 0.50f;               // right roof

// Door
const float DOOR_R = 0.65f, DOOR_G = 0.45f, DOOR_B = 0.25f;

// Window panes
const float PANE_R = 0.65f, PANE_G = 0.65f, PANE_B = 0.65f;

// Outlines
const float OUTLINE_R = 0.15f, OUTLINE_G = 0.12f, OUTLINE_B = 0.10f;

// Window frame
const float FRAME_R = 0.25f, FRAME_G = 0.18f, FRAME_B = 0.12f;

// ── Debug: draw text at position ──
void drawText(float x, float y, const char* text, float r, float g, float b) {
    glColor3f(r, g, b);
    glRasterPos2f(x, y);
    for (const char* c = text; *c != '\0'; c++) {
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_10, *c);
    }
}

void drawGrid() {
    char label[16];

    glColor3f(0.75f, 0.75f, 0.85f);
    glLineWidth(0.5f);
    glBegin(GL_LINES);
    for (int x = 0; x <= 600; x += 50) {
        glVertex2f(x, 0); glVertex2f(x, 500);
    }
    for (int y = 0; y <= 500; y += 50) {
        glVertex2f(0, y); glVertex2f(600, y);
    }
    glEnd();

    glColor3f(0.55f, 0.55f, 0.70f);
    glLineWidth(1.0f);
    glBegin(GL_LINES);
    for (int x = 0; x <= 600; x += 100) {
        glVertex2f(x, 0); glVertex2f(x, 500);
    }
    for (int y = 0; y <= 500; y += 100) {
        glVertex2f(0, y); glVertex2f(600, y);
    }
    glEnd();

    for (int x = 0; x <= 600; x += 100) {
        snprintf(label, sizeof(label), "%d", x);
        drawText(x + 2, 3, label, 0.0f, 0.0f, 0.6f);
    }
    for (int y = 0; y <= 500; y += 100) {
        snprintf(label, sizeof(label), "%d", y);
        drawText(3, y + 2, label, 0.0f, 0.0f, 0.6f);
    }

    float keyPoints[][2] = {
        {30,55}, {210,55}, {530,55},                // wall bottoms
        {30,335}, {210,335}, {530,335},              // wall tops
        {140,420}, {530,420},                        // roof peaks
        {95,55}, {175,55}, {95,235}, {175,235},      // door corners
        {315,155}, {495,155}, {315,310}, {495,310},  // window corners
        {167,145}                                    // door knob
    };
    int numPoints = sizeof(keyPoints) / sizeof(keyPoints[0]);

    for (int i = 0; i < numPoints; i++) {
        float px = keyPoints[i][0];
        float py = keyPoints[i][1];

        glPointSize(6.0f);
        glColor3f(1.0f, 0.0f, 0.0f);
        glBegin(GL_POINTS);
            glVertex2f(px, py);
        glEnd();

        snprintf(label, sizeof(label), "(%d,%d)", (int)px, (int)py);
        drawText(px + 4, py + 4, label, 1.0f, 0.0f, 0.0f);
    }
}

void display() {
    glClear(GL_COLOR_BUFFER_BIT);

    // Left wall (beige)
    drawRectangle(30, 55, 210, 335, BEIGE_R, BEIGE_G, BEIGE_B);
    drawRectangleOutline(30, 55, 210, 335, OUTLINE_R, OUTLINE_G, OUTLINE_B, 2.0f);

    // Right wall (dark brown)
    drawRectangle(210, 55, 530, 335, BROWN_R, BROWN_G, BROWN_B);
    drawRectangleOutline(210, 55, 530, 335, OUTLINE_R, OUTLINE_G, OUTLINE_B, 2.0f);

    // Right roof
    drawQuad(140, 420,
             530, 420,
             530, 335,
             210, 335,
             GRAY_R, GRAY_G, GRAY_B);

    // Left roof
    drawTriangle(30, 335,
                 210, 335,
                 140, 420,
                 DARK_GRAY_R, DARK_GRAY_G, DARK_GRAY_B);

    // Roof outlines (lines)
    drawLine(30, 335, 140, 420, OUTLINE_R, OUTLINE_G, OUTLINE_B, 2.0f);  
    drawLine(140, 420, 530, 420, OUTLINE_R, OUTLINE_G, OUTLINE_B, 2.0f); 
    drawLine(530, 420, 530, 335, OUTLINE_R, OUTLINE_G, OUTLINE_B, 2.0f); 
    drawLine(30, 335, 210, 335, OUTLINE_R, OUTLINE_G, OUTLINE_B, 1.5f);
    drawLine(210, 335, 140, 420, OUTLINE_R, OUTLINE_G, OUTLINE_B, 1.5f);

    // Door body
    drawRectangle(95, 55, 175, 235, DOOR_R, DOOR_G, DOOR_B);
    drawRectangleOutline(95, 55, 175, 235, OUTLINE_R, OUTLINE_G, OUTLINE_B, 2.0f);

    // Door knob (circle)
    drawCircle(167, 145, 5, 0.1f, 0.1f, 0.1f);


    // Window background / frame (rectangle)
    drawRectangle(315, 155, 495, 310, FRAME_R, FRAME_G, FRAME_B);

    drawRectangle(322, 239, 398, 302, PANE_R, PANE_G, PANE_B); 
    drawRectangle(412, 239, 488, 302, PANE_R, PANE_G, PANE_B);
    drawRectangle(322, 162, 398, 225, PANE_R, PANE_G, PANE_B);
    drawRectangle(412, 162, 488, 225, PANE_R, PANE_G, PANE_B); 

    // Window outer outline
    drawRectangleOutline(315, 155, 495, 310, OUTLINE_R, OUTLINE_G, OUTLINE_B, 2.5f);

    drawLine(20, 55, 540, 55, OUTLINE_R, OUTLINE_G, OUTLINE_B, 2.0f);

    // ── Debug grid overlay ──
    
    // if (showGrid) {
    //     drawGrid();
    // }

    glFlush();
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);

    glutInitWindowPosition(80, 80);
    glutInitWindowSize(600, 500);
    glutCreateWindow("House - OpenGL");
    gluOrtho2D(0, 600, 0, 500);

    // Dark background
    glClearColor(0.95f, 0.95f, 0.92f, 1.0f);

    glutDisplayFunc(display);
    glutMainLoop();

    return 0;
}
