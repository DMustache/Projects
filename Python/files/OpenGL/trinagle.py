import pyglet
from pyglet import app, graphics
from pyglet.gl import *
from pyglet.window import Window
dx, dy = 25, 15
dx2 = dx / 2
dy2 = dy / 2
wx, wy = 1.5 * dx2, 1.5 * dy2
width, height = int(20 * wx), int(20 * wy)

window = Window(visible = True, width = width, height = height,
                resizable = True, caption = 'Прямоугольник')
glClearColor(0.1, 0.1, 0.1, 1.0)
glClear(GL_COLOR_BUFFER_BIT)
@window.event
def on_draw():

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-wx, wx, -wy, wy, -1, 1)
    glColor3f(0, 1, 0)
    glBegin(GL_QUADS)
    glVertex3f(-dx2, -dy2, 0)
    glVertex3f(dx2, -dy2, 0)
    glVertex3f(dx2, dy2, 0)
    glVertex3f(-dx2, dy2, 0)
    glEnd()
app.run()