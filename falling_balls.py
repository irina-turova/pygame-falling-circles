import pygame

pygame.init()
size = width, height = 400, 300
screen = pygame.display.set_mode(size)
baked_screen = pygame.Surface(screen.get_size())

clock = pygame.time.Clock()

circle_color = (0, 0, 255)
circle_radius = 10
pixels_per_second_speed = 100
active_circles_positions = set()


def draw_active_circles():
    for pos in active_circles_positions:
        pygame.draw.circle(screen, circle_color, tuple(map(int, pos)), circle_radius)


def process_circles_positions():

    def is_fallen(pos):
        return pos[1] >= height - circle_radius

    global active_circles_positions
    seconds_tick = clock.tick() / 1000
    active_circles_positions = set(map(lambda p: (p[0], p[1] + pixels_per_second_speed * seconds_tick), active_circles_positions))

    for pos in active_circles_positions:
        if is_fallen(pos):
            pygame.draw.circle(baked_screen, circle_color, tuple(map(int, pos)), circle_radius)

    active_circles_positions = set(filter(lambda p: not is_fallen(p), active_circles_positions))


is_running = True
while is_running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("button pressed", event.pos)
            active_circles_positions.add(event.pos)

    screen.blit(baked_screen, (0, 0))
    draw_active_circles()
    process_circles_positions()

    pygame.display.flip()

pygame.quit()
