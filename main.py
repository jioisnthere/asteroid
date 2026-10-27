import sys
import pygame
from constants import SCREEN_WIDTH,SCREEN_HEIGHT
from player import Player 
from asteroid import Asteroid
from asteroidfield  import AsteroidField
from logger import log_state, log_event
from shot import Shot

def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = updatable
    Player.containers = (updatable,drawable)
    Shot.containers = (shots,updatable,drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    while True:
        log_state()
        for event in pygame.event.get():
            pass
        updatable.update(dt) 
        for __ in asteroids:
            for shot in shots:
                if __.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    __.split()
            if __.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        screen.fill("black")
        for drawh in drawable:
            drawh.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
