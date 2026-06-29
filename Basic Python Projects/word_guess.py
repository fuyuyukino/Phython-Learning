#Word guessing game
import random

#Input name of player
name = input("What is your name? ")
print(f"Good luck {name}!")
    
#Main action of the game
def main():
    #Open and start list
    word()
    
    #Initalize the guesses and attempts
    guesses = ""
    attempts = 15
    
    #The game begins
    while attempts > 0:
        failed = 0
        for i in word:
            if i in guesses:
                print(i, end=" ")
            else:
                print("_", end=" ")
                failed += 1
        
        if failed == 0:
            print("\nYou win!")
            print(f"The Word is {word}")
            break
        
        guess = input("\nGuess the character: ")
        
        if len(guess) != 1:
            print("Please enter a single character")
            continue

        guesses += guess
    
        if guess not in word:
            attempts -= 1
            print("Wrong")
            print("You have", attempts, "more guesses")
        
            if attempts == 0:
                print("\nYou lose")
                print("The word was:", word)

#Create list of words and randomly select one
def word():
    global word
    words= ["banana", "apple", "computer", "data",
         "programming", "science", "algorithm", "winter", 
         "monument", "autumn", "spring", "summer", "world"]
    word = random.choice(words)
    print("Guess the characters!")
    return word
    
main()