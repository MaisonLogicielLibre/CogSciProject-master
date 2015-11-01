# -*- coding: utf-8 -*-
from __future__ import division
import random, sys
from psychopy import core, event, gui, sound, visual, data, logging
import numpy as np
import scipy.stats as st
import codecs
#logging.console.setLevel(logging.DEBUG)

audioPath = 'files/Ding.wav'

trialLetters = []
trialLetters.append('m')
trialLetters.append('b')
trialLetters.append('q')
trialLetters.append('h')
trialLetters.append('c')
trialLetters.append('o')
trialLetters.append('x')
trialLetters.append('u')
trialLetters.append('x')
trialLetters.append('l')
trialLetters.append('w')
trialLetters.append('e')
trialLetters.append('w')
trialLetters.append('j')
trialLetters.append('s')
trialLetters.append('t')
trialLetters.append('v')
trialLetters.append('d')
trialLetters.append('v')
trialLetters.append('k')
trialLetters.append('g')
trialLetters.append('p')
trialLetters.append('z')
trialLetters.append('p')
trialLetters.append('i')
trialLetters.append('a')
trialLetters.append('s')
trialLetters.append('r')
trialLetters.append('u')
trialLetters.append('f')
trialLetters.append('u')
trialLetters.append('p')
trialLetters.append('h')
trialLetters.append('o')
trialLetters.append('h')
trialLetters.append('w')
trialLetters.append('j')
trialLetters.append('r')
trialLetters.append('e')
trialLetters.append('d')
trialLetters.append('g')
trialLetters.append('d')
trialLetters.append('c')
trialLetters.append('q')
trialLetters.append('b')
trialLetters.append('t')
trialLetters.append('b')
trialLetters.append('i')
trialLetters.append('k')
trialLetters.append('a')
trialLetters.append('s')
trialLetters.append('x')
trialLetters.append('s')
trialLetters.append('v')
trialLetters.append('m')
trialLetters.append('z')
trialLetters.append('l')
trialLetters.append('a')
trialLetters.append('g')
trialLetters.append('a')
trialLetters.append('z')
trialLetters.append('w')
trialLetters.append('z')
trialLetters.append('h')
trialLetters.append('p')
trialLetters.append('l')
trialLetters.append('r')
trialLetters.append('m')
trialLetters.append('t')
trialLetters.append('j')
trialLetters.append('q')
trialLetters.append('k')
trialLetters.append('o')
trialLetters.append('k')
trialLetters.append('x')
trialLetters.append('f')
trialLetters.append('d')
trialLetters.append('f')
trialLetters.append('a')
trialLetters.append('s')
trialLetters.append('e')
trialLetters.append('u')
trialLetters.append('p')
trialLetters.append('u')
trialLetters.append('x')
trialLetters.append('i')
trialLetters.append('v')
trialLetters.append('z')
trialLetters.append('c')
trialLetters.append('k')
trialLetters.append('o')
trialLetters.append('l')
trialLetters.append('d')
trialLetters.append('l')
trialLetters.append('u')
trialLetters.append('b')
trialLetters.append('j')
trialLetters.append('m')
trialLetters.append('r')
trialLetters.append('e')
trialLetters.append('t')
trialLetters.append('a')
trialLetters.append('t')
trialLetters.append('g')
trialLetters.append('w')
trialLetters.append('h')
trialLetters.append('p')
trialLetters.append('h')
trialLetters.append('q')
trialLetters.append('f')
trialLetters.append('s')
trialLetters.append('f')
trialLetters.append('h')
trialLetters.append('w')
trialLetters.append('j')
trialLetters.append('q')
trialLetters.append('v')
trialLetters.append('q')
trialLetters.append('a')
trialLetters.append('d')
trialLetters.append('k')
trialLetters.append('d')


practiceLetters =[]
practiceLetters.append('b')
practiceLetters.append('r')
practiceLetters.append('i')
practiceLetters.append('h')
practiceLetters.append('g')
practiceLetters.append('h')
practiceLetters.append('a')
practiceLetters.append('n')
practiceLetters.append('a')

examplePath = 'Letters2Back/files/example.bmp'

practiceEngT0 = """
Good work! 
Next, you will do another kind of memory test. Pay close attention to 
the instructions.
You will be shown a series of letters, one at a time in the middle of the screen. 
When each letter appears, you must decide if it is the same letter you saw exactly 
2 letters before.
"""

practiceEngT1 = """
If the letter you are looking at is the SAME as the letter you saw
2 letters before,  press the SPACEBAR. If it is not the same, do nothing. 
Here is an example of a sequence of letters you might see. To help you understand 
we have shown them all in a row, but in the test, they will appear one at a time.
 
In this example, you would press the spacebar when the letter A comes up, 
because it is the SAME letter that appeared 2 letters back. 
You would not press the spacebar for the other letters; each one of them was different than 
the letter that appeared 2 letters before it.

Are you ready for some practice?
"""

practiceFrT0 = """
Bravo!
Maintenant, nous allons faire une autre sorte de test de mémoire. 
 Lisez bien/ soyez bien attentif aux/faites bien attention aux instructions.
Vous allez voir une série de lettres, une à la fois, au centre de l’écran. 
Lorsque chaque lettre apparaîtra, vous devrez décider si c’est la même que celle que 
vous avez vue exactement 2 lettres plus tôt.
"""

practiceFrT1 ="""
Si la  lettre que vous voyez est exactement la MÊME que la lettre que vous avez vue 
deux lettres plus tôt, appuyez sur la BARRE D’ESPACEMENT. Si ce n’est pas la même 
lettre, ne faites rien.
Voici un exemple de séquence de lettres que vous pourriez voir.
Pour vous aider à comprendre, nous vous montrons toutes les lettres sur une ligne, 
mais dans le test, les lettres n’apparaitront qu’une à la fois. 

Dans cet exemple, vous devriez appuyer sur la barre d’espacement quand la lettre ??
apparaît car c’est la MÊME lettre qui est apparue 2 lettres plus tôt.  
Vous ne devriez pas appuyer sur la barre d’espacement pour les autres lettres; 
chacune est différente de la lettre qui est apparue 2 lettres avant elle.

Êtes-vous prêt(e)s pour une pratique?  
"""
practiceEngT2 = """
Here is another example of a sequence of letters you might see. 
To help you understand we have shown them all in a row, 
but in the test, they will appear one at a time. 
In this example, you would press the space bar when the [lightning bolt] came up, 
because it is the SAME shape that appeared 2 letters back. 
You would not press the space bar for the other letters; each
is different than the letter that appeared 2 letters before it.
"""
practiceEndEng = """
Good job! You have completed the practice.

Would you like more practice, or are you
Ready to start?
"""

practiceEndFr = """
Bravo! Vous avez complété l’exercice de réchauffement.
  
Avez-vous besoin de plus de pratique, ou êtes-vous
prêt à commencer? 
"""

practiceEndLookup = {  "English" : practiceEndEng, "French" : codecs.decode(practiceEndFr,"utf-8")}

def welcometext(win,ask,language):
    if language == "English":
        ask(practiceEngT0)
    elif language == "French":
        ask(practiceFrT0)
def practice(win,ask,language):
    if language == "English":
        example = visual.ImageStim(win, image=examplePath, units='deg',pos=(0.0, -7.0),size = (25,6)) 
        drawExample = example.draw(win)
        ask(practiceEngT1)
    elif language == "French":
        example = visual.ImageStim(win, image=examplePath, units='deg',pos=(0.0, -7.0),size = (25,6)) 
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
        if event.getKeys(['escape']):
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

def Letters2Back(win, ask, language, letters):
    
    event.clearEvents()
    win.setRecordFrameIntervals(True)
    mouse = event.Mouse(visible=False)
    list =[random.randint(0,10) for r in xrange(numTrials)]
    #list = [2,3,2,3,2,3,2,3,4,5,6,7,8,9,8]
    keyList=[]
    responses = responses = ['none'] * len(letters)
    demoDisp = visual.TextStim(win, text = letters[0], height = 4, pos=(0.0, 0.0)) #textstim object that will be displayed
    counter = 0  # Counter is unused?
    for x in range(len(letters)):
        # PREPARE STIMULUS
        demoDisp.setText(letters[x])

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
                    print responses
                elif keyList == 'q':
                    core.quit()
            else:
                #responses.append('none')
                #No key was pressed
                continue
        #if not keyList:
         #   responses.append('none')

        # PRESENT BLANK
        for frameN in range(blankFrames):
            # Blank screen with no response recording
            RT.reset()
            win.flip()
        if event.getKeys(['q']):
            core.quit()
    
    print 'Letters 2Back task finished...' 
    return responses
    
    
def accuracyCalculation(win,correctResponse, userResponse):
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
    
def runLetters2Back(win, ask, language,exp):
    #
    # Practice run
    #
    practiceEndLookup = {  "English" : practiceEndEng, "French" : codecs.decode(practiceEndFr,"utf-8")}
    correctPractice = ['none', 'none', 'none', 'none', 'none', 'space', 'none', 'none', 'space'] #Practice Accuracy
    welcometext(win,ask,language)
    score = 1
    while score != 0:
        mouse = event.Mouse(visible=False)
        practice(win,ask, language) # Practice text
        practiceResults = Letters2Back(win, ask, language, practiceLetters) #Run practice trial
        practiceAccuracy = accuracyCalculation(win,correctPractice,practiceResults)[0] #calculate accuracy
        practiceIndicator = accuracyCalculation(win,correctPractice,practiceResults)[1]
        score = practiceEnd(win, practiceIndicator, language)
        
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
    exp.addData('L2Back Omission error', omissionError)
    exp.addData('L2Back Hit Rate', hitRate)
    exp.addData('L2Back False Alarm', falseAlarm)
    exp.addData('L2Back d-Prime', dPrime)
    exp.addData('Task Name', 'Letters 2 Back Practice')
    exp.nextEntry()
    #
    # Actual Run
    #
    correctTrial = ['none','none','none','none','none','none','none','none','space',
    'none','none','none','space','none','none','none','none','none','space','none',
    'none','none','none','space','none','none','none','none','none','none','space','none',
    'none','none','space','none','none','none','none','none','none','space','none','none',
    'none','none','space','none','none','none','none','none','space','none','none','none',
    'none','none','none','space','none','none','space','none','none','none','none','none',
    'none','none','none','none','none','space','none','none','none','space','none','none',
    'none','none','none','space','none','none','none','none','none','none','none','none',
    'none','space','none','none','none','none','none','none','none','none','space','none',
    'none','none','none','space','none','none','none','space','none','none','none','none',
    'none','space','none','none','none','space'] #Trial Accuracy
    trialResults = Letters2Back(win, ask, language, trialLetters) #Run practice trial
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
    exp.addData('L2Back Omission error', omissionError)
    exp.addData('L2Back Hit Rate', hitRate)
    exp.addData('L2Back False Alarm', falseAlarm)
    exp.addData('L2Back d-Prime', dPrime)
    exp.addData('Task Name', 'Letters 2 Back')
    exp.nextEntry()
    if event.getKeys(['q']):
        core.quit()