# Whiteout ❄️  
**A Tactical Roguelite Prototype (Python)**

Whiteout is a tactical, extraction-style roguelike — inspired by titles like *Escape from Tarkov* — built in Python to **test my ability to adapt to new game development environments and tooling**, and to explore real-time systems design in code. This project is planned for release as a demo on itch.io once feature milestones are completed.

---

## 🎯 Project Overview

This repository contains the early prototype of *Whiteout*:  
a roguelike game emphasizing:

- Risk-reward exploration loops
- Procedural encounters
- Player state & persistence
- Combat systems
- Simple AI behavior

It was created as a **learning-focused technical exercise**, not just a game demo — a chance to strengthen real-time programming skills in Python outside my usual backend/web environment.

---

## 🧠 Goals & Motivation

Whiteout was built to:

- Practice adapting to unfamiliar frameworks, tooling, and game loops  
- Explore real-time loop architecture in Python  
- Implement state machines, event handling, and input control  
- Prototype procedural gameplay mechanics  
- Demonstrate ability to ideate and execute systems from concept to prototype

The codebase is intentionally structured to simulate a mini production development cycle.

---

## 🧱 Repository Structure
- .vscode/ ← Editor config
- src/ ← Game code (core logic)
    - Effect/ ← code for on screen effects
    - Enemy/ ← code for enemy generation and logic
    - Gameplay/ ← main gameplay logic
    - Levels/ ← code for level generation
    - Player/ ← code for player generation and logic
    - Sprites/ ← assets for the game
- Main.py ← Game entry point
- level.png ← Example game asset
- .gitignore
- README.md

---

## 🕹 Gameplay Concept

At a high level, Whiteout runs:

1. A **game loop** that handles input, simulation, and rendering  
2. Procedural content or level logic  
3. Player interactions with the world (movement, inventory, combat)  
4. Enemy behaviors and game state changes

This reflects real game engineering concerns such as:

- State management
- Event-driven updates
- Timed actions & collision checks
- Deterministic frame updates

---

## 🚀 Tech Stack

Whiteout is built primarily with:

- 🐍 **Python** — Game logic, event loops, systems  
- Game framework of choice (e.g., Pygame) — rendering & input  
- Structured modular code for future expansion  
- Assets (sprites, PNG level art, UI placeholders)

*(Update details if you adopt a framework like **Pygame** or **Arcade**.)*

---

## 💡 Architecture Highlights

Whiteout separates concerns into:

- **Main game loop** — Inputs, updates, rendering  
- **Game systems** — Combat, movement, entities  
- **World state** — Procedural or static environments  
- **Asset management** — Loading and drawing media

This modular layout prepares the code for:

- Easier unit testing  
- Future feature expansions  
- Clean maintenance

---

## 📈 Current Progress

- ❄️ Core loop created  
- 🧍 Player entity placeholder  
- 📍 Level test asset (`level.png`)  
- 🔄 Primary execution flow (`Main.py`)

---

## 📌 Next Milestones

| Milestone | Status |
|-----------|--------|
| Movement & physics | ⬜ |
| Enemy AI prototype | ⬜ |
| Procedural encounter logic | ⬜ |
| Inventory/loot system | ⬜ |
| Extraction mechanic | ⬜ |
| Sound & UI | ⬜ |
| Build & publish on itch.io | ⬜ |

---

## 🛠 Development Notes

This project demonstrates:

- Ability to work with unfamiliar tooling  
- Intentional code structure for real-time programs
- Practice with modular design and stateful systems
- Exploration of procedural content and game mechanics

It is intentionally **not just a tutorial project** — it reflects adaptation to a new environment and complex problem domains.

---

## 📜 Planned Release

Once Whiteout reaches demo readiness with polished mechanics and stable play loops, a playable build will be published on **itch.io** with its own landing page and downloadable executable.

---

## 🧠 Philosophy

Whiteout is a space to learn intentionally and push boundaries beyond typical backend or web stacks. It is a **technical sandbox** that also aims to be fun — and demonstrates real engineering proficiency in unfamiliar territory.
