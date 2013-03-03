import pygame, sys, os, pgext
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
        image = pygame.image.load(fullname).convert_alpha()
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


    ring_img, ring_rect = load_image('circles/G_new.png', -1)
    background, background_rect, = load_image('starBg.png')
    ringx = 0
    ringy = 0
    ring_rect.center = (500, 375)
    direction = 'right'
    rotateBy = 10
    circle_size = 5
    alpha_count = 255
    change = False

    angle = 0
    going = True
    pygame.key.set_repeat(2, 1)
    while going:  # the main game loop
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                going = False
            elif event.type == KEYDOWN and event.key == K_k:
                circle_size += 10
            elif event.type == KEYDOWN and event.key == K_l:
                if not circle_size <= 10:
                    circle_size -= 10
            elif event.type == KEYDOWN and event.key == K_w:
                change = True
                pgext.color.setAlpha(ring_img, alpha_count, 1)
            elif event.type == KEYDOWN and event.key == K_e:
                change = True
                pgext.color.setAlpha(ring_img, alpha_count, 1)
#        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(background, (0, 0))

        for p in pygame.key.get_pressed():
            if not p:
                angle += rotateBy
        ring_imgNew = pygame.transform.smoothscale(ring_img, (circle_size, circle_size))  # .convert_alpha()
        ring_rectNew = ring_imgNew.get_rect()
        ring_rectNew.center = (550, 425)

        print fpsClock.get_fps()
        DISPLAYSURF.blit(ring_imgNew, ring_rectNew)
        fpsClock.tick(FPS)
        pygame.display.update()


    pygame.quit()
    sys.exit()
if __name__ == '__main__':
    main()

