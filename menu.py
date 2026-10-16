import pygame
import sys
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from groups import initialize_menu_groups

selections = [
    "PLAY",
    "QUIT"
]

def display_menu(clock, dt, screen):
    updatable, drawable, asteroids = initialize_menu_groups()

    field = AsteroidField()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        updatable.update(dt)
        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000
