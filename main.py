import pygame
from constants import *
import sys
from circleshape import *
from player import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
dt = 0
x = SCREEN_WIDTH / 2
y = SCREEN_HEIGHT / 2

def main ():

    player = Player(x, y)
    print("Starting asteroids!")
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                running = False
        
        screen.fill((0, 0, 0))
        pygame.display.flip()
        dt = clock.tick(60) / 1000.0
        player.draw(screen)


if __name__ == "__main__":
    main()