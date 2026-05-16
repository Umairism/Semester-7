#include <GL/glut.h>
#include <iostream>

void draw()
{
    glClearColor(1.0, 1.0, 0.0, 0.0);   // Yellow background (range 0–1)
    glClear(GL_COLOR_BUFFER_BIT);

    // 🔹 First Viewport (Left)
    glViewport(0, 0, 250, 250);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0.0, 50.0, -10.0, 40.0);
    
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();

    glColor3f(0, 0, 1);   // Blue rectangle
    glRectf(0.0, 0.0, 10.0, 30.0);


    // 🔹 Second Viewport (Right)
    glViewport(100, 0, 250, 250);   // moved to right side
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0.0, 50.0, -10.0, 40.0);
    
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();

    glColor3f(1, 0, 0);   // Red rectangle
    glRectf(0.0, 0.0, 10.0, 30.0);

    // 🔹 third Viewport (Right)
    glViewport(200, 0, 250, 250);   // moved to right side
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0.0, 50.0, -10.0, 40.0);
    
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();

    glColor3f(0, 1, 0);   // Green rectangle
    glRectf(0.0, 0.0, 10.0, 30.0);

    glutSwapBuffers();
}

void reshape(int width, int height)
{
    glViewport(0, 0, width, height);
}

void idle()
{
    glutPostRedisplay();
}

int main(int argc, char** argv)
{
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
    glutInitWindowSize(500, 250);
    glutInitWindowPosition(100, 100);
    glutCreateWindow("Viewport System - Two Rectangles");
    
    glutDisplayFunc(draw);
    glutReshapeFunc(reshape);
    glutIdleFunc(idle);
    
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0.0, 500.0, 0.0, 250.0);
    
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    
    glutMainLoop();
    return 0;
}