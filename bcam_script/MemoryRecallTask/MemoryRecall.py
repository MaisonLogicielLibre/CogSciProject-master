# -*- coding: utf-8 -*-

# ==========================
# MemoryRecall.py
# ==========================

#
# Imports
#
import collections
from psychopy import sound, core, visual, event, gui, data, logging
from itertools import product
from os import system
import codecs
#logging.console.setLevel(logging.DEBUG)

# exp = data.ExperimentHandler(name='MemoryRecallTask',
#                 version='0.1',
#                 extraInfo={'participant':'000'},
#                 runtimeInfo=None,
#                 originPath=None,
#                 savePickle=True,
#                 saveWideText=True,
#                 dataFileName='data/memoryRecall')
                
def minimizeWindow(win):
    """
    Minimize the psychopy window passed in as 'window' arg
    """
    win.winHandle.set_visible(False)
    win.winHandle.minimize()
    win.flip() # redraw the (minimised) window


def maximizeWindow(win):
    """
    Maximize the psychopy window passed in as 'window' arg
    """
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

InstrucEngA = """
The computer read some words to you earlier, 
which I asked you to remember.
Tell me as many of those words as you can remember.

When you are ready, please turn away from the computer screen

Press SPACE to continue
"""

InstrFrA = """
L’ordinateur vous a lu une série de mots plus tôt et je 
vous avais demandé de vous en rappeler. 
Maintenant, dites-moi tous les mots dont vous vous rappelez.

Lorsque vous êtes prêt(e), veuillez tourner le dos à l’écran de l’ordinateur.
"""

categoryLookup = {'English':'Category','French':'Catégorie'}
categoryLookup = {k:v.decode("utf-8") for k,v in categoryLookup.items()}
choiceLookup = {'English':'Multiple Choice', 'French':'Choix'}

def CatMultChoice(win,language,category,multipleChoice):
    win.fullscr = True
    categoryHeading = visual.TextStim(win, text=categoryLookup[language], height=.12, pos = (0.0,0.5), color='Green', units='norm')
        
    # Example 1 --------(basic choices)--------
    # create a Category RatingScale object:
    catRatingScale = visual.RatingScale(win, choices=['1', '2'])

    # create a Multiple Choice RatingScale object:
    multRatingScale = visual.RatingScale(win, choices=['1', '2'])

    # Or try this one:
    #myRatingScale = visual.RatingScale(win, choices=map(str, range(1,8)), marker='hover')
    if category != None:
        # the item to-be-rated or respond to:
        myItem = visual.TextStim(win, text=category, height=.12, color='yellow', units='norm')

        # anything with a frame-by-frame .draw() method will work, e.g.:
        #myItem = visual.MovieStim(win, 'jwpIntro.mov')

        event.clearEvents()
        while catRatingScale.noResponse: # show & update until a response has been made
            categoryHeading.draw()
            myItem.draw()
            catRatingScale.draw()
            win.flip()
            if event.getKeys(['escape']):
                core.quit()
    
    print 'Category: rating =', catRatingScale.getRating()
    print 'history =', catRatingScale.getHistory()
        
    if catRatingScale.getRating() == '2' or category == None:
        # Example 1 --------(basic choices)--------
        multplichoiceHeading = visual.TextStim(win, text=choiceLookup[language], height=.12, pos = (0.0,0.5), color='Purple', units='norm')


        # Or try this one:
        #myRatingScale = visual.RatingScale(win, choices=map(str, range(1,8)), marker='hover')

        # the item to-be-rated or respond to:
        myItem = visual.TextStim(win, text=multipleChoice, height=.12,color='yellow', units='norm')

        # anything with a frame-by-frame .draw() method will work, e.g.:
        #myItem = visual.MovieStim(win, 'jwpIntro.mov')

        event.clearEvents()
        while multRatingScale.noResponse: # show & update until a response has been made
            multplichoiceHeading.draw()
            myItem.draw()
            multRatingScale.draw()
            win.flip()
            if event.getKeys(['escape']):
                core.quit()
        print 'Multiple Choice: rating =', multRatingScale.getRating()
        print 'history =', multRatingScale.getHistory()
    if catRatingScale.getRating() == '1':
        score = 2
    if multRatingScale.getRating() == '1':
        score = 3
    elif multRatingScale.getRating() == '2':
        score = 0
    return score

def MemoryRecall(win, ask, instructions, words,orderWords,exp):
    ask(instructions)
    minimizeWindow(win)
    info = words
    infoDlg = gui.DlgFromDict(dictionary=info, title='MemoryRecall',order = orderWords,
    fixed=['ExpVersion'])
    if infoDlg.OK:
        #print key and values
        for key, value in sorted(info.iteritems()):
            if value == True:
                info[key] = 1
                exp.addData(key, info[key])
            else:
                info[key] = 0
        maximizeWindow(win)
    else: print 'User Cancelled'

    return info


def runMemoryRecall(win, ask, language, test,exp):
    win.flip()
    try:
        output = { "A" : { "English" : InstrucEngA, "French" : InstrFrA },
            "B" : { "English" : InstrucEngA,  "French" : InstrFrA },
            "C" : {  "English" : InstrucEngA, "French" :InstrFrA }
            }
        formAEng = {'Lemon':False, 'History':False, 'Sheep':False, 'Majority':False, 'Table':False, 'Dentist':False, 'Hat':False,'Violin':False}
        formAFr = {'Citron':False, 'Histoire':False, 'Mouton':False, 'Majorité':False, 'Table':False, 'Dentiste':False, 'Chapeau':False,'Violon':False}
        formBEng = {'Majority':False, 'Hat':False, 'Method':False, 'Flute':False, 'Table':False, 'Electrician':False, 'Cat':False,'Orange':False}
        formBFr = {'Majorité':False, 'Chapeau':False, 'Methode':False, 'Flute':False, 'Table':False, 'Electricien':False, 'Chat':False,'Orange':False}
        formCEng = {'Orange':False, 'Shoe':False, 'Dog':False, 'Majority':False, 'Table':False, 'Thought':False, 'Journalist':False,'Trumpet':False}
        formCFr = {'Orange':False, 'Soulier':False, 'Chien':False, 'Majorité':False, 'Table':False, 'Pensée':False, 'Journaliste':False,'Trompette':False}
        
        instrOutput = { "A" : { "English" : formAEng, "French" : formAFr },
            "B" : { "English" : formBEng,  "French" : formBFr },
            "C" : {  "English" : formCEng, "French" :formCFr }
            }
            
        orderformAEng =['Lemon', 'History', 'Sheep', 'Majority', 'Table', 'Dentist', 'Hat','Violin']
        orderformAFr = ['Citron', 'Histoire', 'Mouton', 'Majorité', 'Table', 'Dentiste', 'Chapeau','Violon']
        orderformBEng = ['Majority', 'Hat', 'Method', 'Flute', 'Table', 'Electrician', 'Cat','Orange']
        orderformBFr = ['Majorité', 'Chapeau', 'Methode', 'Flute', 'Table', 'Electricien', 'Chat','Orange']
        orderformCEng = ['Orange', 'Shoe', 'Dog', 'Majority', 'Table', 'Thought', 'Journalist','Trumpet']
        orderformCFr = ['Orange', 'Soulier', 'Chien', 'Majorité', 'Table', 'Pensée', 'Journaliste','Trompette']
        
        orderinstrOutput = { "A" : { "English" : orderformAEng, "French" : orderformAFr },
            "B" : { "English" : orderformBEng,  "French" : orderformBFr },
            "C" : {  "English" : orderformCEng, "French" : orderformCFr }
            }
            
       
        instructions = output[test][language] #Get correct instructions based on form and language
        words = {k.decode('utf8'): v for k, v in instrOutput[test][language].items()} #Get correct word list depending on Form and language
        orderWords = [k.decode('utf8') for k in orderinstrOutput[test][language]] #Get correct word order to display in GUI
        
        results = MemoryRecall(win, ask,instructions, words,orderWords, exp) #Run Memory Recall
        
        categoryAEng = {'Lemon':'Fruit', 'History': 'History','Sheep': 'Animal','Majority':'Majority', 'Dentist': 'Profession','Table':'Furniture','Hat':'Clothing', 'Violin': 'Music Instrument'}
        categoryBEng = {'Majority':'Majority','Hat':'Clothing','Method':'Method','Flute': 'Music Instrument','Table':'Furniture','Elictrician': 'Profession', 'Cat': 'Animal','Orange':'Fruit'  }
        categoryCEng = {'Orange':'Fruit', 'Shoe':'Clothing', 'Dog':'Animal', 'Majority':'Majority', 'Table':'Furniture', 'Thought':'Thought', 'Journalist':'Profession','Trumpet':'Music Instrument'}
        
        categoryAFr = {'Citron':'FRUIT', 'Histoire':'Histoire', 'Mouton':'ANIMAL', 'Majorité':'Majorité', 'Table':'MEUBLE', 'Dentiste':'PROFESSION', 'Chapeau':'VÊTEMENT','Violon':'INSTRUMENT DE MUSIQUE'}
        categoryBFr = {'Majorité':'Majorité', 'Chapeau':'VÊTEMENT', 'Methode':'Methode', 'Flute':'INSTRUMENT DE MUSIQUE', 'Table':'MEUBLE', 'Electricien':'PROFESSION', 'Chat':'ANIMAL','Orange':'FRUIT'}
        categoryCFr = {'Orange':'FRUIT', 'Soulier':'VÊTEMENT', 'Chien':'ANIMAL', 'Majorité':'Majorité', 'Table':'MEUBLE', 'Pensée':'Pensée', 'Journaliste':'PROFESSION','Trompette':'INSTRUMENT DE MUSIQUE'}
        
        
        multipleChoiceAEng = {'Fruit':'Lemon-Apple-Cherry','History':'Opinion-History-Justice', 'Animal':'Rat-Sheep-Cow', 'Majority':'Majority-Quality-Liberty','Profession':'Florist-Dentist-Plumber','Furniture':'Table-Chair-Bed', 'Clothing':'Coat-Shirt-Hat', 'Music Instrument': 'Guitar-Piano-Violin'}
        multipleChoiceBEng = {'Majority':'Majority-Quality-Liberty','Clothing':'Coat-Shirt-Hat','Method':'Knowledge-Method-Advice','Music Instrument':'Clarinet-Bass-Flute','Furniture':'Table-Chair-Bed','Profession':'Shoemaker-Electrician-Carpenter','Animal':'Tiger-Cat-Snale','Fruit':'Orange-Banana-Plum'}
        multipleChoiceCEng = {'Fruit':'Orange-Banana-Plum', 'Clothing':'Glove-Scarf-Shoe', 'Animal':'Camel-Dog-Elephant', 'Majority':'Majority-Quality-Liberty', 'Furniture': 'Table-Chair-Bed','Thought':'Thought-SPirit-Trouble','Profession':'Policeman-Journalist-Gardener','Music Instrument':'Banjo-Harmonica-Trumpet'}
        
        multipleChoiceAFr = {'FRUIT':'CITRON-POMME-CERISE','Histoire':'OPINION - HISTOIRE - JUSTICE', 'ANIMAL':'RAT - MOUTON - VACHE', 'Majorité':'MAJORITÉ - QUALITÉ - LIBERTÉ','MEUBLE':'TABLE - CHAISE - LIT','PROFESSION':'FLEURISTE - DENTISTE - PLOMBIER', 'VÊTEMENT':'MANTEAU - CHEMISE - CHAPEAU', 'INSTRUMENT DE MUSIQUE': 'GUITARE - PIANO - VIOLON'}
        multipleChoiceBFr = {'Majorité':'MAJORITÉ - QUALITÉ - LIBERTÉ', 'VÊTEMENT':'MANTEAU - CHEMISE - CHAPEAU', 'Methode':'CONNAISSANCE - MÉTHODE - CONSEIL', 'INSTRUMENT DE MUSIQUE':'CLARINETTE - BASSE - FLUTE', 'MEUBLE': 'TABLE - CHAISE - LIT', 'PROFESSION':'CORDONNIER - ÉLECTRICIEN - MENUISIER','ANIMAL':'TIGRE - CHAT - SERPENT', 'FRUIT':'ORANGE - BANANE - PRUNE'}
        multipleChoiceCFr = {'FRUIT':'ORANGE -  BANANE -  PRUNE', 'VÊTEMENT':'GANT - FOULARD  -  SOULIER', 'ANIMAL':'CHAMEAU - CHIEN - ÉLÉPHANT', 'Majorité':'MAJORITÉ -  QUALITÉ -  LIBERTÉ', 'MEUBLE': 'TABLE - CHAISE - LIT','Pensée':'PENSÉE -  ESPRIT -  TROUBLE','PROFESSION':'POLICIER  -  JOURNALISTE  -  JARDINIER','INSTRUMENT DE MUSIQUE':'BANJO  -  HARMONICA -  TROMPETTE'}
        
        #RETURN CORRECT category
        categoryOutput = { "A" : { "English" : categoryAEng, "French" : categoryAFr },
            "B" : { "English" : categoryBEng,  "French" : categoryBFr },
            "C" : {  "English" : categoryCEng, "French" : categoryBFr }
            }
        
        categoryResults = {k.decode('utf8'): v.decode('utf8') for k, v in categoryOutput[test][language].items()} #Return the category list based on form and language
       
        #RETURN CORRECT category
        multipleChoiceOutput = { "A" : { "English" : multipleChoiceAEng, "French" : multipleChoiceAFr },
            "B" : { "English" : multipleChoiceBEng,  "French" : multipleChoiceBFr },
            "C" : {  "English" : multipleChoiceCEng, "French" : multipleChoiceCFr }
            }
        
        multipleChoiceResults = {k.decode('utf8'): v.decode('utf8') for k, v in multipleChoiceOutput[test][language].items()} #Return the category list based on form and language
        missedCategories = [categoryResults[k] for k, v in results.iteritems() if v == False] #Return the categories the subject missed
        for key in missedCategories:
            missedList = ['History','Majority','Majorité','Histoire','Method','Methode','Thought','Pensée']
            missedList = [x.decode("utf-8") for x in missedList]
            if key in missedList:
                categoryWord = None
                multipleChoiceWords = multipleChoiceResults[key]
            else:
                categoryWord = key
                multipleChoiceWords = multipleChoiceResults[key]
            answers = CatMultChoice(win,language, categoryWord,multipleChoiceWords)
            print answers
            exp.addData(key, answers)
            exp.addData('Task Name', 'Memory Recall')
        exp.nextEntry()
    except KeyboardInterrupt:
        raise
        core.quit()