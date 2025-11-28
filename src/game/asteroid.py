import pygame
import src.game.circleshape as circleshape
from src.config.constants import *
import random
from src.utils.logger import log_event

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        old_radius = self.radius
        old_velocity = self.velocity
        self.kill()
        if old_radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20,50)
        v1 = old_velocity.rotate(angle)
        v2 = old_velocity.rotate(-angle)
        new_radius = old_radius - ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = v1 * 1.2
        a2.velocity = v2 * 1.2

