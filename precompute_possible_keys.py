from itertools import product
from collections import defaultdict
import pickle
from mastermind_classes import * 
from mastermind import *


''' 
# THE LARGER PROBLEM (num_digits=5; num_colors=8) PREVIOUSLY CONSIDERED REQUIRED MORE OPTIMIZATION.
# THE BELOW CODE REDUCES OVERHEAD BY WORKING IMMEDIATELY WITH ARRAYS, NOT THE Key AND Response CLASSES.
# IT IS KEPT HERE FOR FUTURE REFERENCE.
def response(secret_key: tuple[int,...], guess: tuple[int,...]) -> tuple[int,...]:
    num_colors = 6
    full_matches = 0
    freq_secret = [0]*(num_colors+1)
    freq_guess = [0]*(num_colors+1)
    for s, g in zip(secret_key, guess):
        if s == g: full_matches += 1
        else:
            freq_secret[s] += 1
            freq_guess[g] += 1

    partial_matches = sum([min(freq_secret[d], freq_guess[d]) for d in range(1, num_colors+1)])
    return (2,)*full_matches + (1,)*partial_matches


def all_keys() -> tuple[tuple[int ,...], ...]:
    num_digits = 4
    num_colors = 6
    from itertools import product
    return tuple(key for key in product(range(1, num_colors+1), repeat=num_digits))


def all_responses() -> tuple[list[int], ...]:
    num_digits = 4
    def strip_zeros(lst: tuple) -> tuple:
        return tuple(l for l in lst if l != 0)
    from itertools import combinations_with_replacement
    return tuple(tuple(sorted(strip_zeros(r), reverse=True)) for r in combinations_with_replacement(range(3), num_digits))

# OPTIMIZATION
# v1 13.585 s ± 0.205 s / 101 -> Total precompute   25.7 h
# v2 9.448 s ±  0.035 s / 101 ->        "           17.9 h
# v4 7.101 s ±  0.036 s / 101 ->        "           13.4 h
# v5 3.220 s ±  0.009 s / 101 ->        "           6.1 h # IMPROVED response()
'''

if __name__ == "__main__":
    path = 'lookup.pkl'

    keys = all_keys()
    responses = all_responses()
    keypairs = product(keys, responses)
    total_len = len(keys)
    lookup_table = defaultdict(set)
    buckets = defaultdict(set)
    for i, guess in enumerate(keys):
        print(f'Computing lookup table: {i}/{total_len} ({i/total_len*100:.1f} %)\r', end='', flush=True)
        buckets.clear()
        for key in keys:
            r = response(secret_key=key, guess=guess)
            buckets[r].add(key)
            
        for r, group in buckets.items():
            lookup_table[(guess, r)] = group

    print(f'Attempting to save lookup table to {path}...')
    with open(path, 'wb') as f:
        pickle.dump(lookup_table, f)
    print('Succesfully computed lookup table. Exiting.')
