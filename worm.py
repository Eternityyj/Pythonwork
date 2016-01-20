import pygame,sys,random
from pygame.locals import*

FPS = 10
winx = 640#(屏幕长度)
winy = 640#(屏幕宽度)
cellsize = 10#(通过cellsize来控制方格大小)

##(游戏界面64*64)
assert (winx%cellsize == 0 and winy%cellsize == 0),'cell number needs to be interger'
cellx = int(winx/cellsize)#(640%10)
celly = int(winy/cellsize)#(640%10)

red = (255,0,0)
green = (0,255,0)
darkgreen = (0,155,0)
gray = (40,40,40)
white = (255,255,255)
black = (0,0,0)

#方向按键
left = 'left'
right = 'right'
down = 'down'
up = 'up'

head = 0

def main():
    global fpsclock,disp

    pygame.init()
    disp = pygame.display.set_mode((winx,winy))
    pygame.display.set_caption('worm')
    disp.fill(black)    
    fpsclock = pygame.time.Clock()

    startanimation()
    
    while True:
        rungame()
        gameover()
        
        
def rungame():
    global FPS
    
    direction = right
    startx = random.randint(5,cellx - 6)
    starty = random.randint(5,celly - 6)
    #定义小蛇
    worm = [{'x': startx, 'y': starty},
             {'x': startx-1, 'y': starty},
             {'x': startx-2, 'y': starty}]
    #定义苹果
    apple = randomapple()


    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                terminal()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT and direction!=right:
                    direction = left
                elif event.key == K_RIGHT and direction!=left:
                    direction = right
                elif event.key == K_UP and direction!=down:
                    direction = up
                elif event.key == K_DOWN:
                    direction = down
                elif event.key == K_ESCAPE:
                    terminal()
                  
        if worm[head]['x'] == cellx or worm[head]['x'] == -1 or worm[head]['y'] == celly or worm[head]['y'] == -1:
            return
        for wormbody in worm[1:]:
            if wormbody['x'] == worm[head]['x'] and wormbody['y'] == worm[head]['y']:
                return
        if worm[head]['x'] == apple['x'] and  worm[head]['y'] == apple['y']:
            apple = randomapple()
            FPS+=1
        else:
            del worm[-1]
            
        if direction == up:
            newhead = {'x':worm[head]['x'],'y':worm[head]['y']-1}
        if direction == down:
            newhead = {'x':worm[head]['x'],'y':worm[head]['y']+1}
        if direction == left:
            newhead = {'x':worm[head]['x']-1,'y':worm[head]['y']}            
        if direction == right:
            newhead = {'x':worm[head]['x']+1,'y':worm[head]['y']}
            
        worm.insert(0,newhead)
        disp.fill(black)
        drawline()
        
        drawworm(worm)
        drawapple(apple)
        drawscore(len(worm)-3)

        pygame.display.update()
        fpsclock.tick(FPS)

          

      
#显示苹果       
def drawapple(coords):

    pygame.draw.rect(disp,red,(coords['x']*cellsize,coords['y']*cellsize,cellsize,cellsize))


#随机显示位置 
def randomapple():
    applex = random.randint(0,cellx-1)
    appley = random.randint(0,celly-1)
    return {'x':applex,'y':appley}

#画小蛇
def drawworm(worm):
    for board in worm:
        x = board['x']*cellsize
        y = board['y']*cellsize
        pygame.draw.rect(disp,darkgreen,(x,y,cellsize,cellsize))
        pygame.draw.rect(disp,green,(x+4,y+4,cellsize-8,cellsize-8))
        

#背景方格线
def drawline():
    for i in range(cellx):
        pygame.draw.line(disp,gray,(i*cellsize,0),(i*cellsize,winy))
    for j in range(celly):
        pygame.draw.line(disp,gray,(0,j*cellsize),(winx,j*cellsize))



#游戏结束    
def terminal():
    pygame.quit()
    sys.exit()

#检查按键
def checkforpress():
    if len(pygame.event.get(QUIT))> 0 :
        terminal()
    keypress = pygame.event.get(KEYUP)
    if len(keypress) == 0:
        return None
    elif len(keypress)>0:
        if keypress[0].key == K_ESCAPE:
            terminal()
        return keypress[0].key

def drawkey():
    basicfont2 = pygame.font.Font('freesansbold.ttf',20)
    textsurf = basicfont2.render('press a key to play',1,white)
    textrect = textsurf.get_rect()
    textrect.topleft = (winx-200,winy-50)
    disp.blit(textsurf,textrect)#
    basicfont3 = pygame.font.Font('freesansbold.ttf',20)
    textsurf1 = basicfont3.render('1120150625',1,white)
    textrect1 = textsurf1.get_rect()
    textrect1.topleft = (winx-630,winy-610)
    disp.blit(textsurf1,textrect1)#
    basicfont4 = pygame.font.Font('freesansbold.ttf',20)
    textsurf2 = basicfont4.render('1120150629',1,white)
    textrect2 = textsurf2.get_rect()
    textrect2.topleft = (winx-630,winy-590)
    disp.blit(textsurf2,textrect2)#
    basicfont5 = pygame.font.Font('freesansbold.ttf',20)
    textsurf3 = basicfont5.render('PythonFinalPro',1,white)
    textrect3 = textsurf3.get_rect()
    textrect3.topleft = (winx-630,winy-630)
    disp.blit(textsurf3,textrect3)

    
    

#开场背景
def startanimation():
    basicfont1 = pygame.font.Font('freesansbold.ttf',100)
    degree1 = 0
    degree2 = 0
    w1surf = basicfont1.render('PGameWorm',1,black,white)#darkgreen
    #w2surf = basicfont1.render('PGameWorm',1,red)
    
    while True:
        disp.fill(black)#black
        drawkey()
        
        rotate1surf = pygame.transform.rotate(w1surf,degree1)
        rotate1rect = rotate1surf.get_rect()
        rotate1rect.center = (winx-320,winy-320)
        
        
        #rotate2surf = pygame.transform.rotate(w2surf,degree2)
        #rotate2rect = rotate2surf.get_rect()
        #rotate2rect.center = (winx-320,winy-320)
        disp.blit(rotate1surf,rotate1rect)
        #disp.blit(rotate2surf,rotate2rect)
        
        degree1+= 0
        #degree2+= 5#7

        if checkforpress():
            pygame.event.get()
            return

        pygame.display.update()
        fpsclock.tick(FPS)

#分数显示
def drawscore(score):

    basicfont3 = pygame.font.Font('freesansbold.ttf',20)
    textsurf = basicfont3.render('score: %d'%score,1,white)
    textrect = textsurf.get_rect()
    textrect.topleft = (winx-100,10)
    disp.blit(textsurf,textrect)

    
#game over定义
def gameover():
    basicfont4 = pygame.font.Font('freesansbold.ttf',100)
    gamesurf = basicfont4.render('Game',1,white)
    gamerect = gamesurf.get_rect()
    gamerect.topleft = (180,80)
    oversurf = basicfont4.render('Over',1,white)
    overrect = oversurf.get_rect()
    overrect.topleft = (200,200)
    disp.blit(gamesurf,gamerect)
    disp.blit(oversurf,overrect)
    drawkey()
    pygame.display.update()
    pygame.time.wait(500)
    checkforpress()

    while True:
        if checkforpress():
            pygame.event.get()
            return



            

if __name__ =='__main__':
    main()
