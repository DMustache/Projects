import pyglet

window = pyglet.window.Window(1200, 720, resizable=True)

@window.event
def on_resize(width, height):
    print('the window was resized to %dx%d' % (width, height))

pyglet.app.run()