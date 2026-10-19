import pygame
import sys
from constants import *
from game import run_game
from menu import run_menu

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

    playing = True
    try:
        while playing:
            # Start with main menu
            choice = run_menu(clock, dt, screen, title_font, option_font)
            if choice == "PLAY":
                print("Playing game")
                # Start game
                run_game(clock, dt, screen)
            elif choice == "QUIT":
                print("Quitting game")
                playing = False
            else:
                print("Here for some reason")
                raise Exception(f"Invalid choice: {choice}")

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
