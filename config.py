MAX_WRONG_ATTEMPTS = 10

DIFFICULTY_CONFIG = {
    'easy': {
        'length': (4, 5),
        'hard_letters': 0,
        'max_rank': 1000,
        'description': "4-7 letter common words", 
        'difficulty_score': 1
    },
    'medium': {
        'length': (5, 7),
        'hard_letters': 1,
        'max_rank': 1500,
        'description': "5-9 letters, some rare letters",
        'difficulty_score': 2
    },
    'hard': {
        'length': (7, 10),
        'hard_letters': float('inf'),  # No limit
        'max_rank': 2000,
        'description': "7-10 letters, any word",
        'difficulty_score': 3
    },
    'expert': {
        'length': (10, 20),
        'hard_letters': float('inf'),
        'max_rank': float('inf'),
        'description': "10+ letter obscure words\n",
        'difficulty_score': 4
    }
}

IMAGE_LIST = [
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