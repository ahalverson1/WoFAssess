#import random
#open text file of words, save to wordList

#open text file of introduction
#print intro
#close intro file

#variables
#winGame = True
#vowels = [a, e, i, o, u]
#consonants = [b, c, d ... z]
#playersList = (0, 0, 0)
#roundBank = (0, 0, 0)
#totalBank = (0, 0, 0)

#getWord function
    #use random.choice to choose a word from wordList
    #save random word but do not display

#spinWheel function
    #array of cash values with 0 as bankrupt and -1 as lose a turn
    #use random.int to choose a segment from array of cash values, bankrupt, and lose turn
    #print random segment

#checkGuess function
    #use guessing game format for displaying blanks and guessed letters using input
    #if guess is not in word, break turn
    #if guess is in word, continue turn
    #if guess is the word, totalBank = roundBank + 1000, win_game = True

#roundPlay function
    #getWord function
    #display blanks from random word
    #totalBank = []
    #roundBank = []
    #display totalBank
    #display roundBank
    #while loop while win_game = False
        #spinWheel
        #save and display random segment
        #input what would you like to do? consonant 1, vowel 2, guess 3 menu
            #if input = 1:
                #input enter a consonant
                    #checkGuess
            #if input = 2:
                #roundBank = roundBank - 250
                    #if roundBank < 0:
                        #print Sorry you can't buy a vowel
                    #else:
                        #input enter a vowel
                            #checkGuess
            #if input = 3:
                #input guess the word
                    #checkGuess
            #else:
                #Sorry, next player turn.
    #else if win_game = True
        #print congratulations

#finalPlay function
    #getWord function
    #max bank player plays
    #display blanks from random word minus r, s, t, l, n, and e
    #display totalBank
    #while loop while win_final = False
        #input give me 3 consonants and 1 vowel
            #if input = consonant:
            #checkGuess
    #else if win_final = True
        #print congratulations 
        #print cash prize $1000
        #print totalBank + 1000
            