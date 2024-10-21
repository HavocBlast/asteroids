import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            first_vector = pygame.Vector2(self.velocity.rotate(angle))
            second_vector = pygame.Vector2(self.velocity.rotate(-angle))
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            first = Asteroid(self.position.x, self.position.y, new_radius)
            first.velocity = first_vector * 1.2

            second = Asteroid(self.position.x, self.position.y, new_radius)
            second.velocity = second_vector * 1.2
        self.kill()
