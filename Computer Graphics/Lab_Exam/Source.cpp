
#include <GL/glut.h>
#include <iostream>
#include <cmath>
#include <vector>

int winWidth = 600;
int winHeight = 600;
int xs = 50, ys = 50, xe = 500, ye = 450;

std::vector<std::pair<int,int>> bresPoints;

void plotPoint(int x, int y) {
	glVertex2i(x, y);
}

void computeBresenhamPoints(int x0, int y0, int x1, int y1) {
	bresPoints.clear();
	int dx = std::abs(x1 - x0);
	int dy = std::abs(y1 - y0);
	int sx = (x0 < x1) ? 1 : -1;
	int sy = (y0 < y1) ? 1 : -1;
	int err = dx - dy;

	while (true) {
		bresPoints.emplace_back(x0, y0);
		if (x0 == x1 && y0 == y1) break;
		int e2 = 2 * err;
		if (e2 > -dy) { err -= dy; x0 += sx; }
		if (e2 < dx)  { err += dx; y0 += sy; }
	}
}

void drawAxes() {
	glColor3f(0.0f, 0.0f, 0.0f);
	glBegin(GL_LINES);
		glVertex2i(0, winHeight/2); glVertex2i(winWidth, winHeight/2);
		glVertex2i(winWidth/2, 0); glVertex2i(winWidth/2, winHeight);
	glEnd();
}

void display() {
	glClear(GL_COLOR_BUFFER_BIT);

	drawAxes();

	glColor3f(1.0f, 0.0f, 0.0f);
	glPointSize(6.0f);
	glBegin(GL_POINTS);
		for (auto &p : bresPoints) glVertex2i(p.first, p.second);
	glEnd();

	int s = 4;
	glColor3f(0.0f, 0.0f, 1.0f);
	glBegin(GL_QUADS);
		glVertex2i(xs - s, ys - s); glVertex2i(xs + s, ys - s);
		glVertex2i(xs + s, ys + s); glVertex2i(xs - s, ys + s);
		glVertex2i(xe - s, ye - s); glVertex2i(xe + s, ye - s);
		glVertex2i(xe + s, ye + s); glVertex2i(xe - s, ye + s);
	glEnd();

	glutSwapBuffers();
}

void reshape(int w, int h) {
	winWidth = w; winHeight = h;
	glViewport(0, 0, w, h);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluOrtho2D(0, w, 0, h);
	glMatrixMode(GL_MODELVIEW);
}

int main(int argc, char** argv) {
	std::cout << "Enter x0 y0 x1 y1 (0.." << winWidth << ", 0.." << winHeight << "): ";
	if (!(std::cin >> xs >> ys >> xe >> ye)) {
		std::cout << "Using default points: (" << xs << "," << ys << ") -> (" << xe << "," << ye << ")\n";
	} else {
		std::cout << "Reference points: (" << xs << "," << ys << ") -> (" << xe << "," << ye << ")\n";
	}

	computeBresenhamPoints(xs, ys, xe, ye);
	int dx = std::abs(xe - xs);
	int dy = std::abs(ye - ys);
	int sx = (xs < xe) ? 1 : -1;
	int sy = (ys < ye) ? 1 : -1;
	double slope = (dx == 0) ? INFINITY : static_cast<double>(ye - ys) / static_cast<double>(xe - xs);
	std::cout << "dx=" << dx << " dy=" << dy << " sx=" << sx << " sy=" << sy << "\n";
	std::cout << "Approx slope=" << slope << "\n";
	std::cout << "Plotted pixel count: " << bresPoints.size() << "\n";
	std::cout << "Plotted pixels (index: x,y):\n";
	for (size_t i = 0; i < bresPoints.size(); ++i) {
		std::cout << i << ": (" << bresPoints[i].first << "," << bresPoints[i].second << ")\n";
	}

	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
	glutInitWindowSize(winWidth, winHeight);
	glutCreateWindow("Bresenham Line Drawing");

	glClearColor(1.0f, 1.0f, 1.0f, 1.0f);

	glutDisplayFunc(display);
	glutReshapeFunc(reshape);

	glutMainLoop();
	return 0;
}