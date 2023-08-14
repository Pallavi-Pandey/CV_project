 # Import Modules
import pygame

# Initialize 
pygame.init()

#Create Window/Display
width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Game")

#Initialize Clock for FPS
fps = 30
clock = pygame.time.Clock()

#Load Images
Bgimage = pygame.image.load("Resources\Blue_Background.jpg").convert()
Ballimage = pygame.image.load(r"Resources\aa.png").convert_alpha()
rectBall = Ballimage.get_rect()

rectNew = pygame.Rect(500, 0, 200, 200) 

# Game Loop
start = True
while start:
    # Handle Events 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            start = False
            pygame.quit()

    # Apply Logic 
    # window.fill((255, 255, 255))
    print(rectBall.colliderect(rectNew))
    rectBall.x += 5
    # rectBall.y += 5
    window.blit(Bgimage, (0, 0))

    # pygame.draw.rect(window, (255, 0, 0), rectBall)
    # pygame.draw.rect(window, (0, 255, 0), rectNew)
    window.blit(Ballimage, rectBall)  


    # Update Display
    pygame.display.update()
    #Set FPS
    clock.tick(fps)