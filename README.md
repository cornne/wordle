# Wordle Unlimited Game

This is a Python implementation of the Wordle game using Tkinter and the `uv` library. The game allows players to guess a 5-letter word within 6 attempts, with color feedback (green for correct position, yellow for correct letter but wrong position, gray for incorrect letter).

## Requirements
- Python 3.x
- Required libraries (listed in `requirements.txt`)

## Installation
1. Ensure Python 3.x is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
2. Download the following files from the submission:
   - `wordle_game.py` (the game source code)
   - `requirements.txt` (list of required libraries)
   - This `README.md` file
3. Open a terminal or command prompt.
4. Navigate to the directory containing the downloaded files.
5. Install the required libraries by running the following command: pip install -r requirements.txt
- Note: Ensure `pip` is installed. If not, install it by running `python -m ensurepip --upgrade` and `python -m pip install --upgrade pip`.
- The `requirements.txt` file includes the `uv` library and other dependencies needed to run the game.
6. Verify the installation by checking that no errors occur during the `pip install` command.

## How to Run the Game
1. After installing the dependencies, run the game by executing the following command in the terminal: python main.py
2. The game will launch with a main menu. Click "Start Game" to begin.

## How to Play
- **Objective**: Guess the 5-letter word in 6 tries or fewer.
- **Controls**:
- Use the on-screen keyboard or your physical keyboard to input letters.
- Press "ENTER" to submit your guess.
- Press "⌫" (Backspace) to delete the last letter.
- Press "RESTART" to start a new game anytime.
- Press "BACK TO MENU" to return to the main menu.
- **Feedback**:
- Green: The letter is correct and in the right position.
- Yellow: The letter is in the word but in the wrong position.
- Gray: The letter is not in the word.
- After winning or losing, choose to play another round or return to the main menu.

## Additional Resources
- The game uses a predefined list of words embedded in the code. No external resource files (e.g., dictionaries) are required.
- If you need to expand the word list, modify the `WORDS` list in the code.

## Notes
- No modifications to the submission are allowed after the deadline.
- The submission complies with the 25MB size limit and contains only the source code and `requirements.txt`.
- Ensure all dependencies are installed before running the game to avoid errors.

## Contact
For questions, contact [Your Name/Email] (replace with your details).
