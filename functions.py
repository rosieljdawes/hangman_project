from config import DIFFICULTY_CONFIG, MAX_WRONG_ATTEMPTS
import os
import random
import pandas as pd

#load frequency data
def load_frequency_data():
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, 'data', 'unigram_freq.csv')
    
    try:
        df = pd.read_csv(csv_path)
        return {row['word']: idx+1 for idx, row in df.iterrows()}
    except FileNotFoundError:
        print(f"Error: Save unigram_freq.csv at {csv_path}")
        return {}  
    
def length_filter(words, min_len, max_len):
    return [w for w in words if min_len <= len(w) <= max_len]

def hard_letter_filter(words, max_allowed):
    hard_letters = {'x', 'z', 'q', 'v'}
    return [w for w in words if sum(1 for c in w if c in hard_letters) <= max_allowed]

def frequency_filter(words, max_rank, freq_data):
    return [w for w in words if freq_data.get(w, float('inf')) <= max_rank]

def get_secret_word(all_words, difficulty, freq_data):
    config = DIFFICULTY_CONFIG[difficulty]

    words = length_filter(all_words, *config['length'])
    words = hard_letter_filter(words, config['hard_letters'])
    words = frequency_filter(words, config['max_rank'], freq_data)
    
    if not words:  
        words = ["default"] 
    
    return random.choice(words)
def select_difficulty():
    print("\nChoose difficulty:\n")
    for mode, config in DIFFICULTY_CONFIG.items():
        print(f"- {mode}: {config['description']}")
    
    while True:
        choice = input("> ").lower()
        if choice in DIFFICULTY_CONFIG:
            return choice
        print("Invalid choice")

def calculate_score(difficulty_score, incorrect_guesses, total_guesses=MAX_WRONG_ATTEMPTS):
    remaining_attempts = total_guesses - incorrect_guesses
    score = remaining_attempts * difficulty_score * 10
    return max(0, score)
