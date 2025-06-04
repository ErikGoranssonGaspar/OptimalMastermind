from random import vonmisesvariate
from mastermind_classes import *
import pickle


with open('lookup.pkl', 'rb') as f:
    lookup = pickle.load(f)
key_len = 4
num_colors = 6


def best_guess(history: tuple[tuple[Key, Response], ...]) -> tuple[Key, dict[Key, float]]:
    viable_guesses = set.intersection(set(all_keys()), *[possible_keys(guess, response) for guess, response, in history])
    if len(viable_guesses) == 1:
        [only_guess] = viable_guesses
        return only_guess, {only_guess: 0.0}
    guess_entropy = entropy(viable_guesses)
    return max(guess_entropy, key=guess_entropy.get), guess_entropy


def possible_keys(guess: Key, resp: Response) -> set[Key]:
    return lookup[(guess, resp)]


def entropy(viable_guesses: set[Key]) -> dict[Key, float]:
    from math import log2
    total_len = len(viable_guesses)
    responses = all_responses()
    guess_entropy = {}
    # QQ: do we ever want to make a guess TWEIPOA
    for guess in viable_guesses:
    #for guess in all_keys():
        entropy = 0
        for response in responses:
            #print(possible_keys(guess, response))
            #print(len(possible_keys(guess, response).intersection(viable_guesses)))
            p = len(possible_keys(guess, response).intersection(viable_guesses)) / total_len
            if p > 0: entropy += -p * log2(p)
        guess_entropy[guess] = entropy
    return guess_entropy


def all_keys() -> tuple[Key, ...]:
    from itertools import product
    return tuple(Key(key) for key in product(range(1, num_colors+1), repeat=key_len))


def all_responses() -> tuple[Response, ...]:
    def strip_zeros(lst: tuple) -> list:
        return [l for l in lst if l != 0]
    from itertools import combinations_with_replacement
    return tuple(Response(sorted(strip_zeros(r), reverse=True)) for r in combinations_with_replacement(range(3), key_len))


def response(secret_key: Key, guess: Key) -> Response:
    full_matches = 0
    freq_secret = [0]*(num_colors+1)
    freq_guess = [0]*(num_colors+1)
    for s, g in zip(secret_key.key, guess.key):
        if s == g: full_matches += 1
        else:
            freq_secret[s] += 1
            freq_guess[g] += 1

    partial_matches = sum([min(freq_secret[d], freq_guess[d]) for d in range(1, num_colors+1)])
    return Response((2,)*full_matches + (1,)*partial_matches)


def random_key(key_len, num_colors):
    from random import randint
    return Key([randint(1, num_colors) for _ in range(key_len)])


if __name__ == "__main__":
    history = []
    history.append((Key(5326), Response(222)))
    #history.append((Key(5344), Response()))

    guess, guess_entropy = best_guess(history)
    print([(key, guess_entropy[key]) for key in sorted(guess_entropy, key=guess_entropy.get, reverse=False)])
    print(guess)

