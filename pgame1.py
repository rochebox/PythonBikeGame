import pygame
import sys
from random import randint

pPurple = (114, 14, 186)
bSky = (4, 243, 247)
pygame.init()
sWidth = 1000
sHeight = 500
sSize = (sWidth, sHeight)
s = pygame.display.set_mode(sSize)
pygame.display.set_caption("Bicycle Game")
picList = [ ]
curPic  = 0
bScale= 0.4  # 30% of full size
bikeX=0
bikeY=0
bRect = 0
back1Rect = 0
back2Rect = 0
cRect = 0
cSpeed = randint(2,5)

def moveCandy():
    cRect[0] -= cSpeed
    if cRect[0] < -(cRect[2] + 10):
        cRect[0] = sWidth + 10

def moveBackground():
    back1Rect[0] -=1
    back2Rect[0] -=1
    if back1Rect[0] < -(back1Rect[2]+10):
        back1Rect[0] = back2Rect[0]+back2Rect[2]
    if back2Rect[0] < -(back2Rect[2]+10):
        back2Rect[0] = back1Rect[0]+back1Rect[2]
    

#Tree
#t1 = pygame.image.load("tree.png")
#t1Rect = t1.get_rect()

# loop to set up filenames for all of the pictures
for i in range(30):
    fn = "bike/frame_"
    if i < 10:
        fn = fn + "0" + str(i)
    else:
        fn = fn + str(i)

    fn += "_delay-0.03s.gif"
    #print(fn)
    bikeIcon = pygame.image.load(fn)
    bRect = bikeIcon.get_rect()
    bikeIcon = pygame.transform.scale(bikeIcon, (int(bRect[2]*bScale), int(bRect[3]*bScale)))
    bRect = bikeIcon.get_rect()
    picList.append(bikeIcon)
    
    #print(picList)
#bRect[1] is xLoc
#bRect[2] is yLoc
#bRect[3] is width
#bRect[4] is height

bSMRect = (int((sWidth/2)-(bRect[2]/2)),\
           int((sHeight)-(bRect[3])-(bRect[3] * 0.1)) ,bRect[2], bRect[3])

#print(bRect)
#print(bSMRect)

back1Icon = pygame.image.load("road1T1.png")
back1Icon = pygame.transform.scale(back1Icon, (sWidth +20, sHeight))
back1Rect = back1Icon.get_rect()

back2Icon = pygame.image.load("road1T2.png")
back2Icon = pygame.transform.scale(back2Icon, (sWidth +20, sHeight))
back2Rect = back2Icon.get_rect()

back2Rect[0] = sWidth+20
print(back1Rect)
print(back2Rect)

#box1 = pygame.image.load("smBox1.png")
cScale = 0.15
cHeightFactor = 50
candy1 = pygame.image.load("kiss.png")
cRect = candy1.get_rect()
candy1 = pygame.transform.scale(candy1, (int(cRect[2]*cScale), int(cRect[3]*cScale)))
cRect = candy1.get_rect()
cRect[0] = sWidth - cRect[2]  #this moves the x coordinate
cRect[1] = sHeight - cRect[3] + cHeightFactor




# -----BIG GAME LOOP  --- DRAWING LOOP

while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("You should quit")
            pygame.quit()
            sys.exit()       
    s.fill(bSky)
    s.blit( back1Icon, back1Rect )
    s.blit( back2Icon, back2Rect )
    s.blit(candy1,cRect)
    s.blit( picList[curPic] , bSMRect)
    #s.blit( t1, t1Rect)

    
    curPic += 1
    #list management
    if curPic >= len(picList):
        curPic = 0

    
    pygame.display.update()
    moveBackground()
    moveCandy()
