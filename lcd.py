#Chris Kopacz
#created: 19 July 2017
#filename: lcd.py
#mimic an lcd character display using python/pygame graphics modules

import pygame
from pygame.locals import *
import time
import letters
import lines

def main():
    olive = (182,244,66)
    slate = (25,34,58)

    single_width = 150
    single_height = 210
    dot_hw = 30

    blank = ' '
    numChars = 4
    leadingBlanks = 4*blank
    message = ''

    win_width = numChars*single_width
    win_height = single_height

    messageList = []

    #get user input
    userIn = raw_input('Enter your message:\n>>>')     
    message = leadingBlanks + userIn + leadingBlanks
    messageList = list(message)

    #init pygame
    pygame.init()
    if pygame.display.get_init() == 1:
        pygame.display.quit()
    #init window
    screen = pygame.display.set_mode((win_width,win_height))
    screen.fill(olive)
    pygame.display.update()

    """
    #display message
    for iter in range(0,len(message)):
        grid = letters.get_grid(message[iter])
        screen.fill(olive)
        pygame.display.update()
        time.sleep(0.1)
        
        for jter in range(0,len(grid)):
            x = grid[jter]%10
            y = int(grid[jter]/10)
            newx = x*dot_hw
            newy = y*dot_hw
            pygame.draw.rect(screen,slate,(newx,newy,dot_hw,dot_hw),0)
        
        lines.drawLines(screen,win_width,win_height,dot_hw,olive)
        pygame.display.update()
        time.sleep(1)
        """
    #display scrolling message
    while len(messageList) > 0:
        if len(messageList) >= numChars:
            time.sleep(1)
            screen.fill(olive)
            pygame.display.update()
            #time.sleep(1)
            for iter in range(0,numChars):
                grid = letters.get_grid(messageList[iter])
                #screen.fill(olive)
                #pygame.display.update()
                #time.sleep(0.1)

                for jter in range(0,len(grid)):
                    x = grid[jter]%10
                    y = int(grid[jter]/10)
                    newx = x*dot_hw + iter*single_width
                    newy = y*dot_hw
                    pygame.draw.rect(screen,slate,(newx,newy,dot_hw,dot_hw),0)

                lines.drawLines(screen,win_width,win_height,dot_hw,olive,single_width)
                pygame.display.update()
                #time.sleep(0.1)
            messageList.pop(0)
        else:
            break

    #cleanup and quit
    time.sleep(5)
    pygame.quit()
    print('exit')
#============================

if __name__ == "__main__":
    main()
