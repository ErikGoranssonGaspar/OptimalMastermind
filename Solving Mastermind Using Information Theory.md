*[[3blue1brown - Solving Wordle using information theory|3blue1brown used information theory to play optimal Wordle.]] The same method should be applicable to Mastermind, which is also based on revealing limited information. Wordle is of course really a variant of Mastermind, with the key difference that all characters (letters or colors) are equally likely in the original.*

>[!task] Endgoal
>Make a webapp to play optimal Mastermind.

- [x] Implement Mastermind in Python, interactive and machine playable. 
      Architecture: 
	      Func (secret_key, guess) -> (response)
	      Func (codemaster_response, sequence_of_guesses) -> (probability_of_response)
	      Func (codemaster_response, sequence_of_guesses) -> (information of guess)
	      Interactive terminal mode (use manim?)
	      For a guess (or sequence of guesses) show probability of each Codemaker response and its entropy (use manim?)
- [x] Compute optimal move
- [ ] Make web app

I have stated the [[Mastermind Rules|rules of Mastermind]] in another note.
## Optimal Play
With $n = 5$ pegs in a secret key, each of which in one of $k = 8$ colors there are $8^5 = 32 \,764$ possible secret keys. Assume that the secret key is selected uniformly at random, i.e. we have an uninformative prior.  Each wrong guess narrows down the space of possible outcomes; the Codemaster responds with one out of $3^5 = 243$ replies. ==No, fewer! Order doesn't matter.== The more common a reply, the less it reduces the outcome space. The probability of a Codemaster response is the fraction of (still) possible secret keys which give that code. At each guess, we wish to pick the code which reduces the outcome space the most on average, i.e. maximizes the expected reduction. We will use the [[information]] $I$ to characterize the reduction of outcome space. Because of the relationship with the probability we have the standard result
$$
I = -\log_{2} (p).
$$
We thus wish to pick the guess which minimizes
$$
\sum_{\text{responses }x} p(x) \times -{log_{2}}\,p(x)
$$

This quantity, the expected information, is also called the [[entropy]]. 

Algorithm for finding the guess which maximizes entropy:
1. Given a history of guesses & responses, find all still possible secret keys: ``list[(Key, Response)] -> list[Key]``
2. For each still possible secret key, for each possible response, calculate the probability of receiving this response having made the guess. That is, the ratio of the number of then possible secret keys to the larger number of now possible.
3. Calculate the entropy of each viable guess and pick the one with the highest.
## Python Implementation
The original problem (num_digits=5, num_colors=8), i.e. the Mastermind I played as a child, turned out to be so expensive that precomputing possible_keys() would require a > 100 GB lookup table. Without a lookup table the program, while correct, is unusably slow.

It turns out Donald E. Knuth in the first paper on the topic ("The Computer as Master Mind", 1976) considered the reduced version (num_digits=5, num_colors=8). This is much more tractable; I switch to it.
