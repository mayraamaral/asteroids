import pygame
from src.config.constants import *
import src.game.circleshape as circleshape
from src.game.shot import *

class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown_timer = 0

    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        list_points = self.triangle()
        pygame.draw.polygon(screen, "white", list_points, LINE_WIDTH)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.cooldown_timer -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            self.shoot()
        
    def move(self, dt):
        direction = pygame.Vector2(0,1)
        rotated_direction = direction.rotate(self.rotation)
        rotated_direction_w_speed = rotated_direction * PLAYER_SPEED * dt
        self.position += rotated_direction_w_speed

    def shoot(self):
        if(self.cooldown_timer <= 0):
            shot = Shot(self.position.x, self.position.y);
            shot.velocity = pygame.Vector2(0,1)
            shot.velocity.rotate(self.rotation)
            shot.velocity *= PLAYER_SHOOT_SPEED
            self.cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
