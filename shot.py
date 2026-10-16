import pygame.gfxdraw
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y) -> None:
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen) -> None:
        pygame.gfxdraw.filled_circle(screen, int(self.position.x), int(self.position.y), int(self.radius), (255, 80, 80))

    def update(self, dt) -> None:
        self.position += self.velocity * dt
