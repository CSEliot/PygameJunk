import pygame, sys, os, pgext, numpy
from pygame.locals import *
from pygame.compat import geterror
from pygame.examples import *
from pygame import examples
from numpy import *

pygame.init()


main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, 'data')

FPS = 30  # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((1000, 750), DOUBLEBUF | HWSURFACE  , 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

zoom_amount = 0.01

def load_image(name, colorkey=None):
    fullname = os.path.join(data_dir, name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print ('Cannot load image:', fullname)
        raise SystemExit(str(geterror()))
    # image = image.convert_alpha()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

def inverted(img):
   inv = pygame.Surface(img.get_rect().size, pygame.SRCALPHA)
   inv.fill((255, 255, 255, 255))
   inv.blit(img, (0, 0), None, BLEND_RGB_SUB)
   return inv

def main():
    image = pygame.image.load("ring_gray.png")
    # set 40% alpha
    pgext.color.setAlpha(image, 50, 2)
    pygame.image.save(image, "out.png")
    # SET REPEAT
    pygame.key.set_repeat(100, 1)

    i = 0
    circ_img = pygame.image.load('ring_gray.png')
    circ_rect = circ_img.get_rect()
    OGCirc_img, _ = load_image('circles/R_small.png')
    ring_img, ring_rect = load_image('ring_new.png', -1)
    background, background_rect, = load_image('starBg.png')
    light, light_rect = load_image('play.png')
    light = light.convert_alpha()
    lightNew = light
    backCrop = pygame.Surface((DISPLAYSURF.get_width(), DISPLAYSURF.get_height()))
    backCrop.blit(background, (0, 0), (0, 0, DISPLAYSURF.get_width(), DISPLAYSURF.get_height()))
    background, background_rect = backCrop.copy(), backCrop.copy().get_rect()
    backTemp = background.copy()
    ringx = 0
    ringy = 0
    circ_rect.center = (500, 375)
    ring_rect.center = (500, 375)
    direction = 'right'
    rotateBy = 10
    circle_size = 100
    alpha_count = 255
    change = False
    fpsList = []
    light_size = 50
    blitIt = False
    lightUp = False
    l_k_dial = 0

    angle = 0
    going = True
#    pygame.key.set_repeat(2, 1)
#    pgext.color.setAlpha(circ_img, 40, 0)
    while going:  # the main game loop
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                going = False
            elif event.type == KEYDOWN and event.key == K_k:
                if l_k_dial <= 200:
                    l_k_dial += .5
                    background = backTemp.copy()
                    pgext.color.multiply(background, l_k_dial)
                    print 'l', l_k_dial
            elif event.type == KEYDOWN and event.key == K_l:
                if l_k_dial >= 0:
                    l_k_dial -= .5
                    background = backTemp.copy()
                    pgext.color.multiply(background, l_k_dial)
                    print 'l', l_k_dial
            elif event.type == KEYDOWN and event.key == K_w:
                # make it brighter
                if light_size <= 255:
                    light_size += 1
                    print light_size
                    pgext.color.hue(background, light_size, 1)
            elif event.type == KEYDOWN and event.key == K_e:
                # make it darker
                if light_size >= 0:
                    light_size -= 1
                    print light_size
                    pgext.color.hue(background, light_size, 1)
            elif event.type == KEYDOWN and event.key == K_s:
                # change hue
                pixarray = pygame.PixelArray(background)
                pixarray.replace((255, 255, 255), (50, 0, 0))
                del pixarray
                print 's'
            elif event.type == KEYDOWN and event.key == K_z:
                # undo
                print 'z'
                background = backTemp.copy()

        print K_LEFT

        i += 1
#         fpsList.append(fpsClock.get_fps())
#         if i == FPS:
#             print mean(fpsList)
#             i = 0
#             fpsList = []
        DISPLAYSURF.fill((0, 0, 0))
        DISPLAYSURF.blit(background, (0, 0))
        fpsClock.tick(FPS)
        pygame.display.update()



    pygame.quit()
    sys.exit()
if __name__ == '__main__':
    main()

