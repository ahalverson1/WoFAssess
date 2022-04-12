import random

filepath = "words.txt"
f = open(filepath, 'r')
#create word list
wordList = f.readlines()
# close file
f.close()

#open text file of introduction
filepath2 = "introduction.txt"
f = open(filepath2, 'r')
intro = f.read()
#print intro
print(intro)
#close intro file
f.close()

#variables
winRound = False
vowels = ['a', 'e', 'i', 'o', 'u']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
roundBank = 0
totalBank = 0
lettersGuessed = ''

#getWord function
def getWord():
    usedWords = set()
    global word
    global letters
    word = random.choice(wordList).strip()
    letters = len(word)
    print(f'There are ' + str(letters) + ' letters in this word.')
    usedWords.add(word)
    print(f'CHEATTTTTTTTTTTT The word is: ' + str(word))
    return word
    #use random.choice to choose a word from wordList 
    #save random word but do not display 

#word display based on guesses
def displayWord():                              
    displayWord = ''

    for i in range(0, len(word)):
        if word[i] in lettersGuessed:
            displayWord += word[i]
        else:
            displayWord += '_'

    print(f"The word so far: {displayWord}")

def checkGuess():
    lettersGuessed = lettersGuessed + guess
    wrongLetterCount = 0

    for letter in word:
        if letter in lettersGuessed:
            print(f'{letter}', end="")
        else:
            print("_", end="")
            wrongLetterCount += 1
    while winRound == True or wrongLetterCount == 0:
            print('Congrats! The word was ' + word)
            roundBank += 1000
    else:
        spinWheel()


def cGuess(word):
    displayWord()
    wrongLetterCount = 0
    if conGuess in consonants:
        if conGuess in word:
            print(f'{conGuess}', end="")
        else:
            print("_", end="")
            wrongLetterCount += 1
    spinWheel()
    return cGuess

def vGuess(word):
    displayWord()
    wrongLetterCount = 0
    if vowGuess in vowels:
        for letter in word:
            if letter in lettersGuessed:
                print(f'{letter}', end="")
            else:
                print("_", end="")
                wrongLetterCount += 1
                roundBank = (roundBank - 250)
    spinWheel()
    return vGuess

def wordGuess(word):
    displayWord()
    if wGuess == word:
        print(f'{word}', end="")
        print(f'Congrats! You win this round! $'+ str(1000) +' will be added to your total winnings.')
        roundBank = roundBank + 1000
        totalBank = totalBank + roundBank
        winRound = True
    if wGuess != word:
        print(f'Sorry, that is an incorrect guess.')
    return wordGuess

def roundPlay():
    getWord()

#spinWheel function
def spinWheel():
    global conGuess
    global vowGuess
    global wGuess
    global prize
    print(f'Word chosen. Time to spin the wheel!')
    displayWord()
    #array of cash values with 0 as bankrupt and -1 as lose a turn
    wheelLand = [-1, 0, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900]
    prize = random.choice(wheelLand)
    #use random.int to choose a segment from array of cash values, bankrupt, and lose turn
    #if bankrupt or lose a turn
    while prize == -1:
        print(f'Sorry, the wheel landed on Lose Turn.')
        spinWheel()
    while prize == 0:
        roundBank == 0
        print(f'Oh no! The wheel landed on BANKRUPT.')
        spinWheel()
    while prize >= 0:
    #print random segment
        print(f'The wheel landed on ' + str(prize) + '. ')
        userChoice = input('What would you like to do? Guess a consonant, enter 1; Buy a vowel, enter 2; Guess the word, enter 3. ')
        if userChoice <= str(0):
            print(f'Try again.')
        if userChoice >= str(4):
            print(f'Try again.')
        #consonant
        if userChoice == str(1):
            conGuess = input('Guess a consonant: ')
            if conGuess not in consonants:
                print(f'Please enter a consonant.')
            if conGuess in consonants:
                cGuess(conGuess)
        #vowel
        if userChoice == str(2):
            vowGuess = input('Ok, vowels cost $' + str(250) + '. What vowel would you like to buy? ')
            if vowGuess not in vowels:
                print(f'Please enter a vowel.')
            if vowGuess in vowels:
                vGuess(vowGuess)
        #word
        if userChoice == str(3):
            wGuess = input('Ok, what word would you like to guess? ')
            wordGuess(wGuess)

roundPlay()
spinWheel()

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
        #print totalBank + $1000