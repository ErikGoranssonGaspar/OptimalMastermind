from mastermind_classes import *

# Optimization:
# v1 4.673 s ±  0.033 s
# v2 202.9 ms ±   1.0 ms
def best_guess(history: tuple[tuple[Key, Response], ...]) -> tuple[Key, dict[Key, float]]:
    viable_guesses = set.intersection(*[possible_keys(guess, response) for guess, response, in history])
    guess_entropy = entropy(viable_guesses)
    return max(guess_entropy, key=guess_entropy.get), guess_entropy


# PRECOMPUTE THIS 
def possible_keys(guess: Key, resp: Response) -> set[Key]:
    return set(key for key in all_keys() if response(secret_key=key, guess=guess) == resp)


def entropy(viable_guesses: set[Key]) -> dict[Key, float]:
    from math import log2
    total_len = len(viable_guesses)
    responses = all_responses()
    guess_entropy = {}
    for guess in viable_guesses:
        entropy = 0
        for response in responses:
            p = len(possible_keys(guess, response).intersection(viable_guesses)) / total_len
            if p > 0: entropy += -p * log2(p)
    return guess_entropy


def all_keys() -> tuple[Key, ...]:
    from itertools import product
    return tuple(Key(key) for key in product(range(1, 8+1), repeat=5))


def all_responses() -> tuple[Response, ...]:
    def strip_zeros(lst: tuple) -> list:
        return [l for l in lst if l != 0]
    from itertools import combinations_with_replacement
    return tuple(Response(sorted(strip_zeros(r), reverse=True)) for r in combinations_with_replacement(range(3), 5))


def response(secret_key: Key, guess: Key) -> Response:
    response = [2 if key_dig == guess_dig else 0 for key_dig, guess_dig in zip(secret_key.key, guess.key)]

    for i, (key_dig, guess_dig) in enumerate(zip(secret_key.key, guess.key)):
        if key_dig == guess_dig:
            continue

        remaining_key = [k for i, k in enumerate(secret_key.key) if response[i] == 0]
        if guess_dig in remaining_key:
            response[i] = 1

    response = sorted([r for r in response if r != 0], reverse=True)
    return Response(response)


def random_key(key_len, num_colors):
    from random import randint
    return Key([randint(1, num_colors) for _ in range(key_len)])


if __name__ == "__main__":
    history = []
    history.append((Key(53267), Response(21)))
    history.append((Key(53447), Response(2221)))

    guess, guess_entropy = best_guess(history)
    print(guess)
