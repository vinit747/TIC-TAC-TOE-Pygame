import pygame
import controller as ctr
# from pygame.locals import *

pygame.init()

pygame.display.set_caption("TIC-TAC-TOE")
clock = pygame.time.Clock()


def intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONUP:
                gamegl()        
        ctr.screen.fill(ctr.EXT)
        largeText = pygame.font.Font('freesansbold.ttf',80)
        txt = largeText.render("TIC-TAC-TOE",True,ctr.BLACK)
        ctr.screen.blit(txt,(35,250))
        pygame.display.update()
        clock.tick(15)




def gamegl():
    stopped = False
    ctr.drawBoard()

    while not stopped:
        for event in pygame.event.get():
              
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == MOUSEBUTTONUP :
                if ctr.finish == True:
                    pygame.event.clear()
                    ctr.finish = False
                    ctr.chkList = [-1 for i in range(10)]
                    ctr.chkList[0] = -2
                    intro()
                x,y = event.pos
                ctr.move(x,y)
                print(ctr.finish)
                
                  
        pygame.display.update()
        clock.tick(30)
intro()
gamegl()
pygame.quit()
quit()