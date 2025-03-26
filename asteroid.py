import random
from circleshape import CircleShape
import pygame

from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen, pygame.color.Color("white"), self.position, self.radius, 2
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            split_angle = random.uniform(20.0, 50.0)
            new_vector_a = self.velocity.rotate(split_angle)
            new_vector_b = self.velocity.rotate(-1 * split_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)

            new_asteroid_a.velocity = new_vector_a * 1.2
            new_asteroid_b.velocity = new_vector_b * 1.2
