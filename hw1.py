import pygame
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))
        self.color = color

    def update(self, dx=0, dy=0):
        self.rect.x += dx
        self.rect.y += dy

sprite1 = Sprite((255, 0, 0), 200, 300)
sprite2 = Sprite((0, 0, 255), 600, 300)

all_sprites = pygame.sprite.Group()
all_sprites.add(sprite1, sprite2)

special_event = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    dx, dy = 0, 0
    if keys[pygame.K_LEFT]:
        dx = -5
    if keys[pygame.K_RIGHT]:
        dx = 5
    if keys[pygame.K_UP]:
        dy = -5
    if keys[pygame.K_DOWN]:
        dy = 5

    sprite1.update(dx, dy)

    if sprite1.rect.colliderect(sprite2.rect):
        special_event = True

    if special_event:
        sprite1.image = pygame.transform.scale(sprite1.image, (70, 70))
        sprite2.image = pygame.transform.scale(sprite2.image, (70, 70))
        sprite1.image.fill((0, 255, 0))
        sprite2.image.fill((255, 255, 0))

    screen.fill((30, 30, 30))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)