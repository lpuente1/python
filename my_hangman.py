import random, sys

Hangman_pics = [r"""

 +--+

 |  |

    |

    |

    |

    |

=====""",

r"""

 +--+

 |  |

 O  |

    |

    |

    |

=====""",

r"""

 +--+

 |  |

 O  |

 |  |

    |

    |

=====""",

r"""

 +--+

 |  |

 O  |

/|  |

    |

    |

=====""",

r"""

 +--+

 |  |

 O  |

/|\ |

    |

    |

=====""",

r"""

 +--+

 |  |

 O  |

/|\ |

/   |

    |

=====""",

r"""

 +--+

 |  |

 O  |

/|\ |

/ \ |

    |

====="""]



#choosing a category
category = "Animals"

words = "ANT BABOON BADGER BAT BEAR BEAVER CAMEL CAT CLAM COBRA COYOTE CROW DEER DOG DONKEY DUCK EAGLE FERRET FOX FROG COAT GOOSE HAWK LION LIZARD LLAMA MONGOOSE MONKEY MOUSE MULE" .split()



#main function 
def main():

    print('Lets Play Hangman game')

    #setting up variables:

    missedLetters = []  # List of incorrect letter guesses

    correctLetters = []  # List of correct letter guesses

    secretWord = random.choice(words) #random word that player will need to guess 

    while True:  

        drawHangman(missedLetters, correctLetters,secretWord)

        #player enters guesses:

        guess = getPlayerGuess(missedLetters + correctLetters)

        if guess in secretWord:

            # Add correct guess letter to correctLetters:

            correctLetters.append(guess)

            #if the player has won:

            foundalletters = True  

            for secretWordLetter in secretWord:

                if secretWordLetter not in correctLetters:

                    foundalletters = False

                    break

            if foundalletters:

                print('Yes! The secret word is ',secretWord)

                print('You have won!')

                break    

        #if player has not won:
        else:

            missedLetters.append(guess)

            if len(missedLetters)== len(Hangman_pics) - 1:

                drawHangman(missedLetters, correctLetters, secretWord)

                print('You have run out of guesses!')

                print('The word was "{}"'.format(secretWord))

                break

#hangman function 

def drawHangman(missingletters,correctletters,secretword):

    print(Hangman_pics[len(missingletters)])

    print('the category is: ', category)

    print()
    print('Missed letters: ' ,end= '')


    for letter in missingletters:

        print(letter, end='')

    if len(missingletters) == 0:

        print('No missing letters yet')

    print()

    #display blanks 

    blanks = ['_'] * len(secretword)

    #replace blanks with correct letters 

    for i in range(len(secretword)):

        if secretword[i] in correctletters:

            blanks[i] = secretword[i]

    print(''.join(blanks))
    
#while playing game:
def getPlayerGuess(alreadyguessed):

        while True:

            print ('Guess a letter')

            guess = input('>').upper()

            #player enters first letter 

            if len(guess)!= 1:

                print('enter a single letter')

            #if player enters letter that was already used:

            elif guess in alreadyguessed:

                print('You already guessed, choose a different letter')

            #if no repetitite letter was used:

            elif not guess.isalpha():

                print('Enter the letter.')

            else:

                return guess


if __name__ == '__main__':

    try:

        main()

    except KeyboardInterrupt:

        sys.exit()  
