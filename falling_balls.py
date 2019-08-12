import pygame

pygame.init()
size = width, height = 400, 300
screen = pygame.display.set_mode(size)

is_running = True
while is_running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    pygame.display.flip()

pygame.quit()
