# -*- coding: utf-8 -*-

#
# Imports
#
from psychopy import sound,core, gui, visual, event, data, logging
from itertools import product
from os import system
logging.console.setLevel(logging.DEBUG)

                
audioPath = 'VerbalFluencyTask/files/Ding.wav'
stopSignPath = 'VerbalFluencyTask/files/StopSign.bmp'

keysBreak = [' ', 'space']  # Keys to accept at regular break
keysQuit = ['q','escape']  # Keys that quits the experiment
keySkip = ['s'] #keys that skip trial
keyBack = ['b'] # key to go back

FormAEng = """
Please name as many words as you can beginning with the letter 'F'.

You will have ONE minute.
"""
FormBEng = """
Please name as many words as you can beginning with the letter 'A'.

You will have ONE minute.
"""
FormCEng = """
Please name as many words as you can beginning with the letter 'S'.

You will have ONE minute.
"""
FormAFr = """
Veuillez me nommer le plus de mots possible/que vous pouvez commençant par la lettre 'P'.
"""
FormBFr = """
Veuillez me nommer le plus de mots possible/que vous pouvez commençant par la lettre 'L'.
"""
FormCFr = """
Veuillez me nommer le plus de mots possible/que vous pouvez commençant par la lettre 'S'.
"""
def playAudio(audioPath):
    filesound = sound.Sound(audioPath)
    filesound.setVolume(1.0) 
    filesound.play()
    
def runVerbalFluency(win, ask, test, language):
    try:
           
        output = { "A" : { "English" : FormAEng, "French" : FormAFr },
            "B" : { "English" : FormBEng,  "French" : FormBFr },
            "C" : {  "English" : FormCEng, "French" :FormCFr }
            }
        instructions = output[test][language]
        stopSign = visual.SimpleImageStim(win, image = stopSignPath, units='norm', pos=(0.0, 0.0)) #Stop Sign
        ding = sound.Sound(audioPath)
        ding.setVolume(1.0)

        ask(instructions)
        timer = core.CountdownTimer(60)
        while timer.getTime() > 0:  # after 60s will become negative
            win.flip()
            ding.play()
            #instructionText.draw(win)
            responses = event.waitKeys(timeStamped=False)
            if 'q' in responses:
                print 'Program aborted...'
                core.quit()
            elif 's' in responses:
                print "Skipped experiment"
                return
        else:
            win.flip()
            ding.play()
            stopSign.draw(win)
            ask()
            
    except KeyboardInterrupt:
        raise
        core.quit()