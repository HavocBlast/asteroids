import pygame
from asteroid import *
from asteroidfield import *
from constants import *
from player import *
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

     # Groups
    updatable = pygame.sprite.Group()
    drawbable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawbable)
    Asteroid.containers = (asteroids, updatable, drawbable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawbable, shots)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfieldObj = AsteroidField()
    
    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        for obj in drawbable:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

        for obj in updatable:
            obj.update(dt)

        for obj in asteroids:
            if obj.check_collision(player):
                print("Game Over!")
                exit()

        for obj in asteroids:
            for shot in shots:
                if obj.check_collision(shot):
                    obj.split()
                    shot.kill()

if __name__ == "__main__":
    main()
