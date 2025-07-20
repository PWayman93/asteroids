import pygame
from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, rotation):
        super().__init__(x, y, SHOT_RADIUS)
        self.rotation = rotation
        
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.velocity = forward * PLAYER_SHOOT_SPEED
        
    def draw (self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
    
    def update (self, dt):
        self.position += self.velocity * dt
