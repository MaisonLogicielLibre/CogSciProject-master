# -*- coding: utf-8 -*-

""" demo for the class psychopy.visual.RatingScale()
author: Jeremy Gray, Example 4 by Henrik Singmann
"""

from psychopy import visual, event, core, data, logging, monitors
import os
import codecs


#logging.console.setLevel(logging.DEBUG)
#expQuestions = data.ExperimentHandler(name='BCAM',
#                             version='0.3',
#                             extraInfo={},
#                             runtimeInfo=None,
#                             originPath=None,
#                             savePickle=True,
#                             saveWideText=True,
#                             dataFileName='data/Questionnaire')

instructionsEn_1week = """
First please answer a few questions. 
Read each item and click on the one that comes closest to how you have been feeling in the PAST WEEK.

Don't take too long over your replies:
your immediate reaction to each item will probably be more accurate than a long, thought-out response.

"""

instructionsEn_4week = """
The following questions describe several situations in which 
a person may encounter problems with memory, attention or concentration.

Read each item and click on the one that comes 
closest to how you have been feeling in the PAST 4 WEEKS.
"""
headtext_en_1week = """
In the PAST WEEK...
"""

headtext_en_4week = """
In the PAST 4 WEEKS how often did you...
"""

questionsEn = []
questionsEn.append("I feel as if I am slowed down:")
questionsEn.append("I have lost interest in my appearance:")
questionsEn.append("Have difficulty remembering the names of people, even ones you have met several times?")
questionsEn.append("Miss appointments and meetings you have scheduled?")
questionsEn.append("Forget the dates unless you looked it up?")
questionsEn.append("Forget to do things like turn off the stove or turn on the alarm clock?")
questionsEn.append("Forget to take your medication?")
questionsEn.append("Have trouble making decisions?")
questionsEn.append("Have difficulties paying attention (eg. to a conversation, a book, or a movie)?")
questionsEn.append("Forget things that have happened recently, for example, where you put things, appointments?")

answersEn = []
answersEn.append(['Not at All', 'Sometimes', 'Very Often','Nearly All the Time'])
answersEn.append(['\n I take just as much \n care as ever', '\n I may not take quite \n as much care', '\n I don\'t take so much \n care as I should','Definitely'])
answersEn.append(['Never', 'Rarely', 'Sometimes', 'Often', 'Almost always'])
answersEn.append(['Never', 'Rarely', 'Sometimes', 'Often', 'Almost always'])
answersEn.append(['Never', 'Rarely', 'Sometimes', 'Often', 'Almost always'])
answersEn.append(['Never', 'Rarely', 'Sometimes', 'Often', 'Almost always'])
answersEn.append(['Never', 'Rarely', 'Sometimes', 'Often', 'Almost always'])
answersEn.append(['Never', 'Rarely', 'Sometimes', 'Often', 'Almost always'])
answersEn.append(['Never', 'Hardly ever', 'Yes, definitely'])
answersEn.append(['None of \n the time', 'A little \n of the time', 'Some of \n the time', 'A good bit \n of the time', 'Most of \n the time', 'All of \n the time'])

headtext_fr_1week = """
Pendant la DERNIÈRE SEMAINE...
"""
headtext_fr_4week = """
Pendant les 4 DERNIÈRES SEMAINES, est-ce qu'il vous est arrivé...
"""

instructionsFr_1week = """
Tout d’abord veuillez répondre à quelques questions. 
Lisez chaque question et cochez la réponse 
qui se rapproche le plus de la façon 
dont vous vous êtes senti(e)s pendant la DERNIÈRE SEMAINE.
  
Ne prenez pas trop de temps à choisir vos réponses: 
votre réaction immédiate à chaque question est probablement 
plus juste qu’une réponse trop réfléchie
"""
instructionsFr_4week = """
Les questions suivantes  décrivent  plusieurs situations pour lesquelles  
une personne peut rencontrer des difficultés au niveau de la mémoire, 
de l’attention et de la concentration. 

Lisez chaque question et cochez la réponse qui se rapproche 
le plus de la façon dont vous vous êtes senti(e)s pendant les 4 DERNIÈRES SEMAINES.
"""

questionsFr = []
questionsFr.append("Je me suis senti(e) ralenti(e):")
questionsFr.append("J'ai perdu intérêt dans mon apparence:")
questionsFr.append("d'avoir eu de la difficulté. à vous souvenir du nom des gens, même de ceux que vous avez rencontrés plusieurs fois?")
questionsFr.append("d'avoir manqué un rendez-vous ou une réunion que vous aviez planifié?")
questionsFr.append("de ne pas connaître la date à moins de consulter un calendrier?")
questionsFr.append("d'oublier de faire certaines choses comme éteindre le four ou d'allumer votre réveille-matin?")
questionsFr.append("d'avoir de la difficulté à prendre des décisions?")
questionsFr.append("d'oublier de prendre vos médicaments?")
questionsFr.append("d'avoir des difficultés avec votre attention (par exemple suivre une conversation, un film, lire un livre...)")
questionsFr.append("d'oublier des événements récents. : où vous aviez rangé un objet ou l'heure d'un rendez-vous?")

answersFr = []
answersFr.append(["Presque tout le temps", "Très souvent", "Quelques fois", "Jamais"])
answersFr.append(["Définitivement", "\nJe n’e prend pas \n soin de moi autant \n que je le devrais", "\nJe n’e prend pas \n soin de moi autant \n qu’avant", "Je prends soin de \n moi autant qu’avant"])
answersFr.append(["Jamais", "Rarement", "Quelques fois", "Souvent", "Pratiquement toujours"])
answersFr.append(["Jamais", "Rarement", "Quelques fois", "Souvent", "Pratiquement toujours"])
answersFr.append(["Jamais", "Rarement", "Quelques fois", "Souvent", "Pratiquement toujours"])
answersFr.append(["Jamais", "Rarement", "Quelques fois", "Souvent", "Pratiquement toujours"])
answersFr.append(["Jamais", "Rarement", "Quelques fois", "Souvent", "Pratiquement toujours"])
answersFr.append(["Jamais", "Rarement", "Quelques fois", "Souvent", "Pratiquement toujours"])
answersFr.append(["Jamais", "Très rarement", "Oui, définitivement"])
answersFr.append(["Jamais", "Rarement", "Quelques fois", "Souvent", "La plupart \n du temps", "Tout le temps"])

headtext_1week_lookup = {'English':headtext_en_1week,'French':codecs.decode(headtext_fr_1week,"utf-8")}
headtext_4week_lookup = {'English':headtext_en_4week, 'French':codecs.decode(headtext_fr_4week,"utf-8")}

instructionLookup_1week = {'English':instructionsEn_1week,'French':instructionsFr_1week}
instructionLookup_4week = {'English':instructionsEn_4week,'French':instructionsFr_4week}

def questions(win, ask, language, exp):
    win.flip()
    for i in range(0,10):
        if i == 0:
            ask(instructionLookup_1week[language])
        elif i == 2:
            ask(instructionLookup_4week[language])
            
        questionLookup = {'English':questionsEn[i],'French':codecs.decode(questionsFr[i],"utf-8")}
        answerLookup = {'English':answersEn[i], 'French':[codecs.decode(x,'utf-8') for x in answersFr[i]]}
        # Example 1 --------(basic choices)--------
        # create a RatingScale object:
        myRatingScale = visual.RatingScale(win, choices=answerLookup[language],skipKeys=['tab', 's'], textSize = 1, showAccept = False, 
                                singleClick=True, showValue=False, stretch=2.5, pos=(0.0,-0.35), acceptSize=2.5, disappear=True, mouseOnly = True)

        # the item to-be-rated or respond to:
        myItem = visual.TextStim(win, text=questionLookup[language],wrapWidth=999)
        head_1week = visual.TextStim(win, text=headtext_1week_lookup[language],pos=(0.0, 5),wrapWidth=999 )
        head_4week = visual.TextStim(win, text=headtext_4week_lookup[language],pos=(0.0, 5), wrapWidth=999)

        event.clearEvents()
        while myRatingScale.noResponse: # show & update until a response has been made
            if i in range(0,2):
                head_1week.draw()
            if i in range(2,10):
                head_4week.draw()
            myItem.draw()
            myRatingScale.draw()
            win.flip()
            if event.getKeys(['escape','q']):
                exp.abort()
                core.quit()

        exp.addData('Reaction Time', myRatingScale.getRT())
        exp.addData('Answers', myRatingScale.getRating().encode("utf-8"))
        exp.addData('Question', i)
        exp.addData('Task Name', 'Questionnaire')

        #end of trial - move to next line in data output
        exp.nextEntry()
        
        print 'Example 1: rating =', myRatingScale.getRating().encode("utf-8")
        print 'history =', myRatingScale.getHistory()


def runQuestions(win, ask, language, exp):
    questions(win, ask, language, exp)