class Combination:
    def __init__(self, combo: list[int] | tuple[int, ...] | str | int):
        try:
            if isinstance(combo, tuple) and all(isinstance(int(x), int) for x in combo):
                self._combo = combo 
            elif isinstance(combo, list) and all(isinstance(x, int) for x in combo):
                self._combo = tuple(combo)
            elif isinstance(combo, str) and all(isinstance(int(x), int) for x in combo):
                self._combo = tuple((int(x) for x in combo))
            elif isinstance(combo, int):
                self._combo = tuple((int(x) for x in str(combo)))
            else:
                raise TypeError("Combination must be either tuple[int], list[int], str[int], or int.")
        except ValueError:  
            raise TypeError("Combination must be either tuple[int], list[int], str[int], or int.")
            
        self.string = ''.join([str(c) for c in self._combo])

    def __len__(self) -> int:
        return len(self._combo)

    def __eq__(self, other) -> bool:
        return self._combo == other._combo

    def __hash__(self):
        return hash(self._combo)

    def __str__(self) -> str:
        return f'Combination({self.string})'

    def __repr__(self) -> str:
        return self.__str__()



class Key(Combination):
    @property
    def key(self):
        return self._combo

    def __str__(self) -> str:
        return f'Key({self.string})'


class Response(Combination):
    @property
    def response(self):
        return self._combo

    def __str__(self) -> str:
        return f'Response({self.string})'


class GuessOutcome():
    def __init__(self, guess: Key, response: Response):
        self.guess = guess
        self.response = response

    def __str__(self) -> str:
        return f'GuessOutcome(guess:{self.guess.string}, response:{self.response.string})'

    def __repr__(self) -> str:
        return self.__str__()

    def compatible_with(self, key: Key) -> bool:
        return response(secret_key=key, guess=self.guess) == self.response


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
    

def possible_keys(history: list[GuessOutcome], num_colors: int = 8, warm_start: None | list[Key] = None) -> list[Key]:
    from itertools import product
    if warm_start: 
        possible_keys = warm_start
    else:
        possible_keys = [Key(key) for key in product(range(1, num_colors+1), repeat=5)]
    for guess_outcome in history:
        possible_keys = [key for key in possible_keys if guess_outcome.compatible_with(key)]
    return possible_keys


# Optimization:
# v1 4.673 s ±  0.033 s
# v2 202.9 ms ±   1.0 ms
def best_guess(history: list[GuessOutcome]) -> tuple[Key, dict[Key, float]]:
    viable_guesses = possible_keys(history)
    guess_entropy = {guess: entropy(history, guess, keys_history=viable_guesses) for guess in viable_guesses}
    return max(guess_entropy, key=guess_entropy.get), guess_entropy


def entropy(history: list[GuessOutcome], guess: Key, keys_history: None | list[Key] = None) -> float:
    from math import log2
    responses = all_responses()
    entropy = 0
    if not keys_history:
        keys_history = possible_keys(history)

    for response in responses:
        p = len(possible_keys([GuessOutcome(guess=guess, response=response)], warm_start=keys_history)) / len(keys_history)
        if p > 0:
            entropy += -p * log2(p)
    return entropy


def all_responses() -> list[Response]:
    def strip_zeros(lst: tuple) -> list:
        return [l for l in lst if l != 0]
    from itertools import combinations_with_replacement
    return [Response(sorted(strip_zeros(r), reverse=True)) for r in combinations_with_replacement(range(3), 5)]


def prob(history: list[GuessOutcome], guess: Key, response: Response) -> float:
    return len(possible_keys(history + [GuessOutcome(guess=guess, response=response)])) / len(possible_keys(history))


if __name__ == "__main__":
    history = []
    history.append(GuessOutcome(guess=Key(53267), response=Response(21)))
    #history.append(GuessOutcome(guess=Key(53447), response=Response(2221)))

    guess, guess_entropy = best_guess(history)
    print(guess)
