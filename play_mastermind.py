from mastermind import *

key_len = 5
num_colors = 8

#print("Let's play Mastermind! Do you want to set the secret key yourself (1), or play with a random one (2)?")
print(f"Let's play Mastermind! I have selected a secret key, {key_len} pegs long with {num_colors} colors.")

secret_key = random_key(key_len=key_len, num_colors=num_colors)
try:
    while True:
        guess = Key(input('Guess: '))
        if len(guess) != 5:
            print(f'The key is five {key_len} long and so should your guess be — try again')
            continue
        if max(guess.key) > 8:
            print(f'There are only {num_colors} in play. Make another guess!')

        if guess == secret_key:
            print('Congrats! You win 🎉')
            break
        else:
            print(f'The Codemaster responds: {response(secret_key=secret_key, guess=guess).string}')

except KeyboardInterrupt:
    print(f'\nThe secret key was {secret_key.string}.')
    pass
