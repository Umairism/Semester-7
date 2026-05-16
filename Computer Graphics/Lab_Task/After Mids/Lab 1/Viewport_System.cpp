#include <GL/glut.h>
#include <iostream>

// Viewport dimensions
int viewportWidth = 1920;
int viewportHeight = 1080;

// Initialize display
void display() {
    glClear(GL_COLOR_BUFFER_BIT);
    glLoadIdentity();
    
    // Set up orthographic projection
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    glOrtho(0.0, viewportWidth, 0.0, viewportHeight, -1.0, 1.0);
    glMatrixMode(GL_MODELVIEW);
    
    // Set viewport
    glViewport(0, 0, viewportWidth, viewportHeight);
    
    // Draw a simple rectangle using glVertex2f
    glBegin(GL_QUADS);
    glColor3f(1.0f, 0.0f, 0.0f);
    glVertex2f(100.0f, 100.0f);
    glVertex2f(300.0f, 100.0f);
    glVertex2f(300.0f, 300.0f);
    glVertex2f(100.0f, 300.0f);
    glEnd();
    
    // // Draw a triangle
    // glBegin(GL_TRIANGLES);
    // glColor3f(0.0f, 1.0f, 0.0f);
    // glVertex2f(400.0f, 150.0f);
    // glVertex2f(500.0f, 150.0f);
    // glVertex2f(450.0f, 250.0f);
    // glEnd();
    
    glFlush();
}

// Reshape callback
void reshape(int w, int h) {
    viewportWidth = w;
    viewportHeight = h;
}

// Initialize OpenGL
void init() {
    glClearColor(0.0f, 0.0f, 0.0f, 1.0f);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    glOrtho(0.0, viewportWidth, 0.0, viewportHeight, -1.0, 1.0);
    glMatrixMode(GL_MODELVIEW);
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutInitWindowSize(viewportWidth, viewportHeight);
    glutCreateWindow("Viewport System - Ortho2D");
    
    init();
    glutDisplayFunc(display);
    glutReshapeFunc(reshape);
    glutMainLoop();
    
    return 0;
}