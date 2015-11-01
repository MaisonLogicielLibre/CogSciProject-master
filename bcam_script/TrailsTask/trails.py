from psychopy import visual
from psychopy import event
from psychopy import core
from psychopy import colors

INSPECTtime = 5  # sec
DRAWtime = 30    # sec

# create a window, a mouse monitor and a clock
w = visual.Window(winType='pyglet')
m = event.Mouse(win=w)
tick = core.Clock()

# initialize variables
drawlist = []
mousedown = False
tick.reset()
coloridx = -1

# show image for a few seconds
t1 = visual.TextStim(w,text="Study This",pos=(0,0.9))
im = visual.SimpleImageStim(w,'REY.jpeg')
while tick.getTime()<INSPECTtime:
     t1.draw()
     im.draw()
     w.flip()

# now put up space to draw in for a little while
t2 = visual.TextStim(w,text="OK, now reproduce it.",pos=(0,0.9))
while tick.getTime()<INSPECTtime+DRAWtime:
     t2.draw()
     for item in drawlist:
         item.draw()
     w.flip()
     pos = m.getPos().tolist()
     if m.getPressed()[0]==1:
         # if the mouse is down, determine if JUST pressed, or still pressed
         if mousedown == False:
             # start a new drawing phase (and change colors)
             mousedown = True
             coloridx += 1
             c = colors.colors[colors.colors.keys()[coloridx]]
             drawlist.append(visual.ShapeStim(w,lineWidth=2.0,lineColor=c,closeShape=False))
             drawlist[-1].setVertices(pos)
         else:
             # continue last drawing phase
             if len(drawlist[-1].vertices.shape)==1:
                 # only one vertex thus far (vertices is 1D)
                 drawlist[-1].setVertices([drawlist[-1].vertices.tolist()]+[pos])
             else:
                 # more than one vertex (vertices is 2D)
                 drawlist[-1].setVertices(drawlist[-1].vertices.tolist()+[pos])
     elif m.getPressed()[0]==0:
         # if the mouse is up, reset and wait for new drawing phase
         mousedown = False
     if m.getPressed()[2]:
         # if right button is pressed, quit early
         break

# print out the first few vertices from each drawing phase
for i in range(len(drawlist)):
     print
     print i,drawlist[i].vertices[:3]
     print 'etc.'
print "Above are the first few vertices for each drawing phase."