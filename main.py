import pygame
import sys
from constants import *
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

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
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # Initialize asteroid AsteroidField
    field = AsteroidField()

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

        # Check for collision
        for asteroid in asteroids:
            # Check for collision with shots
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()

            # Check for collision with the player
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

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
