import pyglet

music = pyglet.resource.media('Lil Globglogabgalab.mp3', streaming=False)
music.play()
pyglet.app.run()