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

#code blocks
#for game play scroll down to line 229

#variables
winRound = False
wheelLand = [-1, 0, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900]
vowels = ['a', 'e', 'i', 'o', 'u']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
lettersGuessed = ''
roundBank = 0
totalBank = 0
wrongLetterCount = 0

#getWord function
def getWord():
    usedWords = set()
    global word
    global letters
    #choosing random word
    word = random.choice(wordList).strip()
    print(f'Word chosen. Time to spin the wheel!')
    letters = len(word)
    print(f'There are ' + str(letters) + ' letters in this word.')
    #ensure words aren't reused
    usedWords.add(word)
    #print word for cheat for testing
    print(f'CHEATTTTTTTTTTTT The word is: ' + str(word))
    return word
    #use random.choice to choose a word from wordList 
    #save random word but do not display 

def spinWheel():
    global prize
    global roundBank
    #random choice of cash values, lose turn, or bankrupt
    prize = random.choice(wheelLand)
    if prize == -1:
        print(f'Sorry, the wheel landed on Lose Turn.')
        roundPlay()
    if prize == 0:
        print(f'Oh no! The wheel landed on BANKRUPT.')
        #drain round bank
        roundBank = 0
        roundPlay()
    if prize >= 0:
        print(f'The wheel landed on $ {prize}.')
        #continue on to round play loop

def roundPlay():
    global roundBank
    global totalBank
    global lettersGuessed
    global wrongLetterCount
    winRound = False

    while winRound == False:
        print('Your bank this round is: $' + str(roundBank) +'. ')
        print(f'Letters guessed so far: ' + lettersGuessed)
        print('\n')
        #display given letters and appropriate blanks
        for letter in word:
            if letter in lettersGuessed:
                print(f'{letter}', end="")
            else:
                print("_", end="")
    #first con
        print('\n')
        userChoice = input('Would you like to: (1) Guess a consonant, (2) Buy a vowel, or (3) Attempt to solve? ')
        if userChoice == str(1):
            if winRound == True:
                print('\n')
                break
            spinWheel()
            guess = input('Please enter a consonant: ')
            guessChar = len(guess)
            if guessChar > 1:
                print('Too long of an entry.')
            if guess not in consonants:
                print('Sorry! Not a consonant.')
            if guess in lettersGuessed:
                print('Sorry, that has already been guessed.')
            if guess in consonants and guess not in lettersGuessed:
                print('Lets check...')
                lettersGuessed = lettersGuessed + guess
                if guess in word:
                    roundBank += prize
                    print('Good guess!')
                if guess not in word:
                    print('Sorry, that letter is not in the word.')
                    wrongLetterCount += 1

        if userChoice == str(2):
            if roundBank < 250:
                print('Sorry, you do not have enough money to buy a vowel.')
            else:
                roundBank -= 250
                guess = input('Ok, buy a vowel: ')
                guessChar = len(guess)
                if guessChar > 1:
                    print('Too long of an entry.')
                if guess not in vowels:
                    print('Sorry! Not a vowel.')
                if guess in lettersGuessed:
                    print('Sorry, that has already been guessed.')
                if guess in vowels and guess not in lettersGuessed:
                    print('Lets check...')
                    lettersGuessed = lettersGuessed + guess
                    if guess in word:
                        roundBank += prize
                        print('Good guess!') 
                    if guess not in word:
                        print('Sorry, that letter is not in the word.')
                        wrongLetterCount += 1
                   
        if userChoice == str(3):
            guess = input('Ok, try to solve the puzzle: ')
            if guess == word:
                winRound = True
                roundBank += 1000
                totalBank = totalBank + roundBank
                print("")
                print(f'Congrats! The word was {word}.')
                print('Your total bank is: $' + str(totalBank) +'. ')
                return winRound
            else:
                print('Sorry, your guess is incorrect.')
    else:
        winRound = True


def finalGuesses():
    global givenLetters
    global finalLetters
    global guessLetters
    global finalConsonants
    global finalVowels
    finalLetters = []
    guessLetters = []
    givenLetters = ['r', 's', 't', 'l', 'e']
    finalConsonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'm', 'n', 'p', 'q', 'v', 'w', 'x', 'y', 'z']
    finalVowels = ['a', 'i', 'o', 'u']        
    print(f'Letters provided: ' + str(givenLetters))
    print('\n')
    #display given letters and appropriate blanks
    for letter in word:
        if letter in givenLetters:
            print(f'{letter}', end="")
        else:
            print("_", end="")
    #first con
    print('\n')
    guess = input('Please enter your first consonant: ')
    if guess in givenLetters or guess in finalVowels:
        print('Not a consonant or already been picked. Move on to the second consonant.')
    guessChar = len(guess)
    if guessChar > 1:
        print('Too long of an entry.')
    else:
        guessLetters += guess
    #second con
    guess = input('Please enter your second consonant: ')
    if guess in guessLetters or guess in givenLetters or guess in finalVowels:
        print('Not a consonant or already been picked. Move on to the third consonant.')
    guessChar = len(guess)
    if guessChar > 1:
        print('Too long of an entry.')
    else:
        guessLetters += guess
    #third con
    guess = input('Please enter your third consonant: ')
    if guess in guessLetters or guess in givenLetters or guess in finalVowels:
        print('Not a consonant or already been picked. Move on to the vowel.')
    guessChar = len(guess)
    if guessChar > 1:
        print('Too long of an entry.')
    else:
        guessLetters += guess
    #vowel
    guess = input('Please enter your vowel: ')
    if guess in guessLetters or guess in givenLetters or guess in finalConsonants:
        print('Not a vowel or already been picked. Time to guess.')
    guessChar = len(guess)
    if guessChar > 1:
        print('Too long of an entry.')
    else:
        guessLetters += guess
    finalLetters += givenLetters
    finalLetters += guessLetters
    return finalLetters

def finalPlay():
    global totalBank
    global finalLetters
    global givenLetters
    finalConsonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'm', 'n', 'p', 'q', 'v', 'w', 'x', 'y', 'z']
    finalVowels = ['a', 'i', 'o', 'u']
    print(finalLetters)
    while winRound == False:
        for letter in word:
            if letter in finalLetters:
                print(f'{letter}', end="")
            else:
                print("_", end="")
        print('\n')
        finalGuess = input('Ok, try to solve the puzzle: ')
        if finalGuess == word:
            totalBank = totalBank + 10000
            print("")
            print(f'Congrats! The word was {word}.')
            print('The cash prize was...... $10000!')
            print('Your total bank is: $' + str(totalBank) +'. ')
            return winRound == True
        else:
            print('Sorry, your guess is incorrect. Game over.')
            break
    while winRound == True:
        print('Congrats! The word was ' + word)
        print('Your total bank is: $' + str(totalBank) +'. ')
        break



#Round One
getWord()
roundPlay()

#Round Two
print('\n')
print('============================================================')
print('Lets play Round Two! The same rules apply for this round.')
print('============================================================')

getWord()
roundBank -= roundBank
lettersGuessed = ''
roundPlay()

#Round Three
print('\n')
print('============================================================')
print('Lets play the final round!')
print('============================================================')

#open text file of final round introduction
filepath3 = "finalroundintro.txt"
f = open(filepath3, 'r')
final = f.read()
#print final round intro
print(final)
#close file
f.close()

getWord()
finalGuesses()
finalPlay()