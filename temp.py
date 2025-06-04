import pickle
from urllib.parse import parse_qs, parse_qsl
from mastermind_classes import *

colorcode = {
    'red': 1,
    'blue': 2,
    'yellow': 3,
    'green': 4,
    'orange': 5,
    'purple': 6
}

with open("data.pkl", "rb") as f:
    data = [color for i, color in parse_qsl(pickle.load(f))]

history = []
while len(data) >= 4:
    guess, data = data[:4], data[4:]
    guess = Key([colorcode[color] for color in guess])
    num_blacks = 0
    num_whites = 0
    for color in data:
        if color == 'black':
            num_blacks += 1
        elif color == 'white':
            num_whites += 1
        else:
            break
    data = data[num_blacks+num_whites:]
    response = Response([2]*num_blacks + [1]*num_whites)
    history.append((guess, response))
print(history)
