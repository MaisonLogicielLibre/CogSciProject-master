import pyglet
from pyglet import window, image
from pyglet.gl import *
from math import *

win=window.Window(fullscreen=True)

brush_size = 10

def draw_circle(x,y,diameter):
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)
    for angle in range(361):
        glVertex2f( x+sin(angle)*(diameter/2.0), y+cos(angle)*(diameter/
2.0) )
    glEnd()

def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    glColor3f(1,1,1)
    for i in range(2):
        draw_circle(x,y,brush_size)
        draw_circle(x-dx,y-dy,brush_size)
        win.flip()

win.on_mouse_drag = on_mouse_drag

def on_mouse_press(x,y,buttons,modifiers):
    for i in range(2):
        draw_circle(x,y,brush_size)
        win.flip()

win.on_mouse_press=on_mouse_press

while True:
    win.dispatch_events()