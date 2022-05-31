import pygame, sys
import math
import time
# init
pygame.init()
pygame.font.init()

# colors
bg = (200, 200, 200)
line_color = (255, 229, 160)
dot_color = (17, 0, 2)

# location
dot_locations = []
dot_values = {}

# values
width = 900
height = 900
number_input = ""

#start up values
screen = pygame.display.set_mode((width, height))
screen.fill(bg)
font = pygame.font.Font("Pokemon GB.ttf", 10)

def display(x, y, value):
    # clear # left top width height2
    pygame.draw.rect(screen, bg, (x, y, 100, 50))
    draw = font.render(value, False, (0, 0, 0))
    screen.blit(draw, (x, y))

def circle_draw(amount, radius, size):
    for i in range(amount):
        x = int(width/2 + radius * math.cos(math.radians(360/amount * i)))
        y = int(height/2 + radius * math.sin(math.radians(360/amount * i)))
        dot_locations.append([x, y])
        pygame.draw.circle(screen, dot_color, (x, y), size)

def draw_dot():
    for i in range(len(dot_locations)):
        pygame.draw.circle(screen, dot_color, (dot_locations[i][0], dot_locations[i][1]), 3)

def variable_create():
    for i in range(len(dot_locations)):
        dot_values[i] = [i]
        for o in range(2000):
            dot_values[i].append(len(dot_locations) + i)
            dot_values[i].append(len(dot_locations) * (o + 2) + i)

def draw_lines():
    for x in range(len(dot_locations)):
        for y in range(len(dot_locations)):
            if dot_values[x][0] * int(number_input) in dot_values[y]:
                pygame.draw.line(screen, line_color, (dot_locations[y][0], dot_locations[y][1]), (dot_locations[x][0], dot_locations[x][1]), 1)

circle_draw(250, 400, 3)
variable_create()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.unicode.isnumeric():
                number_input += event.unicode
                display(50, 50, number_input)

            elif event.key == pygame.K_BACKSPACE:
                number_input = number_input[:-1]
                display(50, 50, number_input)

            elif event.key == pygame.K_RETURN:
                if number_input == "":
                    pass
                else:
                    screen.fill(bg)
                    draw_lines()
                    draw_dot()
                    number_input = ""

    pygame.display.flip()

    # signed by eriko