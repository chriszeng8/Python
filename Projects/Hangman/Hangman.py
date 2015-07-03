# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
def drawHangman(Mistake):
    if Mistake==8:
        print " _________     ";
        print "|         |    ";
        print "|         0    ";
        print "|        /|\\  ";
        print "|        / \\  ";
        print "|              ";
        print "|              ";
    elif Mistake==7:
        print " _________     ";
        print "|         |    ";
        print "|         0    ";
        print "|        /|\\  ";
        print "|        /     ";
        print "|              ";
        print "|              ";
    elif Mistake==6:
        print " _________     ";
        print "|         |    ";
        print "|         0    ";
        print "|        /|\\  ";
        print "|              ";
        print "|              ";
        print "|              ";
    elif Mistake==5:
        print " _________     ";
        print "|         |    ";
        print "|         0    ";
        print "|        /|    ";
        print "|              ";
        print "|              ";
        print "|              ";
    elif Mistake==4:
        print " _________     ";
        print "|         |    ";
        print "|         0    ";
        print "|        /     ";
        print "|              ";
        print "|              ";
        print "|              ";
    elif Mistake==3:
        print " _________     ";
        print "|         |    ";
        print "|         0    ";
        print "|              ";
        print "|              ";
        print "|              ";
        print "|              ";
    elif Mistake==2:
        print " _________     ";
        print "|         |    ";
        print "|              ";
        print "|              ";
        print "|              ";
        print "|              ";
        print "|              ";
    elif Mistake==1:
        print " _________     ";
        print "|              ";
        print "|              ";
        print "|              ";
        print "|              ";
        print "|              ";
        print "|              ";
    elif Mistake==0:
        print "               ";
        print "|              ";
        print "|              ";
        print "|              ";
        print "|              ";
        print "|              ";
        print "|              ";

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    return (set(secretWord)<=set(lettersGuessed))



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    word=''
    for ch in secretWord:
        if (ch in lettersGuessed):
            word+=ch+''
        else:
            word+='_'
    return word


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    AvaStr=set(string.ascii_lowercase[:]+'')
    FinalStr=''
    for ch in lettersGuessed:
        AvaStr.remove(ch)
    AvaStr=list(AvaStr)
    AvaStr.sort()
    for i in AvaStr:
        FinalStr+=i
    return FinalStr


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''

    # FILL IN YOUR CODE HERE...
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is '+str(len(secretWord))+' letters long.'
    GuessTime=8
    print '-------------'
    lettersGuessed=[]

# only stops when 1. either the word is guessed, or 2. lettersGuessed is greater than the max allowable number of guess times
    while 1:
        print 'You have '+str(GuessTime)+' guesses left.'
        availableLetters=getAvailableLetters(lettersGuessed)
        print 'Available letters: '+availableLetters

        
        guessedletter=None
        while 1:
            guessedletter=raw_input('Please guess a letter: ')
            if (len(guessedletter)==1)&((guessedletter in string.ascii_uppercase)|(guessedletter in string.ascii_lowercase)):
                break
            else:
                print 'This is an invalid input. Please enter a single letter.'
        guessedletter=guessedletter.lower()


        # guessed the right letter
        if ((guessedletter in secretWord)&(guessedletter in availableLetters)):
            lettersGuessed+=[guessedletter,]
            print 'Good guess: '+getGuessedWord(secretWord, lettersGuessed)
        elif(guessedletter in lettersGuessed):
            print 'Oops! You\'ve already guessed that letter: '+getGuessedWord(secretWord, lettersGuessed)
        else:
            lettersGuessed+=[guessedletter,]
            print 'Oops! That letter is not in my word: '+getGuessedWord(secretWord, lettersGuessed)
            GuessTime-=1
        drawHangman(8-GuessTime)

        print '------------'
        if (GuessTime<=0):
            print 'Sorry, you ran out of guesses. The word was else. '
            break
        if isWordGuessed(secretWord, lettersGuessed):
            print 'Congratulations, you won!'
            break

hangman(chooseWord(wordlist))




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)