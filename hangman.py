#Hangman Game - learning Python fun!

#imports
import random

#declare constants . well actually python doesn't have any constants! It's a lie
HANGMAN = (
    """
    --------
    |       |
    |
    |
    |
    |
    |
    |
    ---------
    """,
    """
    --------
    |       |
    |      O
    |
    |
    |
    |
    |
    ---------
    """,
    """
    --------
    |       |
    |      O
    |   -- | --
    |
    |
    |
    |
    ---------
    """,
    """
    --------
    |       |
    |      O
    |   -- | --
    |       |
    |
    |
    |
    ---------
    """,
    """
    --------
    |       |
    |      O
    |   -- | --
    |       |
    |     |
    |     |
    |
    ---------
    """,
    """
    --------
    |       |
    |      O
    |   -- | --
    |       |
    |     |   |
    |     |   |
    |
    ---------
    """
    )

CHANCES = len(HANGMAN) - 1

#possible words to guess
WORDS = ("FLUFFY","STARBUCKS","KOKORO","Llanfairpwllgwyngyll","Supercalifragilisticexpialidocious","PYTHON","AWESOME")

#lets pick a random choice
answer = random.choice(WORDS)

#what the user will see
displayable = "_" * len(answer)

#instantiate chance
wrong = 0
guessed = []

#let the games begin!

print ("Welcome to Hangman! Takaloy's learn to Python first day program. I'm so coming back and go 'WTF?! I WROTE THIS SHIT?' one day");

while wrong < CHANCES and displayable != answer:
    print(HANGMAN[wrong])
    print("\nLetters gussed so far : ", guessed)
    print("\nHere's your word : ", displayable)
    
    guess = input("\n\nEnter your guess: ")
    guess.upper()

    while guess in guessed:
        print ("You've already guessed the letter", guess)
        guess = input("Enter your guess: ")
        guess.upper()

    guessed.append(guess)

    if guess in answer:
        print("\nYes! You've gussed it correctly! Good Job! No You can't eat me.")

        newDisplayable = ""
        for i in range(len(answer)):
            if guess == answer[i]:
                newDisplayable += guess
            else:
                newDisplayable += displayable[i]

        displayable = newDisplayable #replace displayable with temp value
    else:
        print("\nOops. The letter ",guess," is not part of the word")
        wrong += 1

if (wrong >= CHANCES):
    print(HANGMAN[CHANCES])
    print("\nOMG YOU KILLED KENNY!")
else:
    print("\nCongratulations! The vile villian survived the day. Robbin of Mocksley survived it")

print("The answer was ... ", answer)

input("\nPress any key to quit.")

