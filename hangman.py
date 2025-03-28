import random
from english_words import get_english_words_set
import pandas as pd
import os

#levels configuration
DIFFICULTY_CONFIG = {
    'easy': {
        'length': (4, 7),
        'hard_letters': 0,
        'max_rank': 1000,
        'description': "4-7 letter common words"
    },
    'medium': {
        'length': (5, 9),
        'hard_letters': 1,
        'max_rank': 1500,
        'description': "5-9 letters, some rare letters"
    },
    'hard': {
        'length': (7, 10),
        'hard_letters': float('inf'),  # No limit
        'max_rank': 2000,
        'description': "7-10 letters, any word"
    },
    'expert': {
        'length': (10, 20),
        'hard_letters': float('inf'),
        'max_rank': float('inf'),
        'description': "10+ letter obscure words"
    }
}

#load frequency data
def load_frequency_data():
    # Calculate the correct path regardless of where you run the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, 'data', 'unigram_freq.csv')
    
    try:
        df = pd.read_csv(csv_path)
        return {row['word']: idx+1 for idx, row in df.iterrows()}
    except FileNotFoundError:
        print(f"Error: Save unigram_freq.csv at {csv_path}")
        return {}  # Graceful fallback
    
def length_filter(words, min_len, max_len):
    return [w for w in words if min_len <= len(w) <= max_len]

def hard_letter_filter(words, max_allowed):
    hard_letters = {'x', 'z', 'q', 'v'}
    return [w for w in words if sum(1 for c in w if c in hard_letters) <= max_allowed]

def frequency_filter(words, max_rank, freq_data):
    return [w for w in words if freq_data.get(w, float('inf')) <= max_rank]

def get_secret_word(all_words, difficulty, freq_data):
    """Filter words in real-time for the chosen difficulty"""
    config = DIFFICULTY_CONFIG[difficulty]
    
    # Apply filters sequentially
    words = length_filter(all_words, *config['length'])
    words = hard_letter_filter(words, config['hard_letters'])
    words = frequency_filter(words, config['max_rank'], freq_data)
    
    if not words:  # Fallback if no words match
        words = ["default"]  # Default words
    
    return random.choice(words)
def select_difficulty():
    print("\nChoose difficulty:")
    for mode, config in DIFFICULTY_CONFIG.items():
        print(f"- {mode}: {config['description']}")
    
    while True:
        choice = input("> ").lower()
        if choice in DIFFICULTY_CONFIG:
            return choice
        print("Invalid choice")

# CORRECT ORDER:
freq_data = load_frequency_data()
words = list(get_english_words_set(['web2'], lower=True))
difficulty = select_difficulty()
secret_word = get_secret_word(words, difficulty, freq_data)

#TEST WORKFLOW
#print("\nTesting difficulty levels:")
#for difficulty in DIFFICULTY_CONFIG:
    # Get ALL words matching this difficulty
#   config = DIFFICULTY_CONFIG[difficulty]
#    filtered = length_filter(words, *config['length'])
#    filtered = hard_letter_filter(filtered, config['hard_letters'])
#    filtered = frequency_filter(filtered, config['max_rank'], freq_data)
    
#    print(f"{difficulty}: {len(filtered)} words")
#    if filtered:
#        print(f"  Sample: {random.sample(filtered, min(3, len(filtered)))}")
#    else:
#       print("  WARNING: No words found for this level!")


# Gameplay setup list of words, parameters for the game
max_wrong_attempts = 6
incorrect_guesses = 0
guessed_letters = []
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
        print("\nGood guess!")        

    if not found:
        incorrect_guesses += 1
        print(image_list[incorrect_guesses])
        print(f"Sorry, {guess.upper()} is not in the word. Tries left: {max_wrong_attempts - incorrect_guesses}.")

    print("Updated word: " + " ".join(hidden_word))

if "_" not in hidden_word:
    print(f"You won! The word is '{secret_word}'.")
else:
    print(f"Too many guesses, You lose! The word is '{secret_word}'.")

   
    