import pygame

pygame.init()
clock = pygame.time.Clock()
FPS = 60

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Ball setup
ball_center_x = WINDOW_WIDTH // 2
ball_center_y = WINDOW_HEIGHT // 2
ball_radius = 35
ball_color = (255, 100, 0)
# Geschwindigkeit in px/s
ball_vel_x = 200
ball_vel_y = 150

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
    # Ball bewegt sich automatisch
    ball_center_x += ball_vel_x * (dt / 1000)
    ball_center_y += ball_vel_y * (dt / 1000)

    # Collision Handling
    if ball_center_x - ball_radius <= 0:  # links
        ball_vel_x = -ball_vel_x  # Umdrehen
        ball_center_x = ball_radius  # Ball zurück an Rand
    elif ball_center_x + ball_radius >= WINDOW_WIDTH:  # rechts
        ball_vel_x = -ball_vel_x  # Umdrehen
        ball_center_x = WINDOW_WIDTH - ball_radius  # Ball zurück an Rand
    if ball_center_y - ball_radius <= 0:  # oben
        ball_vel_y = -ball_vel_y  # Umdrehen
        ball_center_y = ball_radius   # Ball zurück an Rand
    elif ball_center_y + ball_radius >= WINDOW_HEIGHT:   # unten
        ball_vel_y = -ball_vel_y  # Umdrehen
        ball_center_y = WINDOW_HEIGHT - ball_radius  # Ball zurück an Rand
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
