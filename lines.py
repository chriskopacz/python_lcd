import pygame

def drawLines(screen,w,h,block,color,single_w):
    #draw vertical lines
    for iter in range(0,int(w/block)+1):
        if (iter*block)%single_w == 0:
            pygame.draw.lines(screen,color,True,[(iter*block,0),(iter*block,h)],7)
        else:
            pygame.draw.lines(screen,color,True,[(iter*block,0),(iter*block,h)],1)

    #draw horizontal lines
    for jter in range(0,int(h/block)+1):
        pygame.draw.lines(screen,color,True,[(0,jter*block),(w,jter*block)],1)
