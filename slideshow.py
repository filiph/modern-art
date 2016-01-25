from glob import glob
import traceback
import pygame
import sys


def main():
    white = (255, 255, 255)
    black = (0, 0, 0)
    w = 160
    h = 128
    screen_ratio = float(w) / h
    pygame.init()
    screen = pygame.display.set_mode((w, h))
    screen.fill(black)

    filepaths = glob("paintings/*.jpg")
    filepaths_index = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        path = filepaths[filepaths_index]

        # noinspection PyBroadException
        try:
            img = pygame.image.load(path)
            ratio = float(img.get_width()) / img.get_height()
            # width, height, left, top = None, None, 0, 0
            # if ratio > screen_ratio:
            #     width = int(round(float(img.get_width()) * w / img.get_height()))
            #     height = h
            #     left = int((w - width) / 2)
            # if ratio <= screen_ratio:
            width = w
            height = int(round(w / ratio))
            top, left = 0, 0
            if height <= h:
                top = int((h - height) / 2)
            else:
                top = int((h - height) / 4)
            img = pygame.transform.smoothscale(img, (width, height))
            screen.fill(black)
            screen.blit(img, (left, top))
            pygame.display.flip()
        except:
            traceback.print_exc(file=sys.stdout)

        pygame.time.wait(500)
        screen.fill(black)
        pygame.display.flip()
        pygame.time.wait(100)
        filepaths_index = (filepaths_index + 1) % len(filepaths)


if __name__ == "__main__":
    main()