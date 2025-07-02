import pygame

pygame.init()
clock = pygame.time.Clock()
FPS = 60

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
font = pygame.font.Font(None, 36) 

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Mein erstes Pygame Fenster")

# ------------------------------------------------------------------------------------------------

running = True
while running:
    dt = clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False
    screen.fill((0, 0, 0))
    fps = clock.get_fps()  
    fps_text = font.render(f"FPS: {fps:.0f}", True, (255, 255, 255))
    screen.blit(fps_text, (10, 10)) 
    pygame.display.flip() 

pygame.quit()
