import random
import string
from words import words
from visuals import visuals_dict
# importing libraries and python files

def game():
    word = random.choice(words) # get random word
    uppercase = word.upper() # uppercase for game
    letters = set(uppercase) # letters in the word
    alphabet = set(string.ascii_uppercase) # uppercase alphabet
    usedLetters = set() # what user guessed
    lives = 7
    
    print("Welcome to Hangman!")
    print("You have 7 lives to guess the word.")
    print()
    
    while len(letters) > 0 and lives > 0: # main game loop
        print("Lives:", lives, "            Used Letters: ", " ".join(usedLetters))
        
        wordList = [letter if letter in usedLetters else '-' for letter in uppercase]
        print(visuals_dict[lives])
        print("Word: ", " ".join(wordList))
        # to print letters user guessed correctly
        
        userLetter = input("Guess A Letter: ").upper() # user guesses letter
        if userLetter in alphabet - usedLetters: # guessed letter is in remaining letters
            usedLetters.add(userLetter) # add new used letter
            if userLetter not in letters: # incorrect guess
                lives -= 1 # minus life
                print("\"" + userLetter + "\" is not in the word.")
            elif userLetter in letters: # guessed correctly 
                letters.remove(userLetter) # remove from word letters
                print("Correct Guess! The letter is in the word.")
                print()
        elif userLetter in usedLetters: # if user already used that letter
            print("You already used that letter. Guess another letter.")
            print("")
        else: # invalid input
            print("Invalid Input. Please enter a single letter from the English alphabet.")
            print("")
    
    if lives == 0: # user lost
        print(visuals_dict[lives]) # print visual
        print("You died. The word was", uppercase)
    else: # user won
        print("Congratulations! You got it right! The word was", uppercase)

if __name__ == "__main__":
    game()