import random

def choose_secret_word(words: list[str]) -> str:
    random_word = random.randint(0,len(words))
    return words[random_word]