import random
from english_words import get_english_words_set
import pandas as pd
import os
from functions import load_frequency_data, length_filter, hard_letter_filter
from functions import get_secret_word, select_difficulty, frequency_filter
from functions import calculate_score
from config import MAX_WRONG_ATTEMPTS, IMAGE_LIST, DIFFICULTY_CONFIG

print("Welcome to my shit game of Hangman.")
freq_data = load_frequency_data()
words = list(get_english_words_set(['web2'], lower=True))
difficulty = select_difficulty()
secret_word = get_secret_word(words, difficulty, freq_data)
incorrect_guesses = 0
guessed_letters = []
hidden_word = ["_"] * len(secret_word)

print(IMAGE_LIST[0])
print("Current word: " + " ".join(hidden_word))

while "_" in hidden_word and incorrect_guesses < MAX_WRONG_ATTEMPTS:
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter!!!")
        continue

    if guess in guessed_letters:
        print("You've guessed that one already!")
        continue

    guessed_letters.append(guess)
    found = False

    for i, letter in enumerate(secret_word):
        if letter == guess:
            hidden_word[i] = guess
            found = True

    if found:
        print("\nGood guess!")        

    if not found:
        incorrect_guesses += 1
        print(IMAGE_LIST[incorrect_guesses])
        print(f"Sorry, {guess.upper()} is not in the word. Tries left: {MAX_WRONG_ATTEMPTS - incorrect_guesses}.")

    print("Updated word: " + " ".join(hidden_word))

if "_" not in hidden_word:
    score = calculate_score(DIFFICULTY_CONFIG[difficulty]['difficulty_score'], incorrect_guesses)
    print(f"You won! Score: {score} (Word: '{secret_word}')")
else:
    score = 0  
    print(f"Game over! Score: {score} (Word: '{secret_word}')")
   
    