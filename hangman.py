import random
word_list = []
file = open("word_list.txt")
for word in file:
    word_list.append(word.strip())
file.close()

print(f"{word_list}")

# list of words, parameters for the game
max_attempts = 6
incorrect_guesses = 0
guessed_letters = []
secret_word = random.choice(word_list)
hidden_word = ["_"] * len(secret_word)

print("Welcome to my shit game of Hangman.")
print("Current word: " + " ".join(hidden_word))


while "_" in hidden_word and incorrect_guesses < max_attempts:
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
        print(f"Sorry, {guess.upper()} is not in the word, guess again. Tries left: {max_attempts - incorrect_guesses}.")

    print("Updated word: " + " ".join(hidden_word))

if "_" not in hidden_word:
    print(f"You won! The word is '{secret_word}'.")
else:
    print(f"Too many guesses, You lose! The word is '{secret_word}'.")
 
   
    