import pygame

## Pygame initialisieren
# startet alle Pygame-Module wie (Sound, Display, Font, etc.) | immst der erste Schritt
# clock für Taktung (läuft überall gleich gut)| FPS setzt diese fest
pygame.init()
clock = pygame.time.Clock()
FPS = 60

## Fenstergröße definieren
# const. -> durch GROSS | so können die Werte einfacher geändert werden
# font für Textanzeige notwendig
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
font = pygame.font.Font(None, 36) # Standard-Font gr.36

## Fenster erstellen
# screen ist die "Leinwand"
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Mein erstes Pygame Fenster")

# ------------------------------------------------------------------------------------------------

## Gameloop

running = True
while running:
    # FPS begrenzen
    dt = clock.tick(FPS)  # deltatime von 1/60s
    # Phase 1: Events verarbeiten
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT: # Event: X-Button gedrückt
                running = False
# ------------------------------------------------------------------------------------------------
    # Phase 2: Update | Spielelogik
# ------------------------------------------------------------------------------------------------
    # Phase 3: Draw
    # flip: tauscht die unsichtbare "Mal-Leinwand" mit der sichtbaren "Anzeige-Leinwand", sodass das fertige Bild ohne Flackern angezeigt wird
    # Unsichtbare Leinwand: Back Buffer | Sichtbare Leinwand: Front Buffer
    screen.fill((0, 0, 0))  # RGB
    # FPS Anzeige
    fps = clock.get_fps() # Aktuelle FPS(durchschnittswert) holen
    fps_text = font.render(f"FPS: {fps:.0f}", True, (255, 255, 255)) # Weißer, formatierter Text
    screen.blit(fps_text, (10, 10)) # An Textposition zeichnen 
    pygame.display.flip()  # Alles anzeigen

# Pygame sauber beenden
pygame.quit()
