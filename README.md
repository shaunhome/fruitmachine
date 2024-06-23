# Fruit Machine Game

Welcome to the Fruit Machine Game, implemented in Python!

## Overview
This project simulates a classic fruit machine game where players spin reels to earn points based on specific combinations of symbols. The game includes scoring rules, interactive gameplay, and cumulative score tracking after each spin.

## Features
- **Three Reels Simulation**: Simulates three reels displaying symbols numbered from 1 to 5.
- **Scoring System**:
  - Any three of the same numbers (excluding fives) will pay a bonus of 20 points.
  - Any combination of two fives will pay out 100 points.
  - Three fives pay out the big jackpot of 2000 points.
- **Interactive Gameplay**: Players are prompted to spin the reels and decide whether to play again.
- **Error Handling**: Ensures valid input ('yes' or 'no') from the player during gameplay.

## Coding Practices
- **Modular Design**: Separates logic into functions for scoring calculation, displaying instructions, and managing gameplay loops.
- **Input Validation**: Handles user input to ensure it meets expected criteria (yes/no responses).
- **Random Number Generation**: Utilizes Python's `random` module to generate random numbers for the reels.
- **Clear Instructions**: Provides clear and concise instructions for the game.

## Usage
To play the game:
1. Clone the repository to your local machine.
2. Run `fruit_machine.py` using Python.
3. Follow the on-screen instructions to spin the reels and accumulate points!

## Credits
Developed by Shaun

Enjoy the thrill of the fruit machine and aim for the jackpot!

---
