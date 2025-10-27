def init_state(secret: str, max_tries: int) -> dict:
    state_game = {"secret" : secret,
                 "display": ["_" for _ in secret],
                 "guessed": set(),
                 "wrong_guesses": 0,
                 "max_tries": max_tries}
    return state_game

def validate_guess(ch: str, guessed: set[str]) -> tuple[bool, str]:
    if len(ch) == 1:
        if ch in guessed:
            return False, f"{ch} is already exist"
        else:
            return True, f"{ch} not exist in your guess list"
    else:
        return "enter only one word"


def apply_guess(state: dict, ch: str) -> bool:
    if ch in state["secret"]:
        for k, v in enumerate(state["secret"]):
            if ch == v:
                state["display"][k] = ch
        return True
    else:
        return False


def is_won(state: dict) -> bool:
    return  "_" not in state["display"]


def is_lost(state: dict) -> bool:
    return state["wrong_guesses"] >= state["max_tries"]

def render_display(state: dict) -> str:
    return state["display"]


def render_summary(state:dict) -> str:
    return f"the word is: '{state["secret"]}' this is your guesses words {state["guessed"]}"

# def validate_guesses(ch:str, guessed: set[str]) -> tuple[bool, str]:
#
#     if len(ch) == 1:
#         if ch in guessed:
#             return False, f"{ch} alraedy exist"
#
#         else:
#             return True, f"You hit the right letter {ch}"
#     else:
#         raise "you need enter only one word"
#
#
#
# def apply_guess(state:dict, ch:str) -> bool:
#     state["wrong_guesses"] += 1
#     if ch in state["secret"]:
#         return True
#     else:
#         return False
#
#
# def is_won(state: dict) -> bool:
#     return  "_" not in state["display"]
#
#
# def is_lost(state: dict) -> bool:
#     return state["wrong_guesses"] >= state["max_tries"]
#
#
#
# def render_display(state: dict) -> str:
#     return "".join(state["display"])
#
#
# def render_summary(state: dict) -> str:
#     return state["secret"] + state["guessed"]


