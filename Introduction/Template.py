# # Import Modules
# import pygame

# # Initialize 
# pygame.init()

# #Create Window/Display
# width, height = 1280, 720
# window = pygame.display.set_mode((width, height))
# pygame.display.set_caption("My Game")

# #Initialize Clock for FPS
# fps = 30
# clock = pygame.time.Clock()

# start = True
# while start:
#     # Handle Events
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT: 
#             start = False
#             pygame.quit()

#     # Apply Logic 
#     window.fill((255, 255, 255))

#     # Update Display
#     pygame.display.update()
#     #Set FPS
#     clock.tick(fps)
import pygame

pygame.init()
# the above line is necessary for every pygame program

width, height = 1280, 720
window = pygame.display.set_mode((width, height))
# the above line creates a window of size 1280x720 and stores it in a variable called window
pygame.display.set_caption("My Game")
# the above line sets the title of the window to "My Game" (you can change this to whatever you want)
fps = 30
clock = pygame.time.Clock()
# by default the favicon is the pygame logo, you can change this by adding a .ico file to the folder and adding the line below

start = True
while start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            start = False
            pygame.quit()

    # Apply Logic 
    window.fill((255, 255, 255))

    # Update Display
    pygame.display.update()
    #Set FPS
    clock.tick(fps)