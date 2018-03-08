import pygame, sys, time, random
from pygame.locals import *

pygame.init()
mainClock = pygame.time.Clock()

screenWidth = 800
screenHeight = 600
screen = pygame.display.set_mode((screenWidth, screenHeight), 0, 0)
pygame.display.set_caption('First Person')

torch = pygame.Rect([250,305,10,10])
torch2 = pygame.Rect([525,305,10,10])
torchImage = pygame.image.load('torch.png')
torchScaledImage = pygame.transform.scale(torchImage,(10,10))
torch2ScaledImage = pygame.transform.scale(torchImage,(10,10))

moveForward = False
moveBack = False

distDownHall = 20
hallLength = 1000
linePos = 5
torchList = [torch]
torchList2 = [torch2]

def background():
    pygame.draw.polygon(screen, [100,100,100],[[0,0],[400,300],[0,600]]) #Left 
    pygame.draw.polygon(screen, [100,100,100],[[800,0],[400,300],[800,600]]) #Right
    pygame.draw.polygon(screen,[200,200,200],[[0,0],[400,300],[800,0]]) #Up
    pygame.draw.polygon(screen,[200,200,200],[[0,600],[400,300],[800,600]]) #Down
    #pygame.draw.polygon(screen,[0,0,0],[[300,200],[300,400],[500,400],[500,200]]) #Square
    #lines(linePos)
    #torches()

def lines(linePos):
    if linePos == 1:
        for i in range(403,600,50):
            horizontalX1 = (i-600)/(-2.0/3.0)
            horizontalX2 = (i-67)/(2.0/3.0)
            pygame.draw.line(screen, [150,150,150],[horizontalX1,i], [horizontalX2,i],3)

    if linePos == 2:
        for i in range(407,600,50):
            horizontalX1 = (i-600)/(-2.0/3.0)
            horizontalX2 = (i-67)/(2.0/3.0)
            pygame.draw.line(screen, [150,150,150],[horizontalX1,i], [horizontalX2,i],3)
            
    if linePos == 3:
        for i in range(413,600,50):
            horizontalX1 = (i-600)/(-2.0/3.0)
            horizontalX2 = (i-67)/(2.0/3.0)
            pygame.draw.line(screen, [150,150,150],[horizontalX1,i], [horizontalX2,i],3)
            
    if linePos == 4:
        for i in range(418,600,50):
            horizontalX1 = (i-600)/(-2.0/3.0)
            horizontalX2 = (i-67)/(2.0/3.0)
            pygame.draw.line(screen, [150,150,150],[horizontalX1,i], [horizontalX2,i],3)
            
    if linePos == 5:
        for i in range(423,600,50):
            horizontalX1 = (i-600)/(-2.0/3.0)
            horizontalX2 = (i-67)/(2.0/3.0)
            pygame.draw.line(screen, [150,150,150],[horizontalX1,i], [horizontalX2,i],3)
            
    if linePos == 6:
        for i in range(428,600,50):
            horizontalX1 = (i-600)/(-2.0/3.0)
            horizontalX2 = (i-67)/(2.0/3.0)
            pygame.draw.line(screen, [150,150,150],[horizontalX1,i], [horizontalX2,i],3)
            
    if linePos == 7:
        for i in range(433,600,50):
            horizontalX1 = (i-600)/(-2.0/3.0)
            horizontalX2 = (i-67)/(2.0/3.0)
            pygame.draw.line(screen, [150,150,150],[horizontalX1,i], [horizontalX2,i],3)

    if linePos == 8:
        for i in range(438,600,50):
            horizontalX1 = (i-600)/(-2.0/3.0)
            horizontalX2 = (i-67)/(2.0/3.0)
            pygame.draw.line(screen, [150,150,150],[horizontalX1,i], [horizontalX2,i],3)
    if linePos == 9:
        for i in range(443,600,50):
            horizontalX1 = (i-600)/(-2.0/3.0)
            horizontalX2 = (i-67)/(2.0/3.0)
            pygame.draw.line(screen, [150,150,150],[horizontalX1,i], [horizontalX2,i],3)
            
    if linePos == 10:
        for i in range(448,600,50):
            horizontalX1 = (i-600)/(-2.0/3.0)
            horizontalX2 = (i-67)/(2.0/3.0)
            pygame.draw.line(screen, [150,150,150],[horizontalX1,i], [horizontalX2,i],3) 

    for i in range(100,800,100):
        pygame.draw.line(screen, [150,150,150],[i,600],[i/4 + 300 ,401],3)
        
def torches():
    global torch
    global torchScaledImage
    global torch2ScaledImage
    global torchList
    
    if moveForward:
        for element in torchList:
            element.left -= 5
            element.width += 1
            element.height += 1
            torchScaledImage = pygame.transform.scale(torchImage,(element.width,element.height))
        if torchList[0].left < 100: #placeholder value
            torchList.remove(torchList[0])
            torchList.append(pygame.Rect([250,305,10,10]))
            
        for element in torchList2:
            element.left += 5
            element.width += 1
            element.height += 1
            torch2ScaledImage = pygame.transform.scale(torchImage,(element.width,element.height))
        if torchList2[0].right > 700: #placeholder value
            torchList2.remove(torchList2[0])
            torchList2.append(pygame.Rect([525,305,10,10]))
            
    elif moveBack:
        for element in torchList:
            element.left += 5
            element.width -= 1
            element.height -= 1
            torchScaledImage = pygame.transform.scale(torchImage,(torch.width,torch.height))
        if torchList[0].width < 5: 
            torchList.remove(torchList[0])
            torchList.append(pygame.Rect([100,305,50, 50]))
            
    for element in torchList:
        screen.blit(torchScaledImage, element)
    for element in torchList2:
        screen.blit(torch2ScaledImage, element)

#Walls
blueWall = pygame.image.load('BlueWall.png')
redWall = pygame.image.load('RedWall.png')
def walls():
    totalX = 0
    totalY = 0
    for i in range (27,0,-1):
        currStretch = redWall
        height = 600 - (3.0/4.0*(totalX))*2
        currPanel = pygame.Rect(totalX,totalY,i,height)
        currPanelFlip = pygame.Rect(800 - (i + totalX),totalY,i,height)
        if i % 2 == 0:
            currStretch = pygame.transform.scale(redWall,(currPanel.width,currPanel.height))
        else:
            currStretch = pygame.transform.scale(blueWall,(currPanel.width,currPanel.height))
        screen.blit(currStretch,currPanel)
        totalX += i
        totalY = 3.0/4.0*totalX
        totalY = int(round(totalY))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                moveForward = True
                moveBack = False
            if event.key == K_DOWN:
                moveBack = True
                moveForward = False
        if event.type == KEYUP:
            if event.key == K_UP:
                moveForward = False
            if event.key == K_DOWN:
                moveBack = False    
    
    if moveForward and distDownHall <= hallLength:
        distDownHall += 5
    elif distDownHall >= hallLength - 100:
        moveForward = False
    if moveBack and distDownHall >= 0:
        distDownHall -= 5
    elif distDownHall <= 0:
        moveBack = False   
          
    background() 
    walls() 
    '''
    if moveForward == True:
        if linePos == 10:
            linePos = 1
        else:
            linePos+= 1  
        
    elif moveBack == True:
        if linePos == 1:
            linePos = 10
        else:
            linePos -= 1   
   '''
    if distDownHall > 900:
        length = (distDownHall - (hallLength - 100))
        height = (distDownHall - (hallLength - 100)) * 1.5
        pygame.draw.rect(screen, [255,255,255], [[400-length/2,323-height/2],[length,height]],0) 
    
    pygame.display.flip()
    mainClock.tick(60)