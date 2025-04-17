import random
import string

# Words list
words = ["PYTHON", "DEVELOPER", "HANGMAN", "PROGRAMMING", "COMPUTER", "SCIENCE"]

# Hangman drawings
lives_visual_dict = {
    7: """
       +---+
           |
           |
           |
          ===
    """,
    6: """
       +---+
       O   |
           |
           |
          ===
    """,
    5: """
       +---+
       O   |
       |   |
           |
          ===
    """,
    4: """
       +---+
       O   |
      /|   |
           |
          ===
    """,
    3: """
       +---+
       O   |
      /|\\  |
           |
          ===
    """,
    2: """
       +---+
       O   |
      /|\\  |
      /    |
          ===
    """,
    1: """
       +---+
       O   |
      /|\\  |
      / \\  |
          ===
    """,
    0: """
       +---+
       X   |
      /|\\  |
      / \\  |
          ===
    """
}

# Select a valid word
def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

# Main game
def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 7

    while len(word_letters) > 0 and lives > 0:
        print("\nYou have", lives, "lives left. Used letters:", " ".join(used_letters))
        print(lives_visual_dict[lives])
        current_word = [letter if letter in used_letters else '_' for letter in word]
        print("Word:", " ".join(current_word))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print("Wrong guess.")
        elif user_letter in used_letters:
            print("You've already used that letter.")
        else:
            print("Invalid character.")

    if lives == 0:
        print(lives_visual_dict[lives])
        print("You lost. The word was:", word)
    else:
        print("Congratulations! You guessed the word:", word)

# Start game
hangman()