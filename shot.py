import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, LINE_WIDTH

class Shot(CircleShape):
    def __init__(self, x, y) -> None:
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen) -> None:
        # draw the shot onto the screen using multiple circles
        # don't use gfxdraw.filled_circle() because it requires ints for position
        drawn_radius = self.radius
        while drawn_radius > 0:
            pygame.draw.circle(screen, (255, 80, 80), (self.position.x, self.position.y), drawn_radius, LINE_WIDTH)
            drawn_radius -= 1


    def update(self, dt) -> None:
        self.position += self.velocity * dt
