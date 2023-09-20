import os.path
import time

import pygame
import math

pygame.init()


WIDTH,HEIGHT =1280,720
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Minigolf")
FPS=60
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
PINK = (255, 192, 203)
BROWN = (165, 42, 42)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
AQUA = (100, 200, 200)
BLACK = (0, 0, 0)
GREY = (200, 200, 200)
WHITE = (255, 255, 255)
ball_radius = 20


def draw_trajectory(mouse_start_x, mouse_start_y, mouse_end_x, mouse_end_y):
    # Calculate the direction vector
    dx = mouse_end_x - mouse_start_x
    dy = mouse_end_y - mouse_start_y

    # Calculate the length of the direction vector
    length = math.sqrt(dx**2 + dy**2)

    # Normalize the direction vector (make it a unit vector)
    if length > 0:
        normalized_dx = dx / length
        normalized_dy = dy / length
    else:
        normalized_dx = 0
        normalized_dy = 0

    # Scale the normalized vector to have a length of -150 units
    scaled_dx = normalized_dx * -150
    scaled_dy = normalized_dy * -150

    # Calculate the end point of the line
    line_end_x = mouse_start_x + scaled_dx
    line_end_y = mouse_start_y + scaled_dy

    # Draw the trajectory line
    pygame.draw.line(WIN, BLACK, (mouse_start_x, mouse_start_y), (line_end_x, line_end_y), 5)



def shoot_ball(ball_x, ball_y,horizontal_velocity):
    ball_x += horizontal_velocity
    if horizontal_velocity > 0:
        ball_x += horizontal_velocity
        if ball_x < ball_radius:
            ball_x = ball_radius
        elif ball_x > WIDTH - ball_radius:
            ball_x = WIDTH - ball_radius
        if ball_y < ball_radius:
            ball_y = ball_radius
        elif ball_y > HEIGHT - ball_radius:
            ball_y = HEIGHT - ball_radius


        print("horizontal_velocity:", horizontal_velocity)
        print("Ball position: ", ball_x,ball_y)
        horizontal_velocity -= 1
        # Make ball fall down
        if ball_y < HEIGHT - ball_radius:
            ball_y += 1
        pygame.display.update()

    return ball_x,ball_y,horizontal_velocity


clock = pygame.time.Clock()
ball_x,ball_y = (WIDTH // 10, HEIGHT -20)
ball_centre = (WIDTH // 10,HEIGHT-10)
is_aiming = False
shooting = False
horizontal_velocity = 20
start_x,start_y = 0, 0
end_x,end_y = 0,0
run = True


while run:
    clock.tick(FPS)
    current_fps = clock.get_fps()
    #print("FPS:", current_fps)
    WIN.fill(WHITE)
    BALL = pygame.draw.circle(WIN,BLACK,(ball_x+10,ball_y+10),10,10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            start_x, start_y = pygame.mouse.get_pos()
            if event.button == 1:
                if ball_x + 5 < start_x < ball_x+15:
                    if ball_y + 5 < start_y < ball_y + 15:
                        is_aiming = True
                    else:
                        print("Click and drag on the ball to aim")
                else:
                    print("Click and drag on the ball to aim")
            else:
                print("Use left mouse button to aim")

        if event.type == pygame.MOUSEMOTION and is_aiming:
            end_x,end_y = pygame.mouse.get_pos()
            draw_trajectory(start_x,start_y,end_x,end_y)

        if event.type == pygame.MOUSEBUTTONUP and is_aiming:
            is_aiming = False
            print("shooting")
            shooting = True

    if shooting:
        ball_x, ball_y, horizontal_velocity = shoot_ball(ball_x, ball_y, horizontal_velocity)
        pygame.display.update()
        print(horizontal_velocity)

    if horizontal_velocity <= 0:
        shooting = False



    pygame.display.update()
pygame.quit()

