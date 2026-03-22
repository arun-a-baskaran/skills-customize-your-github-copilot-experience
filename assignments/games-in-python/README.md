
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman game in Python using strings, loops, conditionals, and user input. This assignment will help you practice managing game state and writing interactive programs.

## 📝 Tasks

### 🛠️	Set Up the Hangman Game

#### Description
Use the starter code to choose a secret word, create the variables needed to track progress, and display the hidden word to the player.

#### Requirements
Completed program should:

- Randomly select one word from the provided list.
- Create variables to store guessed letters, incorrect guesses, and the maximum number of incorrect guesses allowed.
- Display the current progress of the word using underscores for letters that have not been guessed yet.
- Show the player how many incorrect guesses remain.


### 🛠️	Implement the Game Loop

#### Description
Write the main game loop so the player can guess letters, update the game state, and see whether they win or lose.

#### Requirements
Completed program should:

- Prompt the player to enter one letter at a time.
- Reveal correctly guessed letters in the word.
- Decrease the remaining attempts only when the player guesses a letter that is not in the word.
- End the game when the full word is guessed or when the player runs out of attempts.
- Display a clear win or lose message at the end of the game.

```text
Example progress display:
Secret word: python
Current progress: p _ _ _ o _
Incorrect guesses remaining: 4
```
