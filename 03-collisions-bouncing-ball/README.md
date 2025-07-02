# Project 3: Bouncing Ball

## 🎯 Lernziele
- **Collision Detection** verstehen (das Herzstück der Spieleentwicklung!)
- Boundary Collisions (Ränder des Bildschirms)
- Velocity-basierte Bewegung (statt Input-basierte)
- Physics Basics (Geschwindigkeit, Richtung)
- Automatische Objektbewegung

## 🏀 Was passiert
Ein Ball springt automatisch durch das Fenster und prallt von den Wänden ab - wie bei Pong oder Breakout!

## 🧠 Neue Konzepte

### Collision Detection
- **Boundary Collision**: Objekt stößt gegen Bildschirmrand
- **Rectangle Collision**: Einfachste Form der Kollisionserkennung
- **Response**: Was passiert NACH einer Kollision?

### Velocity System
- `ball_vel_x` und `ball_vel_y` - Geschwindigkeit in X/Y Richtung
- Bewegung läuft automatisch (keine Tasten erforderlich)
- Richtung ändern durch Geschwindigkeits-Umkehr

### Physics Basics
- Position + Geschwindigkeit = neue Position
- Kollision → Geschwindigkeit umkehren
- Frame-unabhängige Bewegung mit Delta Time

## 🎮 Controls
- **ESC**: Spiel beenden
- **SPACE**: Ball zurücksetzen (Bonus-Feature)

## 🔍 Code-Highlights
```python
# Collision Detection Pattern:
if ball_x <= 0 or ball_x >= WINDOW_WIDTH - ball_size:
    ball_vel_x = -ball_vel_x  # Richtung umkehren

# Velocity-basierte Bewegung:
ball_x += ball_vel_x * dt
ball_y += ball_vel_y * dt
```

## 🚀 Aufbau auf Projekt 2
- Gleiche Game Loop Struktur
- Statt Player Input → automatische Bewegung
- Statt statische Position → dynamische Velocity

## 💡 Erkenntnisse
- Collision Detection ist überall in Spielen (Plattformer, Shooter, Puzzle)
- Velocity-System ist die Basis für alle bewegten Objekte
- Einfache Physik kann sehr befriedigende Effekte erzeugen

## 🎮 Ausführen
```bash
python main.py
```

## 🔄 Von Projekt 2 gelernt
- Event-System Verständnis
- Konstanten vs. Magic Numbers
- Game Loop Struktur