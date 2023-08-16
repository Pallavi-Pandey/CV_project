# Import Modules
import pygame

# Initialize 
pygame.init()

#Create Window/Display
width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("My GUI")

#Initialize Clock for FPS
fps = 30
clock = pygame.time.Clock()

# Colors
c = { "lightgreen": (189,209,197),
      "darkgreen": (158, 171, 162),
      "lightorange": (238, 204, 140),
      "darkpink": (211, 162, 157),
      "lightgrey": (204, 204, 204),
      "darkgrey": (128, 126, 126),
      "black": (0, 0, 0),
      "white": (255, 255, 255),
      "lightpink": (232, 178, 152),
      "yellow": (255, 255, 0),
      "orange": (255, 128, 0),
      "darkbrown": (102, 51, 0),
      }

def resize_image(image, width, height):
    return pygame.transform.scale(image, (width, height))

new_width = 50
new_height = 50

imgBG = pygame.image.load("Resources\Blue_Background.jpg").convert()
imgDes = pygame.image.load("Resources\design.jpg").convert_alpha()
imgbulb = pygame.image.load("Resources\Bulb.png").convert_alpha()
imgdart = pygame.image.load("Resources\dart.png").convert_alpha()
imgfilter = pygame.image.load("Resources\Filter.png").convert_alpha()
imgthumb = pygame.image.load("Resources\Thumb.png").convert_alpha()
imgtoggle_on = pygame.image.load("Resources\Toggle_on.png").convert_alpha()
imgtoggle_off = pygame.image.load("Resources\Toggle_off.png").convert_alpha()
imgshadow = pygame.image.load("Resources\shadow.png").convert_alpha()
imgbulb = resize_image(imgbulb, new_width, new_height)
imgdart = resize_image(imgdart, new_width, new_height)
imgfilter = resize_image(imgfilter, new_width, new_height)
imgthumb = resize_image(imgthumb, new_width, new_height)
imgtoggle_on = resize_image(imgtoggle_on, new_width, new_height)
imgtoggle_off = resize_image(imgtoggle_off, new_width, new_height)
imgshadow = resize_image(imgshadow, new_width, new_height)


pads = [{"no":1, "color": c["lightgreen"], "text": "Original", "icon":imgbulb},
        {"no":2, "color": c["lightorange"], "text": "Grey Scale", "icon":imgdart},
        {"no":3, "color": c["lightpink"], "text": "Edges", "icon":imgthumb},
        {"no":4, "color": c["darkpink"], "text": "Contours", "icon":imgfilter}]

         
def drawWindowPad(pos, color, text, icon):
    xo, yo, w, h = pos
    window.blit(imgshadow, (xo, yo+h -66))
    pygame.draw.rect(window, color, (xo, yo, w, 64),
                     border_top_left_radius=10, border_top_right_radius=10)
    pygame.draw.rect(window, c['white'], (xo, yo+64, w, h-87),
                     border_bottom_left_radius=10, border_bottom_right_radius=10)
    window.blit(icon, (xo+20, yo+12))
    font = pygame.font.SysFont("Arial", 20)
    text = font.render(text, True, c['darkbrown'])
    window.blit(text, (xo+82, yo+20))

def drawfilterPad():
    drawWindowPad((75, 57, 312, 582), c["darkgreen"], "Filter", imgfilter)
    
    font = pygame.font.SysFont("Arial", 20)
    #1
    text1 = font.render("Grey Scale", True, c['darkbrown'])
    window.blit(text1, (106, 165))
    window.blit(imgtoggle_on, (283, 164))
    #2
    text2 = font.render("Edges", True, c['darkbrown'])
    window.blit(text2, (106, 165+60))
    window.blit(imgtoggle_on, (283, 164+60))
    #3
    text3 = font.render("Contours", True, c['darkbrown'])
    window.blit(text3, (106, 165+60*2))
    window.blit(imgtoggle_off, (283, 164+60*2))
    #4
    text4 = font.render("Blur", True, c['darkbrown'])
    window.blit(text4, (106, 165+60*3))
    window.blit(imgtoggle_off, (283, 164+60*3))

    #Sliders
    font = pygame.font.SysFont("Arial", 15)
    for y in range(0,3):
        h =447+y*55
        sliderPos = 105 + 50*y + 30 
        pygame.draw.line(window, c['lightgrey'], (105, h), (105+155, h), 5)
        pygame.draw.line(window, c['darkgrey'], (105, h), (sliderPos, h), 5)
        pygame.draw.rect(window, c['darkgrey'], (sliderPos-5, h-15, 12, 30))
        textDisp = font.render(str(50*y), True, c['darkbrown'])
        window.blit(textDisp, (286, h-18))


def drawAll():
    w, h = 312, 301
    gapW, gapH = 72, 25
    drawWindowPad((484, 57, w, h), pads[0]['color'], pads[0]['text'], pads[0]['icon'])
    drawWindowPad((484+gapW+w, 57, w, h), pads[1]['color'], pads[1]['text'], pads[1]['icon'])
    drawWindowPad((484, 57+gapH+h, w, h), pads[2]['color'], pads[2]['text'], pads[2]['icon'])
    drawWindowPad((484+gapW+w, 57+gapH+h, w, h), pads[3]['color'], pads[3]['text'], pads[3]['icon'])
    drawfilterPad()

start = True
while start:
    # Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            start = False
            pygame.quit()

    # Apply Logic 
    window.blit(imgBG, (0,0)) 
    imgDes.set_alpha(0)
    window.blit(imgDes, (0,0))

    drawAll()

    # Update Display
    pygame.display.update()
    #Set FPS
    clock.tick(fps)