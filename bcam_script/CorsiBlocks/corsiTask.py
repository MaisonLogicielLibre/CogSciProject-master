# -*- coding: utf-8 -*-
__author__ = 'turbosnail9'
import sys
import numpy as np
import random
import codecs
from psychopy import visual, monitors, event, core, data, logging
import itertools

"""ShapeStim can be used to make geometric shapes where you specify the locations of each vertex
relative to some anchor point.

NB for now the fill of objects is performed using glBegin(GL_POLYGON) and that is limited to convex
shapes. With concavities you get unpredictable results (e.g. add a fill colour to the arrow stim below).
To create concavities, you can combine multiple shapes, or stick to just outlines. (If anyone wants
to rewrite ShapeStim to use glu tesselators that would be great!)
"""
# inter-stimuli-interval
isi = 1


instructionsEng = """
On this task, you will see 9 blocks on the screen.

On each trial, several blocks will light up, one at a time.

You must remember the exact order in which they light up and 
repeat the same order by clicking on the blocks with the mouse.

When you are done, click on DONE.

If you wish to correct your sequence, click RESET to start over.

We will start with a sequence of 2 blocks.  Afterwards, the sequence may get longer

Let's begin
"""
instructionsFr = """
Pour cette tâche, vous verrez/allez voir 9 blocs à l'écran.
A chaque essai, plusieurs blocs s'allumeront, l'un après l'autre.
Vous devrez vous rappeler de l'ordre exact dans lequel les blocs se seront allumés 
et répéter cet ordre en cliquant sur les blocs avec la souris.

Lorsque vous aurez terminé, cliquez sur COMPLETÉ.
Si vous souhaitez corriger votre séquence, cliquez sur  REFAIRE afin de recommencer.

Nous commencerons avec une séquence de 2 blocs.  Par la suite, les séquences pourront se ralonger. 

Êtes-vous prêt(e)s à commencer?
"""
instructionsRevEng = """
This task is somewhat similar to the one you just completed, 
except that you have to repeat the sequence in the backwards order.  

Let's start
"""
instructionsRevFr = """
Cette tâche ressemble à celle que vous venez de compléter, 
sauf que vous devez répéter la séquence dans l'ordre inverse. 

Commençons
"""

trialFailEn = """
Whoops, that was not quite right. Try again!
"""

trialFailFr = """
Oups, ce n'était pas tout-à-fait ça. Réessayez!
"""
practiceEndEng = """
Good job! You have completed the practice.

If you would like more practice, click on PRACTICE.
If you are ready to start the task, click on START.
"""

practiceEndFr = """
Bravo! Vous avez complété l’exercice de réchauffement.
  
Si vous voulez refaire la pratique, cliquez sur PRATIQUE.
Si vous voulez commencer le test, cliquez sur TEST.
"""
practiceEndLookup = {  "English" : practiceEndEng, "French" : codecs.decode(practiceEndFr,'utf-8')}
doneLookup = {  "English" : "DONE", "French" : codecs.decode("COMPLETÉ",'utf-8')}
resetLookup = {  "English" : "RESET", "French" : codecs.decode("REFAIRE",'utf-8')}


    
def setupScreen(win, reverse=False):
    sqrVertices = [ [1.2,-1.2], [-1.2,-1.2], [-1.2,1.2], [1.2,1.2] ]
    
    shape = visual.ShapeStim(win,
                   lineColor='blue',
                   lineWidth=2.0, #in pixels
                   fillColor='blue', #beware, with convex shapes this won't work
                   vertices=sqrVertices,#choose something from the above or make your own
                   closeShape=True,#do you want the final vertex to complete a loop with 1st?
                   pos= [-15,12], #the anchor (rotaion and vertices are position with respect to this)
                   interpolate=True,
                   opacity=0.9,
                   name = '0',
                   autoLog=False,
                   autoDraw=True)#this stim changes too much for autologging to be useful

    shape1 = visual.ShapeStim(win,
                   lineColor='blue',
                   lineWidth=2.0, #in pixels
                   fillColor='blue', #beware, with convex shapes this won't work
                   vertices=sqrVertices,#choose something from the above or make your own
                   closeShape=True,#do you want the final vertex to complete a loop with 1st?
                   pos= [-14.5, 1], #the anchor (rotaion and vertices are position with respect to this)
                   interpolate=True,
                   opacity=0.9,
                   name = '1',
                   autoLog=False,
                   autoDraw=True)#this stim changes too much for autologging to be useful

    shape2 = visual.ShapeStim(win,
                   lineColor='blue',
                   lineWidth=2.0, #in pixels
                   fillColor='blue', #beware, with convex shapes this won't work
                   vertices=sqrVertices,#choose something from the above or make your own
                   closeShape=True,#do you want the final vertex to complete a loop with 1st?
                   pos= [-7, -3], #the anchor (rotaion and vertices are position with respect to this)
                   interpolate=True,
                   opacity=0.9,
                   name = '2',
                   autoLog=False,
                   autoDraw=True)#this stim changes too much for autologging to be useful

    shape3 = visual.ShapeStim(win,
                   lineColor='blue',
                   lineWidth=2.0, #in pixels
                   fillColor='blue', #beware, with convex shapes this won't work
                   vertices=sqrVertices,#choose something from the above or make your own
                   closeShape=True,#do you want the final vertex to complete a loop with 1st?
                   pos= [-4,1], #the anchor (rotaion and vertices are position with respect to this)
                   interpolate=True,
                   opacity=0.9,
                   name = '3', 
                   autoLog=False,
                   autoDraw=True)#this stim changes too much for autologging to be useful

    shape4 = visual.ShapeStim(win,
                   lineColor='blue',
                   lineWidth=2.0, #in pixels
                   fillColor='blue', #beware, with convex shapes this won't work
                   vertices=sqrVertices,#choose something from the above or make your own
                   closeShape=True,#do you want the final vertex to complete a loop with 1st?
                   pos= [-2.5,11], #the anchor (rotaion and vertices are position with respect to this)
                   interpolate=True,
                   opacity=0.9,
                   name = '4',
                   autoLog=False,
                   autoDraw=True)#this stim changes too much for autologging to be useful

    shape5 = visual.ShapeStim(win,
                   lineColor='blue',
                   lineWidth=2.0, #in pixels
                   fillColor='blue', #beware, with convex shapes this won't work
                   vertices=sqrVertices,#choose something from the above or make your own
                   closeShape=True,#do you want the final vertex to complete a loop with 1st?
                   pos= [-2,-7], #the anchor (rotaion and vertices are position with respect to this)
                   interpolate=True,
                   opacity=0.9,
                   name = '5',
                   autoLog=False,
                   autoDraw=True)#this stim changes too much for autologging to be useful
    
    shape6 = visual.ShapeStim(win,
                   lineColor='blue',
                   lineWidth=2.0, #in pixels
                   fillColor='blue', #beware, with convex shapes this won't work
                   vertices=sqrVertices,#choose something from the above or make your own
                   closeShape=True,#do you want the final vertex to complete a loop with 1st?
                   pos= [12,0], #the anchor (rotaion and vertices are position with respect to this)
                   interpolate=True,
                   opacity=0.9,
                   name = '6',
                   autoLog=False,
                   autoDraw=True)#this stim changes too much for autologging to be useful

    shape7 = visual.ShapeStim(win,
                   lineColor='blue',
                   lineWidth=2.0, #in pixels
                   fillColor='blue', #beware, with convex shapes this won't work
                   vertices=sqrVertices,#choose something from the above or make your own
                   closeShape=True,#do you want the final vertex to complete a loop with 1st?
                   pos= [15,12], #the anchor (rotaion and vertices are position with respect to this)
                   interpolate=True,
                   opacity=0.9,
                   name = '7',
                   autoLog=False,
                   autoDraw=True)#this stim changes too much for autologging to be useful

    shape8 = visual.ShapeStim(win,
                   lineColor='blue',
                   lineWidth=2.0, #in pixels
                   fillColor='blue', #beware, with convex shapes this won't work
                   vertices=sqrVertices,#choose something from the above or make your own
                   closeShape=True,#do you want the final vertex to complete a loop with 1st?
                   pos= [15,-7], #the anchor (rotaion and vertices are position with respect to this)
                   interpolate=True,
                   opacity=0.9,
                   name = '8',
                   autoLog=False,
                   autoDraw=True)#this stim changes too much for autologging to be useful
    shapes = [shape,shape1,shape2,shape3,shape4,shape5,shape6,shape7,shape8]
    if reverse is True:
        for shape in shapes:
            shape.setFillColor('purple')
            shape.setLineColor('purple')
        return shapes
    else:
        return shapes
#TODO ADD flag for correct response

# generate stim order
def showStim(win,shapes, index, reverse=False):
    # Present Corsi stimuli
    shuffledShapes = random.sample(shapes, 9)
    stimOrder = []
    win.flip()
    core.wait(isi)
    for shape in shuffledShapes[:index]:
        if reverse is True:
            win.flip()
            core.wait(isi)
            shape.opacity = 1
            shape.fillColor = 'green'
            shape.lineColor = 'green'
            win.flip()
            core.wait(isi)
            shape.fillColor = 'purple'
            shape.lineColor = 'purple'
            stimOrder.append(int(shape.name))
            stimOrder.reverse()
        else:
            win.flip()
            core.wait(isi)
            shape.opacity = 1
            shape.fillColor = 'yellow'
            shape.lineColor = 'yellow'
            win.flip()
            core.wait(isi)
            shape.fillColor = 'blue'
            shape.lineColor = 'blue'
            stimOrder.append(int(shape.name))
    return stimOrder

def highlightStim(win, shape, reverse=False):
    
    if reverse is True:
        shape.opacity = 1
        shape.fillColor = 'green'
        shape.lineColor = 'green'
        win.flip()
        core.wait(0.125)
        shape.opacity = 1
        shape.fillColor = 'purple'
        shape.lineColor = 'purple'
    else:
        shape.opacity = 1
        shape.fillColor = 'yellow'
        shape.lineColor = 'yellow'
        win.flip()
        core.wait(0.125)
        shape.opacity = 1
        shape.fillColor = 'blue'
        shape.lineColor = 'blue'

def checkResponse(win, shapes, stimOrder, index, indexHistory, reverse=False):
    mouse = event.Mouse()  #  will use myWin by default
    clock = core.Clock()
    # define a buffer zone around the mouse for proximity detection:
    # use pix units just to show that it works to mix (shape and mouse use norm units)
    bufzone = visual.Circle(win, radius=3, edges=13, units='norm')
    
    #Variable for holding user responses
    responseOrder = []
    trialCorrect = False

    while True:
#        done = False
#        donebutton = visual.ImageStim(win, image='CorsiBlocks/check.png', flipHoriz=False, size=2, pos=(0,-14.50), units='deg')
#        donebutton.draw()
#        if mouse.isPressedIn(donebutton, buttons=[0]) :
#            done = True
        # Handle mouse clicks and record correct responses
        for shape in shapes:
            # dynamic buffer zone around mouse pointer:
            bufzone.pos = mouse.getPos() * win.size / 2  # follow the mouse
            bufzone.size += mouse.getWheelRel()[1] / 20.0  # vert scroll adjusts radius, can go negative
            # is the mouse inside the shape (hovering over it)?
            if shape.contains(mouse):
                #msg.text = 'inside'
                shape.opacity = 1
                bufzone.opacity = 1
                if mouse.isPressedIn(shape, buttons=[0]) :
                    #highlight the stim
                    highlightStim(win,shape,reverse)
                    #Store responses
                    responseOrder.append(int(shape.name))
                    if len(responseOrder) == len(stimOrder):
                        if responseOrder == stimOrder:
                            trialCorrect = True
                            index = index+1
                            return [index, trialCorrect]
                        else:
                            trialCorrect = False
                            index = indexHistory[-1]
                            return [index, trialCorrect]
                    

            elif shape.overlaps(bufzone):
                #msg.text = 'near'
                shape.opacity = 1
                bufzone.opacity = 1
            else:
                #msg.text = 'far away'
                shape.opacity = 1
                bufzone.opacity = 1
            bufzone.draw()  # drawing helps visualize the mechanics
            shape.draw()
        win.flip()

        if event.getKeys(keyList=['escape', 'q']):
            core.quit()
        if event.getKeys(keyList=['s']):
            return
            
#TODO Check if responses matched the stim order
# If correct, advance to new stimOrder
# if wrong, go back in difficulty
def Corsi(win, ask, language, exp, reverse=False, span=0, practice=False):
    runLoop=data.TrialHandler(trialList=[], nReps=span,name='runCorsi',
    method='sequential')
    clock = core.Clock()
    failLookup = {'English': trialFailEn, 'French':codecs.decode(trialFailFr,"utf-8")}
    failText = visual.TextStim(win, text=failLookup[language], pos=(0,0), alignHoriz='center', rgb=(1,1,1), alignVert='bottom')
    #Corsi Forward
    score = 1
    index = 2
    answers = []
    indexHistory = [2]
    trialResult = True
    while index < span and score!=0:
        #Setup the screen with blocks
        shapes = setupScreen(win,reverse)
        #Put buttons on screen
        #buttons = setupButtons(win, language)
        #Hide Mouse
        mouse = event.Mouse(visible=False)
        #Show Corsi Stim
        stimOrder = showStim(win,shapes,index,reverse)
                
        #Show Mouse
        mouse = event.Mouse(visible=True)
        
        
        #check user responses
        nextIndex = checkResponse(win, shapes, stimOrder, index, indexHistory, reverse)[0]
        #done = checkResponse(win, shapes, stimOrder, index, indexHistory, reverse)[2]
        
        #trialResult = checkResponse(win, shapes, stimOrder, index, indexHistory, reverse)[1]
        win.flip()
        
        
        
        index = nextIndex
        indexHistory.append(index)
        runSize = max(sum(1 for _ in l) for n, l in itertools.groupby(indexHistory))
        #if a trial is failed

        if len(indexHistory)==2 and indexHistory[-1]==indexHistory[-2]:
            for shape in shapes:
                shape.setAutoDraw(False)
                failText.draw()
            win.flip()
            core.wait(2)
            score = 1
        elif len(indexHistory)>2 and indexHistory[-1]==indexHistory[-2] and indexHistory[-1]!=indexHistory[-3]:
            win.flip()
            for shape in shapes:
                shape.setAutoDraw(False)
                failText.draw()
            win.flip()
            core.wait(2)
            score = 1
        elif len(indexHistory)>2 and indexHistory[-1]==indexHistory[-2] and indexHistory[-2]==indexHistory[-3]:
            # if 2 consecutive fails end the test
            for shape in shapes:
                shape.setAutoDraw(False)
            #ask(failLookup[language])
            win.flip()
            score = 0
            break
        for shape in shapes:
            shape.setAutoDraw(False)
        win.flip()
    
    if not practice:        
        if reverse:
            exp.addData('Corsi Reverse Span', index-1)
            exp.addData('Task Name', 'Corsi Reverse')
            exp.nextEntry()
        else:
            exp.addData('Corsi Forward', index-1)
            exp.addData('Task Name', 'Corsi Forward Span')
            exp.nextEntry()
    
    return score

    
def runCorsi(win, ask, language, exp, reverse):
    
    #Span length
    span = 9
    streak = 2
    
    
    choicesLookup = {'English':['PRACTICE','START'], 'French':['PRATIQUE', 'TEST']}
    catRatingScale = visual.RatingScale(win, choices=choicesLookup[language], showAccept = False, 
                        singleClick=True, showValue=False)
    myItem = visual.TextStim(win, text=practiceEndLookup[language], color='white')

    event.clearEvents()
    if reverse is True:
        #Corsi Reverse
        instructionsLookup={'English': instructionsRevEng, 'French':instructionsRevFr}
    else:
        instructionsLookup = {'English': instructionsEng, 'French':instructionsFr}
    score = 1
    repeat = 1
    ask(instructionsLookup[language])
    while score!=0:
        score = Corsi(win, ask, language, exp, reverse, span=3, practice=True)
        print score
        event.clearEvents()
        catRatingScale.reset()
        while catRatingScale.noResponse:
            myItem.draw()
            catRatingScale.draw()
            win.flip()
        if catRatingScale.getRating() == 'PRACTICE' or catRatingScale.getRating() == 'PRATIQUE':
            ask(instructionsLookup[language])
            score = 1
        elif catRatingScale.getRating() == 'START' or catRatingScale.getRating() == 'TEST':
            score = 0
    Corsi(win, ask, language, exp, reverse, span,practice=False)