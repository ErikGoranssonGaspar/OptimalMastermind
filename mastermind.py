from typing import List

class Combination:
    def __init__(self, combo: list[int] | tuple[int] | str | int) -> None:
        try:
            if isinstance(combo, list) and all(isinstance(x, int) for x in combo):
                self._combo = combo
            elif isinstance(combo, tuple) and all(isinstance(int(x), int) for x in combo):
                self._combo = list(combo) 
            elif isinstance(combo, str) and all(isinstance(int(x), int) for x in combo):
                self._combo = [int(x) for x in combo]
            elif isinstance(combo, int):
                self._combo = [int(x) for x in str(combo)]
            else:
                raise TypeError("Combination must be either list[int], str[int], or int.")
        except ValueError:  
            raise TypeError("Combination must be either list[int], str[int], or int.")

    def __len__(self) -> int:
        return len(self._combo)

    def __str__(self) -> str:
        combo_string = ''.join(map(str, self._combo))
        return f'Combination({combo_string})'

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other) -> bool:
        return self._combo == other._combo

    @property
    def string(self) -> str:
        return ''.join([str(c) for c in self._combo])

class Key(Combination):
    @property
    def key(self):
        return self._combo

    def __str__(self) -> str:
        combo_string = ''.join(map(str, self._combo))
        return f'Key({combo_string})'


class Response(Combination):
    @property
    def response(self):
        return self._combo

    def __str__(self) -> str:
        combo_string = ''.join(map(str, self._combo))
        return f'Response({combo_string})'


def response(secret_key: Key, guess: Key) -> Response:
    assert len(secret_key) == len(guess), "The guess must be the same length as the secret key." 

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
    

def possible_keys(history: list[tuple[Key, Response]]) -> list[Response]:
    pass

if __name__ == "__main__":
    secret_key = random_key(key_len=5, num_colors=8)
    guess = random_key(key_len=5, num_colors=8)
    print(response(secret_key=secret_key, guess=guess))

