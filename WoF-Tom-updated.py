import random
#modified

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
endTurn = False
winRound = False
wheelLand = [-1, 0, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900]
vowels = ['a', 'e', 'i', 'o', 'u']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
lettersGuessed = ''

roundBank = [0, 0, 0, 0]
totalBank = [0, 0, 0, 0]

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
    #random choice of cash values, lose turn, or bankrupt
    prize = random.choice(wheelLand)
    if prize == -1:
        print(f'Sorry, the wheel landed on Lose Turn.')
        roundPlay()
    if prize == 0:
        print(f'Oh no! The wheel landed on BANKRUPT.')
        #drain round bank
        roundBank[playerTurn] = 0
        playerTurn = playerTurn + 1
        if playerTurn == 3:
            playerTurn -= 3
        roundPlay()
    if prize >= 0:
        print(f'The wheel landed on $ {prize}.')
        #continue on to round play loop

def roundPlay():
    global roundBank
    global totalBank
    global lettersGuessed
    global wrongLetterCount
    global winRound
    global endTurn
    global playerTurn

    winRound = False
    endTurn = False

    if playerTurn > 3:
        playerTurn -= 3

    print('Current player: ' +str(playerTurn + 1))
    
    # while endTurn == False:
    while winRound == False:
        print('Your bank this round is: $' + str(roundBank[playerTurn]) +'. ')
        print(f'Letters guessed so far: ' + lettersGuessed)
        print('Current player: ' +str(playerTurn + 1))
        print('\n')
        #display given letters and appropriate blanks
        for letter in word:
            if letter in lettersGuessed:
                print(f'{letter}', end="")
            else:
                print("_", end="")
        #getting user input from menu
        print('\n')
        userChoice = input('Would you like to: (1) Guess a consonant, (2) Buy a vowel, or (3) Attempt to solve? ')
        #guess word, menu item 3
        if userChoice == str(3):
            guess = input('Ok, try to solve the puzzle: ')
            if guess == word:
                roundBank[playerTurn] += 1000
                totalBank[playerTurn] = totalBank[playerTurn] + roundBank[playerTurn]
                print("")
                print(f'Congrats! The word was {word}.')
                print(f'{playerTurn + 1}s total bank is: $' + str(totalBank[playerTurn]) +'. ')
                endTurn = True
                winRound = True
            else:
                print('Sorry, your guess is incorrect.')
                playerTurn = playerTurn + 1
                if playerTurn == 3:
                    playerTurn -= 3
                endTurn = True
        #guess char, menu item 1
        if userChoice == str(1):
                spinWheel()
                guess = input('Please enter a consonant: ')
                guessChar = len(guess)
                if guessChar > 1:
                    print('Too long of an entry.')
                    playerTurn = playerTurn + 1
                    if playerTurn == 3:
                        playerTurn -= 3
                    endTurn = True
                if guess not in consonants:
                    print('Sorry! Not a consonant.')
                    playerTurn = playerTurn + 1
                    if playerTurn == 3:
                        playerTurn -= 3
                    endTurn = True
                if guess in lettersGuessed:
                    print('Sorry, that has already been guessed.')
                    playerTurn = playerTurn + 1
                    if playerTurn == 3:
                        playerTurn -= 3
                    endTurn = True
                if guess in consonants and guess not in lettersGuessed:
                    print('Lets check...')
                    lettersGuessed = lettersGuessed + guess
                    if guess in word:
                        roundBank[playerTurn] += prize
                        print('Good guess!')
                    if guess not in word:
                        print('Sorry, that letter is not in the word.')
                        wrongLetterCount += 1
                        playerTurn = playerTurn + 1
                        if playerTurn == 3:
                            playerTurn -= 3
                        endTurn = True
        #guess vowel, menu item 2
        if userChoice == str(2):
            if roundBank[playerTurn] < 250:
                print('Sorry, you do not have enough money to buy a vowel.')
                playerTurn = playerTurn + 1
                if playerTurn == 3:
                    playerTurn -= 3
                endTurn = True
            else:
                roundBank[playerTurn] -= 250
                prize == 0
                guess = input('Ok, buy a vowel: ')
                guessChar = len(guess)
                if guessChar > 1:
                    print('Too long of an entry.')
                    playerTurn = playerTurn + 1
                    if playerTurn == 3:
                        playerTurn -= 3
                    endTurn = True
                if guess not in vowels:
                    print('Sorry! Not a vowel.')
                    playerTurn = playerTurn + 1
                    if playerTurn == 3:
                        playerTurn -= 3
                    endTurn = True
                if guess in lettersGuessed:
                    print('Sorry, that has already been guessed.')
                    playerTurn = playerTurn + 1
                    if playerTurn == 3:
                        playerTurn -= 3
                    endTurn = True
                if guess in vowels and guess not in lettersGuessed:
                    print('Lets check...')
                    lettersGuessed = lettersGuessed + guess
                    if guess in word:
                        print('Good guess!') 
                    if guess not in word:
                        print('Sorry, that letter is not in the word.')
                        wrongLetterCount += 1
                        playerTurn = playerTurn + 1
                        if playerTurn == 3:
                            playerTurn -= 3
                        endTurn = True
    while winRound == True:
        break


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
    winRound = False

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
            print("")
            print(f'Congrats! The word was {word}.')
            print('The cash prize was...... $10000!')
            totalBank[playerTurn] += 10000
            print('Your total bank is: $' + str(totalBank[playerTurn]) +'. ')
            return winRound == True
        else:
            print('Sorry, your guess is incorrect. Game over.')
            break
    while winRound == True:
        print(f'Congrats! The word was {word}.')
        print('Your total bank is: $' + str(roundBank[playerTurn]) +'. ')
        break

#Round One
playerTurn = 0
getWord()
roundPlay()

#Round Two
playerTurn = 1
print('\n')
print('============================================================')
print('Lets play Round Two! The same rules apply for this round.')
print('============================================================')

getWord()
roundBank = [0, 0, 0, 0]
lettersGuessed = ''
roundPlay()

#Round Three
finalPlayer = totalBank.index(max(totalBank)) + 1
print('\n')
print('============================================================')
print(f'Lets play the final round! Player {finalPlayer} has the most banked, so they will advance!')
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