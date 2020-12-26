from pyglet.window import Window
from pyglet import window
import pyglet

win = pyglet.window.Window()
win.set_icon(pyglet.image.load('antara.png'))

def on_mouse_motion(x, y, dx, dy):
    pass

pyglet.app.run()