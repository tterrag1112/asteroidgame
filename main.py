import sys

import pygame
import asteroid
import asteroidfield
import player
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
import shot

def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0.0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    player.Player.containers = (updatable, drawable)
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable)
    shot.Shot.containers = (shots, drawable, updatable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    ship = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = asteroidfield.AsteroidField()


    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for rock in asteroids:
            if rock.collides_with(ship):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for rock in asteroids:
            for pew in shots:
                if pew.collides_with(rock):
                    log_event("asteroid_shot")
                    pew.kill()
                    rock.split()
        screen.fill("black")
        for drawn in drawable:
            drawn.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000
        #print(f"dt value = {dt}")


if __name__ == "__main__":
    main()
