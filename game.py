import pygame
import sys
from constants import *
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from groups import initialize_game_groups

def run_game(clock, dt, screen):
    # Initialize groups
    updatable, drawable, asteroids, shots = initialize_game_groups()

    # Initialize asteroid AsteroidField
    field = AsteroidField()

    # Initialize player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Initialize score
    score = 0

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
                    score += 100

            # Check for collision with the player
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                print(f"Score: {score}")
                return

        # Pygame expects certain arguments for draw()
        # that we aren't using, so it's better to iterate
        # over the group normally
        for thing in drawable:
            thing.draw(screen)

        # Refresh screen
        pygame.display.flip()

        dt = clock.tick(60) / 1000

        # add to score
        score += int(dt * 100)
