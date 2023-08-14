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
# pygame.display.set_icon(pygame.image.load("favicon.ico"))

start = True
while start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            start = False
            pygame.quit()

    # Apply Logic 
    window.fill((255, 255, 255))
    red, green, blue, gokul = (255, 0, 0), (0, 255, 0), (0, 0, 255), (255,192,203)
    # Apply Shapes
    pygame.draw.polygon(window, red, ((491, 100), (788, 100), (937, 357),
                                       (788, 614), (491, 614), (342, 357)))
    pygame.draw.circle(window, green, (640, 360), 200)
    pygame.draw.line(window, blue, (468, 392), (812,392),10)
    pygame.draw.rect(window, gokul, (468, 307, 345, 70), border_radius=100)

    # Update Display
    pygame.display.update()
    #Set FPS
    clock.tick(fps)

    