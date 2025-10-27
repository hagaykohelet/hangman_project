
def prompt_guess() -> str:

    char = input("please enter a char: ")
    return char

def print_status(state: dict) -> None:

    print(f"current word: {state["display"]}")
    print(f"The number of letters guessed: {state["guessed"]}")
    print(f"Amount of guesses left: {state["max_tries"] - state["wrong_guesses"]}")



def print_result(state: dict) -> None:
    if "_" not in state["display"]:
        print("you won")

    else:
        print("game over")

