#include <GL/glut.h>
#include <cstdlib>
#include <iostream>
using namespace std;

int g_x1, g_y1, g_x2, g_y2;
int g_pixelSize = 3;
int g_windowWidth = 800;
int g_windowHeight = 600;
int g_worldLeft, g_worldRight, g_worldBottom, g_worldTop;

void setWorldBounds() {
    int margin = 20;

    int minX = (g_x1 < g_x2) ? g_x1 : g_x2;
    int maxX = (g_x1 > g_x2) ? g_x1 : g_x2;
    int minY = (g_y1 < g_y2) ? g_y1 : g_y2;
    int maxY = (g_y1 > g_y2) ? g_y1 : g_y2;

    g_worldLeft = (minX < 0 ? minX : 0) - margin;
    g_worldRight = (maxX > 0 ? maxX : 0) + margin;
    g_worldBottom = (minY < 0 ? minY : 0) - margin;
    g_worldTop = (maxY > 0 ? maxY : 0) + margin;

    if (g_worldLeft == g_worldRight) {
        g_worldRight = g_worldLeft + 1;
    }

    if (g_worldBottom == g_worldTop) {
        g_worldTop = g_worldBottom + 1;
    }
}

void applyProjection(int width, int height) {
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();

    double worldWidth = g_worldRight - g_worldLeft;
    double worldHeight = g_worldTop - g_worldBottom;
    double windowAspect = static_cast<double>(width) / static_cast<double>(height);
    double worldAspect = worldWidth / worldHeight;

    double left = g_worldLeft;
    double right = g_worldRight;
    double bottom = g_worldBottom;
    double top = g_worldTop;

    if (windowAspect > worldAspect) {
        double expandedWidth = worldHeight * windowAspect;
        double centerX = (left + right) / 2.0;
        left = centerX - expandedWidth / 2.0;
        right = centerX + expandedWidth / 2.0;
    } else {
        double expandedHeight = worldWidth / windowAspect;
        double centerY = (bottom + top) / 2.0;
        bottom = centerY - expandedHeight / 2.0;
        top = centerY + expandedHeight / 2.0;
    }

    gluOrtho2D(left, right, bottom, top);

    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
}

void drawPixel(int x, int y) {
    int half = g_pixelSize / 2;
    glRecti(x - half, y - half, x + half + 1, y + half + 1);
}

void drawText(float x, float y, const char* text) {
    glRasterPos2f(x, y);
    for (const char* character = text; *character != '\0'; ++character) {
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, *character);
    }
}

void drawGrid() {
    glColor3f(0.18f, 0.18f, 0.18f);
    glBegin(GL_LINES);

    int step = 10;
    int startX = (g_worldLeft / step) * step;
    int startY = (g_worldBottom / step) * step;

    for (int x = startX; x <= g_worldRight; x += step) {
        glVertex2i(x, g_worldBottom);
        glVertex2i(x, g_worldTop);
    }

    for (int y = startY; y <= g_worldTop; y += step) {
        glVertex2i(g_worldLeft, y);
        glVertex2i(g_worldRight, y);
    }

    glEnd();
}

void drawAxes() {
    glColor3f(0.6f, 0.6f, 0.6f);
    glBegin(GL_LINES);

    if (g_worldBottom <= 0 && g_worldTop >= 0) {
        glVertex2i(g_worldLeft, 0);
        glVertex2i(g_worldRight, 0);
    }

    if (g_worldLeft <= 0 && g_worldRight >= 0) {
        glVertex2i(0, g_worldBottom);
        glVertex2i(0, g_worldTop);
    }

    glEnd();

    glColor3f(0.9f, 0.9f, 0.9f);
    if (g_worldLeft <= 0 && g_worldRight >= 0) {
        drawText(2, g_worldTop - 8, "Y");
    }
    if (g_worldBottom <= 0 && g_worldTop >= 0) {
        drawText(g_worldRight - 8, 2, "X");
    }
}

void drawPointLabel(int x, int y, const char* label) {
    glColor3f(1.0f, 0.85f, 0.2f);
    drawText(static_cast<float>(x + 2), static_cast<float>(y + 2), label);
}

void printBresenhamPoints(int x1, int y1, int x2, int y2) {
    int dx = abs(x2 - x1);
    int dy = abs(y2 - y1);

    int sx = (x1 < x2) ? 1 : -1;
    int sy = (y1 < y2) ? 1 : -1;

    int err = dx - dy;

    cout << "\nPoints on the line:\n";
    while (true) {
        cout << "(" << x1 << ", " << y1 << ")\n";

        if (x1 == x2 && y1 == y2) {
            break;
        }

        int e2 = 2 * err;

        if (e2 > -dy) {
            err -= dy;
            x1 += sx;
        }

        if (e2 < dx) {
            err += dx;
            y1 += sy;
        }
    }
}

// Bresenham's algorithm for all octants. Each point is sent to OpenGL.
void bresenhamLine(int x1, int y1, int x2, int y2) {
    int dx = abs(x2 - x1);
    int dy = abs(y2 - y1);

    int sx = (x1 < x2) ? 1 : -1;
    int sy = (y1 < y2) ? 1 : -1;

    int err = dx - dy;

    while (true) {
        drawPixel(x1, y1);

        if (x1 == x2 && y1 == y2) {
            break;
        }

        int e2 = 2 * err;

        if (e2 > -dy) {
            err -= dy;
            x1 += sx;
        }

        if (e2 < dx) {
            err += dx;
            y1 += sy;
        }
    }
}

void display() {
    glClear(GL_COLOR_BUFFER_BIT);

    drawGrid();
    drawAxes();

    glEnable(GL_BLEND);
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
    glEnable(GL_LINE_SMOOTH);
    glHint(GL_LINE_SMOOTH_HINT, GL_NICEST);
    glColor4f(0.8f, 0.8f, 0.8f, 0.45f);
    glLineWidth(1.5f);
    glBegin(GL_LINES);
    glVertex2i(g_x1, g_y1);
    glVertex2i(g_x2, g_y2);
    glEnd();
    glDisable(GL_LINE_SMOOTH);
    glDisable(GL_BLEND);

    glColor3f(0.95f, 0.95f, 1.0f);
    bresenhamLine(g_x1, g_y1, g_x2, g_y2);

    drawPointLabel(g_x1, g_y1, "P1");
    drawPointLabel(g_x2, g_y2, "P2");

    glColor3f(0.85f, 0.85f, 0.85f);
    char info1[128];
    char info2[128];
    snprintf(info1, sizeof(info1), "P1 = (%d, %d)", g_x1, g_y1);
    snprintf(info2, sizeof(info2), "P2 = (%d, %d)", g_x2, g_y2);
    drawText(g_worldLeft + 5, g_worldTop - 8, info1);
    drawText(g_worldLeft + 5, g_worldTop - 18, info2);

    glutSwapBuffers();
}

void reshape(int width, int height) {
    if (height == 0) {
        height = 1;
    }

    g_windowWidth = width;
    g_windowHeight = height;

    glViewport(0, 0, width, height);
    applyProjection(width, height);
}

int main(int argc, char** argv) {
    cout << "Enter x1 y1: ";
    cin >> g_x1 >> g_y1;

    cout << "Enter x2 y2: ";
    cin >> g_x2 >> g_y2;

    printBresenhamPoints(g_x1, g_y1, g_x2, g_y2);

    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
    glutInitWindowSize(800, 600);
    glutInitWindowPosition(100, 100);
    glutCreateWindow("Bresenham Line - OpenGL GLUT");

    glClearColor(0.0f, 0.0f, 0.0f, 1.0f);
    glEnable(GL_POINT_SMOOTH);
    glHint(GL_POINT_SMOOTH_HINT, GL_NICEST);
    setWorldBounds();
    applyProjection(g_windowWidth, g_windowHeight);

    glutDisplayFunc(display);
    glutReshapeFunc(reshape);
    glutMainLoop();
    return 0;
}