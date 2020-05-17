# -*- coding: utf-8 -*-

from random import choice
from IPython.display import clear_output


words = [ "tree", "basket", "chair", "paper", "python" ]

word = choice(words)   # choose random words from the list
guessed, lives, game_Over = [], 7, False

 
# create a list of underscores to the length of the word

guesses = [ "_ " ] * len(word)

while not game_Over:
    
    ans = input("Type Quit or Guess the letter: ").lower()
    
    if ans == "quit":
        print("Thanks for playing!")
        game_Over = True
        
    hidden_word = "".join(guesses)
    print(f"Word to guess is {hidden_word}")
    print(f"Lives: {lives}")
    ans = input()