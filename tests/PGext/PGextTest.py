import pygame, time, pgext
from pygame.locals import *


def main():

    # Initialize Everything
    pygame.init()
    user_screen_data = pygame.display.Info()
    window_width = user_screen_data.current_w
    window_height = user_screen_data.current_h
    window_size = (window_width, window_height)
    #ignore mouse motion input
    pygame.event.set_blocked((pygame.MOUSEMOTION, pygame.ACTIVEEVENT, pygame.KEYUP))
    screen = pygame.display.set_mode(window_size, FULLSCREEN, 32)
    pygame.display.set_caption('PGext testing.')
    pygame.mouse.set_visible(0)

    # Create The Backgound
    mySurface = pygame.Surface(screen.get_size())
    mySurface = mySurface.convert()
    mySurface.fill((255,255,255))
    screen.blit(mySurface, (0,0))

    orig_image = pygame.image.load('sourced.png')
    picture_size = (window_width/7, window_height/4)
    # resize the image to fit for a 28th of the screen.
    orig_image = pygame.transform.smoothscale(orig_image, picture_size)
    image = orig_image.copy()
    image_rect = image.get_rect()
    
    screen.blit(image, (picture_size[0]*0,picture_size[1]*0))
    pygame.display.flip()
    pygame.event.wait()    
    
    """TESTING all PGext functions! if one doesn't work,
    just comment out the 2 lines: "pygame.display.flip" and
    the print line."""
    
    pgext.color.setColor(image, (255,0,0))
    image_rect = image.get_rect()
    # blit by a part of the grid.
    screen.blit(image, (picture_size[0]*1,picture_size[1]*0))
    pygame.display.flip()
    print "color.setColor Passed"
    pygame.event.wait()    


    image = orig_image.copy()
    image_rect = image.get_rect()
    pgext.color.setAlpha(image, 50, 1)
    # blit by a part of the grid.
    screen.blit(image, (picture_size[0]*2,picture_size[1]*0))
    pygame.display.flip()
    print "color.setAlpha Passed"
    pygame.event.wait() 
    
    image = orig_image.copy()
    image_rect = image.get_rect()
    pgext.color.setAlpha(image, 0, 1)
    # blit by a part of the grid.
    screen.blit(image, (picture_size[0]*2,picture_size[1]*0))
    pygame.display.flip()
    print "color.setAlpha Passed"
    pygame.event.wait()
    
    image = orig_image.copy()
    image_rect = image.get_rect()
    image = pgext.color.alphaMask(image, image)
    # blit by a part of the grid.
    screen.blit(image, (picture_size[0]*3,picture_size[1]*0))
    pygame.display.flip()
    print "color.alphaMask Passed"
    pygame.event.wait()
    
    
    image = orig_image.copy()
    image_rect = image.get_rect()
    pgext.color.hue(image, 100, 1)
    # blit by a part of the grid.
    screen.blit(image, (picture_size[0]*4,picture_size[1]*0))
    pygame.display.flip()
    print "color.hue Passed"
    pygame.event.wait()
    
    image = orig_image.copy()
    image_rect = image.get_rect()
    pgext.color.saturation(image, 100, 1)
    # blit by a part of the grid.
    screen.blit(image, (picture_size[0]*5,picture_size[1]*0))
    pygame.display.flip()
    print "color.saturation Passed"
    pygame.event.wait()

    image = orig_image.copy()
    image_rect = image.get_rect()
    pgext.color.value(image, -50)
    # blit by a part of the grid.
    screen.blit(image, (picture_size[0]*6,picture_size[1]*0))
    pygame.display.flip()
    print "color.value Passed"
    pygame.event.wait()

    image = orig_image.copy()
    image_rect = image.get_rect()
    pgext.color.lightness(image, 20)
    # blit by a part of the grid.
    screen.blit(image, (picture_size[0]*0,picture_size[1]*1))
    pygame.display.flip()
    print "color.lightness Passed"
    pygame.event.wait()
    
    image = orig_image.copy()
    image_rect = image.get_rect()
    pgext.color.multiply(image, 20)
    # blit by a part of the grid.
    screen.blit(image, (picture_size[0]*1,picture_size[1]*1))
    pygame.display.flip()
    print "color.multiply Passed"
    pygame.event.wait()

    image = orig_image.copy()
    image_rect = image.get_rect()
    pgext.color.greyscale(image, 1)
    # blit by a part of the grid.
    screen.blit(image, (picture_size[0]*2,picture_size[1]*1))
    pygame.display.flip()
    print "color.greyscale Passed"
    pygame.event.wait()
    
    image = orig_image.copy()
    image_rect = image.get_rect()
    pgext.color.invert(image)
    # blit by a part of the grid.
    screen.blit(image, (picture_size[0]*3,picture_size[1]*1))
    pygame.display.flip()
    print "color.invert Passed"
    pygame.event.wait()
    
    image = orig_image.copy()
    image_rect = image.get_rect()
    pgext.color.contrast(image, -80)
    # blit by a part of the grid.
    screen.blit(image, (picture_size[0]*4,picture_size[1]*1))
    pygame.display.flip()
    print "color.contrast Passed"
    pygame.event.wait()
    
    image = orig_image.copy()
    image_rect = image.get_rect()
    pgext.color.brightness(image, 80)
    # blit by a part of the grid.
    screen.blit(image, (picture_size[0]*5,picture_size[1]*1))
    pygame.display.flip()
    print "color.brightness Passed"
    pygame.event.wait()
    
    image = orig_image.copy()
    image_rect = image.get_rect()
    pgext.color.colorize(image, 0, 200, -30, 10)
    # blit by a part of the grid.
    screen.blit(image, (picture_size[0]*6,picture_size[1]*1))
    pygame.display.flip()
    print "color.colorize Passed"
    pygame.event.wait()
    
    image = orig_image.copy()
    image_rect = image.get_rect()
    image = pgext.filters.shadow(image, (0,0,0), 5,1, 0.9)
    # blit by a part of the grid.
    screen.blit(image, (picture_size[0]*0,picture_size[1]*2))
    pygame.display.flip()
    print "filter.shadow Passed"
    pygame.event.wait()
    
    image = orig_image.copy()
    image_rect = image.get_rect()
    gradient = pgext.filters.gradient((256, 256), (255, 0, 0, 0), (0, 0, 255, 200 ), 0, 0.3)
    image.blit(gradient, (0,0))
    # blit by a part of the grid.
    screen.blit(image, (picture_size[0]*1,picture_size[1]*2))
    pygame.display.flip()
    print "filter.gradient Passed"
    pygame.event.wait()
    
    image = orig_image.copy()
    image_rect = image.get_rect()
    pgext.filters.blur(image, 4 )
    # blit by a part of the grid.
    screen.blit(image, (picture_size[0]*2,picture_size[1]*2))
    pygame.display.flip()
    print "filter.blur Passed"
    pygame.event.wait()
    
    image = orig_image.copy()
    image_rect = image.get_rect()
    pgext.filters.hvBlur(image, 4 )
    # blit by a part of the grid.
    screen.blit(image, (picture_size[0]*3,picture_size[1]*2))
    pygame.display.flip()
    print "filter.hvBlur Passed"
    pygame.event.wait()
    
    image = orig_image.copy()
    image_rect = image.get_rect()
    pgext.filters.noise(image, 55, 2)
    # blit by a part of the grid.
    screen.blit(image, (picture_size[0]*4,picture_size[1]*2))
    pygame.display.flip()
    print "filter.noise Passed"
    pygame.event.wait()
    
    image = orig_image.copy()
    image_rect = image.get_rect()
    pgext.filters.noiseBlur(image, 5 )
    # blit by a part of the grid.
    screen.blit(image, (picture_size[0]*5,picture_size[1]*2))
    pygame.display.flip()
    print "filter.noiseBlur Passed"
    pygame.event.wait()
    
    image = orig_image.copy()
    image_rect = image.get_rect()
    pgext.filters.scratch(image, 5)
    # blit by a part of the grid.
    screen.blit(image, (picture_size[0]*6,picture_size[1]*2))
    pygame.display.flip()
    print "filter.scratch Passed"
    pygame.event.wait()
    
    image = orig_image.copy()
    image_rect = image.get_rect()
    pgext.filters.pixelize(image, 10)
    # blit by a part of the grid.
    screen.blit(image, (picture_size[0]*0,picture_size[1]*3))
    pygame.display.flip()
    print "filter.pixelize Passed"
    pygame.event.wait()
    
    image = orig_image.copy()
    image_rect = image.get_rect()
    pgext.filters.ripple(image, 30, 4)
    # blit by a part of the grid.
    screen.blit(image, (picture_size[0]*1,picture_size[1]*3))
    pygame.display.flip()
    print "filter.ripple Passed"
    pygame.event.wait()
main()