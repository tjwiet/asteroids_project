import pygame
import sys
from constants import *
from game import run_game

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize pygame
    pygame.init()

    # Set fps
    clock = pygame.time.Clock()
    dt = 0.0

    # Initialize window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    run_game(clock, dt, screen)


if __name__ == "__main__":
    main()
