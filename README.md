# Capstone-turtle-game
# 🐢 Turtle Crossing Game

A retro-style arcade game built using **Python** and the **Turtle** graphics library. This project is a capstone assignment that demonstrates the practical application of **Object-Oriented Programming (OOP)** concepts.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Status](https://img.shields.io/badge/Status-Completed-success)

## 🎮 Game Overview

The goal is simple: Help the turtle cross the road without getting hit by the cars!
* The player controls the turtle at the bottom of the screen.
* Cars move horizontally across the screen at varying speeds.
* When the turtle reaches the top edge, the level increases, and cars move faster.
* If the turtle collides with a car, it's **GAME OVER**.

## 📸 Game Play
![Game Play](https://github.com/user-attachments/assets/ee895c0f-ac1b-41a1-8cc4-563c51953af9)

## ⚙️ Technical Implementation (OOP)

This project is structured using a modular, Object-Oriented approach. The code is split into separate classes to handle specific responsibilities:

1.  **`main.py`**: 
    * Controls the game loop.
    * Initializes the screen object and handles time/refresh rates.
    * Detects collisions between the player and cars.
    
2.  **`player.py` (Inherits from `Turtle`)**: 
    * Handles the turtle's movement and positioning.
    * Detects when the player has successfully crossed the finish line.

3.  **`car_manager.py`**:
    * Generates cars randomly along the Y-axis.
    * Manages the movement of all cars.
    * Increases car speed as the user levels up.

4.  **`scoreboard.py` (Inherits from `Turtle`)**:
    * Tracks and displays the current level.
    * Renders the "GAME OVER" sequence.

## 🕹️ Controls

* **`Up` Key**: Move Forward
* **`Down` Key**: Move Backward (Optional)

## 🚀 How to Run

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YourUsername/turtle-crossing-game.git](https://github.com/YourUsername/turtle-crossing-game.git)
    ```
2.  **Navigate to the directory:**
    ```bash
    cd turtle-crossing-game
    ```
3.  **Run the game:**
    ```bash
    python main.py
    ```

## 👨‍💻 About the Developer

Author
**Haadil Hayath Basha** 
*Computer Science and Engineering Student at IIIT Sri City (IIITS)*

I am a passionate 1st-year undergraduate exploring Python development, Game Logic, and Software Engineering principles. This project was built to solidify my understanding of classes, inheritance, and coordinate systems in Python.

---
*If you enjoyed playing this, feel free to give this repo a ⭐!*
