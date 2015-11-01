# -*- coding: utf-8 -*-
""" 
THE EXPERIMENT:
This is a battery of cognitive tests.
 
FEATURES OF THE SCRIPT:
The important thing is that this experiment incorporates most features that
experiments will use:
    * Initial dialogue box
    * Display messages and ask questions to participants (intro, instructions,
      per-trial-questions etc.). Records reaction time. Also pauses at
      regular intervals of trials.
    * Nice control of blocks and conditions. Easy to run conditions in multiple
      orders to counterbalance possible order effects.
    * Accurate timing of stimulus presentation (by monitor frames instead of
      milliseconds) and assessment of this timing. Read why this is important
      here: 
      Also accurate timing of keyboard responses.
    * Use eye-degrees as units of visual size.
    * Save data after each trial to minimize data loss in the event of a crash.
    * Easily scalable to complex experiments.
 
CODE STRATEGY / PHILOSOPHY
The general coding strategy is to prepare absolutely everything before the
critical data-collection part begins. The purpose is to minimize computational
load and complexity during the actual presentation of the stimuli. As such,
lag and potential errors is minimized prevented during stimulus presentation.
Most of the stuff is done before the welcome screen even hits the participant.
Only a little is left to be done before each trial (change relevant
stimulus parameters for this trial) and this is done before the timing critical
part.
 
Another general coding strategy is to keep stuff-you-or-others-might-change-often
in dedicated sections. This is the VARIABLES and the RUN EXPERIMENT sections.
This is the stuff that you would usually report in your method's section
(like the ISI, number of trials, question text, sequence of blocks etc.).
The philosophy is to keep function and "content" separate so that you (and
others) may easily adapt the experiment without having to scroll down through
the code to change these variables in a lot of obscure places.
 
 
CODE STRUCTURE:
The overall code structure of this template goes like this:
    * VARIABLES: variables pertaining to trials and stimulus presentation.
    * IMPORT the python modules to be used. The python convention is to import in
      the beginning of the script.
    * DIALOGUE AND STIMULI: Initiate psychopy stimuli and handy variables. This is
      computationally heavy.
    * FUNCTIONS: Define functions that does all the stimulus presentation.
    * RUN EXPERIMENT: actually execute the experiment, with the instructions and
      blocks in any order you'd like.
 
"""
 
 
"""
SET VARIABLES
"""

# Fixes issue where you can't change the selection in the dialog box dropdown
import pyglet
import codecs
pyglet.options['shadow_window'] = False

# General variables
monDistance = 60                 # Distance between subject's eyes and monitor
monWidth = 50                    # Width of your monitor in cm
monitorSizePix = [1440, 900]     # Pixel-dimensions of your monitor
saveFolder = 'data'               # Log is saved to this folder. The folder is created if it does not exist.
study_info={}
 
# Questions and messages
messagePos = [0, 3]  # [x, y]
messageHeight = 1  # Height of the text, still in degrees visual angle
textBreak = 'Press SPACE to continue...'  # text of regular break
keysBreak = [' ', 'space']  # Keys to accept at regular break
keysRepeat = ['r']
keysQuit = ['q']  # Keys that quits the experiment
keySkip = ['s'] #keys that skip trial
keyBack = ['b'] # key to go back

preTrialEng = """
Before we start:

Please turn off all cellphones.

Place the 'Do not disturb' sign on the door

Please turn off all electronic devices, yours and the participant's.
"""
preTrialFr = """
Avant de commencer:

Éteindre la sonnerie du téléphone.

Mettre le signe `Ne pas déranger` sur la porte.

Éteindre tous les appareils électroniques, les vôtres et ceux du participant.
"""

preTrialEng = """
Before we start:

Please turn off all cellphones.

Place the 'Do not disturb' sign on the door

Please turn off all electronic devices, yours and the participant's.
"""
preTrialFr = """
Avant de commencer, veuillez :

Éteindre la sonnerie du téléphone.

Placer le signe `Ne pas déranger` sur la porte.

Éteindre tous les appareils électroniques, les vôtres et ceux du participant.
"""

engInstruct = """
    I'm going to ask you to complete several tasks on the computer and on paper.  
    
    If you are not used to computers, don't worry, 
    it will be taken into account and you will have practice exercises. 
    Some tasks may seem really easy for you and others may seem difficult. 
    
    Most people do not answer all the questions or finish every item, 
    but please try to do your best. 
    
    Do you have any questions?
    
    Are you ready to start?
"""

frInstruct = """
    Je vais vous demander de compléter plusieurs 
    tâches à l'ordinateur et sur papier.
    
    Si vous n'êtes pas habitué(e)s aux ordinateurs, 
    ne vous inquiétez pas, nous allons en tenir compte et il y aura des exercices de pratique.  

    Certaines tâches vont vous sembler faciles, d'autres difficiles. 
    
    La plupart des personnes ne répondent pas à toutes les questions ou ne finissent pas tous les items.  
    
    Veuillez essayer de faire de votre mieux.
    Avez-vous des questions ?
    Êtes-vous prêt(e)s à  commencer ?
"""

textInstruct = """
    Press LEFT if the lines are horizontal.
    Press RIGHT if the lines are vertical.
 
    Keep your gaze at the cross at all times."""
    
TitleLetterEng = """
Let's start with a few checks
"""
TitleLetterEng2 = """
What is the letter on the screen?
"""
TitleLetterFr = """
Commençons par quelques vérifications
"""
TitleLetterFr2 = """
Quelle est la lettre inscrite à  l'écran?
"""
ArrowTitleEng = """
Is the middle arrow pointing right or left?
"""
ArrowTitleFr = """
Est-ce que la flèche du milieu pointe vers la gauche ou vers la droite?
"""
AudioTitleEng = """
Can you hear this?

Press R to repeat or SPACE to continue
"""
AudioTitleFr = """
Entendez-vous cela?

Appuyer sur R pour répéter ou sur la BARRE D’ESPACEMENT pour continuer
"""

closingEng = """
That's it for today.  

Thank you very much for your participation.  

Please do not share the content of this test; doing so may decrease its usefulness for others.

Have a nice day!

Thanks to Roger Bourassa and Jim Connell for lending us their voices!
"""
closingFr = """
Voilà , c'est tout pour aujourd'hui.  

Merci beaucoup pour votre participation.  
S'il-vous-plaît, ne partagez pas le contenu de ce test; 
ça le rendrait moins utile pour les autres 

Bonne journée!

Merci à  Denis Bernard pour nous avoir prêté sa voix!
"""
spaceEn = """
[PRESS SPACE BAR TO CONTINUE]
"""
spaceFr = """
[Appuyer sur la BARRE D’ESPACEMENT pour continuer]
"""
spaceLookup = {'English':spaceEn, 'French':spaceFr}
"""
 SHOW DIALOGUE AND INITIATE PSYCHOPY STIMULI
 This is computationally heavy stuff. Thus we do it in the beginning of our experiment
"""
# 
#Imports
#
import collections
#Import Questionnaire
from Questions import questions
# Import Reaction Time Experiment
from RTTask import RT_experiment
# Import Memory Test
from MemoryTask import Memory
# Import Corsi Block test
from CorsiBlocks import corsiTask
# #Import Memory Recall
from MemoryRecallTask import MemoryRecall
#Import Shapes2Back test
from Shapes2BackTask import shapes2back
#Import Letters2Back test
from Letters2Back import letters2back
#Import Letters3Back test
from Letters3Back import letters3back
#Import Flanker Task
from FlankerTask import Flanker
#Import Verbal Fluency
from VerbalFluencyTask import verbalFluency
#Import Trails task
#from TrailsTask import trails2
from psychopy import event
from psychopy import core, visual, gui, monitors, sound, data, logging
import random
import os

#Splash Screen
#import splash
#splash.runSplashScreen()

# Intro-dialogue. Get subject-id and other variables.
# Save input variables in "V" dictionary (V for "variables") 

V = collections.OrderedDict({'subject': '1', 'language':['English','French'],'Form':['A','B','C'],
'preferred hand':['Right', 'Left'], 'group':'BCAM','ExpVersion': 0.3,
'Pre-Trial': True,
'Reaction Time': True,
'Memory':True,
'Corsi Blocks Forward':True,
'Corsi Blocks Reverse':True,
'Flanker': True,
'Memory Recall': True,
'Shapes 2-Back':True,
'Letters 2-Back':True,
'Letters 3-Back':True,
'Verbal Fluency': True})

myDlg = gui.DlgFromDict(V, title='Positive Brain Now Experiment', order=['ExpVersion', 'group','subject','Form', 'language', 'preferred hand',
'Pre-Trial','Reaction Time', 'Memory', 'Flanker','Corsi Blocks Forward','Corsi Blocks Reverse', 'Memory Recall','Shapes 2-Back', 'Letters 2-Back','Letters 3-Back', 'Verbal Fluency'],
tip={'subject': 'Subject\'s ID number'},
fixed=['ExpVersion','group'])

if not myDlg.OK:
    core.quit()

# Parameterize conditions   
subject = myDlg.data[2]
test = myDlg.data[3] 
language = myDlg.data[4]
preferred_hand = myDlg.data[5]

# parameterize tasks
pre_trial = myDlg.data[6]
reaction_time = myDlg.data[7]
memory = myDlg.data[8]
flanker = myDlg.data[9]
corsi_forward = myDlg.data[10]
corsi_reverse = myDlg.data[11]
memory_recall = myDlg.data[12]
shapes_2_back = myDlg.data[13]
letters_2_back = myDlg.data[14]
letters_3_back = myDlg.data[15]
verbal_fluency = myDlg.data[16]
#trails = myDlg.data[17]

flanker_info = [myDlg.data[1],subject]

# Store info about the experiment session
expName = 'BCAM'  # from the Builder filename that created this script
expInfo = {'Subject': subject,'Language':language,'Session':test, 'Handedness':preferred_hand}
#dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
#if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Setup filename for saving
filename = u'data' + os.path.sep + 'Subject_%s' %(expInfo['Subject']) + os.path.sep +'RESULTS_%s_%s_%s' %(expInfo['Subject'], expInfo['date'],test)

# An ExperimentHandler isn't essential but helps with data saving
exp = data.ExperimentHandler(name=expName, version='0.3',
                                 extraInfo=expInfo, runtimeInfo=None,
                                 originPath=None,
                                 savePickle=False, saveWideText=True,
                                 dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file


endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Stuff
clock = core.Clock()  # A clock wich will be used throughout the experiment to time events on a trial-per-trial basis (stimuli and reaction times).
#keyboard = ppc.Keyboard()  # keyboard is now initiated for response collection
# Create psychopy window
myMonitor = monitors.Monitor('testMonitor', width=monWidth, distance=monDistance)  # Create monitor object from the variables above. This is needed to control size of stimuli in degrees.
myMonitor.setSizePix(monitorSizePix)
win = visual.Window(monitor=myMonitor, units='deg', fullscr=True, allowGUI=True, winType="pyglet", color='black')  # Initiate psychopy Window as the object "win", using the myMon object from last line. Use degree as units!
stimText = visual.TextStim(win, pos=messagePos, height=messageHeight, wrapWidth=999)  # Message / question stimulus. 
spaceText = visual.TextStim(win, pos=(0,-10), height=messageHeight, wrapWidth=999)  # Message / question stimulus. 

"""
 FUNCTIONS
"""
def ask(text='', keyList=[]):
    """
    Ask subject something. Shows question and returns answer (keypress)
    and reaction time. Defaults to no text and all keys.
    """
    # Draw the TextStims to visual buffer, then show it and reset timing immediately (at stimulus onset)
    stimText.setText(codecs.decode(text,"utf-8"))
    spaceText.setText(codecs.decode(spaceLookup[language],"utf-8"))
    # Set the text height
    stimText.setHeight(1)
    spaceText.setHeight(1)
    # set the text color
    stimText.setColor('white')
    spaceText.setColor('white')
    stimText.draw()
    spaceText.draw()
    win.flip()
    event.clearEvents('keyboard')

    # Halt everything and wait for (first) responses matching the keys given in the Q object.
    response = event.waitKeys(keyList=['space','q','r'])
    if response[0] in keysQuit:  # Look at first reponse [0]. Quit everything if quit-key was pressed
        core.quit()
    if response[0] in keysBreak:
        event.clearEvents('keyboard')
        win.flip()
    if event.getKeys(keyList=['escape', 'q']):
        core.quit()
    if event.getKeys(keyList=['s']):
        print "Skipped experiment"
        quit()
    return response # When answer given, return it.

"""Tests"""
"""Pretrial"""
def pretrial(language):
    if language == 'English':
        ask(preTrialEng)
    elif language == 'French':
        ask(preTrialFr)
        
"""Letter Test"""
def letterTest(language):
    if language == 'English':
        ask(engInstruct)
        """The Letter"""
        ask(TitleLetterEng)  #Letter check 
        message = visual.TextStim(win, text='A',height=4, color='white')
        message.setAutoDraw(True)  # automatically draw every frame
        ask(TitleLetterEng2)  #Letter check 
        message.setAutoDraw(False)
    elif language == 'French':
        ask(frInstruct)
        """The Letter"""
        ask(TitleLetterFr)  #Letter check 
        message = visual.TextStim(win, text='A',height=4, color='white')
        message.setAutoDraw(True)  # automatically draw every frame
        ask(TitleLetterFr2)  #Letter check 
        message.setAutoDraw(False)
        
"""Arrow Test"""
def arrowTest(language):
    arrowPath = 'files/CongruentLeft.bmp'
    if language == 'English':
        """The Arrow""" 
        arrow = visual.SimpleImageStim(win, image=arrowPath, units='deg',pos=(0.0, 0.0)) 
        drawArrow = arrow.draw(win)
        ask(ArrowTitleEng)
    elif language == 'French':
        """The Arrow"""  
        arrow = visual.SimpleImageStim(win, image=arrowPath, units='deg',pos=(0.0, 0.0)) 
        drawArrow = arrow.draw(win)
        ask(ArrowTitleFr)
        return

"""Audio Test"""
def audioTest(language):
    audioPathEng = 'files/WelcomeEng.wav'
    audioPathFr = 'files/WelcomeFr.wav'
    study_info['responses'] = responses = event.getKeys(timeStamped=clock)
    if language == 'English':
        """Audio Test"""
        trialFinished=False
        filesound = sound.Sound(audioPathEng)
        filesound.setVolume(1.0)
        filesound.play()
        ask(AudioTitleEng)
        #core.wait(0.5)
        while trialFinished != True:
            if event.getKeys(keysRepeat):
                filesound = sound.Sound(audioPathEng)
                filesound.setVolume(1.0)
                filesound.play()
                ask(AudioTitleEng)
                core.wait(0.5)
            if event.getKeys(keysBreak):
                trialFinished=True
            if event.getKeys(keysQuit):
                core.quit()
        
    elif language == 'French':
        """Audio Test"""
        trialFinished=False
        filesound = sound.Sound(audioPathFr)
        filesound.setVolume(1.0)
        filesound.play()
        ask(AudioTitleFr)
        core.wait(0.5)
        while trialFinished != True:
            if event.getKeys(keysRepeat):
                filesound = sound.Sound(audioPathFr)
                filesound.setVolume(1.0)
                filesound.play()
                ask(AudioTitleFr)
                core.wait(0.5)
            if event.getKeys(keysBreak):
                trialFinished=True
            if event.getKeys(keysQuit):
                core.quit()
        
def closing(language):
    if language == 'English':
        ask(closingEng)
    elif language == 'French':
        ask(closingFr)
        
def runPretrial(language):
    pretrial(language)
    letterTest(language)    #Perform letter test
    arrowTest(language)     #Arrow Test
    audioTest(language)     #Audio Test
    
def runBlock():
    """
    Runs a block of trials. This is the presentation of stimuli,
    collection of responses and saving the trial
    """
    if pre_trial:
        runPretrial(language) # Run the pretrial
        questions.runQuestions(win,ask, language, exp)
    if reaction_time:
        RT_experiment.runRT(win, ask, test, language, preferred_hand,exp) #Reaction Time Task
    if memory:
        Memory.runMemory(win, ask,language,test,exp) # Memory Task
    if flanker:
        Flanker.runFlanker(win,flanker_info,ask,language,exp) #Flanker Task NOTES: REMOVE flanker_info param
    if corsi_forward:
        corsiTask.runCorsi(win, ask, language, exp, reverse = False) #Run Corsi Blocks Task Forward
    if corsi_reverse:
        corsiTask.runCorsi(win, ask, language, exp, reverse = True) #Run Corsi Blocks Task Reverse
    if memory_recall:
        MemoryRecall.runMemoryRecall(win,ask,language, test,exp) #Memory Recall
    if shapes_2_back:
        shapes2back.runShapes2Back(win,ask,language,exp) # Shapes2Back Task
    if letters_2_back:
        letters2back.runLetters2Back(win,ask,language,exp) # Letters2Back Task
    if letters_3_back:
        letters3back.runLetters3Back(win,ask,language,exp) # Letters3Back Task
    if verbal_fluency:
        verbalFluency.runVerbalFluency(win,ask,test,language)
    # if trails:
    #     print "run trails"
    #     #trails2.runTrails(win)
    closing(language) # End experiment
"""
 RUN EXPERIMENT
 Now it's really simple. You simply execute things using the functions ask and
 runBlock. Here we order block types given input from dialogue box
"""
 
if __name__ == "__main__":
    runBlock()

