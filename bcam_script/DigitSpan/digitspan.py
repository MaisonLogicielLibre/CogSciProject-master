#!/usr/bin/python
import pygame, time, random, math
from pygame.locals import *
#import heginput
pygame.init()
#pygame.mouse.set_visible(False)
pygame.event.set_blocked(pygame.MOUSEMOTION)
# screensize = (1280, 800)
screensize = pygame.display.list_modes()[0]
flags = pygame.constants.FULLSCREEN
screen = pygame.display.set_mode(screensize, flags)

secsperevent = 2.
secstodisplay = 1.
backwards = True
trialsperblock = 15
levelthreshold = 2
startinglevel = 6


black = (0,0,0)
white = (255, 255, 255)

bgColor = black
textColor = white
bigfont = pygame.font.SysFont('timesnewroman', 64)
font = pygame.font.SysFont('timesnewroman', 24)

screen.fill(black)
pygame.display.flip()


class Abort(Exception):
    pass

mouseclicks = []

def readkeyinput():
    pygame.event.clear()
    repeat = True  
    text = ''
    while (repeat):
        newevent = pygame.event.wait()
        if (newevent.type == 2):
            if (newevent.key == K_RETURN):
                repeat = False
            elif (newevent.key == K_BACKSPACE):
                if len(text) > 0:
                    text = text[:-1]
            elif (newevent.key == K_ESCAPE):
                raise Abort
            else:
                text = text + newevent.unicode
        centered_word(text, textColor)
    return text


def mean_sd(vec):
    meanval = sum(vec)/len(vec)
    sd = 0.
    for t in vec:
        sd += (t - meanval)**2
    sd = math.sqrt(sd/ (len(vec)) )
    return meanval, sd
def display_number(n):
    centered_word(n, textColor, font=bigfont)
    sleep(secstodisplay)
    screen.fill(bgColor)
    pygame.display.flip()
    sleep(secsperevent - secstodisplay)
    
def countdown(message):
    screen.fill(bgColor)
    centered_word(message, textColor)
    sleep(3)
    centered_word('Get ready.', textColor)
    sleep(2)
    screen.fill(bgColor)
    pygame.display.flip()
    sleep(1)
    
def centered_word(word, color = textColor, font=font):
    screen.fill(bgColor)
    renderedword = font.render(word, True, color)
    topleft = (screensize[0]/2 - renderedword.get_width()/2, screensize[1]/2 - renderedword.get_height()/2)
    screen.blit(renderedword, topleft)
    pygame.display.flip()
    
def sleep(secs):
    start = time.time()
    while time.time() < start + secs:
        time.sleep(0.0005)
        newevent = pygame.event.poll()
        if newevent.type == 2:
            if newevent.key == K_ESCAPE:
                raise Abort
        elif newevent.type == pygame.MOUSEBUTTONDOWN:
            mouseclicks.append(time.time())

def generateblock(ishigh):
    blocklen = int(secsperblock / secsperevent)
    block = [ishigh for i in range(int(blocklen/updownratio))]
    block.extend([not ishigh for i in range( int( blocklen * (1 - 1/updownratio)))])
    random.shuffle(block)
    return block

def run_block():
    trial = trialsperblock
    level = startinglevel
    points = levelthreshold / 2
    while trial > 0:
        numbers = [random.randint(0,9) for i in range(level)]
        results = runTrial(numbers).strip()
        try:
            resultnumbers = map (int, results)
        except:
            centered_word("Sorry, invalid response.")
            print "Invalid response: %s" % results
            sleep(2)
        if backwards: resultnumbers.reverse()
        if (numbers == resultnumbers):
            points += 1
            centered_word("Correct.")
        else:
            points -= 1
            centered_word("Incorrect.")
        if points >= levelthreshold:
            level += 1
            points = 0
        elif points < 0:
            level -= 1
            points = levelthreshold - 1
        trial -= 1
        sleep(2)
        screen.fill(bgColor)
        pygame.display.flip()
    return level + (points / float(levelthreshold))
            




def runTrial(numbers):
    for number in numbers:
        display_number(str(number))
    centered_word("Type in your answer now.")
    return readkeyinput()
    
    


centered_word("Please type the subject's name.")
subjname = readkeyinput()

if backwards: foo = "backwards"
else: foo = "in order"
centered_word("Remember the numbers presented, then type them back in %s when prompted." % foo)
sleep(5)

span = run_block()
print span

##blocks = [generateblock(blo) for blo in blockpattern]
##btimes = [run_block(block) for block in blocks]
###b1times = run_block(block1)
###b2times = run_block(block2)
##results = [calctimes(btime) for btime in btimes]
##f = file(subjname + ".tova.txt", 'w')
##for i in range(len(results)):
##    f.write("Block %2i:\n" % (i+1))
##    f.write(results[i][-2])
##    f.write('\n')
##f.write(''.join( [''.rjust(16)]+[("Block %2i"%(i+1)).rjust(10) for i in range(len(results))]+['\n'] ))
##f.write(''.join( ['Response time:' .ljust(16)]+[`result[0]`.rjust(10) for result in results]+['\n'] ))
##f.write(''.join( ['Response stdev:'.ljust(16)]+[('%3.1f'%(result[1])).rjust(10) for result in results]+['\n'] ))
##f.write(''.join( ['False hits:'    .ljust(16)]+[`result[2]`.rjust(10) for result in results]+['\n'] ))
##f.write(''.join( ['Misses:'        .ljust(16)]+[`result[3]`.rjust(10) for result in results]+['\n'] ))
##f.write(''.join( ['Double hits:'   .ljust(16)]+[`result[4]`.rjust(10) for result in results]+['\n'] ))
##f.close()
##
##foo = ''
##foo += '%10s%16s%16s%16s%16s%16s\n' %('', 'Response time', 'Response stdev', 'False hits', 'Misses', 'Double hits')
##for i in range(len(results)):
##    foo += '%10s%16i%16.1f%16i%16i%16i\n' % tuple(['Block %2i: '%(i+1)] + list(results[i][:-2]))
##foo +=     '%10s%16i%16.1f%16i%16i%16i\n' % tuple(["Totals:"]+[mean_sd(vec)[0] for vec in [[results[x][y] for x in range(len(results))] for y in range(len(results[0])-2)]])
##foo +=     '%10s%16i%16.1f%16i%16i%16i\n' % tuple(["StDevs:"]+[mean_sd(vec)[1] for vec in [[results[x][y] for x in range(len(results))] for y in range(len(results[0])-2)]])
##print foo
##
##
##
##
#meantime = sum(reactiontimes)/len(reactiontimes)
#sd = 0.
#for t in reactiontimes:
#    sd += (t - meantime)**2
#sd = math.sqrt(sd/ (len(reactiontimes)) )
            

            

    

pygame.display.quit()