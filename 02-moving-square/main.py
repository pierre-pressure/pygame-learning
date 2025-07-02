import pygame

pygame.init()
clock = pygame.time.Clock()
FPS = 60

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

player_x = WINDOW_WIDTH // 2 
player_y = WINDOW_HEIGHT // 2
player_size = 50
player_speed = 300  
player_color = (0, 255, 0)

font = pygame.font.Font(None, 36)

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Moving Square")

# ------------------------------------------------------------------------------------------------

running = True
while running:
    dt = clock.tick(FPS)
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                running = False
            case pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False         
# ------------------------------------------------------------------------------------------------
    keys = pygame.key.get_pressed()  
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player_y -= player_speed * (dt / 1000)
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player_y += player_speed * (dt / 1000)
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player_x -= player_speed * (dt / 1000)
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player_x += player_speed * (dt / 1000)
# ------------------------------------------------------------------------------------------------
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, player_color, (player_x, player_y, player_size, player_size))
    fps = clock.get_fps()
    fps_text = font.render(f"FPS: {fps:.0f}", True, (255, 255, 255))
    screen.blit(fps_text, (10, 10))

    pos_text = font.render(f"Position: ({int(player_x)}, {int(player_y)})", True, (255, 255, 255))
    screen.blit(pos_text, (10, 50))
    pygame.display.flip()

pygame.quit()
