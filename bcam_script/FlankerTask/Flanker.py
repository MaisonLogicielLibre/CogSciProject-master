#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This is the Flanker Experiment
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import codecs

temp_congruent_rt_list = []
temp_incongruent_rt_list = []
congruent_stimuli = ["CongruentLeft.bmp","CongruentRight.bmp"]
incongruent_stimuli = ["IncongruentLeft.bmp","IncongruentRight.bmp"]
practiceTrials = 3
numTrialReps = 1
posFingerEng = """
The next game also tests your reaction time.
First, position your index fingers on the arrow keys as shown:
"""
posFingerFr = """
Le prochain jeu teste aussi votre vitesse de réaction.
Tout d’abord, veuillez placer vos index sur les 
TOUCHES FLÈCHES du clavier, tel que représenté :
"""
flankerInstEng = """

At the start of each trial, focus your eyes on the cross that 
appears in the middle of the screen.
Then you will see a row of 5 arrows on the screen.







You must decide if the MIDDLE arrow points to the left or to the right.
If the MIDDLE arrow points to the left, press the LEFT ARROW KEY.
If the MIDDLE arrow points to the right, press the RIGHT ARROW KEY.
It is IMPORTANT to press the key AS FAST AS YOU CAN.

Are you ready for some practice?
"""
flankerInstFr = """

Au début de chaque essai,  veuillez fixer la croix qui se trouvera au centre de l’écran.
Vous verrez ensuite une rangée de 5 flèches à l'écran.




Vous devrez décider si la flèche du MILIEU pointe vers la gauche ou vers la droite.
Si la flèche du MILIEU pointe vers la gauche, appuyez sur la TOUCHE FLÈCHE GAUCHE.
Si la flèche du MILIEU pointe vers la droite, appuyez sur la TOUCHE FLÈCHE DROITE.
C’est IMPORTANT d’appuyer sur la flèche LE PLUS RAPIDEMENT POSSIBLE.

Êtes-vous prêt(e)s pour un peu de pratique?
"""

flankerInst2Eng = """
You must decide if the MIDDLE arrow points to the left or to the right.
If the MIDDLE arrow points to the left, press the LEFT ARROW KEY.
If the MIDDLE arrow points to the right, press the RIGHT ARROW KEY.
It is IMPORTANT to press the key AS FAST AS YOU CAN.

Are you ready for some practice?
"""

flankerInst2Fr = """
Vous devez décider si la flèche du MILIEU pointe vers la gauche ou la droite.
Si la flèche du MILIEU pointe vers la gauche, appuyez sur la TOUCHE FLÈCHE GAUCHE.
Si la flèche du MILIEU pointe vers la droite, appuyez sur la TOUCHE FLÈCHE DROITE.
C’est IMPORTANT d’appuyer sur la flèche LE PLUS RAPIDEMENT POSSIBLE.

Êtes-vous prêt pour un peu de pratique?
"""
continueEng = """
Good job! You have completed the practice.

If you would like more practice, click on PRACTICE.
If you are ready to start the task, click on START.
"""

continueFr = """
Bravo! Vous avez complété l’exercice de réchauffement.
  
Si vous voulez refaire la pratique, cliquez sur PRATIQUE.
Si vous voulez commencer le test, cliquez sur TEST.
"""
readyEn = """
Get ready
"""
readyFr = """
Soyez prêts
"""
readyLookup = {'English':readyEn, 'French':codecs.decode(readyFr,"utf-8")}
def redoPractice(language):
    if language == 'English':
        return continueEng
    elif language == 'French':
        return codecs.decode(continueFr,"utf-8")
        
def positionFinger(win, ask, language):
    fingerImgPath = 'FlankerTask/Example.jpg'
    if language == 'English':
        """The Text""" 
        finger = visual.SimpleImageStim(win, image=fingerImgPath, units='norm',pos=(0.0, -0.2)) 
        drawFinger = finger.draw(win)
        ask(posFingerEng)
    elif language == 'French':
        """The Text""" 
        finger = visual.ImageStim(win, image=fingerImgPath, units='norm',pos=(0.0, -0.2)) 
        drawFinger = finger.draw(win)
        ask(posFingerFr)
        return

def practiceAsk(ask, image, language):
    if language == 'English':
        """The Text"""
        image.draw()
        ask(flankerInstEng)
    elif language == 'French':
        """The Text""" 
        image.draw()
        ask(flankerInstFr)
        return
        
def practiceEnd(win, practiceIndicator, language):
    practiceEndLookup = {  "English" : continueEng, "French" : codecs.decode(continueFr,"utf-8")}
    choicesLookup = {'English':['PRACTICE','START'], 'French':['PRATIQUE', 'TEST']}
    catRatingScale = visual.RatingScale(win, choices=choicesLookup[language],showAccept = False, 
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
    if catRatingScale.getRating() == 'PRACTICE' or catRatingScale.getRating() == 'PRATIQUE':
        score = 1
    elif catRatingScale.getRating() == 'START' or catRatingScale.getRating() == 'TEST':
        score = 0
    return score
    
def accuracyCalculation(win,correctResponse, userResponse):
    # Log responses
    if userResponse is not None:
        accurateResponses = [i for i, j in zip(userResponse, correctResponse) if i == j]
        accuracy = np.divide(float(len(accurateResponses)),float(len(correctResponse)))
    else:
        accuracy = 0
    indicator = visual.Circle(win, radius=0.5,edges=64)
    indicator.pos = (12,9)
    if accuracy > 0.7:
        indicator.fillColor  = 'LimeGreen'
        indicator.lineColor = 'LimeGreen'
    elif accuracy > 0.4 and accuracy < 0.7:
        indicator.fillColor  = 'yellow'
        indicator.lineColor = 'yellow'
    else:
        indicator.fillColor  = 'yellow'
        indicator.lineColor = 'yellow'
    return accuracy, indicator
    
def runFlanker(win, expDict,ask,language, exp):
    # Store info about the experiment session
    expName = 'flanker'  # from the Builder filename that created this script
    expInfo = {u'session': expDict[1], u'participant': expDict[0]}
    #dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
    #if dlg.OK == False: core.quit()  # user pressed cancel
    expInfo['date'] = data.getDateStr()  # add a simple timestamp
    expInfo['expName'] = expName

    # Setup filename for saving
    filename = u'FlankerTask'+os.path.sep+ 'data' + os.path.sep + '%s_%s' %(expInfo['participant'], expInfo['date'])

    # An ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath=None,
        savePickle=True, saveWideText=True,
        dataFileName=filename)
    #save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

    endExpNow = False  # flag for 'escape' or other condition => quit the exp

    # Start Code - component code to be run before the window creation

    # store frame rate of monitor if we can measure it successfully
    expInfo['frameRate']=win.getActualFrameRate()
    if expInfo['frameRate']!=None:
        frameDur = 1.0/round(expInfo['frameRate'])
    else:
        frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

    # Initialize components for Routine "apres01"
    firstClock = core.Clock()

    # Show how to position fingers
    positionFinger(win, ask,language)
    
    

    #Initialize fixation cross
    fixations = visual.TextStim(win=win, text='+', height=5, alignHoriz='center', rgb=(1,1,1), alignVert='center')
    
    image = visual.ImageStim(win=win, name='image',units='deg',
        image='FlankerTask/arrowexample.bmp', mask=None,
        ori=0, pos=[0, 5], size=[15, 3],
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-1.0)
    
    #Ask if they want to practice
    practiceResponse = practiceAsk(ask, image,language)
    
    if language == 'English':
        text = visual.TextStim(win=win, ori=0, name='text',
            text= flankerInstEng,    font='Arial',
            pos=[0, 4], height = 1, wrapWidth=999,
            color='white', colorSpace='rgb', opacity=1,
            depth=0.0)
    elif language == 'French':
        text = visual.TextStim(win=win, ori=0, name='text',
            text= codecs.decode(flankerInstFr,"utf-8"),    font='Arial',
            pos=[0, 4], height = 1, wrapWidth=999,
            color='white', colorSpace='rgb', opacity=1,
            depth=0.0)


    # Initialize components for Routine "train"
    trainClock = core.Clock()
    imgTr = visual.ImageStim(win=win, name='imgTr',units='pix',
        image='sin', mask=None,
        ori=0, pos=[0, 0], size=[769, 145],
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-1.0)

    # Initialize components for Routine "fbPractice"
    fbPracticeClock = core.Clock()
    imgPractice2 = ''
    somResposta2 = ''
    corretos2 = 0
    imageFBtrain = visual.ImageStim(win=win, name='imageFBtrain',units='pix',
        image='sin', mask=None,
        ori=0, pos=[0, 0],
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-2.0)
    somFb02 = sound.Sound('A', secs=1.9)
    somFb02.setVolume(0.5)


    # Initialize components for Routine "After Practice"
    secondClock = core.Clock()
    text_3 = visual.TextStim(win=win, ori=0, name='text_3',
        text= redoPractice(language),    font='Arial',
        pos=[0, 0], height=1, wrapWidth=999,
        color='white', colorSpace='rgb', opacity=1,
        depth=0.0)


    # Initialize components for Routine "trFlanker"
    trFlankerClock = core.Clock()
    imgTrial = visual.ImageStim(win=win, name='imgTrial',units='pix',
        image='sin', mask=None,
        ori=0, pos=[0, 0], size=[769,145],
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-1.0)

    # Initialize components for Routine "wait"
    waitClock = core.Clock()
    text_10 = visual.TextStim(win=win, ori=0, name='text_10',
        text=None,    font='Arial',
        pos=[0, 0], height=1, wrapWidth=None,
        color='white', colorSpace='rgb', opacity=1,
        depth=0.0)

    # Initialize components for Routine "thanks"
    thanksClock = core.Clock()
    text_8 = visual.TextStim(win=win, ori=0, name='text_8',
        text='Thank you for participating \n\n\n\nPress the space bar to complete.',    font='Arial',
        pos=[0, 0], height=1, wrapWidth=None,
        color='white', colorSpace='rgb', opacity=1,
        depth=0.0)
    sound_1 = sound.Sound('FlankerTask/hit.wav', secs=10)
    sound_1.setVolume(0.5)

    # Create some handy timers
    globalClock = core.Clock()  # to track the time since experiment started
    routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine

    #------Prepare to start Routine "apres01"-------
    t = 0
    firstClock.reset()  # clock
    frameN = -1
    # update component parameters for each repeat
    keyResp01 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    keyResp01.status = NOT_STARTED
    # keep track of which components have finished
    apres01Components = []
    apres01Components.append(text)
    apres01Components.append(image)
    apres01Components.append(keyResp01)
    for thisComponent in apres01Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "apres01"-------
    continueRoutine = True
    score = 1
    ready = visual.TextStim(win, text=readyLookup[language], color='white')
    while score!=0:
        ready.draw()
        win.flip()
        core.wait(2)
        
        while continueRoutine:
            # get current time
            t = firstClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *text* updates
            if t >= 0.0 and text.status == NOT_STARTED:
                # keep track of start time/frame for later
                text.tStart = t  # underestimates by a little under one frame
                text.frameNStart = frameN  # exact frame index
                #text.setAutoDraw(True)


            # *image* updates
            if t >= 0.0 and image.status == NOT_STARTED:
                # keep track of start time/frame for later
                image.tStart = t  # underestimates by a little under one frame
                image.frameNStart = frameN  # exact frame index
                #image.setAutoDraw(True)

            # *keyResp01* updates
            if t >= 0.0 and keyResp01.status == NOT_STARTED:
                # keep track of start time/frame for later
                keyResp01.tStart = t  # underestimates by a little under one frame
                keyResp01.frameNStart = frameN  # exact frame index
                keyResp01.status = STARTED
                # keyboard checking is just starting
                event.clearEvents(eventType='keyboard')
            if keyResp01.status == STARTED:
                theseKeys = ['space']

                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    # a response ends the routine
                    continueRoutine = False

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in apres01Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
            else:  # this Routine was not non-slip safe so reset non-slip timer
                routineTimer.reset()



        #-------Ending Routine "apres01"-------
        for thisComponent in apres01Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)

        # set up handler to look after randomisation of conditions etc
        trainblue = data.TrialHandler(nReps=practiceTrials, method='random',
            extraInfo=expInfo, originPath=None,
            trialList=data.importConditions('FlankerTask/trialList.csv'),
            seed=None, name='practice')
        thisExp.addLoop(trainblue)  # add the loop to the experiment
        thisPracticeblue = trainblue.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb=thisPracticeblue.rgb)
        if thisPracticeblue != None:
            for paramName in thisPracticeblue.keys():
                exec(paramName + '= thisPracticeblue.' + paramName)
    
        for thisPracticeblue in trainblue:
            currentLoop = trainblue
            # abbreviate parameter names if possible (e.g. rgb = thisPracticeblue.rgb)
            if thisPracticeblue != None:
                for paramName in thisPracticeblue.keys():
                    exec(paramName + '= thisPracticeblue.' + paramName)

            #------Prepare to start Routine "train"-------
            t = 0
            trainClock.reset()  # clock
            frameN = -1
            routineTimer.add(0.000000)
            # update component parameters for each repeat
            imgTr.setImage('FlankerTask/'+nomeImg)
            keyPractice = event.BuilderKeyResponse()  # create an object of type KeyResponse
            keyPractice.status = NOT_STARTED
            # keep track of which components have finished
            trainComponents = []
            #trainComponents.append(trainBackground)
            trainComponents.append(imgTr)
            trainComponents.append(keyPractice)
            for thisComponent in trainComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED

            #-------Start Routine "train"-------
            continueRoutine = True
            
            while continueRoutine and routineTimer.getTime()>0:
                # get current time
                t = trainClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame

                # *backgroundPractice* updates
                if t >= 0.0 and fixations.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    fixations.tStart = t  # underestimates by a little under one frame
                    fixations.frameNStart = frameN  # exact frame index
                    fixations.draw()
                elif fixations.status == STARTED and t >= (0.0 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
                    fixations.setAutoDraw(False)

                # *imgTr* updates
                if t >= 0.5 and imgTr.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    imgTr.tStart = t  # underestimates by a little under one frame
                    imgTr.frameNStart = frameN  # exact frame index
                    imgTr.setAutoDraw(True)
                elif imgTr.status == STARTED and t >= (0.5 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
                    imgTr.setAutoDraw(False)

                # *keyPractice* updates
                if t >= 0.5 and keyPractice.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    keyPractice.tStart = t  # underestimates by a little under one frame
                    keyPractice.frameNStart = frameN  # exact frame index
                    keyPractice.status = STARTED
                    # keyboard checking is just starting
                    keyPractice.clock.reset()  # now t=0
                    event.clearEvents(eventType='keyboard')
                elif keyPractice.status == STARTED and t >= (0.5 + (7.5-win.monitorFramePeriod*0.75)): #most of one frame period left
                    keyPractice.status = STOPPED
                if keyPractice.status == STARTED:
                    theseKeys = event.getKeys(keyList=['left', 'right'])

                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        keyPractice.keys = theseKeys[-1]  # just the last key pressed
                        keyPractice.rt = keyPractice.clock.getTime()
                        # was this 'correct'?
                        if (keyPractice.keys == str(respCorr)) or (keyPractice.keys == respCorr):
                            keyPractice.corr = 1
                        else:
                            keyPractice.corr = 0
                        # a response ends the routine
                        continueRoutine = False

                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineTimer.reset()  # if we abort early the non-slip timer needs reset
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trainComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished

                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()

                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
                

            #-------Ending Routine "train"-------
            for thisComponent in trainComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if keyPractice.keys in ['', [], None]:  # No response was made
               keyPractice.keys=None
               # was no response the correct answer?!
               if str(respCorr).lower() == 'none': keyPractice.corr = 1  # correct non-response
               else: keyPractice.corr = 0  # failed to respond (incorrectly)
            # store data for trainblue (TrialHandler)
            trainblue.addData('keyPractice.keys',keyPractice.keys)
            trainblue.addData('keyPractice.corr', keyPractice.corr)
            if keyPractice.keys != None:  # we had a response
                trainblue.addData('keyPractice.rt', keyPractice.rt)

            #------Prepare to start Routine "fbPractice"-------
            t = 0
            fbPracticeClock.reset()  # clock
            frameN = -1
            routineTimer.add(2.000000)
            # update component parameters for each repeat
            if keyPractice.corr:
                corretos2 = corretos2 + 1
            else:
                corretos2 = 0
            # keep track of which components have finished      
            fbPracticeComponents = []
            for thisComponent in fbPracticeComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED

            #-------Start Routine "fbPractice"-------
            continueRoutine = True
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = fbPracticeClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame

                # *backgroundPractice2* updates
                if t >= 0.0 and fixations.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    fixations.tStart = t  # underestimates by a little under one frame
                    fixations.frameNStart = frameN  # exact frame index
                    fixations.draw()
                elif fixations.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                    fixations.setAutoDraw(False)


                # *imageFBtrain* updates
                if t >= 0.0 and imageFBtrain.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    imageFBtrain.tStart = t  # underestimates by a little under one frame
                    imageFBtrain.frameNStart = frameN  # exact frame index
                    imageFBtrain.setAutoDraw(True)
                elif imageFBtrain.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                    imageFBtrain.setAutoDraw(False)

                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineTimer.reset()  # if we abort early the non-slip timer needs reset
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in fbPracticeComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished

                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()

                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()

            #-------Ending Routine "fbPractice"-------
            for thisComponent in fbPracticeComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)

            thisExp.nextEntry()
            
        # completed 2 repeats of 'trainblue'

        #------Prepare to start Routine "wait"-------
        t = 0
        waitClock.reset()  # clock
        frameN = -1
        routineTimer.add(0.800000)
        # update component parameters for each repeat
        # keep track of which components have finished
        waitComponents = []
        waitComponents.append(text_10)
        for thisComponent in waitComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        #-------Start Routine "wait"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = waitClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *text_10* updates
            if t >= 0.0 and text_10.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_10.tStart = t  # underestimates by a little under one frame
                text_10.frameNStart = frameN  # exact frame index
                text_10.setAutoDraw(True)
            elif text_10.status == STARTED and t >= (0.0 + (0.8-win.monitorFramePeriod*0.75)): #most of one frame period left
                text_10.setAutoDraw(False)

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in waitComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

            if event.getKeys(['y']): #restart practice session if user presses 'y'
                continueRoutine = True
        
        
        #-------Ending Routine "wait"-------
        for thisComponent in waitComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)

        #------Prepare to start Routine "apres02"-------
        t = 0
        secondClock.reset()  # clock
        frameN = -1
        # update component parameters for each repeat
        key_resp_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
        key_resp_3.status = NOT_STARTED
        # keep track of which components have finished
        apres02Components = []
        apres02Components.append(text_3)
        apres02Components.append(key_resp_3)
        for thisComponent in apres02Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        #-------Start Routine "apres02"-------
#        continueRoutine = True
#        while continueRoutine:
#            # get current time
#            t = secondClock.getTime()
#            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
#            # update/draw components on each frame
#
#            # *text_3* updates
#            if t >= 1 and text_3.status == NOT_STARTED:
#                # keep track of start time/frame for later
#                text_3.tStart = t  # underestimates by a little under one frame
#                text_3.frameNStart = frameN  # exact frame index
#                text_3.setAutoDraw(True)
#
#            # *key_resp_3* updates
#            if t >= 0.0 and key_resp_3.status == NOT_STARTED:
#                # keep track of start time/frame for later
#                key_resp_3.tStart = t  # underestimates by a little under one frame
#                key_resp_3.frameNStart = frameN  # exact frame index
#                key_resp_3.status = STARTED
#                # keyboard checking is just starting
#                event.clearEvents(eventType='keyboard')
#            if key_resp_3.status == STARTED:
#                theseKeys = event.getKeys(keyList=['space'])
#
#                # check for quit:
#                if "escape" in theseKeys:
#                    endExpNow = True
#                if len(theseKeys) > 0:  # at least one key was pressed
#                    # a response ends the routine
#                    continueRoutine = False
#
#            # check if all components have finished
#            if not continueRoutine:  # a component has requested a forced-end of Routine
#                routineTimer.reset()  # if we abort early the non-slip timer needs reset
#                break
#            continueRoutine = False  # will revert to True if at least one component still running
#            for thisComponent in apres02Components:
#                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
#                    continueRoutine = True
#                    break  # at least one component has not yet finished
#
#            # check for quit (the Esc key)
#            if endExpNow or event.getKeys(keyList=["escape"]):
#                core.quit()
#
#            # refresh the screen
#            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
#                win.flip()
#            else:  # this Routine was not non-slip safe so reset non-slip timer
#                routineTimer.reset()
#
#        #-------Ending Routine "apres02"-------
#        for thisComponent in apres02Components:
#            if hasattr(thisComponent, "setAutoDraw"):
#                thisComponent.setAutoDraw(False)
        
        # Rating scale for practice repeat
        practiceIndicator = accuracyCalculation(win,correctResponse=respCorr, userResponse=keyPractice.keys)[1]
        score = practiceEnd(win,practiceIndicator, language)

    # set up handler to look after randomisation of conditions etc
    expblue = data.TrialHandler(nReps=numTrialReps, method='sequential',
        extraInfo=expInfo, originPath=None,
        trialList=data.importConditions('FlankerTask/fullList.csv'),
        seed=None, name='Flanker Task')
    thisExp.addLoop(expblue)  # add the loop to the experiment
    thisExpblue = expblue.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisExpblue.rgb)
    if thisExpblue != None:
        for paramName in thisExpblue.keys():
            exec(paramName + '= thisExpblue.' + paramName)

    for thisExpblue in expblue:
        currentLoop = expblue
        # abbreviate parameter names if possible (e.g. rgb = thisExpblue.rgb)
        if thisExpblue != None:
            for paramName in thisExpblue.keys():
                exec(paramName + '= thisExpblue.' + paramName)

        #------Prepare to start Routine "trFlanker"-------
        t = 0
        trFlankerClock.reset()  # clock
        frameN = -1
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        imgTrial.setImage('FlankerTask/'+nomeImg)
        keyTA = event.BuilderKeyResponse()  # create an object of type KeyResponse
        keyTA.status = NOT_STARTED
        # keep track of which components have finished
        trFlankerComponents = []
        #trFlankerComponents.append(backgroundT1)
        trFlankerComponents.append(imgTrial)
        trFlankerComponents.append(keyTA)
        for thisComponent in trFlankerComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        #-------Start Routine "trFlanker"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trFlankerClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *backgroundT1* updates
            if t >= 0.0 and fixations.status == NOT_STARTED:
                # keep track of start time/frame for later
                fixations.tStart = t  # underestimates by a little under one frame
                fixations.frameNStart = frameN  # exact frame index
                fixations.draw()
            elif fixations.status == STARTED and t >= (0.0 + (3.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                fixations.setAutoDraw(False)

            # *imgTrial* updates
            if t >= 0.5 and imgTrial.status == NOT_STARTED:
                # keep track of start time/frame for later
                imgTrial.tStart = t  # underestimates by a little under one frame
                imgTrial.frameNStart = frameN  # exact frame index
                imgTrial.setAutoDraw(True)
            elif imgTrial.status == STARTED and t >= (0.5 + (2.5-win.monitorFramePeriod*0.75)): #most of one frame period left
                imgTrial.setAutoDraw(False)

            # *keyTA* updates
            if t >= 0.5 and keyTA.status == NOT_STARTED:
                # keep track of start time/frame for later
                keyTA.tStart = t  # underestimates by a little under one frame
                keyTA.frameNStart = frameN  # exact frame index
                keyTA.status = STARTED
                # keyboard checking is just starting
                keyTA.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            elif keyTA.status == STARTED and t >= (0.5 + (2.5-win.monitorFramePeriod*0.75)): #most of one frame period left
                keyTA.status = STOPPED
            if keyTA.status == STARTED:
                theseKeys = event.getKeys(keyList=['left', 'right'])

                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    keyTA.keys = theseKeys[-1]  # just the last key pressed
                    keyTA.rt = keyTA.clock.getTime()
                    # was this 'correct'?
                    if (keyTA.keys == str(respCorr)) or (keyTA.keys == respCorr):
                        keyTA.corr = 1
                    else:
                        keyTA.corr = 0
                    # a response ends the routine
                    continueRoutine = False

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trFlankerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        #-------Ending Routine "trFlanker"-------
        for thisComponent in trFlankerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if keyTA.keys in ['', [], None]:  # No response was made
           keyTA.keys=None
           # was no response the correct answer?!
           if str(respCorr).lower() == 'none': keyTA.corr = 1  # correct non-response
           else: keyTA.corr = 0  # failed to respond (incorrectly)
        # store data for expblue (TrialHandler)

        if nomeImg in congruent_stimuli and keyTA.corr == 1:
            if keyTA.rt > 0.15:
                temp_congruent_rt_list.append(keyTA.rt)
        elif nomeImg in incongruent_stimuli and keyTA.corr == 1:
            if keyTA.rt > 0.15:
                temp_incongruent_rt_list.append(keyTA.rt)





        expblue.addData('keyTA.keys',keyTA.keys)
        expblue.addData('keyTA.corr', keyTA.corr)
        if keyTA.keys != None:  # we had a response
            expblue.addData('keyTA.rt', keyTA.rt)
        thisExp.nextEntry()

    # completed 5 repeats of 'expblue'

    # Calculate median RT and  Flanker Effect
    flanker_congruent_rt_median = np.median(temp_congruent_rt_list)
    flanker_incongruent_rt_median = np.median(temp_incongruent_rt_list)
    flanker_congruent_rt_var = np.var(temp_congruent_rt_list)
    flanker_incongruent_rt_var = np.var(temp_incongruent_rt_list)
    flanker_effect = flanker_incongruent_rt_median - flanker_congruent_rt_median
    #Save all results
    exp.addData('Flanker_Cong RT',flanker_congruent_rt_median)
    exp.addData('Flanker_Inc RT',flanker_incongruent_rt_median)
    exp.addData('Flanker_Cong RT Var',flanker_congruent_rt_var)
    exp.addData('Flanker_Cong RT Var',flanker_incongruent_rt_var)
    exp.addData('RT Flanker Effect',flanker_effect)
    exp.addData('Task Name', 'Flanker')

    exp.nextEntry()

    #------Prepare to start Routine "wait"-------
    t = 0
    waitClock.reset()  # clock
    frameN = -1
    routineTimer.add(0.800000)
    # update component parameters for each repeat
    # keep track of which components have finished
    waitComponents = []
    waitComponents.append(text_10)
    for thisComponent in waitComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "wait"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = waitClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *text_10* updates
        if t >= 0.0 and text_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_10.tStart = t  # underestimates by a little under one frame
            text_10.frameNStart = frameN  # exact frame index
            text_10.setAutoDraw(True)
        elif text_10.status == STARTED and t >= (0.0 + (0.8-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_10.setAutoDraw(False)

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in waitComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    #-------Ending Routine "wait"-------
    for thisComponent in waitComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)




    #------Prepare to start Routine "wait"-------
    t = 0
    waitClock.reset()  # clock
    frameN = -1
    routineTimer.add(0.800000)
    # update component parameters for each repeat
    # keep track of which components have finished
    waitComponents = []
    waitComponents.append(text_10)
    for thisComponent in waitComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "wait"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = waitClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *text_10* updates
        if t >= 0.0 and text_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_10.tStart = t  # underestimates by a little under one frame
            text_10.frameNStart = frameN  # exact frame index
            text_10.setAutoDraw(True)
        elif text_10.status == STARTED and t >= (0.0 + (0.8-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_10.setAutoDraw(False)

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in waitComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    #-------Ending Routine "wait"-------
    for thisComponent in waitComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)




    #------Prepare to start Routine "wait"-------
    t = 0
    waitClock.reset()  # clock
    frameN = -1
    routineTimer.add(0.800000)
    # update component parameters for each repeat
    # keep track of which components have finished
    waitComponents = []
    waitComponents.append(text_10)
    for thisComponent in waitComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "wait"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = waitClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *text_10* updates
        if t >= 0.0 and text_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_10.tStart = t  # underestimates by a little under one frame
            text_10.frameNStart = frameN  # exact frame index
            text_10.setAutoDraw(True)
        elif text_10.status == STARTED and t >= (0.0 + (0.8-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_10.setAutoDraw(False)

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in waitComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    #-------Ending Routine "wait"-------
    for thisComponent in waitComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)


    #------Prepare to start Routine "wait"-------
    t = 0
    waitClock.reset()  # clock
    frameN = -1
    routineTimer.add(0.800000)
    # update component parameters for each repeat
    # keep track of which components have finished
    waitComponents = []
    waitComponents.append(text_10)
    for thisComponent in waitComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "wait"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = waitClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *text_10* updates
        if t >= 0.0 and text_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_10.tStart = t  # underestimates by a little under one frame
            text_10.frameNStart = frameN  # exact frame index
            text_10.setAutoDraw(True)
        elif text_10.status == STARTED and t >= (0.0 + (0.8-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_10.setAutoDraw(False)

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in waitComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    #-------Ending Routine "wait"-------
    for thisComponent in waitComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    #------Prepare to start Routine "thanks"-------
    t = 0
    thanksClock.reset()  # clock
    frameN = -1
    # update component parameters for each repeat
    key_resp_7 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_7.status = NOT_STARTED
    # keep track of which components have finished
    thanksComponents = []
    thanksComponents.append(text_8)
    thanksComponents.append(sound_1)
    thanksComponents.append(key_resp_7)
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "thanks"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = thanksClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *text_8* updates
        if t >= 0.0 and text_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_8.tStart = t  # underestimates by a little under one frame
            text_8.frameNStart = frameN  # exact frame index
            text_8.setAutoDraw(True)

        # *key_resp_7* updates
        if t >= 0.0 and key_resp_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_7.tStart = t  # underestimates by a little under one frame
            key_resp_7.frameNStart = frameN  # exact frame index
            key_resp_7.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if key_resp_7.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])

            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in thanksComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()

    #-------Ending Routine "thanks"-------
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)



    win.flip(clearBuffer=True)