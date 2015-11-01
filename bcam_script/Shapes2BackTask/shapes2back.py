# -*- coding: utf-8 -*-
from __future__ import division
import random, sys
from psychopy import core, event, gui, visual, sound, data, logging
import numpy as np
import scipy.stats as st
import codecs

audioPath = 'files/Ding.wav'

trialShapes = []
trialShapes.append('Shapes2BackTask/files/square.bmp')
trialShapes.append('Shapes2BackTask/files/square.bmp')
trialShapes.append('Shapes2BackTask/files/Hexagon.bmp')
trialShapes.append('Shapes2BackTask/files/bluemountains.bmp')
trialShapes.append('Shapes2BackTask/files/Hexagon.bmp')
trialShapes.append('Shapes2BackTask/files/circle.bmp')
trialShapes.append('Shapes2BackTask/files/Star.bmp')
trialShapes.append('Shapes2BackTask/files/Heart.bmp')
trialShapes.append('Shapes2BackTask/files/Pentagon.bmp')
trialShapes.append('Shapes2BackTask/files/Heart.bmp')
trialShapes.append('Shapes2BackTask/files/Thunder.bmp')
trialShapes.append('Shapes2BackTask/files/Triangle.bmp')
trialShapes.append('Shapes2BackTask/files/DoubleTriangle.bmp')
trialShapes.append('Shapes2BackTask/files/FourPointStar.bmp')
trialShapes.append('Shapes2BackTask/files/Lozenge.bmp')
trialShapes.append('Shapes2BackTask/files/Polygon-1.bmp')
trialShapes.append('Shapes2BackTask/files/Lozenge.bmp')
trialShapes.append('Shapes2BackTask/files/Trapezoid.bmp')
trialShapes.append('Shapes2BackTask/files/Cloud.bmp')
trialShapes.append('Shapes2BackTask/files/Thunder.bmp')
trialShapes.append('Shapes2BackTask/files/circle.bmp')
trialShapes.append('Shapes2BackTask/files/Thunder.bmp')
trialShapes.append('Shapes2BackTask/files/Heart.bmp')
trialShapes.append('Shapes2BackTask/files/FourPointStar.bmp')
trialShapes.append('Shapes2BackTask/files/bluemountains.bmp')
trialShapes.append('Shapes2BackTask/files/FourPointStar.bmp')
trialShapes.append('Shapes2BackTask/files/Heart.bmp')
trialShapes.append('Shapes2BackTask/files/Cloud.bmp')
trialShapes.append('Shapes2BackTask/files/Triangle.bmp')
trialShapes.append('Shapes2BackTask/files/Thunder.bmp')
trialShapes.append('Shapes2BackTask/files/Star.bmp')
trialShapes.append('Shapes2BackTask/files/DoubleTriangle.bmp')
trialShapes.append('Shapes2BackTask/files/Star.bmp')
trialShapes.append('Shapes2BackTask/files/square.bmp')
trialShapes.append('Shapes2BackTask/files/Pentagon.bmp')
trialShapes.append('Shapes2BackTask/files/Lozenge.bmp')
trialShapes.append('Shapes2BackTask/files/Pentagon.bmp')
trialShapes.append('Shapes2BackTask/files/Cloud.bmp')
trialShapes.append('Shapes2BackTask/files/circle.bmp')
trialShapes.append('Shapes2BackTask/files/Thunder.bmp')
trialShapes.append('Shapes2BackTask/files/Heart.bmp')
trialShapes.append('Shapes2BackTask/files/Polygon-1.bmp')
trialShapes.append('Shapes2BackTask/files/Trapezoid.bmp')
trialShapes.append('Shapes2BackTask/files/Hexagon.bmp')
trialShapes.append('Shapes2BackTask/files/Trapezoid.bmp')
trialShapes.append('Shapes2BackTask/files/bluemountains.bmp')
trialShapes.append('Shapes2BackTask/files/Polygon-1.bmp')
trialShapes.append('Shapes2BackTask/files/Thunder.bmp')
trialShapes.append('Shapes2BackTask/files/Star.bmp')
trialShapes.append('Shapes2BackTask/files/Thunder.bmp')
trialShapes.append('Shapes2BackTask/files/Heart.bmp')
trialShapes.append('Shapes2BackTask/files/DoubleTriangle.bmp')
trialShapes.append('Shapes2BackTask/files/Star.bmp')
trialShapes.append('Shapes2BackTask/files/Lozenge.bmp')
trialShapes.append('Shapes2BackTask/files/Polygon-1.bmp')
trialShapes.append('Shapes2BackTask/files/square.bmp')
trialShapes.append('Shapes2BackTask/files/Polygon-1.bmp')
trialShapes.append('Shapes2BackTask/files/Lozenge.bmp')
trialShapes.append('Shapes2BackTask/files/Cloud.bmp')
trialShapes.append('Shapes2BackTask/files/Star.bmp')
trialShapes.append('Shapes2BackTask/files/Trapezoid.bmp')
trialShapes.append('Shapes2BackTask/files/Heart.bmp')
trialShapes.append('Shapes2BackTask/files/bluemountains.bmp')
trialShapes.append('Shapes2BackTask/files/Thunder.bmp')
trialShapes.append('Shapes2BackTask/files/bluemountains.bmp')
trialShapes.append('Shapes2BackTask/files/circle.bmp')
trialShapes.append('Shapes2BackTask/files/FourPointStar.bmp')
trialShapes.append('Shapes2BackTask/files/Lozenge.bmp')
trialShapes.append('Shapes2BackTask/files/Polygon-1.bmp')
trialShapes.append('Shapes2BackTask/files/Lozenge.bmp')
trialShapes.append('Shapes2BackTask/files/Heart.bmp')
trialShapes.append('Shapes2BackTask/files/Pentagon.bmp')
trialShapes.append('Shapes2BackTask/files/Heart.bmp')
trialShapes.append('Shapes2BackTask/files/Trapezoid.bmp')
trialShapes.append('Shapes2BackTask/files/square.bmp')
trialShapes.append('Shapes2BackTask/files/Lozenge.bmp')
trialShapes.append('Shapes2BackTask/files/DoubleTriangle.bmp')
trialShapes.append('Shapes2BackTask/files/bluemountains.bmp')
trialShapes.append('Shapes2BackTask/files/Triangle.bmp')
trialShapes.append('Shapes2BackTask/files/bluemountains.bmp')
trialShapes.append('Shapes2BackTask/files/Cloud.bmp')
trialShapes.append('Shapes2BackTask/files/Thunder.bmp')
trialShapes.append('Shapes2BackTask/files/Star.bmp')
trialShapes.append('Shapes2BackTask/files/Trapezoid.bmp')
trialShapes.append('Shapes2BackTask/files/Star.bmp')
trialShapes.append('Shapes2BackTask/files/FourPointStar.bmp')
trialShapes.append('Shapes2BackTask/files/Trapezoid.bmp')
trialShapes.append('Shapes2BackTask/files/Polygon-1.bmp')
trialShapes.append('Shapes2BackTask/files/Trapezoid.bmp')
trialShapes.append('Shapes2BackTask/files/Lozenge.bmp')
trialShapes.append('Shapes2BackTask/files/Thunder.bmp')
trialShapes.append('Shapes2BackTask/files/DoubleTriangle.bmp')
trialShapes.append('Shapes2BackTask/files/Thunder.bmp')
trialShapes.append('Shapes2BackTask/files/Heart.bmp')
trialShapes.append('Shapes2BackTask/files/Pentagon.bmp')
trialShapes.append('Shapes2BackTask/files/Star.bmp')
trialShapes.append('Shapes2BackTask/files/bluemountains.bmp')
trialShapes.append('Shapes2BackTask/files/Cloud.bmp')
trialShapes.append('Shapes2BackTask/files/square.bmp')
trialShapes.append('Shapes2BackTask/files/Triangle.bmp')
trialShapes.append('Shapes2BackTask/files/DoubleTriangle.bmp')
trialShapes.append('Shapes2BackTask/files/Triangle.bmp')
trialShapes.append('Shapes2BackTask/files/FourPointStar.bmp')
trialShapes.append('Shapes2BackTask/files/cloud.bmp')
trialShapes.append('Shapes2BackTask/files/Lozenge.bmp')
trialShapes.append('Shapes2BackTask/files/square.bmp')
trialShapes.append('Shapes2BackTask/files/circle.bmp')
trialShapes.append('Shapes2BackTask/files/Pentagon.bmp')
trialShapes.append('Shapes2BackTask/files/FourPointStar.bmp')
trialShapes.append('Shapes2BackTask/files/Pentagon.bmp')
trialShapes.append('Shapes2BackTask/files/bluemountains.bmp')
trialShapes.append('Shapes2BackTask/files/polygon-1.bmp')
trialShapes.append('Shapes2BackTask/files/square.bmp')
trialShapes.append('Shapes2BackTask/files/Star.bmp')
trialShapes.append('Shapes2BackTask/files/Cloud.bmp')
trialShapes.append('Shapes2BackTask/files/Thunder.bmp')
trialShapes.append('Shapes2BackTask/files/Triangle.bmp')
trialShapes.append('Shapes2BackTask/files/Trapezoid.bmp')
trialShapes.append('Shapes2BackTask/files/Heart.bmp')
trialShapes.append('Shapes2BackTask/files/Trapezoid.bmp')
trialShapes.append('Shapes2BackTask/files/FourPointStar.bmp')


practiceShapes =[]
practiceShapes.append('Shapes2BackTask/files/square.bmp')
practiceShapes.append('Shapes2BackTask/files/Hexagon.bmp')
practiceShapes.append('Shapes2BackTask/files/square.bmp')
practiceShapes.append('Shapes2BackTask/files/Heart.bmp')
practiceShapes.append('Shapes2BackTask/files/Star.bmp')
practiceShapes.append('Shapes2BackTask/files/Thunder.bmp')
practiceShapes.append('Shapes2BackTask/files/Star.bmp')
practiceShapes.append('Shapes2BackTask/files/Thunder.bmp')
practiceShapes.append('Shapes2BackTask/files/Triangle.bmp')

examplePath = 'Shapes2BackTask/files/example.bmp'

practiceEngT0 = """
Good work! 
Next, you will do another kind of memory test. Pay close attention to 
the instructions.
You will be shown a series of shapes, one at a time in the middle of the screen. 
When each shape appears, you must decide if it is the same shape you saw exactly 
2 shapes before.
"""

practiceEngT1 = """
If the shape you are looking at is the SAME as the shape you saw
2 shapes before,  press the SPACEBAR. If it is not the same, do nothing. 
Here is an example of a sequence of shapes you might see. To help you understand 
we have shown them all in a row, but in the test, they will appear one at a time.
 
In this example, you would press the SPACEBAR when the lightning bolt came up, 
because it is the SAME shape that appeared 2 shapes back. 
You would not press the space bar for the other shapes; each one of them was different than 
the shape that appeared 2 shapes before it.

Are you ready for some practice?
"""

practiceFrT0 = """
Bravo!
Maintenant, nous allons faire une autre sorte de jeu de mémoire. 
Lisez bien/ soyez bien attentif aux/faites bien attention aux  instructions.
Vous allez voir une série de formes, une à la fois, au centre de l’écran. 
Lorsque chaque forme apparaîtra, vous devrez décider si c’est la même que celle que 
vous avez vue exactement 2 formes plus tôt.
"""

practiceFrT1 ="""
Si la forme que vous voyez est exactement la MÊME que la forme que vous avez vu 
deux formes plus tôt, appuyez sur la BARRE D’ESPACEMENT. Si ce n’est pas la même 
forme, ne faites rien.
Voici un exemple de séquence de formes que vous pourriez voir.
D’autres types de formes pourraient aussi apparaitre.
Pour vous aider à comprendre, nous vous montrons toutes les formes sur une ligne, 
mais dans le test, les formes n’apparaissent qu’une à la fois. 

Dans cet exemple, vous devriez appuyer sur la barre d’espacement quand la foudre 
apparaît car c’est la MÊME forme qui est apparue 2 formes plus tôt.  
Vous ne devriez pas appuyer sur la barre d’espacement pour les autres formes; 
chacune est différente de la forme qui est apparue 2 formes avant elle.

Êtes-vous prêt(e) pour une pratique? 
"""
practiceEngT2 = """
Here is another example of a sequence of shapes you might see. 
To help you understand we have shown them all in a row, 
but in the test, they will appear one at a time. 
In this example, you would press the space bar when the [lightning bolt] came up, 
because it is the SAME shape that appeared two shapes back. 
You would not press the space bar for the other shapes; each
is different than the shape that appeared two shapes before it.
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
practiceEndLookup = {  "English" : practiceEndEng, "French" : codecs.decode(practiceEndFr,"utf-8")}

def welcometext(win,ask,language):
    if language == "English":
        ask(practiceEngT0)
    elif language == "French":
        ask(practiceFrT0)
def practice(win,ask,language):
    if language == "English":
        example = visual.ImageStim(win, image=examplePath, units='deg',pos=(0.0, -7.0),size = (25,8)) 
        drawExample = example.draw(win)
        ask(practiceEngT1)
    elif language == "French":
        example = visual.ImageStim(win, image=examplePath, units='deg',pos=(0.0, -7.0),size = (25,8)) 
        drawExample = example.draw(win)
        ask(practiceFrT1)
        
def practiceEnd(win, practiceIndicator, language):
    choicesLookup = {'English':['Redo Practice','Start Task'], 'French':['Oui', 'Non']}
    catRatingScale = visual.RatingScale(win, choices=choicesLookup[language], showAccept = False, 
                        singleClick=True, showValue=False)
    myItem = visual.TextStim(win, text=practiceEndLookup[language], color='white')

    event.clearEvents()
    while catRatingScale.noResponse: # show & update until a response has been made
        myItem.draw()
        catRatingScale.draw()
        practiceIndicator.draw()
        win.flip()
        if event.getKeys(['q','escape']):
            core.quit()
    if catRatingScale.getRating() == 'Redo Practice' or catRatingScale.getRating() == 'Oui':
        score = 1
    elif catRatingScale.getRating() == 'Start Task' or catRatingScale.getRating() == 'Non':
        score = 0
    return score

#timer
RT = core.Clock()

# parameters
numTrials=25
frameRate = 60  # Hz
stimDuration = 1.5  # secs
blankDuration = 0.5  # secs

stimFrames = int(frameRate * stimDuration)
blankFrames = int(frameRate * blankDuration)  # rounds down / floor. 212.5 becomes 212.
totalFrames = stimFrames + blankFrames

def Shapes2Back(win, ask, language, shapes):
    
    event.clearEvents()
    win.setRecordFrameIntervals(True)
    mouse = event.Mouse(visible=False)
    list =[random.randint(0,10) for r in xrange(numTrials)]
    keyList=[]
    responses = ['none'] * len(shapes)
    demoDisp = visual.ImageStim(win, image = shapes[0], units='pix', pos=(0.0, 0.0), size=None) #textstim object that will be displayed
    counter = 0  # Counter is unused?
    for x in range(len(shapes)):
        # PREPARE STIMULUS
        demoDisp.setImage(shapes[x])

        # PRESENT STIMULUS
        for frameN in range(stimFrames):
            # Display stimulus
            demoDisp.draw()
            win.flip()
            RT.reset()
            # Reset timer on onset
            if frameN == 0:
                RT.reset()
            if event.getKeys(['q','escape']):
                core.quit()
            # RECORD RESPONSES
            keyList=event.getKeys(timeStamped=RT)     
            if keyList:
                # keyList[N][Y], N is response number if multiple keys were pressed. Y=0 is key-name. Y=1 is time
                if 'space' in keyList[0][0]:
                    #Play sound when key pressed
                    #filesound = sound.Sound(audioPath)
                    #filesound.setVolume(1.0)
                    #filesound.play()
                    #Save responses
                    responses[x]= keyList[0][0]
                elif keyList == 'q':
                    core.quit()
            else:
                #responses.append('none')
                #No key was pressed
                continue
        
        #if not keyList:
        #    print x
        #    responses.append('none')
        # PRESENT BLANK
        for frameN in range(blankFrames):
            # Blank screen with no response recording
            RT.reset()
            win.flip()
        
        if event.getKeys(['q','escape']):
            core.quit()
    print 'Shapes 2Back task finished...' 
    return responses
    
    
def accuracyCalculation(win,correctResponse, userResponse):
    # Log responses
    accurateResponses = [i for i, j in zip(userResponse, correctResponse) if i == j]
    accuracy = np.divide(float(len(accurateResponses)),float(len(correctResponse)))
    indicator = visual.Circle(win, radius=0.5,edges=64)
    indicator.pos = (12,9)
    if accuracy > 0.8:
        indicator.fillColor  = 'LimeGreen'
        indicator.lineColor = 'LimeGreen'
    elif accuracy > 0.7 and accuracy < 0.8:
        indicator.fillColor  = 'yellow'
        indicator.lineColor = 'yellow'
    else:
        indicator.fillColor  = 'yellow'
        indicator.lineColor = 'yellow'
    return accuracy, indicator

def listCompare(correctResponse, userResponse):
    corrLen = len(correctResponse)
    #matches = [i for i, j in zip(userResponse, correctResponse) if i == j]
    matches = [x for x in correctResponse if x in userResponse]
    omission = len(correctResponse) - len(matches)
    rate = len(matches)/len(correctResponse)
    d = st.norm.ppf(rate)
    zScore = st.norm.cdf(d)
    #hitRate = np.divide(float(len(matches)),float(len(correctResponse)))
    return omission,rate,zScore
 
    
def runShapes2Back(win, ask, language,exp):
    #
    # Practice run
    #
    practiceEndLookup = {  "English" : practiceEndEng, "French" : codecs.decode(practiceEndFr,"utf-8")}
    correctPractice = ['none', 'none', 'space', 'none', 'none', 'none', 'space', 'space', 'none'] #Practice Accuracy
    score = 1
    welcometext(win,ask,language)
    while score != 0:
        mouse = event.Mouse(visible=False)
        practice(win,ask, language) # Practice text
        practiceResults = Shapes2Back(win, ask, language, practiceShapes) #Run practice trial
        practiceAccuracy = accuracyCalculation(win,correctPractice,practiceResults)[0] #calculate accuracy
        practiceIndicator = accuracyCalculation(win,correctPractice,practiceResults)[1] #show the indicator
        score = practiceEnd(win, practiceIndicator, language) #Show the rating scale
    
    correctHit = [i for i, x in enumerate(correctPractice) if x == 'space']
    correctMiss = [i for i, x in enumerate(correctPractice) if x == 'none']
    userHit = [i for i, x in enumerate(practiceResults) if x == 'space']
    omissionError = listCompare(correctHit,userHit)[0]
    hitRate = listCompare(correctHit,userHit)[1]
    falseAlarm = listCompare(correctMiss,userHit)[1]
    zScoreHit = listCompare(correctHit,userHit)[2]
    zScoreFalseAlarm = listCompare(correctMiss,userHit)[2]
    
    dPrime =  zScoreHit - zScoreFalseAlarm
    
    #Change this calculation
    exp.addData('S2Back Omission error', omissionError)
    exp.addData('S2Back Hit Rate', hitRate)
    exp.addData('S2Back False Alarm', falseAlarm)
    exp.addData('S2Back d-Prime', dPrime)
    exp.addData('Task Name', 'Shapes 2 Back Practice')
    exp.nextEntry()
    #
    # Actual Run
    #
    correctTrial = ['none','none','none','space','none','none','none','none','space',
    'none','none','space','none','none','none','space','none','none','none','none',
    'space','none','none','none','none','none','none','none','none','none','none','space',
    'none','none','none','space','none','none','none','none','none','none','none','space',
    'none','none','none','none','space','none','none','none','none','none','none','space',
    'none','none','none','none','none','none','none','space','none','none','none','none',
    'space','none','none','space','none','none','none','none','none','none','space','none',
    'none','none','none','space','none','none','none','none','space','none','none','space','none',
    'none','none','none','none','none','none','none','space','none','none','none','none','none',
    'none','none','space','none','none','none','none','none','none','none','none','none','space','none'] #Trial Accuracy
    
    trialResults = Shapes2Back(win, ask, language, trialShapes) #Run practice trial
    trialAccuracy = accuracyCalculation(win,correctTrial,trialResults)[0] #calculate accuracy
    trialIndicator = accuracyCalculation(win,correctTrial,trialResults)[1]
    mouse = event.Mouse(visible=False)
    correctHit = [i for i, x in enumerate(correctTrial) if x == 'space']
    correctMiss = [i for i, x in enumerate(correctTrial) if x == 'none']
    userHit = [i for i, x in enumerate(trialResults) if x == 'space']
    omissionError = listCompare(correctHit,userHit)[0]
    hitRate = listCompare(correctHit,userHit)[1]
    falseAlarm = listCompare(correctMiss,userHit)[1]
    
    zScoreHit = listCompare(correctHit,userHit)[2]
    zScoreFalseAlarm = listCompare(correctMiss,userHit)[2]
    
    dPrime =  zScoreHit - zScoreFalseAlarm
    
    trialIndicator.draw(win)
    exp.addData('S2Back Omission error', omissionError)
    exp.addData('S2Back Hit Rate', hitRate)
    exp.addData('S2Back False Alarm', falseAlarm)
    exp.addData('S2Back d-Prime', dPrime)
    exp.addData('Task Name', 'Shapes 2 Back')
    exp.nextEntry()
    if event.getKeys(['q']):
        core.quit()