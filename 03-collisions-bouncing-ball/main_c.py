import pygame

pygame.init()
clock = pygame.time.Clock()
FPS = 60

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Ball setup
ball_center_x = WINDOW_WIDTH // 2
ball_center_y = WINDOW_HEIGHT // 2
ball_radius = 25
ball_color = (255, 100, 0)
ball_vel_x = 0  # Geschwindigkeit in px/s
ball_vel_y = 0
gravity_acceleration = 800  # px/s^2
horizontal_speed = 400
jump_y = -500
friction = 0.955

font = pygame.font.Font(None, 36)

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Bouncing Ball")

# ------------------------------------------------------------------------------------------------

running = True
while running:
    dt = clock.tick(FPS)
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                running = False
    # ------------------------------------------------------------------------------------------------
    ball_vel_y += gravity_acceleration * (dt / 1000)  # Beschleunigung

    keys = pygame.key.get_pressed()

    # user-input (nur noch x, da y durch SPACE ersetzt wird)
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        ball_vel_x = -horizontal_speed
    elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        ball_vel_x = horizontal_speed
    else:
        ball_vel_x *= friction  # Friction Luft -> Ball bremst ohne userinput

    # Sprung vom Boden
    is_on_ground = ball_center_y + ball_radius >= WINDOW_HEIGHT
    if keys[pygame.K_SPACE] and is_on_ground:
        ball_vel_y = jump_y

    # Velocity ändert Position
    ball_center_x += ball_vel_x * (dt / 1000)
    ball_center_y += ball_vel_y * (dt / 1000)  

    # Collision Handling
    if ball_center_x - ball_radius <= 0:  # links
        ball_center_x = ball_radius  # Ball zurück an Rand
        ball_vel_x = -ball_vel_x * 0.7
    elif ball_center_x + ball_radius >= WINDOW_WIDTH:  # rechts
        ball_center_x = WINDOW_WIDTH - ball_radius  # Ball zurück an Rand
        ball_vel_x = -ball_vel_x * 0.7
    if ball_center_y - ball_radius <= 0:  # oben
        ball_center_y = ball_radius  # Ball zurück an Rand
        ball_vel_y = -ball_vel_y * 0.8
    elif ball_center_y + ball_radius >= WINDOW_HEIGHT:  # unten
        ball_center_y = WINDOW_HEIGHT - ball_radius  # Ball zurück an Rand
        ball_vel_y = -ball_vel_y * 0.1  # Sprung vom Boden
        ball_vel_x *= 0.8
    # ------------------------------------------------------------------------------------------------
    screen.fill((0, 0, 0))

    # Ball zeichnen
    pygame.draw.circle(screen, ball_color, (int(ball_center_x), int(ball_center_y)), ball_radius)
    fps = clock.get_fps()
    fps_text = font.render(f"FPS: {fps:.0f}", True, (255, 255, 255))
    screen.blit(fps_text, (10, 10))

    pos_text = font.render(f"Position: ({int(ball_center_x)}, {int(ball_center_y)})", True, (255, 255, 255))
    screen.blit(pos_text, (10, 50))
    pygame.display.flip()

pygame.quit()
