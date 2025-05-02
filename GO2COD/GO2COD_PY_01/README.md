# GO2COD_PY_01
# NUMBER GUESSING AI

# Description 
In this task, the user is challenged to predict a randomly generated number in this Python program. The numbers the player can predict fall into one of two categories: **1 to 50** or **1 to 100**. The application gives feedback following each guess, indicating how near the goal number the guess was. 

## The Mechanism 
1. Upon beginning the game, you will be asked to select a range:
   Option 1: Choose a number from **1 to 50**.
   Option 2: Guess a number between **1 and 100** 
2. The program will generate a random number.
3. You'll keep guessing until you figure out the right number, with suggestions given each time:
**Very close** : If you are about three numbers away from the target, you are .
**Getting closer** : If you are within ten numbers away.
**A bit far** : If you're within 20 numbers.
**Far away** : If you're more than twenty numbers away.
4. When you make an accurate estimate, the computer not only counts the number of attempts but also congratulates you.

## Features
1. **Range Selection**: The user has a choice between two ranges: 1–50 and 1–100.
2. **Infinite Trys**: The game keeps going until the right number is guessed.
3. **Proximity Feedback**: The degree to which the guess resembles the goal.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/codelassey/GO2COD_PY_01.git
   cd GO2COD_PY_01
   python script.py

## Use Case Example 
```plaintext
The Number Guessing AI welcomes you! Select a range to estimate:
1. From 1 to 50
2. From 1 to 100

Put in 1 or 2: 2

I have chosen a number from 1 to 100. Attempt to predict it!

Put in your prediction: 30
Way off! Give it another try.

Put in your estimate: 45
Still a bit far.

Put in your estimate: 70
You're getting closer!

Put in your guess: 88
You're so near!

Put in your estimate: 90 
Well done! 
You made 5 guesses about the number
