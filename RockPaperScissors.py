import random

def score():
    if numberOfGuesses == 3:
        if userWins >= 2:
            print ("Congratulations, you beat the computer! You won %s rounds out of 3" % (userWins))
        else:
            print ("Sorry the computer beat you this time. You won %s rounds out of 3"% (userWins))

def computerMove():
    options = ["Rock","Paper","Scissors"]
    compMove = random.choice(options)
    return (compMove)

def anotherTurn():
    if numberOfGuesses != 3:
        print ("\nLets go again, best out of 3")
    else:
        print ("You are all out of turns, Lets see who won...")

print("Welcome to the game of Rock, Paper Sissors! Hope your ready to play :)")

userWins = 0
numberOfGuesses = 0
while numberOfGuesses !=3:
    compGuess = computerMove()
    userGuess = input("Enter Rock,Paper,Scissors to make your move:   \n")

    if (userGuess == compGuess):
        print("Ooooh it's a draw!The computer guessed %s." % (compGuess))
        numberOfGuesses += 1
        anotherTurn()
        score()

    elif (userGuess == "Scissors" and compGuess == "Paper"):
        print("You won! Congratulations!The computer guessed %s. "%(compGuess))
        userWins += 1
        numberOfGuesses += 1
        anotherTurn()
        score()

    elif (userGuess == "Rock" and compGuess == "Scissors"):
        print("Yeah you won! Congratulations!The computer guessed %s." %(compGuess))
        userWins += 1
        numberOfGuesses += 1
        anotherTurn()
        score()

    elif (userGuess == "Paper" and compGuess == "Rock"):
        print ("You won! Congratulations!The computer guessed %s." %(compGuess))
        userWins += 1
        numberOfGuesses += 1
        anotherTurn()
        score()
    else:
        print ("Sorry, computer won this round. The computer guessed %s." %(compGuess))
        numberOfGuesses += 1
        anotherTurn()
        score()