import pygame
import math


WIDTH, HEIGHT = 1280, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minigolf")

G=0.1
BOUNCE_FACTOR = .4
FRICTION_COEFFICIENT = 0.1


FPS = 60

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



def draw_trajectory(mouse_start_x, mouse_start_y, mouse_end_x, mouse_end_y):
    # Calculate the direction vector
    dx = mouse_end_x - mouse_start_x
    dy = mouse_end_y - mouse_start_y

    # Calculate the length of the direction vector
    length = math.sqrt(dx ** 2 + dy ** 2)

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


class Ball:
    def __init__(self,x,y,mass):
        self.x = x
        self.y = y
        self.ball_radius = 8
        self.mass = self.ball_radius
        self.vx = 0
        self.vy = 0
        self.ifx =
        self.ify =
        self.bounce_count = 0

    def apply_force(self, force_x, force_y):
        # a = F/m

        #ax,ay: applied force
        ax = round(force_x/self.mass, 2)
        ay = round(force_y/self.mass, 2)

        # Friction force (opposes motion)
        ax_friction = -round(FRICTION_COEFFICIENT * self.vx, 2)
        print("Friction: ",ax_friction, "Applied Force: ", ax)
        ax_total = ax_friction + ax

        # Update velocity using Euler integration
        self.vx += ax_total
        self.vy += ay
        print("Acceleration: ",round(ax_total,2)) #"Horizontal Velocity: ", round(self.vx, 2))

        # Update position using Euler integration
        self.x += round(self.vx, 2)
        self.y += round(self.vy,2)
        # print("Positiion: ", round(self.x,2), round(self.y,2), "Velocity: " ,round(self.vx,2), round(self.vy,2))

    def draw_ball(self):
        pygame.draw.circle(WIN,BLACK,(self.x,self.y),self.ball_radius,10)

    def get_position(self):
        return self.x, self.y

    def check_bounce(self):
        if self.y >= HEIGHT - self.ball_radius:
            self.y = HEIGHT - self.ball_radius
            self.vy = -self.vy * BOUNCE_FACTOR
            self.bounce_count+=1

        if self.bounce_count >= 5:
            self.bounce_count = 0
            self.vy = 0




clock = pygame.time.Clock()

ball = Ball(50,50, 30)
is_aiming = False
shooting = False
horizontal_velocity = 20
vertical_velocity = 50
start_x, start_y = 0, 0
end_x, end_y = 0, 0
run = True


while run:
    clock.tick(FPS)
    current_fps = clock.get_fps()
    # print("FPS:", current_fps)
    WIN.fill(WHITE)
    ball.draw_ball()
    ball_x,ball_y = ball.get_position()
    ball.apply_force(1,ball.mass * G)
    ball.check_bounce()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #     if event.type == pygame.MOUSEBUTTONDOWN:
    #         start_x, start_y = pygame.mouse.get_pos()
    #         if event.button == 1:
    #             if ball_x + 5 < start_x < ball_x + 15:
    #                 if ball_y + 5 < start_y < ball_y + 15:
    #                     is_aiming = True
    #                 else:
    #                     print("Click and drag on the ball to aim")
    #             else:
    #                 print("Click and drag on the ball to aim")
    #         else:
    #             print("Use left mouse button to aim")
    #
    #     if event.type == pygame.MOUSEMOTION and is_aiming:
    #         end_x, end_y = pygame.mouse.get_pos()
    #         draw_trajectory(start_x, start_y, end_x, end_y)
    #
    #     if event.type == pygame.MOUSEBUTTONUP and is_aiming:
    #         is_aiming = False
    #         print("shooting: \n")
    #         shooting = True
    #
    # if shooting:
    #
    #     shooting = False

    pygame.display.update()
pygame.quit()
