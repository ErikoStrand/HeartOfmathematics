import pygame, sys
import math
import numpy as np
import time
# init
pygame.init()
pygame.font.init()

# colors
bg = (200, 200, 200)
line_color = (255, 229, 160)
dot_color = (17, 0, 2)
active_box_color = (20, 255, 20)
deactivated_box_color = (255, 20, 20)
middle_color = (110, 110, 110)

# values
width = 900
height = 900
number_input = ""
circle_input = ""
circle_amount = False
random_button = False

# location
dot_locations = []
dot_values = {}
random_color_button = pygame.Rect(width - 100, height - 880, 50, 50)

#start up stuff
screen = pygame.display.set_mode((width, height))
screen.fill(bg)
font = pygame.font.Font("Pokemon GB.ttf", 10)
middle_font = pygame.font.Font("Pokemon GB.ttf", 80)

def display(x, y, value, text, length):
    # clear # left top width height2
    #print(pygame.font.Font.size(font, text + value))
    pygame.draw.rect(screen, bg, (x, y, length, 10))
    draw = font.render(text + value, False, (0, 0, 0))
    screen.blit(draw, (x, y))

def circle_draw(amount, radius, size):
    pygame.draw.circle(screen, bg, (width / 2, height / 2), 450)
    for i in range(amount):
        x = int(width/2 + radius * math.cos(math.radians(360/amount * i)))
        y = int(height/2 + radius * math.sin(math.radians(360/amount * i)))
        dot_locations.append([x, y])
        pygame.draw.circle(screen, dot_color, (x, y), size)

def draw_dot():
    for i in range(len(dot_locations)):
        pygame.draw.circle(screen, dot_color, (dot_locations[i][0], dot_locations[i][1]), 3)

def variable_create(input_, circles):
    for i in range(len(dot_locations)):
        dot_values[i] = [i]
        add = i * input_
        while 1:
            if add <= circles - 1:
                dot_values[i].append(add)
                break
            elif add >= circles - 1:
                if add >= 100000000:
                    add -= 90000000
                if add >= 10000000:
                    add -= 9000000
                if add >= 1000000:
                    add -= 900000
                if add >= 100000:
                    add -= 90000
                if add >= 10000:
                    add -= 9000
                else:
                    add -= circles

def draw_lines():

    if random_button == True:
        r, g, b = np.random.randint(0, 255, 3)
        color = (r, g, b)

    if random_button == False:
        color = line_color

    pygame.draw.circle(screen, bg, (width/2, height/2), 400)

    a, b = pygame.font.Font.size(middle_font, str(number_input))
    draw = middle_font.render(str(number_input), False, middle_color)
    screen.blit(draw, (450 - a/2, 400))

    for x in range(len(dot_locations)):
        pygame.draw.line(screen, color, (dot_locations[dot_values[x][0]]), (dot_locations[dot_values[x][1]]), 1)
        #print(dot_values[x][0], dot_values[x][1], "Start:", dot_locations[dot_values[x][0]], "End:", dot_locations[dot_values[x][1]])

circle_draw(250, 400, 3)
display(20, 50, number_input, "Multiply: ", 300)
display(20, 75, circle_input, "DPC: ", 250)
pygame.draw.rect(screen, active_box_color, (10, 50, 8, 8))
pygame.draw.rect(screen, deactivated_box_color, (10, 75, 8, 8))
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if random_color_button.collidepoint(event.pos):
                random_button = not random_button

            color = active_box_color if random_button else deactivated_box_color
            pygame.draw.rect(screen, color, random_color_button)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RSHIFT:
                circle_amount = not circle_amount
                if circle_amount:
                    pygame.draw.rect(screen, deactivated_box_color, (10, 50, 8, 8))
                    pygame.draw.rect(screen, active_box_color, (10, 75, 8, 8))
                if not circle_amount:
                    pygame.draw.rect(screen, deactivated_box_color, (10, 75, 8, 8))
                    pygame.draw.rect(screen, active_box_color, (10, 50, 8, 8))

            if not circle_amount:
                if event.unicode.isnumeric():
                    number_input += event.unicode
                    display(20, 50, number_input, "Multiply: ", 300)

            if circle_amount:
                if event.unicode.isnumeric():
                    circle_input += event.unicode
                    display(20, 75, circle_input, "DPC: ", 250)

            if event.key == pygame.K_RETURN and circle_amount:
                dot_locations = []
                circle_draw(int(circle_input), 400, 3)
                circle_input = ""

            if event.key == pygame.K_BACKSPACE:
                if not circle_amount:
                    number_input = number_input[:-1]
                    display(20, 50, number_input, "Multiply: ", 300)

                if circle_amount:
                    circle_input = circle_input[:-1]
                    display(20, 75, circle_input, "DPC: ", 250)

            if event.key == pygame.K_RETURN and not circle_amount:
                if number_input == "":
                    pass
                else:
                    dot_values = {}
                    variable_create(int(number_input), len(dot_locations))
                    draw_lines()
                    draw_dot()
                    number_input = ""
                    draw = font.render("0", False, (0, 0, 0))
                    screen.blit(draw, (dot_locations[0][0] + 5, dot_locations[0][1] - 3))


    pygame.display.flip()

    # signed by eriko