# This code is going wonkers when tested from the console.
# Especially, the getEnglishCount() function.

import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')


# Constants
UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + '\t\n'


# This loads the English dictionary file
def loadDictionary():
    dictionaryFile = open('smalldict.txt')
    englishWords = {}  # Using a dictionary data type helps to work faster as Python loops through a dictionary faster
    # a list.
    # Iteration splitting the words in the dictionary on presence of newline character
    for word in dictionaryFile.read().split('\n'):
        englishWords[word] = None
    dictionaryFile.close()
    return englishWords


# Calls the loadDictionary() function and saved as a variable.
ENGLISH_WORDS = loadDictionary()


# Gets the ratio of English words in the message.


def getEnglishCount(message):
    logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
    logging.debug('Start of function program')
    message = message.upper()
    message = removeNonLetters(message)  # This removes the non-alphabets in the message leaving the new message
    # which is stored in possibleWords.
    logging.debug('Message is %s' % message)
    possibleWords = message.split()  # Splits this into individual strings
    logging.debug('Possible Words is %s' % possibleWords)
    logging.debug('Possible Words is %s' % len(possibleWords))
    # if possibleWords == []:
    #   return 0.0  # Returns this when there is no word that matches an English text

    matches = 0  # Store the number of matches of the word in the decrypted text to the dictionary file.

    for word in possibleWords:
        if word in ENGLISH_WORDS:
            logging.debug('The word iterated is %s' % word)
            matches += 1  # Add 1 for each iteration checking if the word exists in the dictionary.
            logging.debug('Value for matches is %s' % matches)
            logging.debug('Value for the ratio of words that appear in the dictionary %s'
                          % (matches/len(possibleWords)))
    return matches / len(possibleWords)
    # return matches / len(possibleWords)

    #  if possibleWords == []:
    #   return 0.0  # Returns this when there is no word that matches an English text


# print(getEnglishCount('hello'))

    # return float(matches) / len(possibleWords)
logging.debug('End of program')

# This removes other characters from the code, this include numbers and punctuations.


def removeNonLetters(message):
    lettersOnly = []
    # Iterate through the characters in the message
    for symbol in message:
        # Check if the character is in the LETTERS_AND_SPACE constant, if it exists, it is added to the list
        if symbol in LETTERS_AND_SPACE:
            lettersOnly.append(symbol)
    return ''.join(lettersOnly)


# removeNonLetters('hello')
# Detects the presence of English words


def isEnglish(message, wordPercentage=20, letterPercentage=85):
    # Gets the percentage of the occurence of English words in the decrypted text
    wordsMatch = getEnglishCount(message) * 100 >= wordPercentage
    numLetters = len(removeNonLetters(message))
    messageLettersPercentage = (float(numLetters) / len(message)) * 100
    lettersMatch = messageLettersPercentage >= letterPercentage
    return wordsMatch and lettersMatch
