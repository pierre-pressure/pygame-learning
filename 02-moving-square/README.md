# Project 2: Moving Square

## 🎯 Lernziele
- Tastatur-Input verarbeiten
- Player-Position tracken und aktualisieren
- Bewegungslogik implementieren
- Einfache Grafiken zeichnen (Rechtecke)
- Koordinatensystem verstehen

## 🕹️ Controls
- **WASD** oder **Pfeiltasten**: Player bewegen
- **ESC**: Spiel beenden

## 🧠 Neue Konzepte

### Input Handling
- `pygame.key.get_pressed()` - Welche Tasten sind AKTUELL gedrückt
- Kontinuierliche vs. Event-basierte Eingabe
- Mehrere Tasten gleichzeitig verarbeiten

### Player System
- Position als separate Variablen (player_x, player_y)
- Bewegungsgeschwindigkeit kontrollieren
- Koordinatensystem: (0,0) = oben links

### Grafik-Grundlagen
- `pygame.draw.rect()` - Rechtecke zeichnen
- RGB-Farbsystem
- Objekte auf dem Screen positionieren

## 🚀 Aufbau auf Projekt 1
Verwendet das gleiche Game Loop Pattern:
1. **Events**: Fenster schließen + neue Tastatur-Eingabe
2. **Update**: Player-Position basierend auf Input ändern
3. **Draw**: Player als Rechteck zeichnen

## 💡 Erkenntnisse
- Movement fühlt sich erst "richtig" an mit konstanter Framerate
- Input-System ist die Basis für alle Player-Interaktionen
- Einfache Grafiken reichen für Gameplay-Prototyping

## 🎮 Ausführen
```bash
python main.py
```

## 🔄 Von Projekt 1 gelernt
- Match/Case für Event-Handling
- Saubere Code-Struktur
- FPS-Monitoring

---
*Next: Projekt 3 wird Collision Detection mit Wänden hinzufügen*