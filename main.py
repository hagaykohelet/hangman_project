from hangman.game import init_state, validate_guesses, apply_guess,is_won,is_lost,render_display,render_summary
from hangman.io import prompt_guess,print_status,print_result
from hangman.words import choose_secret_word
from data.words import words
def play(words: list[str], max_tries: int=6):
    state_game = init_state(choose_secret_word(words),max_tries)

    while not is_won(state_game) and not is_lost(state_game):
        print_status(state_game)
        char = prompt_guess()
        test = validate_guesses(char, state_game["guessed"])

        if test[0]:
            if apply_guess(state_game,char):
                for k, v in enumerate(state_game["secret"]):
                    if v == char:
                        state_game["display"][k]=v
        else:
            state_game["guessed"] = test[1]
            print(state_game)
            render_summary(state_game)

        if is_won(state_game):
            print("You found the word")
            print(f"the word is {state_game["secret"]}")








if __name__ == "__main__":
    print(play(words))