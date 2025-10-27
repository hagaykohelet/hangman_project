from hangman.game import *
def prompt_guess() -> str:
    try:
        char = input("please enter a char")
    except ValueError:
        print("you need enter a wotd")
    return char

def print_status(state: dict) -> None:


    print(f"current word: {state["display"]}")
    print(f"The number of letters guessed: {state["guessed"]}")
    print(f"Amount of guesses left: {state["max_tries"] - state["wrong_guesses"]}")



def print_result(state: dict) -> None:
    if is_won:
        return f"very good you hit in word"

    return f"game over {render_summary(state)}"