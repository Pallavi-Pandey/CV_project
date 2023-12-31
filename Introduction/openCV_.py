# Import Modules
import pygame
import cv2
import numpy as np


# Initialize 
pygame.init()

#Create Window/Display
width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Game")

# Webcam
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)


#Initialize Clock for FPS
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
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    imgRGB = np.rot90(imgRGB)
    frame = pygame.surfarray.make_surface(imgRGB).convert()
    frame = pygame.transform.flip(frame, True, False)
    window.blit(frame, (0, 0))

    # Update Display
    pygame.display.update()
    #Set FPS
    clock.tick(fps)