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

    @property 
    def integer(self) -> int:
        return int(self.string)

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
