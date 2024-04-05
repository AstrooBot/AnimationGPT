# -*- coding: utf-8 -*-
import pygame
import sys

# Inicialización de Pygame
pygame.init()

# Definición de colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Dimensiones de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bola moviendose con las flechas")

# Clase para la bola
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        pygame.draw.circle(self.image, BLACK, (25, 25), 25)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            if self.rect.right < 0:  # Si la bola sale por la izquierda
                self.rect.left = WIDTH  # Aparecer a la derecha
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            if self.rect.left > WIDTH:  # Si la bola sale por la derecha
                self.rect.right = 0  # Aparecer a la izquierda
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
            if self.rect.bottom < 0:  # Si la bola sale por la parte superior
                self.rect.top = HEIGHT  # Aparecer en la parte inferior
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            if self.rect.top > HEIGHT:  # Si la bola sale por la parte inferior
                self.rect.bottom = 0  # Aparecer en la parte superior

# Creación de la bola
ball = Ball()

# Grupo de sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(ball)

# Bucle principal
running = True
while running:
    # Control de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualización de los sprites
    all_sprites.update()

    # Dibujado en la pantalla
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()

    # Limitación de frames por segundo
    pygame.time.Clock().tick(60)

# Finalización de Pygame
pygame.quit()
sys.exit()