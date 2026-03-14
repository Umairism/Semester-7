#ifdef __APPLE_CC__
#include <GLUT/glut.h>
#else
#include <GL/glut.h>
#endif

int windowWidth = 800;
int windowHeight = 600;

float houseX = 400.0f;
float houseY = 300.0f;
bool dragEnabled = false;
bool leftButtonDown = false;

void drawHouse() {
	// House dimensions are based on the original lab shape, centered around (0, 0).
	const float left = -65.0f;
	const float split = -20.0f;
	const float right = 60.0f;
	const float bottom = -60.0f;
	const float wallTop = 10.0f;
	const float roofTop = 40.0f;

	// Left wall
	glColor3f(0.82f, 0.71f, 0.55f);
	glBegin(GL_QUADS);
	glVertex2f(left, bottom);
	glVertex2f(split, bottom);
	glVertex2f(split, wallTop);
	glVertex2f(left, wallTop);
	glEnd();

	// Right wall
	glColor3f(0.40f, 0.26f, 0.13f);
	glBegin(GL_QUADS);
	glVertex2f(split, bottom);
	glVertex2f(right, bottom);
	glVertex2f(right, wallTop);
	glVertex2f(split, wallTop);
	glEnd();

	// Roof (left triangle)
	glColor3f(0.38f, 0.38f, 0.38f);
	glBegin(GL_TRIANGLES);
	glVertex2f(left, wallTop);
	glVertex2f(split, wallTop);
	glVertex2f(-37.0f, roofTop);
	glEnd();

	// Roof (right quad)
	glColor3f(0.50f, 0.50f, 0.50f);
	glBegin(GL_QUADS);
	glVertex2f(-37.0f, roofTop);
	glVertex2f(right, roofTop);
	glVertex2f(right, wallTop);
	glVertex2f(split, wallTop);
	glEnd();

	// Door
	glColor3f(0.65f, 0.45f, 0.25f);
	glBegin(GL_QUADS);
	glVertex2f(-48.0f, bottom);
	glVertex2f(-28.0f, bottom);
	glVertex2f(-28.0f, -15.0f);
	glVertex2f(-48.0f, -15.0f);
	glEnd();

	// Window
	glColor3f(0.65f, 0.65f, 0.65f);
	glBegin(GL_QUADS);
	glVertex2f(5.0f, -30.0f);
	glVertex2f(50.0f, -30.0f);
	glVertex2f(50.0f, 0.0f);
	glVertex2f(5.0f, 0.0f);
	glEnd();

	// Outline
	glColor3f(0.15f, 0.12f, 0.10f);
	glLineWidth(2.0f);
	glBegin(GL_LINE_LOOP);
	glVertex2f(left, bottom);
	glVertex2f(left, wallTop);
	glVertex2f(-37.0f, roofTop);
	glVertex2f(right, roofTop);
	glVertex2f(right, bottom);
	glEnd();
}

void display() {
	glClear(GL_COLOR_BUFFER_BIT);

	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();
	glTranslatef(houseX, houseY, 0.0f);
	drawHouse();

	glFlush();
}

void updateHousePositionFromMouse(int x, int y) {
	houseX = static_cast<float>(x);
	houseY = static_cast<float>(windowHeight - y);
	glutPostRedisplay();
}

void activeMouseMotion(int x, int y) {
	if (dragEnabled && leftButtonDown) {
		updateHousePositionFromMouse(x, y);
	}
}

void passiveMouseMotion(int x, int y) {
	(void)x;
	(void)y;
}

void mouseButton(int button, int state, int x, int y) {
	if (button == GLUT_LEFT_BUTTON) {
		if (state == GLUT_DOWN) {
			dragEnabled = true;
			leftButtonDown = true;
			updateHousePositionFromMouse(x, y);
		} else if (state == GLUT_UP) {
			leftButtonDown = false;
		}
	}

	if (button == GLUT_RIGHT_BUTTON && state == GLUT_DOWN) {
		dragEnabled = false;
		leftButtonDown = false;
	}
}

void reshape(int width, int height) {
	if (height == 0) {
		height = 1;
	}

	windowWidth = width;
	windowHeight = height;

	glViewport(0, 0, width, height);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluOrtho2D(0.0, static_cast<double>(width), 0.0, static_cast<double>(height));

	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();
}

int main(int argc, char** argv) {
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
	glutInitWindowPosition(100, 100);
	glutInitWindowSize(windowWidth, windowHeight);
	glutCreateWindow("Lab Task 5 - Mouse Handling with House Pointer");

	glClearColor(0.93f, 0.95f, 0.98f, 1.0f);

	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluOrtho2D(0.0, static_cast<double>(windowWidth), 0.0, static_cast<double>(windowHeight));

	glutDisplayFunc(display);
	glutReshapeFunc(reshape);
	glutMouseFunc(mouseButton);

	// Required callbacks for this lab.
	glutMotionFunc(activeMouseMotion);
	glutPassiveMotionFunc(passiveMouseMotion);

	glutMainLoop();
	return 0;
}
