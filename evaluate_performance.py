from mastermind import *
from mastermind_classes import *
import csv

def play_game(secret_key: Key) -> int:
    history = []
    while True:
        guess, _ = best_guess(history)
        resp = response(secret_key=secret_key, guess=guess)
        history.append((guess, resp))

        if resp == Response(2222):
            return len(history)


if __name__ == '__main__':
    keys = all_keys()
    num_total = len(keys)
    num_guesses = []
    for i, secret_key in enumerate(keys):
        n = play_game(secret_key)
        num_guesses.append({"key": secret_key.integer, "num_guesses": n})
        print(f'Game {i}/{num_total} ({int(i/num_total*100)} %): {n} guesses\r', end='', flush=True)

    path = "num_guesses.csv"
    print(f'Attempting to write to {path}...')
    with open(path, mode="w", newline="") as file:
        fieldnames = ["key", "num_guesses"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(num_guesses)
    print('Succesfully recorded output.')

# TODO: Randomize chosen move among equal best?
