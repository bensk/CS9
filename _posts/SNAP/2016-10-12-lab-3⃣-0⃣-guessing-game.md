---
layout: "post"
category: "Unit 1: SNAP"
title: "Lab 3⃣.0⃣ Guessing Game"
date: "2016-10-13 22:18"
---

In this lab, you will use conditional statements and variables to build a simple number guessing game.

## Section 1 - I'm Thinking of a Number...
You will write a SNAP program to choose a random number between 1 and 10 and then ask the user to guess a number.

If the user's guess matches the random number, the user wins. If not, the user loses. In either case, the user should be shown a message indicating whether she won or lost and the secret random number should be revealed.

- Write the simple version of the guessing game program described above.
- Modify the program to keep asking the user for guesses until the correct number is given. Be sure to give a message after each guess, but only reveal the secret number when the user has guessed correctly and the game is over.
- Add code to ask the player their name at the start of the game. Then, personalize the message for an incorrect guess by adding the player's name. For example, if Scout is playing the game, then the message should say "Sorry, Scout, that guess is not correct" instead of just "Sorry" when Scout guesses incorrectly.

## Section 2 - Game Upgrades
- Modify your guessing game so that the player can decide the range of possible numbers from which the secret number can be chosen. After asking the player's name, ask what she wants the highest possible number to be. Then, instead of choosing a random number between 1 and 10, choose a random number between 1 and the number the player requested.
- Add code to keep track of how many guesses the player has made. After the player guesses correctly, inform her how many tries it took before the correct number was guessed.
- Increase the player's chances by telling her whether the guessed number is too high or too low instead of just that it is incorrect.
