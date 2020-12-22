from pyglet.window import Window
from pyglet import window
import pyglet

win = window.Window(caption='Initial caption')

class HelloWorldWindow(pyglet.window.Window):
    def __init__(self):
        super(HelloWorldWindow, self).__init__()

        self.label = pyglet.text.Label('Hello World!')
        self.set_icon = pyglet.image.load('trainer/007-pomatinyas.png')

    def on_draw(self):
        self.clear()
        self.label.draw()
        self.set_icon()

if __name__ == '__main__':
    window = HelloWorldWindow()
    pyglet.app.run()