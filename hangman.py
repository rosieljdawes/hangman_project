import random
from english_words import get_english_words_set
import os

#SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
#WORD_FILE = os.path.join(SCRIPT_DIR, "data", "word_list.txt")

#try:
#    with open(WORD_FILE) as f:
#        words = [line.strip() for line in f]
#    #print("Words loaded successfully!")
#except FileNotFoundError:
#    print(f"Error: File not found at {WORD_FILE}")
#    print("Directory contents:", os.listdir(SCRIPT_DIR))


words = list(get_english_words_set(['web2'], lower=True))
secret_word = random.choice([w for w in words if len(w) > 4])

# list of words, parameters for the game
max_wrong_attempts = 6
incorrect_guesses = 0
guessed_letters = []
secret_word = random.choice(words)
hidden_word = ["_"] * len(secret_word)

image_list = [
    r"""
    +---+
    |   |
        |
        |
        |
        |
    =========""",
    r"""
    +---+
    |   |
    O   |
        |
        |
        |
    =========""",
    r"""
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========""",
    r"""
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========""",
    r"""
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========""",
    r"""
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========""",
    r"""
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    ========="""]

print("Welcome to my shit game of Hangman.")
print(image_list[0])
print("Current word: " + " ".join(hidden_word))


while "_" in hidden_word and incorrect_guesses < max_wrong_attempts:
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
        print("Good guess!")        

    if not found:
        incorrect_guesses += 1
        print(image_list[incorrect_guesses])
        print(f"Sorry, {guess.upper()} is not in the word, guess again. Tries left: {max_wrong_attempts - incorrect_guesses}.")

    print("Updated word: " + " ".join(hidden_word))

if "_" not in hidden_word:
    print(f"You won! The word is '{secret_word}'.")
else:
    print(f"Too many guesses, You lose! The word is '{secret_word}'.")

   
    