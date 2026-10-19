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
    if choice["num"] == current_selection:
        render = font.render(choice["text"], True, choice["color"])
    # If not, display in default white
    else:
        render = font.render(choice["text"], True, (255, 255, 255))
    render_pos = render.get_rect(centerx = screen.get_width() / 2, centery = (screen.get_height() / 2) + dy)
    return render, render_pos

def update_menu(choices_len, current_selection) -> tuple[int, bool]:
    keys = pygame.key.get_pressed()
    new_selection = current_selection
    chosen = False

    if keys[pygame.K_w] and current_selection > 0:
        new_selection -= 1
    if keys[pygame.K_s] and current_selection < choices_len:
        new_selection += 1
    if keys[pygame.K_SPACE]:
        chosen = True

    return new_selection, chosen



def run_menu(clock, dt, screen, title_font, option_font):
    # Initialize groups for background of asteroids
    updatable, drawable, asteroids = initialize_menu_groups()

    # Create asteroid field
    field = AsteroidField()

    # Create title text
    title, title_pos = create_title(screen, title_font)

    choices = [
        {
            "num": 0,
            "text": "PLAY",
            "color": (80, 255, 80)
        },
        {
            "num": 1,
            "text": "QUIT",
            "color": (255, 80, 80)
        }
    ]

    current_selection = 0
    undecided = True
    while undecided:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        current_selection, chosen = update_menu(len(choices) - 1, current_selection)

        # Fill background with black color
        screen.fill("black")

        # Update asteroids
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
        if chosen:
            return choices[current_selection]["text"]
