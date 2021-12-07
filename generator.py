import random  #import number 
loop = "y"  #looping to guess over and over 
while loop=="y":  #while looping
    number= random.randrange(500)+ 1 #random number is an integer
    guess = int(input("Guess a number between 1 and 500: "))  #integer converted to string
    number = 75    #correct guess is 75
    if guess > 75:      #if number is higher than 75
        print ("Too high, try again:")    #display too high, try again
        guess = int (input("Guess again: "))  #integer converted to string
        guess= random          #number must be equal to 75


    if guess < 75:    #if number is lower than 75
        print ("Too low, try again:")    #display too low, try again
        guess = (int(input("Guess again: ")))   #integer converted to string. User has to guess again
        guess= random        #number must be equal to 75

    if guess : 75   #if guess is equal to 75
    print ("You guessed the number!! ")    #output will say user guessed the correct number

    loop = "y"     #start again when game is over

