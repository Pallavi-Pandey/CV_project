# Import Modules
import pygame
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector


# Initialize 
pygame.init()

#Create Window/Display

width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Balloon Pop")

# Webcam
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

imgBalloon = pygame.image.load("Resources/aa.png").convert_alpha()
rectBalloon = imgBalloon.get_rect()
rectBalloon.x,rectBalloon.y = 500,300

speed = 1

detecteor = HandDetector(detectionCon=0.8, maxHands=1)

def resetBalloon():
    rectBalloon.x = np.random.randint(100, width-rectBalloon.width)
    rectBalloon.y = img.shape[0]
    # rectBalloon.x,rectBalloon.y = 500,300

#Initialize Clock f3or FPS
fps = 30
clock = pygame.time.Clock()

start = True
while start:
    # Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            start = False
            pygame.quit()

    # Apply Logic 
    # window.fill((255, 255, 255))

    #OPENCV
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detecteor.findHands(img, flipType=False)

    rectBalloon.y -= speed

    if rectBalloon.y < 0:
        resetBalloon()
        # speed += 1

    import time

    if hands:
        x,y=0,0
        hand = hands[0]
        x, y = hand["lmList"][8][1:]
       
        diff=(x-rectBalloon.x,y-rectBalloon.y)
        print(diff)
        # the above line will give you the x and y coordinates of the tip of the index finger
        # print("hands",x, y)
        # print("baloon", rectBalloon.x, rectBalloon.y)
        # print("colli", rectBalloon.collidepoint(x, y))

        if rectBalloon.collidepoint(x, y):
            print("collide",x,y)
            resetBalloon()


    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    imgRGB = np.rot90(imgRGB)
    frame = pygame.surfarray.make_surface(imgRGB).convert()
    frame = pygame.transform.flip(frame, True, False)
    window.blit(frame, (0, 0))

    
    window.blit(imgBalloon, rectBalloon)

    
    # Update Display
    pygame.display.update()
    #Set FPSz
    clock.tick(fps)