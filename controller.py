import pygame
from random import randint

screen_x = 600
screen_y = 600


BLACK = (0,0,0)
RED = (255,0,0)
WHITE = (255,255,255)
DM = (88,245,101)
EXT = (247,186,54)
finish = False
pygame.init()
fnt = pygame.font.Font(None,80)
Ximg = pygame.image.load('RX.jpg')
Oimg = pygame.image.load('RO.jpg')



chkList = [-1 for i in range(10)]
chkList[0] = -2
size = (screen_x,screen_y)
screen = pygame.display.set_mode(size)

locate = {1:[25,25],2:[int((screen_x/3)+25),25],3:[int((2*screen_x/3)+25),25],4:[25,int((screen_y/3)+25)],5:[int((screen_x/3)+25),int((screen_y/3)+25)],6:[int((2*screen_x/3)+25),int((screen_y/3)+25)],7:[25,int((2*screen_y/3)+25)],8:[int((screen_x/3)+25),int((2*screen_y/3)+25)],9:[int((2*screen_x/3)+25),int((2*screen_y/3)+25)]}

winCombo = [[1,2,3],
            [4,5,6],
            [7,8,9],
            [1,4,7],
            [2,5,8],
            [3,6,9],
            [3,5,7],
            [1,5,9]]


def drawBoard():

    screen.fill(WHITE)
    pygame.draw.line(screen, BLACK, [int(screen_x/3), 5],[int(screen_x/3), int(screen_y-5)],5)
    pygame.draw.line(screen, BLACK, [int(2*screen_x/3), 5],[int(2*screen_x/3), int(screen_y-5)],5)
    pygame.draw.line(screen, BLACK, [5, int(screen_y/3)],[int(screen_x-5), int(screen_x/3)],5)
    pygame.draw.line(screen, BLACK, [5, int(2*screen_x/3)],[int(screen_x-5), int(2*screen_x/3)],5)



def move(x,y):
    bNum = findBox(x,y)
    if isEmpty(bNum):
        chkList[bNum] = 1
        screen.blit(Ximg,tuple(locate[bNum]))
        qw = Over()
        if not qw:
            co = findEmpty()
            chkList[co] = 0
            screen.blit(Oimg,tuple(locate[co]))
            qw = Over()


def findBox(x,y):
    abrl = [0 for i in range(4)]
    if x > (2*screen_x/3):
        abrl[2] = 1
    elif x < (screen_x/3):
        abrl[3] = 1
    if y > (2*screen_y/3):
        abrl[1] = 1
    elif y < (screen_y/3):
        abrl[0] = 1
    
    if cmp(abrl,[0,0,0,0]) == 0:
        return 5
    elif cmp(abrl,[1,0,0,1]) == 0:
        return 1
    elif cmp(abrl,[1,0,0,0]) == 0:
        return 2
    elif cmp(abrl,[1,0,1,0]) == 0:
        return 3
    elif cmp(abrl,[0,0,0,1]) == 0:
        return 4
    elif cmp(abrl,[0,0,1,0]) == 0:
        return 6
    elif cmp(abrl,[0,1,0,1]) == 0:
        return 7
    elif cmp(abrl,[0,1,0,0]) == 0:
        return 8
    elif cmp(abrl,[0,1,1,0]) == 0:
        return 9 



def isEmpty(n):
    if chkList[n] != -1:
        return False
    return True


def Over():
    if -1 not in chkList:
        w = heckWinner()
        if not w:
            global finish 
            finish = True
            text = fnt.render("-----Game Drawn----- ",True,RED)
            pygame.draw.rect(screen, WHITE, [25,220, 555,150],0)
            screen.blit (text, (35,250))
            
        return True
    else:
        w = heckWinner()
        return w
        # for i in range(len(winCombo)):
        #     if chkList[winCombo[i][0]] == chkList[winCombo[i][1]] == chkList[winCombo[i][2]]!=-1:
        #         finishGame(winCombo[i][0],winCombo[i][2])
        #         return True
        return False


def heckWinner():
    for i in range(len(winCombo)):
        if chkList[winCombo[i][0]] == chkList[winCombo[i][1]] == chkList[winCombo[i][2]]!=-1:
            finishGame(winCombo[i][0],winCombo[i][2])
            return True
    return False


def findEmpty():
    ind = [i for i,x in enumerate(chkList) if x == -1]
    if 5 in ind:
        return 5
    jk = [ind[j] for j in range(len(ind)) if ind[j]%2 != 0]
    if len(jk) > 0:
        x = randint(0,len(jk)-1)
        return jk[x]
    
    x = randint(0,len(ind)-1)
    return ind[x]


def finishGame(num1,num2):
    global finish 
    finish = True
    pygame.draw.line(screen,DM,[locate[num1][0]+75,locate[num1][1]+75],[locate[num2][0]+75,locate[num2][1]+75],10)
    if chkList[num1] == 1:
        text = fnt.render("X Wins Game Over ",True,RED)
    else:
        text = fnt.render("O Wins Game Over ",True,RED)
    
    pygame.draw.rect(screen, WHITE, [25,220, 555,150],0)
    screen.blit (text, (35,250))


def cmp(a,b):
    return (a>b)-(a<b)
