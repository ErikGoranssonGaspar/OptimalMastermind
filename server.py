from flask import Flask, render_template, request, render_template_string, redirect, url_for
from urllib.parse import parse_qs, parse_qsl
from mastermind_classes import *
from mastermind import *
from jinja_markdown2 import MarkdownExtension
from jinja2 import ChoiceLoader, FileSystemLoader
import math

app = Flask(__name__)
app.jinja_env.add_extension(MarkdownExtension)
app.jinja_loader = ChoiceLoader([
    app.jinja_loader,
    FileSystemLoader(['static/docs'])
])
@app.route("/")
def index():
    return redirect(url_for("mastermind"))


@app.route("/mastermind", methods=["GET"])
def mastermind():    
    secret_key = random_key(key_len=4, num_colors=6)
    _, sug_guess = best_guess(history=[])
    return render_template(
        #'base.html',
        'mastermind_start.html',
        secret_key=secret_key,
        sug_guess=sorted(sug_guess.items(), key=lambda x: x[1], reverse=True),
        colorcode=colorcode,
    )

@app.route("/guess", methods=["PUT"])
def guess():
    secret_key = Key(1364)
    data = [color for i, color in parse_qsl(request.get_data(as_text=True))]
    secret_key, guess, history = parse_response(data)
    history.append((guess, response(secret_key, guess)))
    _, sug_guess = best_guess(history)
    viable_guesses = set.intersection(set(all_keys()), *[possible_keys(guess, response) for guess, response, in history])
    num_viable = len(viable_guesses)
    return render_template('mastermind_play.html',
                           history=history,
                           colorcode=colorcode,
                           sug_guess=sorted(sug_guess.items(), key=lambda x: x[1], reverse=True),
                           num_viable=num_viable
    )

@app.template_filter("log2")
def log2_filter(value):
    return math.log2(value)

@app.template_filter("nonzero")
def filter_nonzero(d):
    return {(k, v) for k, v in d if v != 0}

colorcode = {
    'red': 1,
    'blue': 2,
    'yellow': 3,
    'green': 4,
    'orange': 5,
    'purple': 6,
    1: 'red',
    2: 'blue',
    3: 'yellow',
    4: 'green',
    5: 'orange',
    6: 'purple'
}

def parse_response(data):
    secret_key, data = Key(data[0]), data[1:]
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
    guess, history = history[-1][0], history[:-1]
    return secret_key, guess, history

if __name__ == '__main__':
    app.run(debug=True, port=8000)
