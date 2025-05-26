import pandas as pd
from matplotlib import pyplot as plt

path = 'num_guesses.csv'
data = pd.read_csv(path)

print(f'Mean number of guesses: {data['num_guesses'].mean():.2f} (σ = {data["num_guesses"].std():.2f})')
print(f'Worst case: {max(data["num_guesses"])}; Best case: {min(data["num_guesses"])}')

plt.figure(figsize=(8, 8))
plt.hist(data["num_guesses"], bins=range(data["num_guesses"].min(), data["num_guesses"].max() + 2))
plt.title("Distribution of Number of Guesses in Mastermind")
plt.xlabel("Number of Guesses")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()
