import pygame
from constants import *
from logger import log_state

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize pygame
    pygame.init()

    # Initialize window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Run the game
    running = True
    while running:
        log_state()

        # Process event queue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Fill screen
        screen.fill("black")

        # Refresh screen
        pygame.display.flip()


if __name__ == "__main__":
    main()
