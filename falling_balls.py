import pygame

pygame.init()
size = width, height = 400, 300
screen = pygame.display.set_mode(size)

active_circles_positions = set()


def draw_active_circles():
    for pos in active_circles_positions:
        pygame.draw.circle(screen, (0, 0, 255), pos, 10)


is_running = True
while is_running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("button pressed", event.pos)
            active_circles_positions.add(event.pos)

    draw_active_circles()

    pygame.display.flip()

pygame.quit()
