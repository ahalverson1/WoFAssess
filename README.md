Wheel of Fortune Assessment M06

This is a terminal-based Wheel of Fortune game with 3 rounds and 1 player (hoping to expand to 3 players eventually with more experience).
I am happy with the resulting game (WoF-single-player-code.py) knowing that this is my very first experience with Python and programming in general.
My code is messy, but for the most part works.

Known Bugs:
- occasionally when solving the puzzle, the loop does not appropriately close and it reverts player to picking a consonant
   to resolve, input a consonant and try solving the puzzle again.

File I/O was used for:
- dictionary
- introduction
- final round introduction

Game rules:
2 regular rounds with 1 player (hope to expand) and 1 final round with 1 player
Each round has one randomly chosen word from a dictionary file

Regular rounds (1 + 2) rules:
Player will choose from a menu to either spin the wheel and guess a consonant, buy a vowel with appropriate funds, or solve the puzzle
For each spin, the wheel will have a randomly chosen segment ranging from cash values $100-$900, BANKRUPT, and Lose a Turn
Contrary from the TV show, correctly guessed consonants will only earn the amount shown on the wheel 1x, not for each consonant. (Hope to fix this in future)
Each vowel costs a $250 flat fee and player must have the funds available from their round's bank in order to buy
BANKRUPT drains the player's round's bank but leaves their total bank intact.
Lose Turn does not drain either player's banks.
For each guessed character, a display of underscores will appear for char not in the word and the guessed character will appear for char in the word.
The round continues until the puzzle has been solved. The player must input the word to solve the puzzle, even if all characters are displaying. 
At the start of Round 2, the round bank is reduced to $0 and Round 1's round bank is converted to the player's total bank.

Final round (3) rules:
Cash prize is $10000
Word with blanks and R-S-T-L-N-E is displayed before player input.
Player is only allowed to input 3 consonants and 1 vowel. If the player inputs incorrectly, there is no opportunity to fix.
Then, the word is displayed again with the given letters and the guessed letters along with underscores.
Player is only allowed to solve the puzzle 1 time. If they input the wrong word, the game is over. If they correctly solve the puzzle, they win the cash prize plus their total bank from the first two rounds.



