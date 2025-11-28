# Asteroids 🚀

<p align="center">
<img src="https://img.shields.io/badge/python-%233776AB.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python badge" />
<img src="https://img.shields.io/badge/pygame-%2300D800.svg?style=for-the-badge&logo=python&logoColor=white" alt="Pygame badge" />
</p>

A classic Asteroids arcade game clone built with Python and Pygame. Navigate your spaceship, dodge asteroids, and blast them into smaller pieces!

## 🎮 Gameplay

- Control a triangular spaceship in an asteroid field
- Shoot asteroids to split them into smaller pieces
- Avoid collisions with asteroids — one hit and it's game over!

## 🕹️ Controls

| Key | Action |
|-----|--------|
| `W` | Move forward |
| `S` | Move backward |
| `A` | Rotate left |
| `D` | Rotate right |
| `Space` | Shoot |

## 🛠️ Technologies

- **Language:** Python 3.12+
- **Game Library:** [Pygame](https://www.pygame.org/) 2.6.1
- **Package Manager:** [uv](https://github.com/astral-sh/uv)

## 🚀 Getting Started

### Prerequisites

- Python >= 3.12
- uv

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mayraamaral/asteroids.git
   cd asteroids
   ```

2. Install dependencies with uv:
   ```bash
   uv sync
   ```

### Running the Game

```bash
uv run main.py
```

## 📂 Project Structure

```
📦asteroids
┣ 📜main.py              # Game entry point and main loop
┣ 📂src/
┃ ┣ 📂game/              # Game entities
┃ ┃ ┣ 📜player.py        # Player spaceship class
┃ ┃ ┣ 📜asteroid.py      # Asteroid class with split mechanics
┃ ┃ ┣ 📜asteroidfield.py # Asteroid spawner from screen edges
┃ ┃ ┣ 📜shot.py          # Projectile class
┃ ┃ ┗ 📜circleshape.py   # Base class for circular game objects
┃ ┣ 📂utils/             # Utilities
┃ ┃ ┗ 📜logger.py        # Game state and event logging
┃ ┗ 📂config/            # Configuration
┃   ┗ 📜constants.py     # Game configuration constants
┣ 📂logs/                # Game logs (generated at runtime)
┣ 📜pyproject.toml       # Project dependencies
┗ 📜uv.lock              # Locked dependencies
```

## ✨ Features

- 🎯 **Collision Detection** — Circle-based collision system for accurate hit detection
- 💥 **Asteroid Splitting** — Large asteroids break into smaller, faster pieces when shot
- 🔄 **Continuous Spawning** — Asteroids spawn from random screen edges
- 📊 **Game Logging** — State snapshots and events logged to JSONL files for analysis
- ⏱️ **60 FPS** — Smooth gameplay with delta-time based movement

## 🎛️ Game Constants

| Setting | Value |
|---------|-------|
| Screen Size | 1280 × 720 |
| Player Speed | 200 |
| Turn Speed | 300 |
| Shoot Cooldown | 0.3s |
| Asteroid Spawn Rate | 0.8s |

---

Made with ❤️ using Python and Pygame
