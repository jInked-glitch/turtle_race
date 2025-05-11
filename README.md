# 🐢 Turtle Race Game

A colorful turtle race game built using Python's turtle module.  
The user places a bet on a turtle color and watches the race unfold — will your turtle win?

---

## 🎬 New Features Updated! (as of 11 May 2025)

This version includes full game loop support and polished design:

🎯 **Tie Detection**: Multiple turtles reaching the goal together are counted as a tie. If your turtle is one of them, it's a win for you!

🌈 **Color-Coded Results**: The result message appears in the same color as your chosen turtle.

🧨 **Start Countdown Animation**: “Ready... Set... Go!” appears in the center of the screen before the race begins.

🔊 **Sound Effects**:
- Start race: 🎵 start.wav
- Win or tie: 🎉 yeah.wav
- Loss: 😢 lost.wav

🔁 **Replay Functionality**: After each round, you're prompted whether to play again. The game resets completely — turtles and messages are cleared.

🧠 **Fully Object-Oriented Design**:
- All logic is encapsulated in a `RacingTurtle` class
- Cleaner code organization, reusable structure
- Clear method separation: setup, movement, animation, judging, reset

---

## 🎮 How to Play

1. When prompted, bet on a turtle by entering a color.
2. Watch the countdown: "Ready... Set... Go!"
3. The turtles race at random speeds toward the finish line.
4. You win if your turtle is first — or one of the first in case of a tie.
5. Play again as many times as you like!

---

## 🛠 Technologies Used

- Python 3.x
- `turtle` (standard library for graphics)
- `winsound` (for sound on Windows)

---

## 📁 Project Structure

turtle_race/
├── main.py # Entry point & game loop
├── racing_turtle.py # RacingTurtle class with all logic
├── start.wav # Start race sound
├── yeah.wav # Win/tie sound
├── lost.wav # Lose sound
└── README.md
└── docs/
    └── racing_turtle_notes.md
---

## 🔧 Planned Features (To-Do)

- [ ] Colorful output in the terminal for winners (e.g., green text)
- [ ] Replay feature (“Would you like to race again?” prompt)
- [ ] Refactor using a `RacingTurtle` class for better code structure
- [ ] Add a start countdown and sound effects


---

## 📖 Learning Goals

This project helps reinforce the following Python concepts:

- Object-Oriented Programming (OOP)
- Using the turtle graphics module for UI/animation
- Handling user input and interactivity
- Structuring a complete game loop with replay support
- Managing sound and display feedback

---

## ✨ Special Thanks

Inspired by the “100 Days of Code” Python Bootcamp on Udemy.  
This project is part of my personal learning journey and a fun way to grow as a programmer.

---

## 🧑‍💻 Author

**jInked-glitch**  
- Based in France — runner and passionate Python learner on a journey toward mastery  
- GitHub: [jInked-glitch](https://github.com/jInked-glitch)
