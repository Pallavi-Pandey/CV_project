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

start = True
while start:
    # Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            start = False
            pygame.quit()

    # Apply Logic 
    window.fill((255, 255, 255))
    font = pygame.font.SysFont('Resources\BricolageGrotesque-VariableFont_opsz,wdth,wght.ttf', 100)
    font2 = pygame.font.SysFont('arial', 100)
    text = font.render("My Game", True, (70, 60, 50))
    text2 = font2.render("My Game", True, (70, 60, 50))
    window.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
    window.blit(text2, (width/2 - text2.get_width()/2, height/2 - text2.get_height()/2 + 100))
    # Update Display
    pygame.display.update()
    #Set FPS
    clock.tick(fps)