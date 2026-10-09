import pygame
from constants import *
from logger import log_state
from player import Player

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

    # Initialize groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    # Initialize player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

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

        # Update and draw groups
        updatable.update(dt)

        # Pygame expects certain arguments for draw()
        # that we aren't using, so it's better to iterate
        # over the group normally
        for thing in drawable:
            thing.draw(screen)

        # Refresh screen
        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
