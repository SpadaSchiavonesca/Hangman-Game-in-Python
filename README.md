# 📚 CS50's Introduction to Programming with Python - Hangman Game

> Project for Harvard University's CS50 Introduction to Programming with Python.
> An introduction to programming using Python, a popular language for general-purpose programming, data science, web programming, and more.

---

# 🕹️ Hangman Game (Python)

[![Video Demo](https://img.shields.io/badge/Video%20Demo-Watch%20Now-blue)](https://www.dropbox.com/scl/fi/h00nadgm56ktzbzbtxrjp/Hangman.mp4?rlkey=mbh5qnnqsbxoxuernbh05alky&e=1&st=iduqac45&dl=0)

> A classic Hangman game implemented in Python, showcasing fundamental programming concepts and user interaction.

---

## 🎯 Quick Overview

This project demonstrates:

* **Python Fundamentals:** Variables, loops, conditional statements, functions.
* **Data Structures:** Lists and dictionaries for managing words and categories.
* **User Input & Output:** Interactive gameplay through terminal prompts.
* **Basic Error Handling:** Ensuring a smooth user experience.

---

## 🎥 Video Demonstration

[![Video Demo](https://i.ibb.co/Xy3v4f8/play-button.png)](https://www.dropbox.com/scl/fi/h00nadgm56ktzbzbtxrjp/Hangman.mp4?rlkey=mbh5qnnqsbxoxuernbh05alky&e=1&st=iduqac45&dl=0)

> Watch a short demo of the game in action!

---

## ✨ Key Features

* 🎨 **Multiple Word Categories:** Choose from Fruits, Animals, or Objects for personalized gameplay.
* 💀 **Dynamic Hangman Art:** Visual feedback on incorrect guesses, adding a sense of urgency.
* 🎮 **User-Friendly Interface:** Clear instructions and intuitive terminal interaction.
* 🎲 **Random Word Selection:** Ensures a unique challenge each time you play.
* 🛡️ **Basic Error Handling:** Prevents crashes due to invalid input.

---

## 🚀 How to Play

1.  **Clone or Download:** Get the code from this repository.
2.  **Install Python (if needed):** Make sure Python 3 is installed on your system.
3.  **Run the Script:** Open your terminal/command prompt, navigate to the project directory, and run `python hangman.py`.
4.  **Follow Prompts:** Choose a category and guess letters to uncover the hidden word.

---

## 🛠️ Setup

1.  **Python Installation:** [Download Python](https://www.python.org/downloads/) if you haven't already.
2.  **Get the Code:** Clone this repository or download the `hangman.py` file.
3.  **Run the Game:** Open your terminal, navigate to the directory, and execute `python hangman.py`.

---

## 💡 Code Highlights

```python
def choose_category():
    """Prompts the user to choose a word category."""
    # ... (rest of the code for choose_category)

def select_word(category):
    """Selects a random word from the chosen category."""
    # ... (rest of the code for select_word)

def display_hangman(incorrect_guesses):
    """Displays the hangman art based on the number of incorrect guesses."""
    # ... (rest of the hangman art list)
    print(hangman[incorrect_guesses])

# ... (rest of your Python code)
