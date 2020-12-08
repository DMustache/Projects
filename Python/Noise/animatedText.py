import os
import math
import pyglet
from pyglet.gl import glPixelStorei, glTextImage3D, glTextParameteri
from pyglet.gl import glEnable, glViewport, glMatrixMode, glLoadIdentity
from pyglet.gl import gluPerspective, glClear, glTranslatef, glRotate
from pyglet.gl import glBegin, glTexCoord3f, glVertex3f, glEnd, gl_BYTE
from pyglet.gl import GL_UNPACK_ALIGNMENT, GL_TEXTURE_3D, GL_LUMINANCE
from pyglet.gl import GL_TEXTURE_MAG_FILTER, GL_TEXTURE_WRAP_T
from pyglet.gl import GL_TEXTURE_WRAP_S, GL_TEXTURE_MIN_FILTER
import ctypes
import noise
from noise import pnoise3, snoise3

def create_3d_texture(width, scale):
    coords = range(width)
    texel = (ctypes.c_byte * width ** 3)()
    half = 0

    for z in coords:
        for y in coords:
            for x in coords:
                v = snoise3(x * scale - half, z * scale - half, octaves=4, persistence=0.25)
                texel[x + (y * width) + (z * width ** 2)] = int(v * 127.0)

    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glTextImage3D(GL_TEXTURE_3D, 0, GL_LUMINANCE, width, width, width, 0,
    GL_LUMINANCE, gl_BYTE, ctypes.byref(texel))

    return texel

if __name__ == '__main__':
    import sys
    global xrot, yrot, d
    win = pyglet.window.Window(width=320, height=320, resizable=True,
    visible=False, config=pyglet.gl.Config(sample_buffers=1, samples=4, 
    double_buffer=True, depth_size=24))

    glTextParameteri(GL_TEXTURE_3D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTextParameteri(GL_TEXTURE_3D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTextParameteri(GL_TEXTURE_3D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTextParameteri(GL_TEXTURE_3D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glEnable(GL_TEXTURE_3D)
    xrot = yrot = d = 0

    def 
