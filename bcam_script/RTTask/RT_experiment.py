# -*- coding: utf-8 -*-

# ==========================
# RT_experiment.py
# ==========================
"""
Present an image  randomly,
press a key asap,
measure response time.
(press 'q' to quit)
"""
import numpy as np
import os
import codecs
from psychopy import visual, sound, event, core, data, logging
import random, time

keysBreak = [' ', 'space']  # Keys to accept at regular break
keysQuit = ['q','escape']  # Keys that quits the experiment
keySkip = ['s'] #keys that skip trial
keyBack = ['b'] # key to go back

# Some function shortcuts for dual monitor presentations
def draw(x):
    x.draw()

def flip(x):
    x.flip()

def close(x):
    x.close()
    
study_info={} #this dict will contain the important study info as the experiment progresses
practicetrials = 5
trials = 40
clock = core.Clock() # make a clock for capturing RT (reaction time)
sqrVertices = [ [3,-3], [-3,-3], [-3,3], [3,3] ]

RTLeftEng = """
Good job! Now we will test your reaction time. 

Place the index finger of your LEFT hand on the middle of the SPACEBAR. 
Your task is to press the space bar as quickly as possible after a RED SQUARE 
is flashed on the screen.

At the start of each trial, focus your eyes on the cross that appears in 
the middle of the screen. A RED SQUARE will then appear in the same place.
As soon as you see the RED SQUARE, press the spacebar as fast as you can.

It is an error if you press the SPACE BAR before the RED SQUARE appears.

Try to respond as quickly as possible.
Are you ready to try some practice?
"""

RTRightEng = """
Place the index finger of your RIGHT hand on the middle of the SPACEBAR. 
Your task is to press the space bar as quickly as possible after a RED SQUARE 
is flashed on the screen.

At the start of each trial, focus your eyes on the cross that appears in 
the middle of the screen. A RED SQUARE will then appear in the same place.
As soon as you see the RED SQUARE, press the spacebar as fast as you can.

It is an error if you press the SPACE BAR before the RED SQUARE appears.

Try to respond as quickly as possible.
Are you ready to try some practice?
"""
RTLeftFr = """Bravo! Maintenant, nous allons tester votre vitesse de réaction.

Placez l'index de votre main GAUCHE sur le milieu de la BARRE D’ESPACEMENT.
Votre tâche est d’appuyer sur la BARRE D’ESPACEMENT  le plus rapidement 
possible quand le CARRÉ ROUGE apparaît à l’écran.  

Au début de chaque essai,  veuillez fixer la croix qui se trouvera/apparait
au milieu de l’écran.  Un carré rouge apparaîtra à cet endroit.  
Aussitôt que vous verrez le CARRÉ ROUGE, appuyez sur la BARRE D’ESPACEMENT 
le plus rapidement possible. 

Veuillez éviter d’appuyer sur la BARRE D’ESPACEMENT avant que le CARRÉ ROUGE n’apparaîsse, 
car cela sera compté comme étant une erreur. 

Essayez de répondre le plus rapidement possible.
Êtes-vous prêt(e)s pour un peu de pratique?
"""

RTRightFr = """
Bravo! Maintenant, nous allons tester votre vitesse de réaction.

Placez l'index de votre main DROITE sur le milieu de la BARRE D’ESPACE.
Votre tâche est d’appuyer sur la BARRE D’ESPACE  le plus rapidement 
possible quand le CARRÉ ROUGE apparaît à l’écran.  

Au début de chaque essai,  veuillez fixer la croix qui se trouvera/apparait
au milieu de l’écran.  Un carré rouge apparaîtra à cet endroit.  
Aussitôt que vous verrez le CARRÉ ROUGE, appuyez sur la BARRE D’ESPACEMENT 
le plus rapidement possible. 

Veuillez éviter d’appuyer sur la BARRE D’ESPACEMENT avant que le CARRÉ ROUGE n’apparaîsse, 
car cela sera compté comme étant une erreur. 

Essayez de répondre le plus rapidement possible.
Êtes-vous prêt(e)s pour un peu de pratique?

"""
practiceEng = """
First let's start with a few practice trials

Press the R to return to instruction
"""

practiceFr = """
D’abord, commençons par un exercice de réchauffement.

Appuyer sur la touche 'R' pour retourner aux instructions.
"""

practiceEndEng = """
Good job! You have completed the practice.

Would you like more practice, or are you

Ready to start?
"""

practiceEndFr = """
Bravo! Vous avez complété l’exercice de réchauffement.
  
Si vous désirez retourner à la pratique, cliquez sur PRATIQUE.

Si vous désirez commencer le test, cliquez sur TEST.
"""
 
errorTooSoonEng = """
PRESSED TOO SOON
"""
errorTooSoonFr = """
VOUS AVEZ APPUYÉ TROP TÔT
"""

getReadyEng = """
Get ready!
"""

getReadyFr = """
Êtes-vous prêt?
"""

wrongkeyEng = """
Wrong Key
"""

wrongkeyFr = """
Mauvaise Touche
"""
def practiceEnd(win,language):
    choicesLookup = {'English':['PRACTICE','START'], 'French':['PRATIQUE', 'TEST']}
    catRatingScale = visual.RatingScale(win, choices=choicesLookup[language], acceptKeys='space',showAccept = False, 
                        singleClick=True, showValue=False)
    myItem = visual.TextStim(win, text=codecs.decode(practiceEndLookup[language],"utf-8"), color='white')

    event.clearEvents()
    while catRatingScale.noResponse: # show & update until a response has been made
        myItem.draw()
        catRatingScale.draw()
        win.flip()
        if event.getKeys(['escape']):
            core.quit()
    if catRatingScale.getRating() == 'PRACTICE' or catRatingScale.getRating() == 'PRATIQUE':
        score = 1
    elif catRatingScale.getRating() == 'START' or catRatingScale.getRating() == 'TEST':
        score = 0
    return score
    


lookup = { "A" : { "English" : {"Right" : RTRightEng,
                                          "Left"  : RTLeftEng
                                          }, 
                            "French" : {"Right" : RTRightFr,
                                         "Left" : RTLeftFr
                                         }
                            },
            "B" : { "English" : {"Right" : RTRightEng,
                                          "Left"  : RTLeftEng
                                          }, 
                            "French" : {"Right" : RTRightFr,
                                         "Left" : RTLeftFr
                                         }
                            },
            "C" : { "English" : {"Right" : RTRightEng,
                                          "Left"  : RTLeftEng
                                          }, 
                            "French" : {"Right" : RTRightFr,
                                         "Left" : RTLeftFr
                                         }
                            }
            } 
practiceLookup = {  "English" : practiceEng, "French" : practiceFr}
practiceEndLookup = {  "English" : practiceEndEng, "French" : practiceEndFr}
lookupError = { "English" : errorTooSoonEng, "French" : errorTooSoonFr}
lookupGetReady = { "English" : getReadyEng, "French" : getReadyFr}
lookupwrongKey = { "English" : wrongkeyEng, "French" : wrongkeyFr}

audioPath = 'files/Ding.wav'
filesound = sound.Sound(audioPath)
filesound.setVolume(1.0)

def run(window,clock, ask, error, getReady,wrongkey,language, exp,practice=False):
    filename =  u'RTTask'+ os.path.sep + exp.dataFileName
    #logging.console.setLevel(logging.DEBUG)
    expRT = data.ExperimentHandler(name='BCAM',
                             version='0.3',
                             extraInfo={},
                             runtimeInfo=None,
                             originPath=None,
                             savePickle=False,
                             saveWideText=True,
                             dataFileName=filename)
    #temp RT variable
    temp_RT_List = []
    if practice is not True:
        stimColor = 'red'
        numTrials = trials
    elif practice is True:
        stimColor = 'red'
        numTrials = practicetrials
    # Stimulus Image to be presented
    stim2 = visual.ShapeStim(
                     win=window, 
                     lineColor=stimColor,
                     lineWidth=1.0, #in pixels
                     fillColor=stimColor, #beware, with convex shapes this won't work
                     fillColorSpace='rgb',
                     vertices=sqrVertices,#choose something from the above or make your own
                     closeShape=True,#do you want the final vertex to complete a loop with 1st?
                     pos= [0.0,0.0], #the anchor (rotaion and vertices are position with respect to this)
                     interpolate=True,
                     opacity=1,
                     autoLog=False)#this stim changes too much for autologging to be useful               

    # Fixations for ISI's
    fixations = visual.TextStim(window, text='+', height=5, alignHoriz='center', rgb=(1,1,1), alignVert='center')
    wrongKeyPress = visual.TextStim(window, text=lookupwrongKey[language].decode('utf-8'), pos=(0,0), alignHoriz='center', rgb=(1,1,1), alignVert='bottom')
    earlyKeyPress = visual.TextStim(window, text=lookupError[language].decode('utf-8'), pos=(0,0), alignHoriz='center', rgb=(1,1,1), alignVert='bottom',wrapWidth=999)
    getReadyKeyPress = visual.TextStim(window, text=lookupGetReady[language].decode('utf-8'), pos=(0,0), alignHoriz='center', rgb=(1,1,1), alignVert='bottom')
    runLoop=data.TrialHandler(trialList=[], nReps=numTrials,name='runRT',
    method='sequential')
    #exp.addLoop(runLoop)

    for trial in runLoop:
        event.clearEvents() #clear everything before starting
        #Hide Mouse
        mouse = event.Mouse(visible=False)
        clock.reset()
        #let's draw a stimulus for 2s, drifting for middle 0.5s
        while clock.getTime() < 1.0 and runLoop.thisRepN == 0:  # clock times are in seconds
            flip(window)
            getReadyKeyPress.draw()            
        flip(window)
        draw(fixations)
        flip(window)
        clock.reset()
        core.wait(1 + random.random()) #have uncertain wait time before trial begins.
        if 'space' in event.getKeys():
            earlyKeyPress.draw()
            flip(window)
        elif 'space' not in event.getKeys() and len(event.getKeys()) > 0:
            wrongKeyPress.draw()
            flip(window)
        else:
            stim2.draw()
            flip(window)
        
        clock.reset() # reaction time starts immediately after window flips
        
        study_info['responses'] = responses = event.waitKeys(maxWait=1, timeStamped=clock)
        # initially, set the Reaction Time to None for no reactions given (for potential catch trials in real study script).
        study_info['reaction time'] = theRT = ''

        # Unpack allKeys, taking the first keypress
        if responses is not None:
            if 'space' in responses[0][0]:
                #Play sound when key pressed   
                filesound.play()
                theKey = responses[0][0]
                theRT = responses[0][1]
                if theRT > 0.15 and theRT<3:
                    temp_RT_List.append(theRT)
                expRT.addData('resp.rt', theRT)
                expRT.addData('resp.key', theKey)
                #end of trial - move to next line in data output
                expRT.nextEntry()
            elif 'q' or'escape' in responses[0][0]:
                exp.abort()
                print 'Program aborted...'
                core.quit()
                runLoop.finished = True
                break
            elif 's' in responses[0][0]:
                print "Skipped experiment"
                runLoop.finished = True
                return
            else:
                wrongKeyPress.draw()
                flip(window)
                core.wait(0.5)
        else:
            if practice is not True:
                theKey = 'None'
                theRT = 'NA'
                expRT.addData('resp.rt', theRT)
                expRT.addData('resp.key', theKey)
                #end of trial - move to next line in data output
                expRT.nextEntry()
                #wrongKeyPress.draw()
                #flip(window)
                #core.wait(0.5)
                continue
            else:
                #wrongKeyPress.draw()
                #flip(window)
                #core.wait(0.5)
                continue
    
    simple_rt_median = np.median(temp_RT_List)
    simple_rt_mean = np.mean(temp_RT_List)
    simple_rt_std = np.var(temp_RT_List)
    sizeofRTList = []
    for rt in temp_RT_List:
        if rt > 3*simple_rt_std:
            sizeofRTList.append(rt)
    if practice is not True:
        exp.addData('#RT\'s >3 STD',len(sizeofRTList))
        #end of trial - move to next line in data output
        #add RT median
        exp.addData('Simple RT_Median', simple_rt_median)
        exp.addData('Simple RT_Mean', simple_rt_mean)
        exp.addData('Simple RT STD', simple_rt_std)
        exp.addData('Task Name', 'Reaction Time')
        #move to next line in data output
        exp.nextEntry()
        window.flip()
        return
    if practice is not True:
        print 'Reaction Time task finished...'
    elif practice is True:
        return practiceEnd(window,language)
    
    if event.getKeys(keyList=['escape', 'q']):
        core.quit()
    if event.getKeys(keyList=['s']):
        print "Skipped experiment"
        return

def runRT(window,ask,test,language,preferred_hand,exp):
    try:
        while True:
            ask(lookup[test][language][preferred_hand])
            response = ask(practiceLookup[language])
            if event.getKeys(keyList=['escape', 'q']):
                core.quit()
            if 'r' in response:
                print 'r pressed'
                continue
            if 'space' in response:
                break
            if event.getKeys(keyList=['s']):
                print "Skipped experiment"
                return
            
        getReady = lookupGetReady[language]
        error = lookupError[language]
        wrongkey = lookupwrongKey[language]

        score=1
        while score != 0:
            score = run(window,clock, ask, error,getReady,wrongkey,language, exp,practice=True)
            print score
        #Run experiment
        run(window,clock, ask, error,getReady,wrongkey,language,exp)
    except KeyboardInterrupt:
        raise
        core.quit()