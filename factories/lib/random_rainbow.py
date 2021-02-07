import pygame
import pygame.gfxdraw
import math
import random
from mss import mss
import pyautogui
import pygetwindow
import time
import PIL

import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 0)


def r(): return random.randint(20, 80)


def save_file(screen, screenWidth, screenHeight):
    try:
        # * Update Screen
        pygame.display.flip()
        rect = pygame.Rect(0, 0, screenWidth, screenHeight)
        print("drew rectangle")
        sub = screen.subsurface(rect)
        print("drew subsurface")
        screenshot = pygame.Surface((screenWidth * 2, screenHeight * 2))
        print("created pygame Surface")
        screenshot.blit(sub, (0, 0))
        print("blit screenshot")
        pygame.image.save(screenshot, filename)

    except:
        print("Failed to save file")


def main(filename, title, screenWidth=400, screenHeight=400):
    pygame.init()
    pygame.display.set_caption(title)

    screen = pygame.display.set_mode((screenWidth, screenHeight))
    clock = pygame.time.Clock()

    white = (255, 255, 255)
    black = (0, 0, 0)

    running = True

    plusX = random.randint(screenWidth // 6, screenWidth // 3)
    plusY = random.randint(screenWidth // 6, screenHeight // 3)

    def draw_flat_line(screen, x1, y1, length, color):
        for x in range(x1, x1 + length):
            pygame.gfxdraw.pixel(screen, x, y1, color)

    def draw_vertical_line(screen, x1, y1, length, color):
        for y in range(y1, y1 + length):
            pygame.gfxdraw.pixel(screen, x1, y, color)

    def draw_plus_sign(screen, x, y, size, color):
        draw_flat_line(screen, x - (size // 2), y, size, color)
        draw_vertical_line(screen, x, y - (size // 2), size, color)

    # Add a new list before our loop starts
    cursorList = []

    # * Try to save file
    # save_file(screen, screenWidth, screenHeight)
    # quit()

    counter = 0
    max_count = random.randint(6000, 10000)
    random_direction = r()
    random_space = r()

    space_mod = random.randint(200, 300)
    direction_mod = random.randint(200, 300)

    while running and counter < max_count:
        screen.fill(black)

        # draw cursorList
        for i, plusSign in enumerate(cursorList):
            rR = math.sin(i * .01) * 127 + 128
            rG = math.sin(i * .01 + 5) * 127 + 128
            rB = math.sin(i * .01 + 10) * 127 + 128

            # Generate a separate fader for all of them to be scaled by
            # Remember, we need from 0 - 1, not -1 to 1, hence the add
            # and divide.
            fader = (math.sin(i * .02) + 1) / 2
            rR = rR * fader
            rG = rG * fader
            rB = rB * fader

            # try changing the value below from .005 - 5.2
            # you'll get some interesting results in between
            sizer = int(math.sin(i * .043) * 35 + 35)
            draw_plus_sign(screen, plusSign[0],
                           plusSign[1], sizer, (rR, rG, rB))

        draw_plus_sign(screen, plusX, plusY, 15, white)

        # loop over each of our cursor positions. if empty, skips
        # First we take top left quarter of screen, make a copy
        cropped = pygame.Surface((screenWidth // 2, screenHeight // 2))
        cropped.blit(screen, (0, 0), pygame.Rect(0, 0,
                                                 screenWidth // 2,
                                                 screenHeight // 2))

        # flip that copy on just the y axis, paste below
        belowFlipped = pygame.transform.flip(cropped, False, True)
        screen.blit(belowFlipped, pygame.Rect(0, screenHeight // 2,
                                              screenWidth // 2, screenHeight))

        # flip original copy on just x axis, paste to the right
        topRight = pygame.transform.flip(cropped, True, False)
        screen.blit(topRight, pygame.Rect(screenWidth // 2, 0,
                                          screenWidth, screenHeight // 2))

        # finally flip both axis, paste bottom right
        bottomRight = pygame.transform.flip(cropped, True, True)
        screen.blit(bottomRight, pygame.Rect(screenWidth // 2,
                                             screenHeight // 2, screenWidth,
                                             screenHeight))

        if counter % space_mod == 0:
            random_space = r()
            space_mod = random.randint(200, 300)
        if counter % direction_mod == 0:
            random_direction = r()
            direction_mod = random.randint(200, 300)

        if random_space % 2 == 0:
            newPlace = [plusX, plusY]
            cursorList.append(newPlace)

        if random_direction <= 50 and plusY > 0:
            plusY = plusY - 1
        elif random_direction <= 100 and plusY < (screenHeight // 2):
            plusY = plusY + 1
        if random_direction <= 50 and random_direction % 2 == 0 and plusX > 0:
            plusX = plusX - 1
        elif random_direction <= 100 and random_direction % 2 == 0 and plusX < (screenWidth // 2):
            plusX = plusX + 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # * Update counter
        counter += 1
        if counter >= max_count:

            # * Reset
            screen.fill(black)
            # draw cursorList
            for i, plusSign in enumerate(cursorList):
                rR = math.sin(i * .01) * 127 + 128
                rG = math.sin(i * .01 + 5) * 127 + 128
                rB = math.sin(i * .01 + 10) * 127 + 128

                # Generate a separate fader for all of them to be scaled by
                # Remember, we need from 0 - 1, not -1 to 1, hence the add
                # and divide.
                fader = (math.sin(i * .02) + 1) / 2
                rR = rR * fader
                rG = rG * fader
                rB = rB * fader

                # try changing the value below from .005 - 5.2
                # you'll get some interesting results in between
                sizer = int(math.sin(i * .043) * 35 + 35)
                draw_plus_sign(screen, plusSign[0],
                               plusSign[1], sizer, (rR, rG, rB))
            plusX = 3 * screenWidth
            plusY = 3 * screenHeight
            draw_plus_sign(screen, plusX, plusY, 15, white)
            # loop over each of our cursor positions. if empty, skips
            # First we take top left quarter of screen, make a copy
            cropped = pygame.Surface((screenWidth // 2, screenHeight // 2))
            cropped.blit(screen, (0, 0), pygame.Rect(0, 0,
                                                     screenWidth // 2,
                                                     screenHeight // 2))

            # flip that copy on just the y axis, paste below
            belowFlipped = pygame.transform.flip(cropped, False, True)
            screen.blit(belowFlipped, pygame.Rect(0, screenHeight // 2,
                                                  screenWidth // 2, screenHeight))

            # flip original copy on just x axis, paste to the right
            topRight = pygame.transform.flip(cropped, True, False)
            screen.blit(topRight, pygame.Rect(screenWidth // 2, 0,
                                              screenWidth, screenHeight // 2))

            # finally flip both axis, paste bottom right
            bottomRight = pygame.transform.flip(cropped, True, True)
            screen.blit(bottomRight, pygame.Rect(screenWidth // 2,
                                                 screenHeight // 2, screenWidth,
                                                 screenHeight))

        # * Update Screen
        pygame.display.flip()

    # * Try to save file
    with mss() as sct:
        sct.shot()
        im = PIL.Image.open('monitor-1.png')
        im_crop = im.crop((0, 100, screenWidth*2, screenHeight*2))
        im_crop.save(filename, quality=95)
        os.remove('monitor-1.png', dir_fd=None)


if __name__ == "__main__":
    filename = "test_images/test.png"
    main(filename, "Rainbow Mirror " + str(1), 1200, 1200)
