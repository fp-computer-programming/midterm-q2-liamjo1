# Author: Liam O'Hara
import random
print ("Liam's Hangman")
print("------------------------------------")

wordDictionary =["table", "tissue", "helmet", "rugby", "computer", "bottle", "earphones", "tennis", "hockey"]

# Pick a random word
randomWord = random.choice(wordDictionary)

# Print letter spaces for random word
for x in randomWord:
    print("_", end=" ")
# Create function to depict hangman after each incorrect guess
def print_hangman(incorrect):
    if(incorrect == 0):
        print("\n+---+")
        print("   |")
        print("   |")
        print("   |")
        print("   ===")
    elif(incorrect == 1):
        print("\n+---+")
        print(" O  |")
        print("   |")
        print("   |")
        print("   ===")
    elif(incorrect == 2):
        print("\n+---+")
        print(" O  |")
        print(" |  |")
        print("   |")
        print("   ===")
    elif(incorrect == 3):
        print("\n+---+")
        print(" O  |")
        print(" |\  |")
        print("   |")
        print("   ===")
    elif(incorrect == 4):
        print("\n+---+")
        print(" O  |")
        print("/|\  |")
        print("   |")
        print("   ===")
    elif(incorrect == 5):
        print("\n+---+")
        print(" O  |")
        print("/|\  |")
        print("/  |")
        print("   ===")
    elif(incorrect == 6):
        print("\n+---+")
        print(" O  |")
        print("/|\   |")
        print("/ \ |")
        print("   ===")
# Function to accuratly update lines with correct letters      
def printWord(guessedLetters):
    counter=0
    rightLetters=0
    for char in randomWord:
        if(char in guessedLetters):
            print(randomWord[counter], end=" ")
            rightLetters+=1
        else:
            print(" ", end=" ")
        counter+=1
    return rightLetters

def printLines():
   print("\r")
   for char in randomWord:
      print("\u203E", end=" ")

length_of_word_to_guess = len(randomWord)
amount_of_times_wrong = 0
current_guess_index = 0
current_letters_guessed = []
current_letters_right = 0
# Update all incorrect letters and log
while(amount_of_times_wrong != 6 and current_letters_right != length_of_word_to_guess):
    print("\nLetter guessed so far: ")
    for letter in current_letters_guessed:
        print(letter, end=" ")
   # Prompt user for input
    letterGuessed = input("\nGuess a letter: ")
   # User is correct
    if(randomWord[current_guess_index] == letterGuessed): 
      print_hangman(amount_of_times_wrong)
      # Print word
      current_guess_index+=1
      current_letters_guessed.append(letterGuessed)
      current_letters_right = printWord(current_letters_guessed)
      printLines()
      # User was incorrect
    
    else:
      amount_of_times_wrong+=1
      current_letters_guessed.append(letterGuessed)
      # Update the drawing
      print_hangman(amount_of_times_wrong)
      # Print word
      current_letters_right = printWord(current_letters_guessed)
      printLines()

print("Game is over! Good Job!")