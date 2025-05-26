from mastermind import *

key_len = 4
num_colors = 6

#print("Let's play Mastermind! Do you want to set the secret key yourself (1), or play with a random one (2)?")
print(f"Let's play Mastermind! I have selected a secret key, {key_len} pegs long with {num_colors} colors. Type 'best' to see the optimal moves.")

secret_key = random_key(key_len=key_len, num_colors=num_colors)
history = []
while True:
    try:
        guess = input('> ')
        if guess == 'best':
            num_guesses = 5
            _, guess_entropy = best_guess(history)
            if len(guess_entropy) == 1:
                print(f'The only viable guess is {list(guess_entropy.items())[0][0].string}.')
                continue
            guess_entropy = sorted(guess_entropy.items(), key=lambda x: x[1], reverse=True)[:num_guesses]
            print('Best guesses:')
            for guess, entropy in guess_entropy:
                print(f'{guess.string}: {entropy:.2f}')
            continue

        guess = Key(guess)
        resp = response(secret_key=secret_key, guess=guess)
        history.append((guess, resp))
        if len(guess) != key_len:
            print(f'The key is {key_len} digits long and so should your guess be — try again')
            continue
        if max(guess.key) > num_colors:
            print(f'There are only {num_colors} in play. Make another guess!')

        if resp == Response([2]*key_len):
            print('Congrats! You win 🎉')
            break
        else:
            print(f'The Codemaster responds: {resp.string}')
    except KeyboardInterrupt:
        print(f'\nThe secret key was {secret_key.string}.')
        break
    except TypeError:
        print('Invalid guess. Try again!')
        continue
