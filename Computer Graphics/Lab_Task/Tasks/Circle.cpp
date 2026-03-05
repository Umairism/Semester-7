#ifdef __APPLE_CC__
#include <GLUT/glut.h>
#include <math.h>
#else
#include <GL/glut.h>
#include <math.h>
#endif

void display() {

  glClear(GL_COLOR_BUFFER_BIT);

//   glBegin(GL_LINE_LOOP);
//     glColor3f(1, 0, 0); glVertex3f(-0.6, -0.75, 0.5);
//     glColor3f(0, 1, 0); glVertex3f(0.6, -0.75, 0);
//     glColor3f(0, 0, 1); glVertex3f(0, 0.75, 0);
//   glEnd();
    drawCircle(0.0, 0.0, 0.5, 100);

  glFlush();
}

void drawCircle(float cx, float cy, float r, int num_segments) {
    glBegin(GL_POLYGON);
    for(int i = 0; i < num_segments; i++) {
        float theta = 2.0f * 3.1415926f * float(i) / float(num_segments);
        glVertex2f(cx + r * cosf(theta), cy + r * sinf(theta));
    }
    glEnd();
}

int main(int argc, char** argv) {

  glutInit(&argc, argv);
  glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);

  glutInitWindowPosition(80, 80);
  glutInitWindowSize(500, 500);
  glutCreateWindow("A Simple Circle");
  // gluOrtho2D(-500, 500, -500, 500);
  glutDisplayFunc(display);
  glutMainLoop();
}
