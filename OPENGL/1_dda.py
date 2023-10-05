#!/usr/bin/env python3
# -*- coding:utf-8 -*-


from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def init():
    """初始化函数"""
    glClearColor(1, 1, 1, 1)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-50, 50, -50, 50, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glutPostRedisplay()


def line_dda(x1, y1, x2, y2):
    """使用DDA算法绘制线段"""
    dx = x2 - x1
    dy = y2 - y1
    if dx != 0:
        m = dy * 2.0 / dx
        if -1 <= m <= 1:
            if dx < 0:
                x1, x2 = x2, x1
                y = y2
            else:
                y = y1

            for x in range(x1, x2 + 1):
                glVertex2i(int(x), int(y + 0.5))
                y += m
        else:
            m = 1.0 / m
            x = x1
            if dy < 0:
                y1, y2 = y2, y1
                x = x2
            else:
                x = x1

            for y in range(y1, y2 + 1):
                glVertex2i(int(x), int(y + 0.5))
                x += m
    else:
        if dy < 0:
            y1, y2 = y2, y1
            x = x1

            for y in range(y1, y2 + 1):
                glVertex2i(int(x), int(y + 0.5))


def display():
    """显示回调函数"""
    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_POINTS)

    glColor3f(1, 0, 0) 
# 是一个OpenGL函数调用，用于设置当前绘图颜色。
# 在OpenGL中，颜色由红色（R）、绿色（G）和蓝色（B）三个分量组成，每个分量的取值范围为0.0到1.0之间。`glColor3f`函数的参数指定了红色、绿色和蓝色的分量值。
# 在这个例子中，`glColor3f(1, 0, 0)` 设置绘图颜色为红色，因为红色的红色分量（R）设置为1，绿色分量（G）和蓝色分量（B）均设置为0。这是一种使用RGB颜色模型的表示方法。
# 您可以根据需要使用不同的分量值来设置不同的颜色。例如，`glColor3f(0, 1, 0)` 设置绘图颜色为绿色，而`glColor3f(0, 0, 1)` 设置绘图颜色为蓝色。
# 请注意，这只是设置绘图颜色的一种方式，您可以使用其他函数和方法来设置颜色，例如使用十六进制值表示颜色或使用RGBA颜色模型等。这取决于您使用的图形库和具体需求。
    line_dda(-20, -20, 30, 25)

    glEnd()
    glFlush()


def main():
    """主函数"""
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

    glutCreateWindow("dda_algorithm")
    glutInitWindowSize(100, 100)

    glutDisplayFunc(display)

    init()

    glutMainLoop()

if __name__ == '__main__':
    main()