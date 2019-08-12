import pygame, random

pygame.init()
size = width, height = 400, 300
screen = pygame.display.set_mode(size)
baked_screen = pygame.Surface(screen.get_size())

clock = pygame.time.Clock()

circle_radius = 10
pixels_per_second_speed = 100
active_circles = set()


class Circle:
    def __init__(self, pos, color):
        self.pos = pos
        self.color = color

    def get_position(self):
        return self.pos

    def set_position(self, x, y):
        self.pos = (x, y)

    def get_int_position(self):
        return tuple(map(int, self.pos))

    def get_color(self):
        return self.color


def draw_active_circles():
    for circle in active_circles:
        pygame.draw.circle(screen, circle.get_color(), circle.get_int_position(), circle_radius)


def process_circles_positions():
    def is_fallen(circle):
        return circle.get_position()[1] >= height - circle_radius

    global active_circles

    seconds_tick = clock.tick() / 1000
    for circle in active_circles:
        circle.set_position(circle.get_position()[0], circle.get_position()[1] + pixels_per_second_speed * seconds_tick)

    for circle in active_circles:
        if is_fallen(circle):
            pygame.draw.circle(baked_screen, circle.get_color(), circle.get_int_position(), circle_radius)

    active_circles = set(filter(lambda c: not is_fallen(c), active_circles))


def get_random_color():
    color = pygame.Color(0, 0, 0)
    hsv = random.randint(0, 360), random.randint(50, 100), random.randint(50, 100)
    color.hsva = hsv + (100,)
    return color


is_running = True
while is_running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("button pressed", event.pos)
            active_circles.add(Circle(event.pos, get_random_color()))

    screen.blit(baked_screen, (0, 0))
    draw_active_circles()
    process_circles_positions()

    pygame.display.flip()

pygame.quit()
