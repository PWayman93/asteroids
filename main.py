import pygame
from constants import *
from player import *

clock = pygame.time.Clock()

dt = 0

number = 0

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    player = Player(640, 360)
    
    screen = pygame.display.set_mode((1280, 720))
    
    while number == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                
        dt = clock.tick(60) / 1000
                
        screen.fill("black")
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        
        


if __name__ == "__main__":
    main()
