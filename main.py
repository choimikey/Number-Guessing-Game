# Number Guessing Game
# This program will generate a random number 1-100 and you will have to guess the correct number

import random
import time
from art import logo

EASY_LEVEL_TURNS = 20
HARD_LEVEL_TURNS = 10

def check_answer(guess, answer, turns):
  """Checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Your guess was too high.")
    return turns - 1
  elif guess < answer:
    print("Your guess was too low.")
    return turns - 1
  else:
    print(f"You guess it right! The answer was {answer}!")

def set_difficulty():
  level = input("Choose a difficulty, Type \"easy\" or \"hard\": ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = random.randint(1, 100)
  print(f"Pssst, the correct answer is {answer}.")

  turns = set_difficulty()
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the correct number.")
    guess = int(input("Take a guess: "))

    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      # A return keyword by itself will exit and end a function
      return
    elif guess != answer:
      print("Guess again.")

while input("Do you want to play a game of \"Guess the number\"? Type \"y\" or \"n\": ") == "y":
  game()
  
print("Alright. Because you said no, I guess we will have to part ways... I hope I see you again soon.\n")
