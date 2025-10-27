from hangman.game import init_state, validate_guess, apply_guess,is_won,is_lost,render_display,render_summary
from hangman.io import prompt_guess,print_status,print_result
from hangman.words import choose_secret_word
from data.words import words
def play(words: list[str], max_tries: int=6):
    state_game = init_state(choose_secret_word(words),max_tries)
    while not is_won(state_game) and not is_lost(state_game):

        print_status(state_game)

        char = prompt_guess()
        if char not in state_game["guessed"]:
            state_game["wrong_guesses"] += 1
            vali = validate_guess(char,state_game["guessed"])

            print(vali)

            state_game["guessed"].update(char)

            if not vali[0]:
                state_game["guessed"].add(char)

            elif vali[0]:
                test2 = apply_guess(state_game,char)
                print(render_display(state_game))

    print(render_summary(state_game))
    print_result(state_game)


if __name__ == "__main__":
    print(play(words))