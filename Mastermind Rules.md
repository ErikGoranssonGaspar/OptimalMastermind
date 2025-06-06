*Based on the official [[mastermind_rules.pdf|American rules of Advanced Mastermind]].*

One player, the *Codemaker*, sets a secret code consisting of $n=5$ pegs, each of which is one of $k=8$ colors. A total of $8^5 = 32 \,764$ different codes are therefore possible. 

The other player, the *Codebreaker*, guesses a code. The Codemaker responds by a combination of key pegs:

- Red peg — right color in right spot
- White peg — right color in wrong spot

Conflicts can occur if the secret code or the guess contains multiples of the same color. They should be handled in accordance with the principle: one key peg for one code peg; red key peg takes presedence over white. The correct behaviour is illsutrated in the following examples:
![[mastermind_rules.pdf#page=2&rect=548,208,775,388|mastermind_rules, p.2]]
![[mastermind_rules.pdf#page=2&rect=550,13,777,142|mastermind_rules, p.2]]
![[mastermind_rules.pdf#page=1&rect=159,446,383,596|mastermind_rules, p.1]]
If the Codebreaker has not found the correct code in 12 guesses, the Codemaker wins.