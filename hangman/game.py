

from words import choose_secret_word

def init_state(secret: str, max_tries: int) -> dict:
    state_game = {"secret" : secret,
                 "display": list[str],
                 "guessed": set[str],
                 "wrong_guesses": int,
                 "max_tries": max_tries}
    return state_game


def validate_guesses(ch:str, guessed: set[str]) -> tuple[bool, str]:
    if len(ch) == 1:
        if ch in guessed:
            return False, f"{ch} alraedy exist"
        else:
            return True, f"You hit the right letter {ch}"
    else:
        raise "you need enter only one word"


def apply_guess(state:dict, ch:str) -> bool:
    if ch in state["secret"]:
        return True
    else:
        return False


def is_won(state: dict) -> bool:
    if "_" not in state["display"]:
        return True



def is_lost(state: dict) -> bool:
    if state["wrong_guesses"] >= state["max_tries"]:
        return True

def render_display(state: dict) -> str:
    return " ".join(state["display"])


def render_summary(state: dict) -> str:
    return state["secret"], state["guessed"]