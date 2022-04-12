import random
import time

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
    word = random.choice(wordList).strip()
    print(f'Word chosen. Time to spin the wheel!')
    letters = len(word)
    print(f'There are ' + str(letters) + ' letters in this word.')
    usedWords.add(word)
    print(f'CHEATTTTTTTTTTTT The word is: ' + str(word))
    return word
    #use random.choice to choose a word from wordList 
    #save random word but do not display 

getWord()

def winnings():
    roundBank = roundBank + prize
    print('Your bank this round is: $' + str(roundBank) +'. ')
    return roundBank

def endRound():
    roundBank = roundBank + 1000
    totalBank = totalBank + roundBank
    print('Your total bank is: $' + str(roundBank) +'. ')

def bankruptcy():
    roundBank == 0
    return roundBank

def spinWheel():
    global prize
    global roundBank
    prize = random.choice(wheelLand)
    if prize == -1:
        print(f'Sorry, the wheel landed on Lose Turn.')
        roundPlay()
    if prize == 0:
        print(f'Oh no! The wheel landed on BANKRUPT.')
        roundBank = 0
        roundPlay()
    if prize >= 0:
        print(f'The wheel landed on $ {prize}.')

def winnings():
    global roundBank
    global totalBank    
    roundBank = 0
    totalBank = 0
    roundBank = roundBank + prize
    print('Your bank this round is: $' + str(roundBank) +'. ')

# def checkGuess():
#     wrongLetterCount = 0
#     print(f'Letters guessed so far: ' +lettersGuessed)
#     for letter in word:
#         if letter in lettersGuessed:
#             winnings()
#         else:
#             wrongLetterCount += 1
#     while winRound == True or wrongLetterCount == 0:
#             print('Congrats! The word was ' + word)
#             endRound()
#             break
#     else:
#         roundPlay()

def endRound():
    roundBank += 1000
    totalBank = totalBank + roundBank
    print('Your total bank is: $' + str(totalBank) +'. ')

def roundPlay():
    global roundBank
    global totalBank
    global lettersGuessed
    global wrongLetterCount

    while winRound == False:
        print('Your bank this round is: $' + str(roundBank) +'. ')
        print(f'Letters guessed so far: ' + lettersGuessed)

        userChoice = input('Would you like to: (1) Guess a consonant, (2) Buy a vowel, or (3) Attempt to solve? ')
        if winRound == True:
            break
        if userChoice == str(1):
            spinWheel()
            guess = input('Please enter a consonant: ')
            guessChar = len(guess)
            if guessChar > 1:
                print('Too long of an entry.')
            if guess not in consonants:
                print('Sorry! Not a consonant.')
            if guess in consonants:
                print('Lets check...')
                lettersGuessed = lettersGuessed + guess
                for letter in word:
                    if letter in lettersGuessed:
                        print(f'{letter}', end="")
                    else:
                        print("_", end="")
                if guess in word:
                    roundBank += prize
                    print('  Good guess!')
                # if word in lettersGuessed:
                #     roundBank += 1000
                #     totalBank = totalBank + roundBank
                #     print("")
                #     print(f'  Congrats! The word was {word}')
                #     print('Your total bank is: $' + str(totalBank) +'. ')
                #     winRound == True
                if guess not in word:
                    print('  Sorry, that letter is not in the word.')
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
                if guess in vowels:
                    print('Lets check...')
                    lettersGuessed = lettersGuessed + guess
                    for letter in word:
                        if letter in lettersGuessed:
                            print(f'{letter}', end="")
                        else:
                            print("_", end="")
                    if guess in word:
                        roundBank += prize
                        print('  Good guess!') 
                    if guess not in word:
                        print('  Sorry, that letter is not in the word.')
                        wrongLetterCount += 1
            #         if word in lettersGuessed:
            #             roundBank += 1000
            #             totalBank = totalBank + roundBank
            #             print("")
            #             print(f'  Congrats! The word was {word}')
            #             print('Your total bank is: $' + str(totalBank) +'. ')
            #             winRound == True
            #             break
                   
        if userChoice == str(3):
            guess = input('Ok, try to solve the puzzle: ')
            if guess == word:
                roundBank += 1000
                totalBank = totalBank + roundBank
                print("")
                print(f'Congrats! The word was {word}.')
                print('Your total bank is: $' + str(totalBank) +'. ')
                return winRound == True
            else:
                print('Sorry, your guess is incorrect.')
    while winRound == True or wrongLetterCount == 0:
        print('Congrats! The word was ' + word)
        print('Your total bank is: $' + str(totalBank) +'. ')
        break
    else:
        print('Try again.')

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
    #first con
    guess = input('Please enter your first consonant: ')
    if guess in givenLetters or guess in finalVowels:
        print('Please try another consonant.')
    guessChar = len(guess)
    if guessChar > 1:
        print('Too long of an entry.')
    else:
        guessLetters += guess
    #second con
    guess = input('Please enter your second consonant: ')
    if guess in guessLetters or guess in givenLetters or guess in finalVowels:
        print('Please try another consonant.')
    guessChar = len(guess)
    if guessChar > 1:
        print('Too long of an entry.')
    else:
        guessLetters += guess
    #third con
    guess = input('Please enter your third consonant: ')
    if guess in guessLetters or guess in givenLetters or guess in finalVowels:
        print('Please try another consonant.')
    guessChar = len(guess)
    if guessChar > 1:
        print('Too long of an entry.')
    else:
        guessLetters += guess
    #vowel
    guess = input('Please enter your vowel: ')
    if guess in guessLetters or guess in givenLetters or guess in finalConsonants:
        print('Please try another vowel.')
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
            print('Sorry, your guess is incorrect. Try again.')
    else:
        print('Try again.')
    while winRound == True:
        print('Congrats! The word was ' + word)
        print('Your total bank is: $' + str(totalBank) +'. ')
        break



#Round One
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