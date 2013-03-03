import pygame as pg
import pygame.locals as local
import sys

def main():
    pg.init()

    xres = 800
    yres = 600

    try:
        xres = int(sys.argv[1])
        yres = int(sys.argv[2])

    except IndexError:
        pass

    screen = pg.display.set_mode((xres, yres))
    pg.display.set_caption("future rpg prepreprepalphawhatever")

    pg.mouse.set_visible(1)
    pg.key.set_repeat(1, 30)

    clock = pg.time.Clock()

    rotation_stat = 0.0

    planet01 = pg.image.load("earth.png")
    planet01.set_colorkey((251, 0, 250), local.RLEACCEL)  # load planet01

    sun = pg.image.load("sun.png")  # load sun
    bg = pg.image.load("bg.png")  # load background

    sizedbg = pg.transform.smoothscale(bg, (xres, yres))

    planet_pos = (xres / 5 - planet01.get_width() / 2, yres / 2 - planet01.get_height() / 2)

    running = 1

    xres_cent, yres_cent = xres / 2, yres / 2

    while running:

        clock.tick(30)

        for event in pg.event.get():
            if event.type == local.QUIT:
                running = 0
            if event.type == local.KEYDOWN:
                if event.key == local.K_ESCAPE:
                    pg.event.post(pg.event.Event(local.QUIT))

        rotation_stat += 1
        if rotation_stat % 360 == 0:
            rotation_stat = 0.0

        screen.blit(sizedbg, (0, 0))
        screen.blit(planet01, planet_pos)

        sun_rect = sun.get_rect()
        sun_rotated = pg.transform.rotozoom(sun, rotation_stat, 1)

        center = sun_rotated.get_rect().center
        sun_pos = (xres_cent - center[0], yres_cent - center[1])
        screen.blit(sun_rotated, sun_pos)

        pg.display.flip()

    pg.quit()


if __name__ == "__main__":
    main()
