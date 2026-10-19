import pygame
import sys
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from groups import initialize_menu_groups


def create_title(screen, font):
    # Create title surface
    title = font.render("Asteroids", True, (175, 195, 225))
    # Create location for title, right above center of screen
    title_pos = title.get_rect(centerx = screen.get_width() / 2, centery = (screen.get_height() / 2) - 128)
    return title, title_pos


def create_option(screen, font, choice, current_selection, dy):
    if choice["text"] == current_selection:
        render = font.render(choice["text"], True, choice["color"])
    # If not, display in default white
    else:
        render = font.render(choice["text"], True, (255, 255, 255))
    render_pos = render.get_rect(centerx = screen.get_width() / 2, centery = (screen.get_height() / 2) + dy)
    return render, render_pos


def display_menu(clock, dt, screen, title_font, option_font):
    # Initialize groups for background of asteroids
    updatable, drawable, asteroids = initialize_menu_groups()

    # Create asteroid field
    field = AsteroidField()

    # Create title text
    title, title_pos = create_title(screen, title_font)

    choices = [
        {
            "text": "PLAY",
            "color": (80, 255, 80)
        },
        {
            "text": "QUIT",
            "color": (255, 80, 80)
        }
    ]

    current_selection = "PLAY"
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        updatable.update(dt)
        for thing in drawable:
            thing.draw(screen)

        # Add the title to the screen
        screen.blit(title, title_pos)

        # For each option, add the text to the screen
        dy = 128
        for choice in choices:
            render, render_pos = create_option(screen, option_font, choice, current_selection, dy)
            screen.blit(render, render_pos)
            dy += 128

        pygame.display.flip()
        dt = clock.tick(60) / 1000
