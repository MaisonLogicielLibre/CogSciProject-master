# -*- coding: utf-8 -*-
#
# Imports
#
from psychopy import visual, sound,core, gui, data, event, logging
from collections import defaultdict
from itertools import product
from os import system
import sys
import codecs
#logging.console.setLevel(logging.DEBUG)

def minimizeWindow(win):
    """
    Minimize the psychopy window passed in as 'window' arg
    """
    win.winHandle.set_visible(False)
    win.winHandle.minimize()
#    win.winHandle.minimize() #minimize the PsychoPy window
#    win.fullscr = False #disable fullscreen
    win.flip() #redraw the (minimized) window

def maximizeWindow(win):
    """
    Maximize the psychopy window passed in as 'window' arg
    """
    win.winHandle.maximize()
#    window.winHandle.set_visible(True)
#    window.winHandle.activate()
    #win.winHandle.maximize() #when external program closes, maximize PsychoPy window again
    win.fullscr = True
    #win.winHandle.maximize() #when external program closes, maximize PsychoPy window again
    win.winHandle.set_visible(True)
    win.flip()
    win.winHandle.activate() #re-activate window

"""
Memory Test
"""

"""
English
"""
WordsBaselineEng = """
Lemon

History

Sheep

Majority

Table

Dentist

Hat

Violin
"""

Words3MoEng = """
Majority

Hat

Method

Flute

Table

Electrician

Cat

Orange
"""
Words6MoEng = """
Orange

Shoe

Dog

Majority

Table

Thought

Journalist

Trumpet
"""
# Create an empty dictionary.
InstrEng = {}

# Add a new item.
InstrEng['0'] = """
Good job!

Next is a memory test.
The computer will read a list of 8 words to you, and you will try to remember them.
Listen carefully. After you hear the whole list,
you will tell me as many of the words as you can remember.

You can say the words in any order.

We will do this three times.

When you are ready, please turn away from the computer screen.
"""


InstrEng['1'] = """
Now, the computer is going to read the same list to you again.

Listen carefully.

When you have heard the whole list, tell me all the

words you can remember, including words you said the first time.
"""

InstrEng['2'] = """
Now, the computer is going to read the same list one final time.

Listen carefully.

When you have heard the whole list, tell me as many

words as you can remember, including words you said before.
"""

InstrEng['3'] = """
Good!

I will ask you to remember those words again in a few minutes.

Try your best not to forget those words
"""


"""
French
"""
WordsBaselineFr = """
Citron

Histoire

Mouton

Majorité

Table

Dentiste

Chapeau

Violon
"""
Words3MoFr = """
Majorité

Chapeau

Methode

Flute

Table

Electricien

Chat

Orange
"""

Words6MoFr = """
Orange

Soulier

Chien

Majorité

Table

Pensée

Journaliste

Trompette
"""
InstrFr = {}

InstrFr['0'] = """
Bravo! Le prochain exercice est un test de mémoire.

L'ordinateur va vous lire une liste de 8 mots.

Écoutez attentivement. Lorsque vous aurez entendu la liste complète,
dites-moi tous les mots dont vous vous rappelez.
L'ordre dans lequel vous les répétez n'est pas important.

Lorsque vous êtes prêt(e)s veuillez tourner le dos à l’écran de l’ordinateur.
"""
InstrFr['1'] = """
Maintenant l'ordinateur va lire la même liste de mots une deuxième fois.

Écoutez attentivement.

Lorsque vous aurez entendu la liste complète, dites-moi le plus de mots possible dont vous vous rappelez,
y compris ceux que vous avez répétés la première fois.
"""

InstrFr['2'] = """
Maintenant l'ordinateur va lire la même liste de mots une dernière fois.

Écoutez attentivement.

Lorsque vous aurez entendu la liste complète,
dites-moi le plus de mots possible dont vous vous rappelez,
y compris ceux que vous avez répétés les deux premières fois
"""
InstrFr['3'] = """
Bien!

Je vais vous demander de vous rappeler de ces mots dans quelques minutes.

Faites de votre mieux pour ne pas oublier ces mots.
"""
turnaway_en = """
Please turn screen away from participant

Press SPACE when ready
"""

turnaway_fr = """
Please turn screen away from participant

Press SPACE when ready
"""

turnaway_lookup = {'English': turnaway_en, 'French':turnaway_fr}

"""
Audio Paths
"""

""""
Baseline English Files
"""
audioPathEng =[]
audioPathEng.append('MemoryTask/files/Eng/Lemon.wav')
audioPathEng.append('MemoryTask/files/Eng/History.wav')
audioPathEng.append('MemoryTask/files/Eng/Sheep.wav')
audioPathEng.append('MemoryTask/files/Eng/Majority.wav')
audioPathEng.append('MemoryTask/files/Eng/Table.wav')
audioPathEng.append('MemoryTask/files/Eng/Dentist.wav')
audioPathEng.append('MemoryTask/files/Eng/Hat.wav')
audioPathEng.append('MemoryTask/files/Eng/Violin.wav')

""""3 Mo English Files """
audioPathEng3Mo =[]
audioPathEng3Mo.append('MemoryTask/files/Eng/Majority.wav')
audioPathEng3Mo.append('MemoryTask/files/Eng/Hat.wav')
audioPathEng3Mo.append('MemoryTask/files/Eng/Method.wav')
audioPathEng3Mo.append('MemoryTask/files/Eng/Flute.wav')
audioPathEng3Mo.append('MemoryTask/files/Eng/Table.wav')
audioPathEng3Mo.append('MemoryTask/files/Eng/Electrician.wav')
audioPathEng3Mo.append('MemoryTask/files/Eng/Cat.wav')
audioPathEng3Mo.append('MemoryTask/files/Eng/Orange.wav')

"""6 Mo English Files"""
audioPathEng6Mo =[]
audioPathEng6Mo.append('MemoryTask/files/Eng/Orange.wav')
audioPathEng6Mo.append('MemoryTask/files/Eng/Shoe.wav')
audioPathEng6Mo.append('MemoryTask/files/Eng/Dog.wav')
audioPathEng6Mo.append('MemoryTask/files/Eng/Majority.wav')
audioPathEng6Mo.append('MemoryTask/files/Eng/Table.wav')
audioPathEng6Mo.append('MemoryTask/files/Eng/Thought.wav')
audioPathEng6Mo.append('MemoryTask/files/Eng/Journalist.wav')
audioPathEng6Mo.append('MemoryTask/files/Eng/Trumpet.wav')

"""Baseline French Files"""
audioPathFr = []
audioPathFr.append('MemoryTask/files/Fr/Citron.wav')
audioPathFr.append('MemoryTask/files/Fr/Histoire.wav')
audioPathFr.append('MemoryTask/files/Fr/Mouton.wav')
audioPathFr.append('MemoryTask/files/Fr/Majorite.wav')
audioPathFr.append('MemoryTask/files/Fr/TableFr.wav')
audioPathFr.append('MemoryTask/files/Fr/Dentiste.wav')
audioPathFr.append('MemoryTask/files/Fr/Chapeau.wav')
audioPathFr.append('MemoryTask/files/Fr/Violon.wav')


""""3 Mo French Files """
audioPathFr3Mo =[]
audioPathFr3Mo.append('MemoryTask/files/Fr/Majorite.wav')
audioPathFr3Mo.append('MemoryTask/files/Fr/Chapeau.wav')
audioPathFr3Mo.append('MemoryTask/files/Fr/Methode.wav')
audioPathFr3Mo.append('MemoryTask/files/Fr/FluteFr.wav')
audioPathFr3Mo.append('MemoryTask/files/Fr/TableFr.wav')
audioPathFr3Mo.append('MemoryTask/files/Fr/Electricien.wav')
audioPathFr3Mo.append('MemoryTask/files/Fr/Chat.wav')
audioPathFr3Mo.append('MemoryTask/files/Fr/OrangeFr.wav')

"""6 Mo French Files"""
audioPathFr6Mo =[]
audioPathFr6Mo.append('MemoryTask/files/Fr/OrangeFr.wav')
audioPathFr6Mo.append('MemoryTask/files/Fr/Soulier.wav')
audioPathFr6Mo.append('MemoryTask/files/Fr/Chien.wav')
audioPathFr6Mo.append('MemoryTask/files/Fr/Majorite.wav')
audioPathFr6Mo.append('MemoryTask/files/Fr/TableFr.wav')
audioPathFr6Mo.append('MemoryTask/files/Fr/Pensee.wav')
audioPathFr6Mo.append('MemoryTask/files/Fr/Journaliste.wav')
audioPathFr6Mo.append('MemoryTask/files/Fr/Trompette.wav')


wordLookup = { "A" : { "English" : WordsBaselineEng, "French" : codecs.decode(WordsBaselineFr, 'utf-8') },
         "B" : { "English" : Words3MoEng,  "French" : codecs.decode(Words3MoFr,'utf-8') },
         "C" : {  "English" : Words6MoEng, "French" : codecs.decode(Words6MoFr, 'utf-8') }
        }
audioLookup = { "A" : { "English" : audioPathEng, "French" : audioPathFr },
        "B" : { "English" : audioPathEng3Mo,  "French" : audioPathFr3Mo },
        "C" : {  "English" : audioPathEng6Mo, "French" : audioPathFr6Mo }
        }
instrLookup = { "A" : { "English" : InstrEng, "French" : InstrFr },
        "B" : { "English" : InstrEng,  "French" : InstrFr },
        "C" : {  "English" : InstrEng, "French" : InstrFr }
        }

wordsAEng = {'Lemon':'Words-IM_1', 'History':'Words-IM_2', 'Sheep':'Words-IM_3',
             'Majority':'Words-IM_4', 'Table':'Words-IM_5', 'Dentist':'Words-IM_6',
             'Hat':'Words-IM_7','Violin':'Words-IM_8'}

wordsAFr= {'Citron':'Words-IM_1', 'Histoire':'Words-IM_2', 'Mouton':'Words-IM_3',
            'Majorité':'Words-IM_4', 'Table':'Words-IM_5', 'Dentiste':'Words-IM_6',
            'Chapeau':'Words-IM_1','Violon':'Words-IM_1'}

wordsBEng={'Majority':'Words-IM_1', 'Hat':'Words-IM_2', 'Method':'Words-IM_3',
           'Flute':'Words-IM_4', 'Table':'Words-IM_5', 'Electrician':'Words-IM_6',
           'Cat':'Words-IM_7','Orange':'Words-IM_8'}

wordsBFr={'Majorité':'Words-IM_1', 'Chapeau':'Words-IM_2', 'Methode':'Words-IM_3',
           'Flute':'Words-IM_4', 'Table':'Words-IM_5', 'Electricien':'Words-IM_6',
           'Chat':'Words-IM_7','Orange':'Words-IM_8'}

wordsCEng={'Orange':'Words-IM_1', 'Shoe':'Words-IM_2', 'Dog':'Words-IM_3',
           'Majority':'Words-IM_4', 'Table':'Words-IM_5', 'Thought':'Words-IM_6',
           'Journalist':'Words-IM_7','Trumpet':'Words-IM_8'}

wordsCFr={'Orange':'Words-IM_1', 'Soulier':'Words-IM_2', 'Chien':'Words-IM_3',
           'Majorité':'Words-IM_4', 'Table':'Words-IM_5', 'Pensée':'Words-IM_6',
           'Journaliste':'Words-IM_7','Trompette':'Words-IM_8'}

wordListLookup = { "A" : { "English" : wordsAEng, "French" : dict((k.decode('utf8'), v.decode('utf8')) for k, v in wordsAFr.items()) },
        "B" : { "English" : wordsBEng,  "French" : dict((k.decode('utf8'), v.decode('utf8')) for k, v in wordsBFr.items()) },
        "C" : {  "English" : wordsCEng, "French" : dict((k.decode('utf8'), v.decode('utf8')) for k, v in wordsCFr.items())}
        }

infoAEng = {'Lemon':False, 'History':False, 'Sheep':False, 'Majority':False, 'Table':False, 'Dentist':False, 'Hat':False,'Violin':False}
infoAFr = {'Citron':False, 'Histoire':False, 'Mouton':False, 'Majorité':False, 'Table':False, 'Dentiste':False, 'Chapeau':False,'Violon':False}
infoBEng = {'Majority':False, 'Hat':False, 'Method':False, 'Flute':False, 'Table':False, 'Electrician':False, 'Cat':False,'Orange':False}
infoBFr = {'Majorité':False, 'Chapeau':False, 'Methode':False, 'Flute':False, 'Table':False, 'Electricien':False, 'Chat':False,'Orange':False}
infoCEng = {'Orange':False, 'Shoe':False, 'Dog':False, 'Majority':False, 'Table':False, 'Thought':False, 'Journalist':False,'Trumpet':False}
infoCFr = {'Orange':False, 'Soulier':False, 'Chien':False, 'Majorité':False, 'Table':False, 'Pensée':False, 'Journaliste':False,'Trompette':False}
infoLookup = { "A" : { "English" : infoAEng, "French" : infoAFr },
        "B" : { "English" : infoBEng,  "French" : infoBFr },
        "C" : {  "English" : infoBEng, "French" : infoCFr}
        }

orderAEng = ['Lemon','History','Sheep','Majority','Table','Dentist','Hat','Violin']
orderAFr = ['Citron','Histoire','Mouton', 'Majorité', 'Table', 'Dentiste','Chapeau','Violon']
orderBEng=['Majority', 'Hat', 'Method', 'Flute', 'Table','Electrician', 'Cat','Orange']
orderBFr=['Majorité', 'Chapeau', 'Methode', 'Flute', 'Table', 'Electricien', 'Chat','Orange']
orderCEng=['Orange', 'Shoe', 'Dog', 'Majority', 'Table', 'Thought', 'Journalist','Trumpet']
orderCFr=['Orange', 'Soulier', 'Chien', 'Majorité', 'Table', 'Pensée', 'Journaliste','Trompette']
orderLookup = { "A" : { "English" : orderAEng, "French" : orderAFr },
        "B" : { "English" : orderBEng,  "French" : orderBFr },
        "C" : {  "English" : orderCEng, "French" : orderCFr}
        }

"""Method Definitions"""

def playAudio(audioPath,index):
    filesound = sound.Sound(audioPath[index])
    filesound.setVolume(1.0)
    filesound.play()
    core.wait(filesound.getDuration())

def memory(ask,win,exp, test, language):
    """Memory Test"""

    for i in xrange(0,3):
        win.clearBuffer() #clears screen to present new text
        ask(instrLookup[test][language]['{0}'.format(i)]) #Display instructions
        
        ask(turnaway_lookup[language])
        for j in range(len(audioLookup[test][language])):
            #Display Words
            wordsDisplay = visual.TextStim(win, text=wordLookup[test][language], pos=(0,0), alignHoriz='center', rgb=(1,1,1), alignVert='center')
            wordsDisplay.draw()
            win.flip()
            #Play Audio
            playAudio(audioLookup[test][language],j)
            

        minimizeWindow(win)
        info = {k.decode('utf8'): v for k, v in infoLookup[test][language].items()}
        defaultInfo = defaultdict(lambda: -1, info)
        dlgOrder = [codecs.decode(x,'utf-8') for x in orderLookup[test][language]]
        infoDlg = gui.DlgFromDict(dictionary=defaultInfo, title='Memory',order=dlgOrder, fixed=['ExpVersion'])
        if infoDlg.OK:
            #print key and values
            for key, value in sorted(defaultInfo.iteritems()):
                score = 0
                if value == True:
                    score = 1
                else:
                    score = 0
                try:
                    exp.addData(wordListLookup[test][language][key]+'-%i' % i, score)
                    exp.addData('Task Name', 'Memory')
                except KeyError as e:
                    print key.decode("utf-8")
        else:
            exp.abort()
            print 'User Cancelled'
        #end of trial - move to next line in data output
        exp.nextEntry()
        maximizeWindow(win)
    ask(instrLookup[test][language]['3'])
    win.flip()
    return


def runMemory(win, ask,language,test,exp):
    try:
        if 'q' in event.getKeys():
            exp.abort()
            print 'Program aborted...'
            core.quit()
        elif 'escape' in event.getKeys():
            exp.abort()
            print 'Program aborted...'
            core.quit()
        else:
            memory(ask,win,exp,test, language)
            win.flip()
    except KeyboardInterrupt:
        raise
        core.quit()
