# -*- coding: utf-8 -*-
import random, sys
from psychopy import core, event, gui, visual, logging

#window
win = visual.Window(size = (1200,800), color = 'black', units = 'pix')
win.setRecordFrameIntervals(True)
win._refreshThreshold=1/85.0+0.004 #i've got 85Hz monitor and want to allow 4ms tolerance
#set the log module to report warnings to the std output window (default is errors only)
logging.console.setLevel(logging.WARNING)

#timer
RT = core.Clock()

# parameters
numTrials=25
frameRate = 85  # Hz
stimDuration = 5  # secs
blankDuration = 2.5  # secs

stimFrames = int(frameRate * stimDuration)
blankFrames = int(frameRate * blankDuration)  # rounds down / floor. 212.5 becomes 212.
totalFrames = stimFrames + blankFrames

def experiment():
    list =[random.randint(0,10) for r in xrange(numTrials)]
    #list = [2,3,2,3,2,3,2,3,4,5,6,7,8,9,8]
    keyList=[]
    demoDisp = visual.TextStim(win, text = '', height = 100) #textstim object that will be displayed
    counter = 0  # Counter is unused?
    for x in list:
        # PREPARE STIMULUS
        demoDisp.setText(x)

        # PRESENT STIMULUS
        for frameN in range(stimFrames):
            # Display stimulus
            demoDisp.draw()
            win.flip()

            # Reset timer on onset
            if frameN == 0:
                RT.reset()

        # PRESENT BLANK
        for frameN in range(blankFrames):
            # Blank screen with no response recording
            win.flip()

        # RECORD RESPONSES
        keyList = event.getKeys(timeStamped=RT)
        # keyList[N][Y], N is response number if multiple keys were pressed. Y=0 is key-name. Y=1 is time
        if keyList:
            print keyList[0][0], 'key was pressed after', str(keyList[0][1]), 'seconds'
        else:
            print 'no key was pressed'

experiment()