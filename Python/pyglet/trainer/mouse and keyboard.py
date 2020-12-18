import pyglet
from pyglet.window import Window, key, mouse

window = Window()

@window.event
def on_key_press(symbol, modifiers):
    if (symbol == key.A):
        print("A")
    elif (symbol == key.LEFT):
        print("Left arrow")
    elif (symbol == key.ENTER):
        print("ENTER")

@window.event
def on_mouse_press(x, y, button, modifires):
    if button == mouse.LEFT:
        print('LMS')

event_logger = pyglet.window.event.WindowEventLogger()
window.push_handlers(event_logger)

pyglet.app.run()
