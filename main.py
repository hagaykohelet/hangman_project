from hangman.game import init_state,validate_guesses
from hangman.words import choose_secret_word
from data.words import words
if __name__ == "__main__":
    print(init_state(choose_secret_word(words)))