import pygame
from constants import *
import sys
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main ():
    print("Starting asteroids!")
  
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.fill((0, 0, 0))
        pygame.display.flip()

if __name__ == "__main__":
    main()