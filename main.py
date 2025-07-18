import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

clock = pygame.time.Clock()

dt = 0

number = 0

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)
    
    player = Player(640, 360)
    
    asteroid_field = AsteroidField()
    
    
    screen = pygame.display.set_mode((1280, 720))
    
    while number == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                
        dt = clock.tick(60) / 1000
                
        screen.fill("black")
        updateable.update(dt)
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        
        


if __name__ == "__main__":
    main()
