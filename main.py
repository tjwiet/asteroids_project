import pygame
import sys
from constants import *
from game import run_game
from menu import display_menu

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize pygame
    pygame.init()

    # Set fps
    clock = pygame.time.Clock()
    dt = 0.0

    # Set text font
    title_font = pygame.font.Font(None, TITLE_FONT_SIZE)
    option_font = pygame.font.Font(None, OPTION_FONT_SIZE)


    # Initialize window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")

    # Start with main menu
    display_menu(clock, dt, screen, title_font, option_font)


    # Start game
    run_game(clock, dt, screen)


if __name__ == "__main__":
    main()
