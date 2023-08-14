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
Ballimage = pygame.image.load( r"Resources\aa.png").convert_alpha()
# Ballimage = pygame.transform. rotate(Ballimage, ( 100))
# Ballimage = pygame.transform.flip(Ballimage, ( False, True))


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
    Ballimage = pygame.transform.scale(Ballimage, (50, 100))

    window.blit(Bgimage, (0, 0))
    window.blit(Ballimage, (200, 300))

    # Update Display
    pygame.display.update()
    #Set FPS
    clock.tick(fps)